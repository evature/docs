==================
API - The Response
==================

The response of the Eva Web API is a JSON encoded.

HTTP Status Codes
=================

   The following is a list of the codes Eva returns:

   * 200 OK = The request has succeeded.
   * 400 BAD REQUEST = faulty values in the request parameters. Most often returned when the input_text field is empty.
   * 401 UNAUTHORIZED = The request requires user authentication, which failed.
     Please check your :ref:`credentials <site_code and api_key>`.
   * 404 NOT FOUND = The server has not found anything at your requested URL.
   * 405 METHOD NOT ALLOWED =  Eva text end-points currently supports only "HTTP GET" requests.
   * 429 TOO MANY REQUESTS = The site_code quota has been exceeded.  See http://tools.ietf.org/html/rfc6585#section-4

     Please contact us!
   * 500 INTERNAL SERVER ERROR = A bug escaped us. Sorry. We are on it.


   Please make sure your application can handle these return codes.


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
    It appears in v1.1 and is a copy of "Derived From" value. It will become obsolete in v1.2

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
Flow is a high level API reply element, describing the to-do list for the application developers.
It consists of a List of Actions, ordered by "Travel Logic" (for example, search for flights first, hotels later).
There are several possible Flow Actions, identified by a Type.

Each Flow Action is a Dictionary object containing the following keys:

**Type** - an enumeration that describes the scope of the flow action. :ref:`flow_action_hotel`, :ref:`flow_action_car`, :ref:`flow_action_flight`, :ref:`flow_action_cruise` or :ref:`flow_action_question`.

**RelatedLocations** - a list of integer location indexes in the *api_reply/Locations* list for use in the specific Flow Action. Note this key will be returned only if applicable.

**SayIt** - A string with the textual description of the specific flow action, to be used for chat and Text-to-Speech

.. _flow_action_flight:

Flight
------
A flow action of type ``Flight`` indicates that there is a flight request in the user's input.
The related locations contains the indexes of locations between origin and destination of a flight (including transit locations).
A list of [1,2] means a flight from location #1 to location #2 in the Locations list (the first element is index #0).

Round trip flights have an additional key:

**ReturnTrip** - a dictionary with the following keys:
   **ActionIndex** - a 0-indexed integer pointing to the return trip flow action in the *api_reply/Flow* list.

   **SayIt** - A string with the textual description of the specific round trip flight action, to be used for chat and Text-to-Speech

.. _flow_action_car:

Car
---
A flow action of type ``Car`` indicates that there is a car rental request in the user's input.
Related locations is a list of the relevant location indexes. It can contain:

#. A single location, in case the car is to be picked up and returned at the same location
#. Two locations, in which case the car is to be picked up in the first location and dropped off at the second

.. _flow_action_hotel:

Hotel
-----
A flow action of type ``Hotel`` indicates that there is an accommodation request in the user's input.
The related locations list contains a single location index where an accommodation is requested.

.. _flow_action_cruise:

Cruise
------
A flow action of type ``Cruise`` indicates that there is a cruise request in the user's input.
The related locations list is similar to the related locations list in the Car Flow Action.


Train
------
A flow action of type ``Train`` indicates that there is a train request in the user's input.
The related locations list is similar to the related locations list in the Car Flow Action.

.. _flow_action_question:

Reply
-----
flow action of type ``Reply``  indicates that the end user requested an applicative reply.
This happens when the user asks a question such as "How do I contact customer service?" (Service Attributes)

**AttributeType** - the type of the attribute such as: "Service Attributes", "Request Attributes" etc.
**AttributeKey** - the key of the attribute that triggers the reply such as: "Call Support".

Statement
---------
flow action ``Statement`` indicates that there is some information to the end user. (activated using 'ffi_statement' in the query string)

**StatementType**
   * Understanding - Eva did not understand the input.
   * Chat          - A dialog with the end-user.
   * Unsupported   - The requested travel search category is unsupported based on site_code definition and the 'scope' query parameter.
   * Unknown Expression - Eva did not understand the expression

