.. _rest_api:

====================
The HTTP RESTful API
====================

.. highlight:: none

Location IDs
============
Locations returned by Eva are identified using the `Geonames <http://www.geonames.org/about.html>`_ tagging system. 
Geoname IDs are integers. 

Eva also provides a list of prioritized airports for each location in the API reply.
Airports are identified by their
`IATA code <http://en.wikipedia.org/wiki/International_Air_Transport_Association_airport_code>`_.

Other identification schemes as well as customer specific codes are available on demand.

JSON
====
The web service reply is `JSON <http://en.wikipedia.org/wiki/Json>`_ (an acronym for JavaScript Object Notation) encoded.

URL Encoding
============
The parameters for the web service have to be both UTF-8 and URL encoded. 
If you call the web service with "New York" you have to URL encode "New York", otherwise our service 
will search for "New" and the rest of the sentence, as well as all the other parameters will be lost. 
When URL encoding, "New York" becomes "New+York". With UTF-8 encoding ö becomes %C3%B6. 

URL Encoding replaces spaces with "+" signs, and unsafe ASCII characters with "%" followed by their hex equivalent. 
Safe characters are defined in RFC2396. 
They are the 7-bit ASCII alphanumerics and the mark characters "-_.!~*'()". 

Versions
========
API versions are specified via the URL in the following manner:
`http://freeapi.evature.com/v1.0?input_text=chicago`__

__ http://freeapi.evature.com/v1.0?site_code=123&api_key=456&input_text=chicago

.. automodule:: core.api_versions
   :synopsis: Supported API versions

.. _maintaining_state:

Maintaining State - Sessions and Meta-Sessions
==============================================
The Eva web service provides two modes of operation - `Stateless`_ and `Statefull`_.
The mobile SDKs automatically maintain state.

Stateless
---------
In Stateless mode, Eva provides the best understanding of the input regardless of missing information and ambiguity.
Since there in no state there cannot be any Discourse and Eva cannot ask questions.
To invoke Eva in Stateless mode, simply omit the session_id parameter.
Example::

    User: "one way flight from JFK"

http://freeapi.evature.com/v1.0?input_text=one+way+flight+from+JFK
 
.. code-block:: javascript
    :caption: Simplified Eva API Reply

    "api_reply": {
        "Flow": [
          {
            "SayIt": "One way flights from John F Kennedy International Airport New York", 
            "Type": "Flight", 
            "RelatedLocations": [
              0, 
              1
            ]
          }
        ], 
        "Locations": [
          {
            "Airports": "JFK", 
            "Name": "'JFK' = John F Kennedy Intl, US", 
            "Request Attributes": {
              "Transport Type": [
                "Airplane"
              ]
            }, 
            "Type": "Airport", 
          }, 
          {
            "Actions": [
              "Get There"
            ]
          }
        ], 
        "Flight Attributes": {
          "One-Way": true
        }, 
      }  

Basically, what Eva is telling the application is that the end user is requesting a flight from JFK airport heading "somewhere".

Statefull
---------
To initiate a new session add a session_id request parameter with a value of '1'. Example::

    User: "one way flight from JFK"

http://freeapi.evature.com/v1.0?input_text=one+way+flight+from+JFK&session_id=1

In this case, the API reply will change. Eva instructs the application using the Flow mechanism to ask the user
where he wants to fly to.

.. code-block:: javascript
    :caption: Simplified Eva API Reply

    "session_id": "11e5-78fa-94ba0740-8acf-22000bd848a8", 
    "api_reply": {
        "Flight Attributes": {
          "One-Way": true
        }, 
        "Flow": [
          {
            "Type": "Question", 
            "SayIt": "Where would you like to fly to?"
          }
        ], 
        "Locations": [
          {
            "Airports": "JFK", 
            "Name": "'JFK' = John F Kennedy Intl, US", 
            "Request Attributes": {
              "Transport Type": [
                "Airplane"
              ]
            }, 
            "Type": "Airport", 
          }, 
          {
            "Actions": [
              "Get There"
            ]
          }
        ], 
      }

You will also notice that Eva returns a new session_id.
Use this session_id in subsequent requests to continue the session.
If, for example the user replies with::

    User: "SFO"

http://freeapi.evature.com/v1.0?input_text=SFO&session_id=11e5-78fa-94ba0740-8acf-22000bd848a8

Eva will continue the dialog:

