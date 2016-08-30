==================
API - The Response
==================

The response of the Eva Web API is a JSON encoded.

HTTP Status Codes
=================

.. automodule:: core.eva_return_codes
   :synopsis: HTTP Status Codes returned by the system. 


Top Level Response
==================

The response always includes the following elements:

**status**
    A boolean parameter specifying whether or not the request was successfully handled.
    *status* does **not** indicate any level of text understanding
    but instead expresses that the Eva processing logic was implemented correctly.

**input_text**
    The selected input text copied from the request. see: :ref:`multiple_input_text`.
    
    To semantic-highlight the input text you need to use the *ProcessedText* field inside
    the :ref:`api_reply field <api_reply>`.
    There are situations, such as spelling correction, in which the returned input text is different
    from the original input text, for which case the *ProcessedText* field is provided.

**message**
    Human readable status messages, most of which are self explanatory.
    
    Here are some of the more common responses:
    
    * *Site-Code / API-Key invalid*
    * *No Site Code*
    
    See :ref:`credentials <site_code and api_key>`.
    
    * *You have reached the daily API limit. Please contact info@evature.com*
    
    Please do!
    
    * *Unsupported Language*
    
    Eva is currently trained in English. Please contact us for additional language support.
        
    * *Partial Parse*
    * *Successful Parse*
    
    A natural language indication that Eva "understood" the input, before trying to apply business logic.
    It does not mean that the input makes sense.
    
    For example these would be considered a *Successful Parse*::

        User: "Flight from Beverly Hills to Shiraz Iran for 2 kids for under $12 departing august 2020"
        User: "Pet friendly cruise from the Eiffel tower to the Willis tower"
    
    *Partial Parse* means that not all the input was Successfully Parsed,
    which indicates that one or more words were unrecognized, horribly misspelled or out of domain,
    possibly even the entire sentence!
    
    Note that Eva might completely overcome a *Partial Parse* and reply with a result that makes perfect sense,
    for example::

        User: "United Airlines zxczxczxc flight from JFK to SFO"
     
.. note::
       
       The **message** is intended to be consumed by humans.
       Please do not use it as an indication of the quality of the result.
       Instead, use the confidence field in the API reply.
    
**api_reply**
    Eva's understanding of the user's request in a detailed structured form. See `api_reply - in depth`_.

**ver**
    Eva's current software version.

**rid**
    A user provided request ID number, returned to the user. Usage is deprecated.

.. _transaction_key:

**transaction_key**
    Unique transaction identifier.

    Each interaction with Eva is assigned a globally unique transaction key which is returned in the Eva JSON reply,
    such as

.. code-block:: javascript
    :caption: Simplified Eva API Reply

    "transaction_key": "11e5-60ea-df167fe3-8a1c-22000bda434f"

.. note::
       
       If you come across any specific Eva problem which you would like to report back to the team,
       which can be either a speech recognition problem (Eva did not "hear" you correctly)
       or an understanding problem (Eva heard you correctly but did not quite "get" what you meant)
       please report it to us. The easiest and most effective way to do this is using a transaction_key.
       
       We log everything.

**session_id**
    Unique session identifier. It is both an input to Eva and an output from Eva. See :ref:`session_id`

**confidence**
    The level of confidence Eva has in the reply reported both numerically and categorically
    per the last utterance and accumulating over the entire session.
    Numeric scope is is a float between 0.0 and 1.0,
    while categories are a string enumeration with values 'Low', 'Medium' and 'High'. For example:

.. code-block:: javascript
    :caption: Simplified Eva API Reply

    "confidence": {
       "accumulated": "High", 
       "last_utterance_score": 0.5794277, 
       "accumulated_score": 0.98, 
       "last_utterance": "High"
    }, 

.. _api_reply:

api_reply - in depth
====================

The api_reply details the complete understanding of the user's request, accumulating over the session.

.. note::
    Human Language is very broad, flexible and dynamic.
    Trying to capture the wealth of information in the user's request in structured form
    led us to the following guidelines:
    
    * keys in the *api_reply* object indicate they were applicable and specifically requested by the user.
      A missing key means the user did not specifically request it or that it is not applicable.
      
      For example: "Hotel in Madrid on Monday" would have an "Arrival" key but no "Departure" key
      for the Madrid Location in the reply,
      while "Flight from Madrid on Monday" would have a "Departure" key but no "Arrival" key
      for the Mardid location in the reply.
    * Boolean attributes that are set to *false* mean the user specifically requested for them to be negative
      as opposed to not mentioning them at all.     

The top level api_reply can include the following keys:

**Flow**
    Flow of Actions describing a simple to-do list for the application    