Question
--------
When the Dialog Engine is configured (per site code), Flow Actions of type ``Question`` may appear in the flow.
Questions help Eva understand the user's request.
In addition to the above keys, Question Flow Actions contain:

**QuestionType** - The type of question. An enumeration with the following string values:
   * "Open"             - defines an open question
   * "Multiple Choice"  - defines a multi-choice question, in which case an additional *QuestionChoices* key will appear.

**ActionType** - The type of the related action. For example 'Hotel', 'Flight', etc...

**QuestionCategory** - The purpose of the question. An enumeration with the following string values:
   * Location Ambiguity  - The location cannot be uniquely identified, e.g. "arlington"
   * Missing Date        - There is a required but missing date in the input that cannot be derived from the text.
   * Missing Duration    - There is a required but missing duration in the input that cannot be derived from the text.
   * Missing Location    - There is a required but missing location in the text, e.g. "flights on Monday".
   * Informative         - A question containing some information to the end user
   * Missing Action      - There is a missing action for a location e.g. "ny"
   * Missing Travelers   - There is a required but missing travelers (adults, children or infants) that cannot be derived from text.
   * Missing Direction   - if location mentioned and it cannot be uniquely identified whether the location is an origin or target location.

**QuestionSubCategory** - Additional key describing the sub category of the question.
   * For the Missing Date Category the following sub categories exist:
       * Pickup Car    - missing date of pickup car.
       * Return Car    - missing date of return car.
       * Arrival       - missing date of arrival.
       * Departure     - missing date of departure.
       * Return Date   - missing return date.
   * For the Informative Category the following sub categories exist:
       * Understanding - Eva did not understand the input.
       * Chat          - A dialog with the end-user.
       * Unsupported   - The requested travel search category is unsupported based on site_code definition and the 'scope' query parameter.
       * Unknown Expression - Eva did not understand the expression
   * For the Missing Duration Category the following sub categories exist:
       * Stay - missing duration of stay, relevant to accommodation requests.

**QuestionChoices** - A list of possible string answers for responding to multiple choice questions.
The developer may wish to implement a dialog GUI, presenting this list to the end user.
If the user selects from this list the response needs to be sent back to Eva as a ``dialog_repsonse`` request parameter.


**Flow Engine reply examples:**


input_text: "hotel in arlington"

.. code-block:: javascript

   "api_reply": {
       "Flow": [
           {
               "QuestionType": "Open",
               "QuestionCategory": "Location Ambiguity",
               "RelatedLocations": [
                   1
               ],
               "Type": "Question",
               "SayIt": "Which Arlington did you mean?"
           }
       ],
   }


Here is a more complex example:

input_text: "hotel and flight to ny from Boston tomorrow night"

.. code-block:: javascript

   "api_reply": {
           "Flow": [
               {
                   "RelatedLocations": [
                       0,
                       1
                   ],
                   "Type": "Flight",
                   "SayIt": "Flights from Boston, Massachusetts to New York City, New York, departing July 2nd, 2013, at 09:00PM"
               },
               {
                   "QuestionType": "Open",
                   "QuestionSubCategory": "Stay",
                   "QuestionCategory": "Missing Duration",
                   "SayIt": "How many nights would you like to stay in New York City, New York?",
                   "Type": "Question",
                   "RelatedLocations": [
                       1
                   ]
               }
           ]
       }

The above Flow has 2 actions: First, search for flights. When the flight search is resolved, ask about the Missing Duration.



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

Chain
-----

The chain of the hotel (e.g. Sheraton)


Board
-----

The hotel board, with the following potential values:

* Self Catering
* Bed and Breakfast
* Half Board
* Full Board
* All Inclusive
* Drinks Inclusive

The value is an Array of the above options (e.g. "half or full board")

Quality
-------

The quality of the hotel, measure in Stars.
The return value is a Array with 2 numbers (or null):

* Min Stars  = integer from 0 to 6
* Max Stars  = integer from 0 to 6

Examples:

* "2 to 3 stars"     -> [2, 3]
* "At least 4 stars" -> [4, null]
* "1 star"           -> [1, 1]