.. code-block:: javascript
    :caption: Simplified Eva API Reply

    "session_id": "11e5-78fa-94ba0740-8acf-22000bd848a8", 
    "api_reply": {
        "QuestionAnswered": true, 
        "Flight Attributes": {
          "One-Way": true
        }, 
        "Flow": [
          {
            "Type": "Question", 
            "SayIt": "Please specify, When would you like to depart from John F Kennedy International Airport New York to San Francisco International Airport California?"
          }
        ], 
        "Locations": [
          {
            "Airports": "JFK", 
            "Name": "'JFK' = John F Kennedy Intl, US", 
            "Request Attributes": {
              "Transport Type": [
                "Airplane"
              ]
            }, 
            "Type": "Airport", 
          }, 
          {
            "Airports": "SFO", 
            "Name": "'SFO' = San Francisco International, US", 
            "Actions": [
              "Get There"
            ], 
            "Type": "Airport", 
          }
        ], 
      }

Here is an example of accumulating state::
    
    User: "Hotels in Los Angeles tomorrow for 2 nights"
     - Eva instructs the application to show a list of hotels in Los Angeles
    User: "3 stars"
     - Eva instructs the application to show a filtered list of 3 stars hotels in Los Angeles

.. _metasessions:

Meta-Sessions
-------------

Sessions may expire by the server due to inactivity so the developer needs to be prepared to save
the latest *session_id* returned from Eva, which may be different from the *session_id* that was sent.

Eva may also start a new session if the end user specifically said "start over" (or similar request).

Furthermore, the developer may force a session reset by sending a *session_id* with a value of '1' at any time,
for example if the end user requested to start over by clicking on a trash-can icon in the GUI.

In order for Eva to better understand and adapt to the end users by maintaining history on a per-end-user basis across sessions,
as well as better statistics gathering and reporting,
the developer needs to add a globally unique *uid* parameter to each request. See :ref:`uid` for details.


Flow
====
Eva manages the conversation with the end users automatically, asking questions and even handling chit-chat as needed.
When using the raw API directly (not via the SDK) Eva instructs the application to do things on her behalf,
such as asking the user a question, or performing a cruise-search.
The instructions to the application are gathered in a section of the reply called the Flow.
The Flow is a list of Flow Actions, such as:

.. code-block:: javascript
    :caption: Simplified Eva API Reply

    "Flow": [
      {
        "QuestionType": "Open", 
        "Type": "Question", 
        "RelatedLocations": [
          0
        ], 
        "QuestionSubCategory": "Departure", 
        "ActionType": "Flight", 
        "QuestionCategory": "Missing Date", 
        "SayIt": "Please specify, When would you like to depart from John F Kennedy International Airport New York to San Francisco International Airport California?"
      }
    ]

The Flow is the main integration point for the application with the Eva API reply.

Internally, the Flow is created by the following Eva logic blocks: 

#. **Utterance Classifier** 
   
   Analyzes the input utterances and classifies them into various categories
   such as a 'Hotel Search', 'Rental Car Search', 'Flight Search', 
   as well as 'Chat', 'Itinerary Request', 'Question', 'Answer' or a combination of the above. 
   For example, an input of "3 nights in NY" would be classified as a Hotel Search, 
   while an input of "United Airlines to Boston" would be classified as a Flight Search.
   The utterance classification is the key input to Eva's Desires (motivational state and applicative objective).
   Other inputs to the classification are the utterance metadata, such as :ref:`context`.
   For example, the user might say "Chicago" when looking at the hotel search page in the application,
   and this utterance would be categorizes as a Hotel Search,
   while the same utterance would be categorized as a Rental Car Search if the end user is looking at the rental cars page.

#. **Desire Manager**
   
   Desires represent Eva's motivational state.
   They represent objectives that Eva would like to accomplish or bring about. Examples of desires may be: 

   * Flight Search
   * Hotel Search
   * Rental Car Search

   There may be multiple desires in a single session (e.g. "Chicago flights and hotel"),
   however Eva maintains a single Goal in the Dialog Manager as it goes through the desires until they are met.
   This is consistent with the behavior of a human Travel Agent, which usually anchors the flights and then
   moves on to finding accommodations and ground transportation. 
   Desires are maintained in the server session state to allow for Dialog.