**Locations**
    Information about the locations included in the trip as specified by the user
    (countries, cities, areas, airports, properties) and their related information (including all **time** information).
    
    Note: All the attributes described bellow **may** appear within a location if the attribute
    is related specifically to a particular location.
    Example "Center of Chicago" - the Geo Attribute "Center" will appear under Chicago and not in the global context.                

**Alt Locations**
    Structured the same as Locations, but includes alternate locations specifically requested for by the user,
    referencing locations with similar indices in the *Locations* key. 
    
    Example: "vacation in Italy or France" will place "France" in Locations while Italy in "Alt Locations"
    while both would share the same *Index*.
    
**Travelers**
    Information about the travelers number and age.

**Geo Attributes**
    Attributes representing locations. 
    
    Example: "vacations somewhere hot"
    
**Hotel Attributes**
    Attributes representing properties. 
    
    Example: "hotel with a pool"
    
**Flight Attributes**
    Attributes representing flights. 
    
    Example: "Red eye flights"
    
**Activity Attributes**
    Attributes representing activities. 
    
    Example: "Scuba Diving in Australia"

**Request Attributes**
    Attributes representing the type of deal being sought. 
    
    Example: "Last minute deals to Egypt"
    
**Money**
    Information about money. 
    
    Example: "vacations in Italy for less than $500"
    
**Chat**
    Attempts to chat with Eva. 
    
    Example: "Hello, how are you?"

**Warnings**
    Various warnings provided by the system. 
    
    The format is a list made of warning type, warning value and if the warning relates to a particular part of the text, a dictionary with the related text and its position in the input.  


Locations (Alt Locations)
=========================

A list of locations representing the trip requested. Each location item may have the following keys:

**Index**
    A number representing the location index in the trip. Index numbers usually progress with the duration of the trip (so a location with index 11 is visited before a location with index 21).
    
    An index number is unique for a locations in Locations (unless the same location visited multiple times, for example home location at start and end of trip will have the same index) but "Alt Locations" may have multiple locations with the same index, indicating alternatives for the same part of a trip.
    
    Index numbers are not serial, so indexes can be (0,1,11,21,22, etc.).
    
    Index number '0' is unique and always represents the home location.             

**Next**
    The index number of the location in a trip, if known.

**Geoid**
    A global identifier for the location. IATA code for airports and Geoname ID for other locations.
     Note: if Geoname ID is not defined for a location, a string representing the name of the location will be given in as value instead. The format of this name is currently not set and MAY CHANGE. If you plan to use this field, please contact us.

**Country**
    The ISO code for the country of the location (not present in case of continents and cross country regions).
            
**Name**
    The location name. Mostly for debug purposes. Locations should be accessed with Geoid.            
    
**Type**
    The location type. Example values: Continent, Country, City, Island, Airport.

**Longitude**
    The Location longitude.
    
**Latitude**
    The location latitude.

**Derived From**
    Exists only at certain locations.
    
    Currently it will always appear in the 1st location (Home) 
    and sometimes in the 2nd location (which is the 1st destination) to represent a case where the user is at the destination.

    Text - Location is defined in the text. Example: "fly from NY to LA"
    
    Request - The defined location in the request (for example - "home" value).
    
    Bias - The defined location in the request "bias" value.
    
    IP - Based on the IP address - as provided in the request.
    
    GPS - Based on longitude and latitude coordinates - as provided in the request.
    
    Default - Default location (for example - default Home).

    Example: "Hotel tonight" will assume that IP or GPS information is referring to the location where the hotel is searched for (the destination). 
    Location 1 will still be the Home, only the user is currently not there.

**Ambiguity**
    True if the location did not have a clear meaning (Example: "Arlington" - there are many and its unclear which one was meant).
    The list of location options would appear under "Possible Locations".
    
**PossibleLocations**
    A list of possible locations in case of ambiguity. The list includes: Name, Country, Longitude, Latitude, Type, and Geoid.  

**Home**
    Applicable only to the 1st (Home) location on the list. Defines the source of the information about the home location.
    It appears in v1.0 and a copy of "Derived From" value. It will become obsolete in v1.1
    
**Arrival**
    Time of arrival to location (see Time key explained bellow).

**Departure**
    Time of departure to location (see Time key explained bellow).

**Stay**
    Stay time in the location (see Time key explained bellow). 
    Note: this is specific stay time, example: "hotel in NY for 3 nights". Arrival and Departure may also implicitly define stay, but it will not appear in the Stay key, for example: "arrive in NY on Monday and depart to LA on Thursday.

**Pickup Car**
    Time for rental car pickup (see Time key explained bellow).

**Return Car**
    Time for rental car return (see Time key explained bellow).