Numeric Rating
--------------

The hotel ratings, with values as floats.
This is the result of expressions such as "...with a review score of 7.6 or more".


Rating
------

The hotel ratings, with the following potential values (normalized to the values in TripAdvisor):

* Excellent
* Very Good
* Average
* Poor
* Terrible


Child Free
----------

A Child free hotel (adults only) - Boolean attribute

Business
--------

A Business hotel - Boolean attribute

Airport Shuttle
---------------

Airport Shuttle services - Boolean attribute

Casino
------

The hotel has a casino (or is located next to a casino) - Boolean attribute

Fishing
-------

The hotel has fishing facilities (or is located next to fishing facilities) - Boolean attribute


Snow Conditions
---------------

The area has good snow conditions - Boolean attribute

Snorkeling
----------

The hotel has snorkeling facilities (or is located next to snorkeling facilities) - Boolean attribute


Diving
------

The hotel has diving facilities (or is located next to diving facilities) - Boolean attribute

Activity
--------

An Activity hotel - Boolean attribute


Ski
---

A Ski hotel - Boolean attribute

Ski In/Out
----------

A Ski In / Ski Out accommodation - Boolean attribute


Golf
----

The hotel has golf facilities, or is situated by a golf course - Boolean attribute

Kids for free
-------------

Kids are free in parent's room - Boolean attribute

City
----

A City hotel - Boolean attribute

Family
------

A family friendly hotel - Boolean attribute

Pet Friendly
------------

A pet friendly hotel - Boolean attribute

Romantic
--------

A Romantic hotel - Boolean attribute

Adventure
---------

A hotel with an Adventure motif - Boolean attribute

Designer:
---------

A Designer / Boutique hotel - Boolean attribute

Gym
---

The hotel has a gym - Boolean attribute


Quiet
-----

A request for quiet accommodations - Boolean attribute


Pool
----

The hotel has a swimming pool - an enumerated attribute:

* 'Any'     - The hotel needs to have a pool
* 'Indoor'  - The hotel needs to have an indoor pool
* 'Outdoor' - The hotel needs to have a outdoor pool


Meeting Room
------------

The hotel has meeting rooms - Boolean attribute


Accommodation Type
------------------

The type of the requested accommodation - an enumerated attribute:

* Chalet
* Villa
* Apartment
* Motel
* Camping
* Hostel
* Mobile Home
* Guest House
* Holiday Village
* Hotel Residence
* Guest Accommodations
* Resort
* Hotel
* Zimmer
* Farm
* Youth Hostel
* Bungalow
* Inn


Restaurant
----------

The hotel has a restaurant - Boolean attribute

Gourmet
-------

A Gourmet hotel - Boolean attribute

Only
----

The request is specifically asking for just-a-hotel (and no flight, car etc.) - Boolean attribute

Disabled
--------

Handicapped friendly establishment - Boolean attribute

Spa
---

The establishment has a spa - Boolean attribute

Parking
-------

Parking facilities, contains these attributes:

* Facilities - Boolean attribute
* Valet      - Boolean attribute
* Free       - Boolean attribute

Castle
------

Hotel in a Castle - Boolean attributes

Sport
-----

Sport hotel - Boolean attribute

Countryside
-----------

Countryside hotel - Boolean attribute

Rooms
-----

The hotel rooms is a complex structure, containing a list of room elements, each with the following attributes:

* Multiple      -  How many of the same rooms (e.g. 3 airconditioned rooms)
* Beds          -  A list of tuples, each tuple has a number of beds (int) and Type of bed, with the following potential values:
    + Twin
    + King
    + Queen
    + Single
    + Double
    + Triple
    + Quadruple
    + Quintuple
    + Sextuple
    + Crib
* Room Type     -  The type of the room
    + Room
    + Family Room
    + Suite
* Air Con       -  Air conditioning (boolean, if exists)
* Internet      -  The requested data service in the room, with the following potential values:
    + Internet service
    + Free Internet service
    + Wi-Fi
    + Free Wi-Fi