#. **Belief Manager** 
   
   Manages Eva's beliefs inside the session state with respect to the predefined abilities and requirements of the application
   and the Travel search engine.
   Using the term `belief` rather than `knowledge` recognizes that what Eva believes in may not necessarily be true
   (and in fact may change in future utterances).
   This is especially important when using Voice input as Eva may have heard the user incorrectly,
   but is also valid with Text input in case of spelling mistakes or input ambiguity.

   **Example of disambiguation**::

       User: "Hotel in Arlington"
       Eva:  "Which "Arlington" did you mean?"
       User: "Kentucky"
        - Eva instructs the application to show a list of hotels in Arlington Kentucky

   **Example of correction**::

       User: "Hotel in Paris"
        - Eva instructs the application to show a list of hotels in Paris, France
       User: "I meant Paris Texas"
        - Eva instructs the application to show a list of hotels in Paris, Texas
   
   Based on the classification of the input, Eva may realize that key information is missing to achieve the Goal.
   Examples of missing information pieces are 'Missing Date', 'Missing Location' and 'Missing Duration'.
   For example, let's assume the booking engine needs an explicit Duration for hotel searches
   and the user requested "Hotel in Madrid tomorrow".
   The Belief Manager will identify the Duration as a missing requirement, which leads to the:

#. **Dialog Manager** 
   
   Facilitates a non-linear state-full dialog with the user for clarifications, questions and answers, disambiguation and so on.
   The Dialog manager chooses a Goal (a single active Desire) and reviews the Beliefs related to achieving this goal,
   asking questions when necessary and reviewing the received information.
   
   **Example of questions**::

      User: "Flights to NY"
      (Assuming the belief engine identifies a missing departure time)
      Eva:  "When would you like to depart from Chicago, Illinois?"
      User: "Tomorrow night"
      - Eva instructs the application to show a list of flights from Chicago to New York departing July 2nd at 8:00PM

   Linearity is not mandated, for example::

      User: "Flight to SFO"
      Eva: "Where would you like to fly from?" (assumes no GPS or related metadata)
      User: "One way from Chicago on the 23rd"
      - Eva instructs the application to show a list of one-way flights from Chicago to SFO departing July 23rd


#. **Flow Engine** 

   Orchestrates the Utterance Classifier, the Desire and Belief Managers and the Dialog Manager to returns a Flow of Actions. 
   This Actions Flow is ordered by "Travel Logic" (for example, search for flights first, hotels later). 
   
   The Flow Actions can be 'Answer', 'Question', 'Greeting', 'Statement', 'Hotel', 'Car', 'Flight'. 
   The Flow Actions are a simple Todo list for the application to implement, e.g.:

   * Search for flights from Boston to New York City
   * Ask the user how many days he wants to stay at his New York hotel?
   * Search for a hotel in New York City
   * Show the boarding pass

   Each Action has its own SayIt to feed into the Text-to-Speech engine.

See :ref:`flow` for details.   

.. _multiple_input_text:

Multiple Input Texts
====================
When the end-user text originates from a Speech Recognition engine, there are often several probable hypotheses.
Eva implements a rescorring mechanism which is domain-specific and context aware.
This feature significantly improves the quality of the speech recognition engine by fully utilizing its response.
Speech recognition engines are usually generic (not trained specifically in the Travel domain).
Moreover, they are missing the context of the conversation, as for example they would not be aware that
the user was asked a question, such as When she would like to stay at the hotel,
thus have no way of prioritizing "Today" over "Two Day", especially as many users enunciate their speech.

* Use the following endpoint for the Eva service: https://vproxy.evaws.com

* Add all the input_text query parameters to the request URL **in the order returned by the speech recognition engine**.

* Don't forget to add :ref:`from_speech`, :ref:`scope`, :ref:`context` as usual.

* The chosen input text might be different than the one you currently display
  (which is usually first result from the speech recognition engine).
  This will need to be corrected in case Eva selects a different input when Eva replies.

For example, assume the speech recognition engine returned these results:

-  "flint to roston"
-  "flight to boston"
-  "slight to horton"

This is the resulting URL:

`vproxy.evaws.com/v1.0?input_text=flint+to+roston&input_text=flight+to+boston&input_text=slight+to+horton`__

__ https://vproxy.evaws.com/v1.0?site_code=123&api_key=456&scope=fhc&session_id=1&input_text=flint+from+jail+aviv+to+roston&input_text=flight+from+tel+aviv+to+boston&input_text=slight+from+beit+achziv+to+horton

  