**Actions**
    Provides a list of actions requested for this location. Actions can include the following values:
    'Get There' (request any way to be transported there, mostly flights but can be train, bus etc.), 'Get Accommodation', 'Get Car'.

**Purpose**
    Provides a list of purpose items if known. Values can include:
    'Meeting', 'Pleasure', 'Business', 'Convention', 'Medical', 'Transit', 'Home'.
    Example: "fly to NY. My home is Tokyo"        
    
**Airports**
    If a location is not an airport, this key provides 5 recommended airports for this location.
    Airports are named by their IATA code.
    
**All Airports Code**
    Will be present in cities that have an "all airports" IATA code (e.g. San Francisco, New York, etc.).
    
**Keys**
    Provide the location/property key based on a particular customer's data.
        
            
Time key (Arrival, Departure, Stay)
===================================

Time is defined with the following keys: Date, Time, Delta, Restriction

**Date, Time** 
    Represent a specific date and time if given. 
    
    Example: "fly to ny 3/4/2010 at 10am" results: "date": "2010-04-03", "time": "10:00:00".
 
**Delta**
    May represent:
        A range starting from Date/Time. Example: "next week" results: "date": "2010-10-25", "delta": "days=+6"
        
        A duration without an anchor date. Example: "hotel for a week" results: "delta": "days=+7"
        
**Restriction**
    A restriction on the date/time requirement. Values can be:
    'no_earlier', 'no_later', 'no_more', 'no_less', 'latest', 'earliest'
    
    Example: "depart NY no later than 10am" results: "restriction": "no_later", "time": "10:00:00"

**Calculated**
    A boolean flag representing that a particular time has been calculated from other times,
    and not directly derived from the input text.
    In most cases if an arrival time to a location is specified, the departure time from the previous location is calculated.                      

**ProcessedText**
    A cleaned up version of the input text which may be used for client-side semantic highlighting based on
    character positioning within the string (which may be different from the input_text.
    Example: if there is a warning that "blahblah" was misunderstood at position 17,
    This position is the 17th character in *ProcessedText*


.. _flow:

Flow
====
.. automodule:: core.dialog.eva_flow_docs
   :synopsis: simple to-do list for the application consisting of flow actions


Money
=====

Includes the following keys: 
    * **Amount**: the amount of money.
    * **Currency**: the currency used, per `ISO 4217 codes <http://www.iso.org/iso/support/faqs/faqs_widely_used_standards/widely_used_standards_other/currency_codes/currency_codes_list-1.htm>`_
    * **Restriction**: restrictions can have the following values: '**Less**', '**More**', '**Least**', '**Most**', '**Medium**' 
    * **Per Person**: boolean to indicate whether or not the price is per-person.
    
Example: "hotel for less than $500 pp" 

results: "Currency": "USD", "Amount": "500", "Per Person": True
        
Chat
====

An attempt to chat with Eva or a request that may require a chat reply as opposed to going straight to search.

Chat values may include:
    * **Hello**: Example: "hello" 
    * **Who/What**: Example: "Who are you?"
    * **Name**: Example: "My name is Joe"
    * **How are you**: Example: "How are you?"
    * **Bookings**: Identified a previous booking number. Example:"XBS-23452". Note - this is identified based per site.    
    * **Cancellations**: A request to cancel a previous order. Example:"Cancel my order"
    * **Yes**: Some variant of an affirmative reply, usually as a response to a question.
    * **No**: Some variant of a negative reply, usually as a response to a question.

If a chat type has value, the value will be given (Example: "my name is Joe" results in "Name": "Joe") otherwise
the value will be *true* (Example: "hello" results in "Hello": true).

Hotel Attributes
================
                
.. automodule:: core.attributes.hotel
   :synopsis: Various hotel attributes.


Flight Attributes
=================
   
.. automodule:: core.attributes.flight
   :synopsis: Various flight attributes.
   
Request Attributes
==================

.. automodule:: core.attributes.request
   :synopsis: Various request attributes.
   
Geo Attributes
==============

.. automodule:: core.attributes.geography
   :synopsis: Various geo attributes.
   
Cruise Attributes
=================

.. automodule:: core.attributes.cruise
   :synopsis: Various cruise attributes.

Car Attributes
=================

.. automodule:: core.attributes.car
   :synopsis: Various car attributes.

Activity Attributes
===================

.. automodule:: core.attributes.activity
   :synopsis: Various activity attributes.

Ski Attributes
==============
                
.. automodule:: core.attributes.ski
   :synopsis: Various ski attributes.


Warnings
========

.. automodule:: core.warning
   :synopsis: Various Warnings provided by the system. 
   