* Cable         -  Cable TV in the room (boolean, if exists)
* Kitchen       -  A Kitchen in the room (boolean, if exists)
* Mini Bar      -  Mini-bar in the room (boolean, if exists)
* Tub           -  A hot tub in the room (boolean, if exists)
* Smoking       -  Either Smoking (True) or Non Smoking (False) room (boolean, if exists)

Loyalty
-------

Hotal Loyalty rewards

* Accor AI Club
* Hilton HHonors
* Wyndham Rewards
* Starwood Starpoints
* InterContinental Priority Club Rewards
* Hyatt Gold Passport
* Marriott Rewards
* Carlson Goldpoints
* LaQuinta Returns
* BestWestern Reward Points
* Choice Privileges
* Isrotel Sun Club

The value is an Array of the above options


Flight Attributes
=================

These are attributes describing the requested flight.

Redeye
------

A Red eye flight - Boolean attribute.


Nonstop
-------

A Non stop flight -
Boolean attribute. Nonstop is related to the location from which the flight departs and will appear under that location.

In API v1.0 Nonstop will also appear in global scope-
if it relates to all flight departure locations. This is will become obsolete in v1.1

Food
----

Food preferences for the flight
Potential values are:

* **Religious**:
 'Kosher', 'Glatt Kosher', 'Muslim', 'Hindu',
* **Vegetarian**:
 'Vegetarian', 'Vegan', 'Indian Vegetarian', 'Raw Vegetarian', 'Oriental Vegetarian', 'Lacto Ovo Vegetarian',
 'Lacto Vegetarian', 'Ovo Vegetarian', 'Jain Vegetarian',
* **Medical meals**:
 'Bland', 'Diabetic', 'Fruit Platter', 'Gluten Free', 'Low Sodium', 'Low Calorie', 'Low Fat', 'Low Fibre',
 'Non-Carbohydrate', 'Non-Lactose', 'Soft Fluid', 'Semi Fluid', 'Ulcer Diet', 'Nut Free', 'Low Purine',
 'Low Protein', 'High Fibre',
* **Infant and child**:
 'Baby', 'Post Weaning', 'Child', # In airline jargon, baby and infant < 2 years. 1 year < Toddler < 3 years.
* **Other**:
 'Seafood', 'Japanese',


Seat
----

The requested seat - values are "Window" / "Aisle".

Airline
-------

Airlines are related to the location from which the flight departs and will appear under that location.

A list of the Red airlines that are options requested from a given location. Each item in the list is an object with
these attributes:

* airline - contains the official airline name
* iata - contains the IATA code of the airline
* flight_number (optional) - contains the flight number of the requested flight,
if it is available. Otherwise this attribute is not present

In case that the airlines requested apply to all locations they will appear in EACH location.

In API v1.0 all airlines will also appear in global scope. This is will become obsolete in v1.1

Alliance
--------

A list of requested airline alliances. Each item on the list is a dictionary:

* Name - Contains the name of the alliance, currently supporting: Star Alliance, SkyTeam, Oneworld

Seat Class
----------

Requested seat class.

Values are an array of this enumeration (regardless of how the class is called by a particular airline)
   * First
   * Business
   * Premium
   * Economy

Example: "business or first class" results in key value [Business, First]


One-Way
-------

Specific request for one way trip.

Example: "united airlines one way flights to ny"

Boolean Attribute.


Two-Way
-------

Specific request for round trip.

Example: "3 ticket roundtrip from tagbilaran to manila/ 1/26/2011-1/30/2011"

Request Attributes
==================


| There are many general request attributes that apply to the entire request and not just some portion of it.
| Examples: "last minute deals" and "Low deposits".

Last Minute Deals
-----------------

Looking for last minute travel deals - Boolean attribute.

Low Deposit
-----------

Looking for Low Deposit travel vacations - Boolean attribute.


Transport Type
--------------

The requested type of transportation. It uses the following enumeration:

* Bus
* Train
* Coach
* Airplane
* Transfer
* Taxi
* Shuttle
* Hovercraft
* Cruise

The actual value is a list of potential vehicles for the travel (e.g. "bus or taxi").

The transport type will be listed as part of the Related Location - the origin of the requested travel.

Fares
-----

The GDS fares. An enumeration:

* Private (equates to a ‘:P’ modifier being added to an itinerary).
* Public (equates to a ‘:N’ modifier being added to an itinerary).
* Net (equates to a ‘:C’ modifier being added to an itinerary).
* Agency Private (equates to a ‘:G’ modifier being added to an itinerary).


Corporate Fares
---------------

* Ask to use the corporate prices - a boolean attribute


Travel Agent Rates
------------------

* Ask to use the Travel Agency / Travel Industry rates - a dictionary with the following keys:

**Requested** - Boolean


Convention Rates
----------------

* Ask to use the Convention rates - a dictionary with the following keys:

**Requested** - Boolean


Military Rates
--------------

* Ask to use the Military rates - a dictionary with the following keys:

**Requested** - Boolean


Government Rates
----------------

* Ask to use the Government rates - a dictionary with the following keys:

**Requested** - Boolean


Reservation ID
--------------

A reservation ID (e.g. "reservation # 12345")

Refundable
----------

* Ask for refundable tickets

**Requested** - Boolean

Flexible Dates
--------------

* Ask for  flexible dates

**Requested** - Boolean

Scope
-----

The requested scope of the query. A dictionary with one or more of the following keys:

* "hotel"
* "flight"
* "cruise"
* "car"

The value of each of the items in the dictionary is an enumeration:

* "only" - as in the request "flights only"
* "no" - as in the request "no hotel"


Sort
----

A request to sort the results. A dictionary with one or more of the following string keys:

**Requested** - Boolean

**Order** - an Enumeration with the following string values:
   * "ascending"
   * "descending"
   * "reverse"
**By** - an enumeration with the following string values:
   * "reviews"
   * "location"
   * "price"
   * "price per person"
   * "distance"
   * "rating"
   * "guest rating"
   * "stars"
   * "time"
   * "total time"
   * "duration"
   * "arrival time"
   * "departure time"
   * "outbound arrival time"
   * "outbound departure time"
   * "inbound arrival time"
   * "inbound departure time"
   * "airline"
   * "operator"
   * "cruiseline"
   * "cruiseship"
   * "name"
   * "popularity"
   * "recommendations"

Geo Attributes
==============


Various attributes describing locations.

Winter Sun
----------

Locations where the sun shines in the winter (assuming northern hemisphere origin) - Boolean attribute.

Mountains
---------

Locations in the mountains - Boolean attribute.

Hot Location
------------

Somewhere hot - Boolean attribute.

Cold Location
-------------

Somewhere cold - Boolean attribute.

Sunny Location
--------------

Somewhere sunny - Boolean attribute.

Island
------

Some island destination - Boolean attribute

Nearby
------

Indicates requested proximity to a location.
Related to a location and will appear in that location.
The value is boolean.

Distance
--------

Indicates a requested distance from a location.
Related to a location and will appear in that location.
The value is a dictionary with the following keys:

* Quantity    - a number indicating how many units of distance are requested
* Units       - An enumeration with the following values:
    + Kilometers
    + Miles
    + Nautical Miles
    + City Blocks
    + Minutes (as in "not more than a 3 hours' drive from the airport")
* Restriction - An enumeration with the following values:
    + Less Than
    + More Than
* Transport   - An enumerations with the following values:
   + Walking
   + Car
   + Public Transportation
   + Bus
   + Taxi
   + Train
   + Airplane
* KM Quantity - The distance in KM, regardless of the original units used. This is the easiest attribute to use.

Center
------

This attribute indicates requested location is in the center of another, related location (e.g. hotel in 'the center of Chicago').
Related to a location and will appear in that location.
The value is boolean.

Downtown
--------

This attribute indicates requested location is in the downtown of another, related location (e.g. hotel in 'the downtown of Chicago').
Related to a location and will appear in that location.
The value is boolean.

Beach
-----

This attribute indicates requested location is by a beach - Boolean attribute


Nowhere
-------

This attribute indicates travel without a specific destination - Boolean attribute

Around the World
----------------

This attribute indicates travel around the world - Boolean attribute

Airport
-------

This attribute indicates an Airport - Boolean attribute

Office
------

This attribute indicates requested location is an office of a related location (e.g. 'at the Chicago office').
The attribute will be returned "inside" the related location of the results.
The value is boolean.


Cruise Attributes
=================

These are attributes describing the requested cruise.

Cruiseline
----------

A list of the requested cruiselines. Each item in the list is a dictionary:

* Name - contains the official cruiseline name

Cruiseship
----------

A list of the requested cruiseships. Each item in the list is a dictionary:

* Name - contains the official cruiseship name


Cabin
-----

An enumeration of the types of cabin:

* Windowless
* Regular Cabin
* Balcony
* Port-Hole
* Picture
* Full Wall
* Balcony
* Internal
* Oceanview
* Window
* External
* Suite
* Cabin
* Mini Suite
* Family Suite
* Presidential Suite

Pool
----

The ship has a swimming pool - an enumerated attribute:

* 'Any'      - The ship needs to have a pool
* 'Indoor'   - The ship needs to have an indoor pool
* 'Outdoor'  - The ship needs to have a outdoor pool
* 'Children' - The ship needs to have a children's pool

Family
------

A family friendly cruise - Boolean attribute


Romantic
--------

A Romantic cruise - Boolean attribute


Adventure
---------

A cruise with an Adventure motif - Boolean attribute

Board
-----

The cruise board, an enumeration with the following potential values:

* Full Board
* All Inclusive

Quality
-------

The quality of the cruise, measure in Stars.
The return value is a Array with 2 numbers (or null):

* Min Stars  = integer from 0 to 6
* Max Stars  = integer from 0 to 6

Examples:

* "2 to 3 stars"     -> [2, 3]
* "At least 4 stars" -> [4, null]
* "1 star"           -> [1, 1]
* "Contemporary"     -> [3, 4]

Child Free
----------

A Child free cruise (adults only) - Boolean attribute

Yacht
-----

A Yacht - Boolean attribute

Barge
-----

A Barge - Boolean attribute


Sailing Ship
------------

Sailing Ship - Boolean attribute

River Cruise
------------

A River Cruise - Boolean attribute

Ship Size
---------

A Ship Size attribute - an enumeration of:

* Small
* Medium
* Large

For Singles
-----------

A Cruise for singles - Boolean attribute

For Gays
--------

A Cruise for gays - Boolean attribute

Steamboat
---------

A Steamboat cruise - Boolean attribute

Pet Friendly
------------

A pet friendly cruise - Boolean attribute

Yoga
----

A Yoga cruise - Boolean attribute

Land Tour
---------

Land Tours - Boolean attribute


One-Way
-------

Specific request for one way trip - Boolean attribute.


Car Attributes
=================

These are attributes describing the requested car rental.

Car Rental Vendor
-----------------

Car rental agency - a list of options of car rental agency.

For each car rental agency a dictionary containing:

* 'Name'  - The official name of the agency
* 'Code'  - A string code for the agency

Car Rental Program
------------------

Car Rental Program - a list containing an enumeration of the following:

* "Avis Wizard"
* "Hertz Gold"
* "Budget RapidRez"
* "Budget Fast Break"
* "National Emerald Aisle"
* "Sixt Express",
* "Alamo Insiders"
* "Dollar Express"
* "Enterprise Plus"
* "Europcar Privilege"
* "Thrifty Blue Chip"


GPS
---

Satellite navigation - Boolean attribute.

Snow Tires
----------

Snow Tires - Boolean attribute.

Hybrid
------

A hybrid electric vehicle (HEV) - Boolean attribute

Green
------

A Green, environmentally friendly vehicle - Boolean attribute

Transmission
------------

Car Transmission - an enumerated attribute:

* 'Manual'     - Manual Transmission
* 'Automatic'  - Automatic Transmission

Car Type
--------

Type of car  - an enumerated attribute:

* 'Mini'
* 'Economy'
* 'Compact'
* 'Intermediate'
* 'Standard'
* 'Full Size'
* 'Mini Van'
* 'Luxury'
* 'Premium'
* 'Intermediate SUV'
* 'Standard SUV'
* 'Full Size SUV'
* 'Full Size Pickup'
* 'Convertible'

Air Conditioning
----------------

Is the car air conditioned? - Boolean attribute.

Car Doors
---------

How many car doors are requested? A list of integer options.

Skoking
-------

Smoking in the car? A Boolean attribute

Satellite Radio
---------------

Satellite Radio - Boolean attribute

Fuel Efficient
--------------

Fuel Efficient - Boolean attribute

ABS
---

Vehicle with ABS - Boolean attribute

Ski Rack
--------

Vehicle with a ski rack - Boolean attribute

Roadside Assistance
-------------------

Roadside Assistance requested


Car Child Seat
--------------

A list of requested child seat elements, each with these potential attributes:

* Quantity - a number
* Direction - an enumeration with the following values:
    + "Front Facing"
    + "Back Facing"
    + "Convertible"
* Position - an enumeration with the following values:
  + "Front Seat"
  + "Back Seat"

Tranmission Type
----------------

Sorry about the typo. To be fixed in the next release of the API.
An enumeration:

* Manual

* Automatic


Activity Attributes
===================

These are attributes describing activities.

Note: We are constantly adding activities. If you find something you wish was on the list, please let us know.

Here is a list of currently supported activities:

* Climbing - Various Climbing activities.

* Trekking

* Hand Gliding

* Hot Air Balloon

* Diving

* Snorkeling

* Mountain Bike

* Paragliding

* Survival Training

* Martial Arts

* Photography

* Dog Sledding

* Bird Watching

* Tours

* Rafting

* White Water

* Walking

* Water Sports

* Volcanology

* Summer Camp

* Archaeology

* Horse Riding

* Tennis

* Extreme Sports

* Astronomy

* Shopping

* Fooding

* Partying

* Theme Parks

* Wine Tasting

* Weaving

* Performing Arts


Ski Attributes
==============

Ski Hire
--------

The Ski Hire attribute is a complex structure, containing **a list** of equipment elements, each with the following attributes:

* Multiple         - How many of the same equipment (e.g. 3 adult snowboards)
* Equipment Type   - An enumeration:
  + Skis
  + Snowboard
  + Mini Skis
* Boots           - Would you like boots with your gear?
 Boolean, appearing in response only if implicitly specified
* Helmet          - Would you like a helmet with your gear?
 Boolean, appearing in response only if implicitly specified
* Poles           - Would you like poles with your skis?
 Boolean, appearing in response only if implicitly specified
* Quality         - An enumeration (based on definitions from http://www.snowrental.net/):
  + Exclusive
  + Premium
  + Standard
  + Low cost
  + Starter

* Person          - An enumeration (based on definitions from http://www.snowrental.net/):
   + Regular
   + Women
   + Teenager  : 12 - 15 years
   + Junior    : 7  - 12 years
   + Child     : Up to 6 years

* Guarantee       - Would you like a guarentee for your gear?

Boolean, appearing in response only if implicitly specified


Warnings
========


Various Warnings provided by the system.

API Warning
-----------

API related warnings:

Unsupported Version - An unsupported API version is used, please check documentation for supported versions.

Obsolete Version - An obsolete API version is used, please upgrade to a newer version.

Unspecified Version - API version was unspecified - latest version is used.

Time Warning
------------

Time issues related warnings:

Past Date - There was some past date in the request.

Bad Order - Some of the time Order may be incorrect (an earlier event specified after a later one).

Dates Conflict - Two or more dates seem to refer to the same event ("Fly to NY on Monday. Depart on Tuesday")

Parse Warning
-------------

Parsing issues:

The value is an unparsed part of the text

Home Warning
-------------

Bad input at the home request parameter issues:

Unknown Location - The string does not seem to represent any known location (ex: "home=some_strange_string")

Ambiguous Location - The string represents an ambiguous location name with no clear choice (ex: "home=arlington")
