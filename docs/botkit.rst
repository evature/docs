.. _eva_botkit:

==============
The Eva BotKit
==============

.. highlight:: none


Overview
========
The Eva BotKit enables building a single AI assisted Bot for providing applicative Travel functionality across
all messaging platforms with a bot platform API.
Botkit bundles Eva's Natural Language Understanding and Dialog Management features with robust cloud based spelling correction.
Furthermore, the Eva API reply is automatically parsed and dialog is handled by Eva.
The backend application is only called upon to implement applicative directives, such as *ShowBoardingPass* or *PerformFlightSearch*.
Applicative integration is done via customizable webhooks.
Eva automatically reformats the applicative webhook replies to comply with all messaging platforms so you don't have to integrate
separately with each one.

Integration with all messaging platforms consists of the following steps:

#. **Create a new Bot**

   Log in to  https://chat.evature.com/botkit using your Eva credentials.

   .. note::

      For **free** API access please register here: https://w.evature.com/registration/form

   You will be prompted to create a new Bot, proving a name, a description and a default greeting.


#. **Add a Chat Service Integration**

   Add a chat integration with one of the following providers::

   * Facebook
   * Telegram
   * Line
   * Slack
   * Kik
   * SMS
   * WeChat
   * Skype

   The integrations are platform specific.

#. **Implement applicative webhooks**

   Eva defines many webhook functions for applicative requests that may be queried by the end users.
   This is usually existing functionality in your backend servers that the developer
   needs to "wire" to the corresponding webhook function.

   Here are some examples:

   * Perform a Flight Search
   * Perform a Hotel Search
   * Show a Boarding Pass
   * Show an Itinerary

   You can simply ignore the applicative webhooks that are non-applicable to your backend.
   Eva will automatically reply to end users explicitly requesting these services with a "not supported" message.


#. **Add more messaging platform integrations**

   Repeat step 2 to provide additional messaging platform integrations.


Chat Service Integrations
=========================

Here is the ever growing list of Chat Service integrations.

Telegram integration
--------------------

#. **Create a new Telegram Bot**

   Currently this can only be done by chatting with BotFather from within the Telegram application.
   BotFather is available `Here <https://web.telegram.org/#/im?p=@BotFather>`_

   Tell him I sent you.

   Create a new Bot by issuing the **/newbot** command.

   Follow the in-app configuration instructions until the bot is created.
   You will be provided with an HTTP API token such as "232021539:AAGGFCHb3dRCkOIi18Vscnu7T6bDzWcb_ro"

#. **Create a new Telegram Integration**

   Head back to https://chat.evature.com/botkit and (after logging in if needed), click on the **Add Chat Integration** button.

   Choose Type = Telegram.

   Type in your Telegram HTTP API token.


#. **Say hi to Eva on Telegram!**

   Now try chatting with your new bot in Telegram! Go ahead - try typing "hi" and "Who are you?"


Line integration
----------------

   .. note::

        On September 29 LINE announced the release of Messaging API,
        which will improve bot development and functionality as well as help better support developers.  
        
        **All BOT API Trial Accounts are scheduled to be deleted on November 16**.



#. **Create a new Line Bot**

   Create a Line messaging API account from the LINE Business Center.
   You need to have a business account - https://business.line.me

#. **Create a new Line Integration**

   Head back to https://chat.evature.com/botkit and (after logging in if needed), click on the **Add Chat Integration** button.

   Choose Type = "Line - Messaging API".

   Fill in your Channel Secret and access token.

#. **Configure Eva as the Line Bot**

   Set the Webhook URL to the value provided after saving the "Chat integration" in Botkit admin.

#. **Say hi to Eva on Line!**

   Scan the QR code in Line Business center.  
   Now try chatting with your new bot in Line.
   Go ahead - try typing "hi" and "Who are you?"


Facebook Messenger integration
------------------------------

#. **Facebook Page and App**

   Create a new Facebook App and Page or use existing ones.
   Your Facebook App can remain in sandbox mode and your Page does NOT have to be publicly visible.
   The Page profile pic and name will be used to form the "identity" of your bot and is what people will see when they engage it.
   Please note your Page "Facebook Page ID", e.g. 135827446828726

   Go to your app settings and, under Product Settings, click "Add Product." Select "Messenger."
   In the settings you will see a Token Generation section. Select your Page and copy the generated Page Access Token.


#. **Create a new Facebook Integration**

   Head back to https://chat.evature.com/botkit and (after logging in if needed), click on the **Add Chat Integration** button.

   Choose Type = Facebook.

   Fill in the Page Access Token generated in the previous step.

   Fill in your Facebook Page ID.

   Click Save.


#. **Configure Eva as the Facebook bot**

   After you create Facebook Integration you will be guided on screen to go back to your Facebook Admin and do the following:

   Under the "PRODUCT SETTINGS" section, click on the "Messenger" product you just added,
   find the Webhooks section and click Setup Webhooks.
   Enter the following URL for a webhook - "https://chat.evature.com/fb".

   Enter the Verify Token that will shown in Botkit's Admin.

   Select all checkboxes under Subscription Fields, specifically: message_deliveries, message_echoes, message_reads, messages,
   messaging_account_linking, messaging_optins, messaging_postbacks.

   Verify and Save.

   You should see a green checkmark with the text "Completed".
   
   In that same panel, Select your pages to subscribe your webhook to the page events in the "select a page" drop-down and
   click "Subscribe".

#. **Request Permissions for your app**

   Under the "PRODUCT SETTINGS" section, click on the "Messenger" product you just added,
   find the App Review for Messenger section and click Request Permissions.


   Select pages_messaging

   Click Add 1 Item


#. **Say hi to Eva on Facebook Messenger!**

   Now try chatting with your new bot in Facebook Messenger. Go ahead - try typing "hi" and "Who are you?"


Kik integration
---------------


#. **Create a new Kik Bot**

   Using the Kik application scan the QR here - https://dev.kik.com/#/home

   You will start a chat with Botsworth.

   Note the Bot username from the chat with Botsworth.

   Once the bot is created Botsworth will suggest to log you in to the Bot Dashboard.

   In the configuration you will be able to see your API key, which looks like this: "e15ee13d-e84f-466e-b93e-d2c1eb0508f7"



#. **Create a new Kik Integration**

   Head back to https://chat.evature.com/botkit and (after logging in if needed), click on the **Add Chat Integration** button.

   Choose Type = Kik.

   Fill in the username and API Key generated in the previous step.

   Click Save.


#. **Say hi to Eva on Kik!**

   Now try chatting with your new bot in Kik. Go ahead - try typing "hi" and "Who are you?"


Skype integration
-----------------

#. **Create a new Skype Bot**

   You will need to register as a developer here:
   https://www.skype.com/en/developer/
   
   Then head over to "register a bot" at https://dev.botframework.com/bots/new
   
   In the Configuration / Messaging endpoint
   please enter
   "https://chat.evature.com/skype"
   Press:
   Create Microsoft App ID
   Generate App ID and password
   Make sure to copy the application ID and password!



#. **Create a new Skype Integration**

   Head back to https://chat.evature.com/botkit and (after logging in if needed), click on the **Add Chat Integration** button.

   Choose Type = Skype.

   Type in your Skype App ID and App Secret (the password).


#. **Make sure your endpoint is configured correctly**

   In the Bots page, https://dev.botframework.com/bots
   Under "Test connection to your bot", press the **Test** button.
   You should see: "Endpoint authorization succeeded".

#. **Add your new bot to Skype**

   In the https://dev.botframework.com/bots page, in the Channels pane next to Skype,
   press the **Add to Skype** button.
   
   .. note::

      Skype Bots might not be available in your country yet.
      You might have to workaround this by changing your billing address, or using a pre-release client,
      such as this: https://community.skype.com/t5/Linux/Where-to-get-the-latest-Skype-for-Linux-Alpha/td-p/4536964 

#. **Say hi to Eva on Skype!**
   
   Now try chatting with your new bot in Skype! Go ahead - try typing "hi" and "Who are you?"


Adding Webhooks
===============

Here are the list of available applicative webhooks. The list is constantly being updated, based on the input data.
If you would like to add functionality please contact us directly at info@evature.com

For each added webhook there is a demo implementation at https://github.com/evature/botkit-integrations

Evature also provides a simple repository with super simple Python demos of webhook replies:  https://github.com/evature/webhooks

General
-------


All webhooks are HTTP/S POSTs with a JSON encoded body and expect a JSON formatted response.

Eva provides a standardized way to access all messaging providers so you don't need to learn how to integrate with each one.
Eva does this by providing several generic formats of messages that can be returned by the applicative webhooks.
These formats are automatically matched to the native formats supported by each messaging platform:

:Text: Simple text message
:Image: Eva will handle format conversions, resizing and serving multiple resolutions dynamically
:RichMessage: Images with buttons, clickable URLs, Title and Subtitle, optionally grouped together horizontally
:HTML: Eva will render the HTML to an image with the optimal screen setting for each messaging provider
:DataMessage: Template based pre-formatted messages that will render correctly across platforms
:Raw: Properly formatted for the requested messaging provider

In addition, Eva supports returning a list of messages, which will be sent to the end user one by one.

Webhooks deliver a ``messagingProvider`` key which signals the implementation where the request came from.
``messagingProvider`` is an enumeration for the different messaging providers, one of the Chat Service Integrations.
This can be used by the implementation to provide unique, content specific content,
or to apply formatting when returning Raw messages.

Webhooks also deliver a globally unique ``ChatKey``.
This allows the application to asynchronously send messages to the end user by POSTing the data to
https://chat.evature.com/send_botkit_message

When applicable, webhooks also deliver a ``language`` key. Value is a 2 character string with an ISO 639-1 code.
This allows the application to send messages using the correct language.

All DateTimes are in ISO 8601 format https://en.wikipedia.org/wiki/ISO_8601 .
DateTimes that are ranges (e.g. 'next week', or 'July') are expressed as a combination of 2 DateTimes - a "Min" and a "Max".
DateTimes that are NOT ranges are expressed as a combination of 2 IDENTICAL DateTimes.

Here is the minimal webhook reply with a single text message:

.. code-block:: javascript
    :caption: Webhook Reply with single Text message

    {
      "botkitVersion": "0.4.0", // Without this key the content is considered a Raw message and is passed as-is
      "messages": [
        {
          "_type": "TextMessage",
          "text": "Hello"
        }
      ]
    }

When asynchronously sending messages to the end user by POSTing the data to https://chat.evature.com/send_botkit_message ,
The ``ChatKey`` must be included in the reply:


.. code-block:: javascript
    :caption: Single Text message, sent asynchronously

    {
      "botkitVersion": "0.4.0",
      "chatKey": "3648b2a2-1aee-4d5a-7ef4-13a0aa441c21", // Is Mandatory only when asynchronously sent
      "messages": [
        {
          "_type": "TextMessage",
          "text": "Good Morning!"
        }
      ]
    }

Here is an example of returning a picture:


.. code-block:: javascript
    :caption: Webhook Reply with single Image message

    {
      "botkitVersion": "0.4.0",
      "messages": [
        {
          "_type": "ImageMessage",
          "imageUrl": "http://image-url.com/url-to-img",
        },
      ]
    }


Here is an HTML message response:


.. code-block:: javascript
    :caption: Webhook Reply with an HTML message

    {
      "botkitVersion": "0.4.0", // Without this key the content is considered a Raw message and is passed as-is
      "messages": [
        {
          "_type": "HtmlMessage",
          "height": 200,
          "width": 350
          "html": "<h1>Hello World</h1> <strong>This</strong> <small>is</small> <em>HTML</em>",
        }
      ]
    }

Here is a Rich message response:

.. code-block:: javascript
    :caption: Webhook Reply with an Rich message

    {
      "botkitVersion": "0.4.0", // Without this key the content is considered a Raw message and is passed as-is
      "messages": [
        {
          "_type": "RichMessage",
          "imageUrl": "http://url-to-img.com/image.jpg",
          "title": "The RichMessage Title",
          "subtitle": "Subtitle will appear below the title (optional)",
          "url": "http://image-clicked.com",    // optional - clicking the image will open webbrowser to this url
          "buttons": [    // optional
              {"_type": "ButtonMessage", "text": "click to open webbrowser", "url": "http://button-pressed.com"}
          ]
        }
      ]
    }

Here is "MultiRich" message response - horizontally scrolled list of Rich messages:

.. code-block:: javascript
    :caption: Webhook Reply example with MultiRichMessage

    {  "botkitVersion": "0.4.0",
       "messages": [
          { "_type":"MultiRichMessage", "messages":[
             { "_type": "RichMessage", ... see above ... },
             { "_type": "RichMessage", ... see above ... },
          ]}
       ]
    }

Here is a "DataMessage" template based response - for Flight Status:

.. code-block:: javascript
    :caption: Webhook Reply example with DataMessage - for Flight Status

    {  "botkitVersion": "0.4.0",
       "messages": [
        {
          "_type":"DataMessage",
          "subType":"airline_update",
          "asAttachment":false,
          "jsonData":{
            "flight_number":"UAL123",
            "departure_airport":{
              "terminal":"",
              "city":"London Heathrow",
              "airport_code":"LHR",
              "gate":"232"
            },
            "arrival_airport":{
              "terminal":"B",
              "city":"Washington Dulles Intl",
              "airport_code":"IAD",
              "gate":"C2"
            },
            "flight_schedule":{
              "departure_time_actual":"2016-08-09T08:16:00",
              "arrival_time":"2016-08-09T10:51:00",
              "departure_time":"2016-08-09T07:30:00",
              "boarding_time":""
            },
            "airline_name":"United",
            "number":123
          },
          "introMessage":"Here is an example of a Flight Status"
        }
       ]
    }


And here is a "DataMessage" template based response - for a Boarding Pass:


.. code-block:: javascript
    :caption: Webhook Reply example with DataMessage - for Boarding Pass


    {
      "messages":[
        {
          "subType":"airline_boardingpass",
          "_type":"DataMessage",
          "asAttachment":true,
          "jsonData":{
            "seat":"75A",
            "travel_class":"business",
            "auxiliary_fields":[
              {
                "value":"T1",
                "label":"Terminal"
              },
              {
                "value":"30OCT 19:05",
                "label":"Departure"
              }
            ],
            "qr_code":"M1WEISS\\/TAL  CG4X7U nawouehgawgnapwi3jfa0wfh",
            "pnr_number":"CG4X7U",
            "logo_image_url":"https://d2hbukybm05hyt.cloudfront.net/images/airline_logos/logo_JB.png",
            "passenger_name":"TAL WEISS",
            "secondary_fields":[
              {
                "value":"18:30",
                "label":"Boarding"
              },
              {
                "value":"D57",
                "label":"Gate"
              },
              {
                "value":"75A",
                "label":"Seat"
              },
              {
                "value":"003",
                "label":"Sec.Nr."
              }
            ],
            "flight_info":{
              "arrival_airport":{
                "city":"Amsterdam",
                "airport_code":"AMS"
              },
              "flight_schedule":{
                "arrival_time":"2016-01-05T17:30",
                "departure_time":"2016-01-02T19:05"
              },
              "flight_number":"KL0642",
              "departure_airport":{
                "terminal":"T1",
                "city":"New York",
                "airport_code":"JFK",
                "gate":"D57"
              }
            },
            "header_image_url":"https://d1hz6cg1a1lrv6.cloudfront.net/media/images/evature/logo4-19b0ca62fbf2b08e3bbc9d25298523ea4600422e.jpg"
          },
          "introMessage":"Here is an example of a Boarding Pass"
        }
      ],
      "botkitVersion":"0.4.0"
    }


Here is a generic, all inclusive example of a webhook reply that is returned by the implementation:

.. code-block:: javascript
    :caption: Generic Webhook Reply

    {
      "botkitVersion": "0.4.0",
      "chatKey": "1234b2a2-1aee-4d5a-7ef4-13a0aa441cb1",
      "messages": [
        {
          "_type": "TextMessage",
          "text": "Hello"
        },
        {
            "_type": "ImageMessage",
            "imageUrl": "http://url-to-img.com/image.png"
        },
        {
          "_type": "RichMessage",
          "buttons": [
            {
              "_type": "ButtonMessage",
              "payload": null,
              "text": "1st button text",
              "url": "http://button-pressed.com"
            },
            {
              "_type": "ButtonMessage",
              "text": "2nd button text",
              "url": "http://second-button-pressed.com"
            }
          ],
          "imageUrl": "http://image-url.com/url-to-img",
          "subtitle": "subtitle (optional)",
          "title": "title (optional)",
          "url": "http://on-click-url.com/(optional)"
        },
        {
          "_type": "HtmlMessage",
          "height": 200,
          "html": "<h1>Hello World</h1> <strong>This</strong> <small>is</small> <em>HTML</em>",
          "width": 350
        },
        {
          "_type": "MultiRichMessage",
          "messages": [
            {
              "_type": "RichMessage",
              "buttons": [],
              "imageUrl": "http://image-url.com/url-to-img-1",
              "subtitle": null,
              "title": "Image 1",
              "url": null
            },
            {
              "_type": "RichMessage",
              "buttons": [],
              "imageUrl": "http://image-url.com/url-to-img-2",
              "subtitle": null,
              "title": "Image 2",
              "url": null
            },
            {
              "_type": "RichMessage",
              "buttons": [],
              "imageUrl": "http://image-url.com/url-to-img-3",
              "subtitle": null,
              "title": "Image 3",
              "url": null
            }
          ]
        }
      ]
    }


Log Messages between Eva and User
---------------------------------

Allows logging of all communication between Eva to the end user and helpful debug information regarding the integration.  

Eva BotKit logs all activity to this Webhook as simple JSON HTTP POSTs.  

.. tip::

   To set up a simple view for this log, head over to https://gomix.com/  
   
   * Log in to GitHub.  
   
   * Start a new project.  
   
   * Click on the project name, `Advanced Options`, `Import from Github` and input 'iftahh/bot_logger'.  
   
   * Click on `Show` and you will see a scrolling list of logs from the BotKit.  
   
   Enter "Hi" to Eva in any messenger to see some logs.  


Webhooks health
---------------

Please note that a webhook which fails for 5 consecutive times will be disabled.
Use the management UI at https://chat.evature.com/botkit to re-enable.
Disabled webhooks will be colored red.

Session Storage
---------------

BotKit implements a server-side storage for developer convenience.
This is useful for keeping dialog state and known information about the end user (eg. his PNR number or home town),
and to avoid asking the end user the same questions again and again ("Do you like dogs?").
An example scenario is asking the end user what her favorite hotel chain is in the implementation a hotel search webhook.
The next time she requests a hotel search the application can use the favorite hotel chain stored in the Session Storage.
Session Storage is a simple JSON object that is stored in Eva's database per end user.
The sessions are stored forever with no timeout.

Each webhook payload will include the Session Storage (if it is non-empty) in the ``session`` key.

It is the responsibility of the webhook developers to handle the session, adding, modifying and removing information.
For example, you may wish to remove the dialog state after the dialog is complete or a long time has passed.

To remove/add/modify the contents of the Session Storage simply return the updated session in the webhook response ``session`` key.

To examine the session simply check if the webhook payload has a ``session`` key and if so examine its content.


Search for Flights
------------------

When the dialog with the end user is done and Eva has all the required information the flight search webhook is triggered.
Here is an example of a flight search request::


    User: "fly from London to Moscow on Tuesday for 3 adults redeye and return 3 days later"


.. code-block:: javascript
    :caption: Flight Search Request Example

    {"messagingProvider": "FACEBOOK",
     "chatKey": "3648b2a2-1aee-4d5a-7ef4-13a0aa441cb1",
     "attributes": {"redeye": true,
                    "twoWay": true},
     "departDateMax": "2016-05-31T00:00:00",
     "departDateMin": "2016-05-31T00:00:00",
     "returnDateMax": "2016-06-03T00:00:00",
     "returnDateMin": "2016-06-03T00:00:00",
     "origin": {"airports": ["LHR", "LGW", "LCY", "STN"],
                "allAirportsCode": "LON",
                "geoid": 2643743,
                "latitude": 51.50853,
                "longitude": -0.12574,
                "name": "London, United Kingdom",
                "type": "City"},
     "destination": {"airports": ["SVO", "DME", "VKO", "BKA"],
                     "allAirportsCode": "MOW",
                     "geoid": 524901,
                     "latitude": 55.75222,
                     "longitude": 37.61556,
                     "name": "Moscow, Russia",
                     "type": "City"},
     "travelers": {"adult": 3}}

allAirportsCode is a key that exists only for cities that have a special IATA code for searching all-airports.


Search for Hotels
------------------

When the dialog with the end user is done and Eva has all the required information the hotel search webhook is triggered.
Here is an example of a hotel search request::


    User: "3 to 4 star Hilton in paris tomorrow 5 nights sort by price ascending for 2 adults and 3 kids"


.. code-block:: javascript
    :caption: Hotel Search Request Example

    {"messagingProvider": "FACEBOOK",
     "chatKey": "3648b2a2-1aee-4d5a-7ef4-13a0aa441cb1",
     "arriveDate": "2016-05-31T00:00:00",
     "duration": 5,
     "attributes": {"chain": [{"name": "Hilton Hotels",
                               "evaCode": "EPC-47",
                               "gdsCode": "HH",
                               "simpleName": "Hilton"}],
                    "quality": [3, 4]},
     "location": {"airports": ["CDG", "ORY", "BVA", "LIL"],
                  "allAirportsCode": "PAR",
                  "geoid": 2988507,
                  "latitude": 48.85341,
                  "longitude": 2.3488,
                  "name": "Paris, France",
                  "type": "City"},
     "sortBy": "price",
     "sortOrder": "ascending",
     "travelers": {"adult": 2, "child": 3}}


Search for Cars
---------------

When the dialog with the end user is done and Eva has all the required information the car rental search webhook is triggered.
Here is an example of a car rental search request::


    User: "rent an SUV with a GPS from JFK tomorrow morning return in 3 days"


.. code-block:: javascript
    :caption: Car Search Request Example

    {"messagingProvider": "FACEBOOK",
     "chatKey": "3648b2a2-1aee-4d5a-7ef4-13a0aa441cb1",
     "attributes": {"carType": "Standard SUV", "GPS": true},
     "destination": {"airports": ["JFK"],
                     "allAirportsCode": null,
                     "geoid": "JFK",
                     "latitude": 40.633333,
                     "longitude": -73.783333,
                     "name": u"'JFK' = John F Kennedy Intl, US",
                     "type": "Airport"},
     "origin": {"airports": ["JFK"],
                "allAirportsCode": null,
                "geoid": "JFK",
                "latitude": 40.633333,
                "longitude": -73.783333,
                "name": u"'JFK' = John F Kennedy Intl, US",
                "type": "Airport"},
     "pickupDate": "2016-05-31T08:00:00",
     "returnDate": "2016-06-03T00:00:00"}


Search for Cruises
------------------

When the dialog with the end user is done and Eva has all the required information the cruise search webhook is triggered.
Here is an example of a cruise search request::

    User: "cruise to Alaska in the summer with Carnival"


.. code-block:: javascript
    :caption: Cruise Request Example

    {"attributes": {"cruiseline": [{"name": "Carnival Cruises"}]},
     "dateFrom": "2016-06-01T00:00:00",
     "dateTo": "2016-08-30T00:00:00",
     "durationMin": 10,
     "durationMax": 10,
     "messagingProvider": "FACEBOOK",
     "chatKey": "3648b2a2-1aee-4d5a-7ef4-13a0aa441cb1",
     "to": {"geoid": 5879092,
            "latitude": 64.00028,
            "longitude": -150.00028,
            "name": "Alaska, United States",
            "type": "State"}}


Greet the User:
---------------

Override the greeting to the user.
Eva calls this webhook with information about the scenario encoded in a key called ``greeting_type``.
The values of this key is one of the following enumeration:

existing_user_sent_from_webpage
  After clicking "send to messenger" button - for a returning user

new_user_sent_from_webpage
  After clicking "send to messenger" button - for a first time user

new_user
  First time ever that the user sends a message to the Bot

requested_by_user
  User requested, eg. typed "Start over"

new_chat_after_idle
  Eva session timeout, 

new_chat_after_terminated_by_agent
  First message after terminating chat by Agent


Here is an example of an outgoing webhook payload greeting request:

.. code-block:: javascript
    :caption: Greeting Request Example

    {
      "chatKey":"01437b93-7089-418c-8beb-269951fae9c8",
      "providerID":"312333852447351",
      "greeting_type":"new_chat_after_terminated_by_agent",
      "messagingProvider":"FACEBOOK",
      "user":{
        "lastName":"Weiss",
        "firstName":"Tal"
      }
    }

As usual, you can reply with a list of messages, such as text messages, image messages and even interacive messages.


Display Gate Number
-------------------

Display the gate number to a specific user


Display Departure Time
----------------------

Display the departure time to a specific user


Display Arrival Time
--------------------

Display the arrival time to a specific user


Display Boarding Time
---------------------

Display the boarding time to a specific user


Display boarding pass
---------------------

Display the boarding pass to a specific user.

You can reply with any of the message formats, such as text or images,
but you can also use the predefined template for displaying a Boarding Pass described at 

`Webhook Reply example with DataMessage - for Boarding Pass`_ .



Display Itinerary
-----------------

Display the itinerary to a specific user


Display Reservation
-------------------

Display the reservation to a specific user


Cancel Reservation
------------------

Please cancel my  reservation


Check In To Flight
------------------

Try "check in to my flight"


Display Flight Status
---------------------

Allow the user to request the status of a specific flight::


    User: "What is the status of United Airlines flight 123?"


.. code-block:: javascript
    :caption: Flight Status Request Example

    {"messagingProvider": "FACEBOOK",
     "chatKey": "3648b2a2-1aee-4d5a-7ef4-13a0aa441cb1",
     "IATA": "UA",
     "ICAO": "UAL",
     "name": "United",
     "number": 123,
     }

You can reply with any of the message formats, such as text or images,
but you can also use the predefined template for Flight Status described at 

`Webhook Reply example with DataMessage - for Flight Status`_ .



Interactive Messages - General
------------------------------
There are several types of interactive messages that can be returned from the applicative webhooks.
These messages are instructions to the BotKit to interact with the end users.
The interactive message must be the last in the list of returned messages.
There can only be a single interactive message in the list of returned messages.

These are the types of interactive messages:

* A Login request

  The end user needs to log into your back-end before continuing the chat.
* A Question

  Eva will ask the end user a question. Questions can be open, Yes / No and Multiple Choice.
* Validate Email
* Validate Phone Number
* Transfer the chat to a Human Agent
* Subscription management of Group Notifications


Interactive Message - Logging In End Users - OAuth
--------------------------------------------------

When a user starts a conversation with your business, you may want to identify her as a customer who already has
an account with your business. To help with this, we have created a platform-agnostic secured protocol to link and unlink
the messaging end-user identity with your business user identity.

OAuth-style LogIn allows you to invite users to log-in using your existing authentication flow thus to provide a more secure,
personalized and relevant experience to users.

To request a Log In return a special message of type `LoginOAuthEvent` from any applicative webhook.
As this is an interactive message it can only be the last in the list of returned messages
and there can only be a single interactive message in the list.

Here is an example of such a reply:

.. code-block:: javascript
    :caption: OAuth LogIn Reply Example

    {
      "botkitVersion": "0.4.0", 
      "messages": [
        {
          "_type": "LoginOAuthEvent", 
          "loginSuccessHook": {
            "webhook": "flight_boarding_pass"
          }, 
          "text": "Please Login in first", 
          "webLoginUrl": "https://chat.evature.com/demo_login"
        }
      ]
    }


:_type: Must be "LoginOAuthEvent"
:loginSuccessHook: a JSON object with either `webhook` - an enumeration of an existing webhook, or `url`
:text: any text message - mandatory.
:webLoginUrl: a URL to the web login page.

The end user will be presented with a log in request. Once she clicks on it she will be redirected outside the messaging platform
and into the a web browser window with the business specific log in process.  

The URL `webLoginUrl` will be extended with a query parameter called `redirect_uri`.
If the log in is successful, redirect the browser to the `redirect_uri` specified in your callback to complete the flow,
and append a new `authorization_code` query parameter. Eva will add the contents of `authorization_code` to the subsequent
applicative webhook calls as a new key called ``loginData``.

Interactive Message - Transfer chat to a Human Agent
----------------------------------------------------

When this message is returned from an applicative webhook, Eva will attempt to transfer the chat to a human agent.
This assumes that an Agency of Human Agents has been set up in advance. The message looks like this:

.. code-block:: javascript
    :caption: Transfer Chat to Human Agent Reply Example

    {
      "botkitVersion": "0.4.0", 
      "messages": [
        {
          "_type": "HandoffToHumanEvent",
          "noAgentsOnlineText": "text to display when no agents are online (if not using noAgentsOnlineHook)",
          "agentsOnlineText": "Text to display"
        }
      ]
    }

:noAgentsOnlineText: an optional text to be displayed
:agentsOnlineText: an optional text to be displayed

To request a Human Agent Transfer return a special message of type `HandoffToHumanEvent` from any applicative webhook.
As this is an interactive message it can only be the last in the list of returned messages
and there can only be a single interactive message in the list.

If there are no relevant agents online the end user sees a default "Sorry, no agents are online" message.

If there are agents online, Eva shows the end user a choice of available chat topics. 
Chat topics are configured in the EvaChat Admin page. Only chat topics which have matching agents online are shown.
When the user makes a Chat Topic choice the chat is transferred and the user sees "Please wait while an agent joins"
followed (eventually) by "Agent [name] has joined".

The application can configure what happens when there are no agents online by returning the following optional parameter key:
"noAgentsOnlineHook". The content of this key is either a wehbook enumeration or a url.
This follow-up webhook is activated instead of showing the default "Sorry, no agents are online"
allowing that webhook to return a custom reply (e.g. present a phone number, and/or working hours).

.. code-block:: javascript
    :caption: Specify no agents behavior with Webhook Reply Example

    {
      "botkitVersion": "0.4.0", 
      "_type": "HandoffToHumanEvent",
      "noAgentsOnlineHook": {
        "webhook": "contact_support",      
        "payload":  {"whatever_payload_here": true}
      }
    }

:payload: an optional payload that will be delivered to the webhook

or alternatively:

.. code-block:: javascript
    :caption: Specify no agents behavior with URL Reply Example

    {
      "botkitVersion": "0.4.0", 
      "_type": "HandoffToHumanEvent", 
      "noAgentsOnlineHook": {
        "url": "https://my-server.com/no_agents_online/",
        "payload":  {"whatever_payload_here": true}
      }
    }

The application may wish to skip the choosing of Chat Topic by returning the "chooseTopic" optional key parameter. 

:chooseTopic: An optional string that MUST match one of the pre-configured chat-topics

.. code-block:: javascript
    :caption: Specify Chat Topic Reply Example

    {
      "botkitVersion": "0.4.0", 
      "_type": "HandoffToHumanEvent", 
      "chooseTopic":  "Existing Booking"
    }

When the ``chooseTopic`` parameter is specified the chat topic is chosen without presenting the choices to the user.
The end user immediately sees either the "Please wait while an agent joins" or the "Sorry, no agents are online" messages.
This functionality is useful in cases when the handoff-to-human is activated from a webhook which already narrowed down
the chat topic, for example the `change_booking` webhook may hand-off to a human with a chat topic of "Existing Booking".


Interactive Message - Subscribe to List
---------------------------------------

Eva supports subscription list management for multicast notifications.
To subscribe end users to a new or existing subscriptions list
return the following interactive message from any applicative webhook:

.. code-block:: javascript
    :caption: Subscribe to List Reply Example

    {
      "botkitVersion": "0.4.0",
      "messages": [
        {
          "_type": "SubscribeEvent",
          "text": "Would you like to receive updates for this flight?",
          "buttonText": "Subscribe",
          "subscriptionId": "A unique name for this subscription"
        }
      ]
    }

As this is an interactive message it can only be the last in the list of returned messages
and there can only be a single interactive message in the list.


Interactive Message - questionnaires
------------------------------------

questionnaires are the ChatBot equivalent of forms,
where user interaction is better served with simple UI elements such as buttons.
A questionnaire is a list of questions of various types that Eva will ask the end user.
As a questionnaire is an interactive message it can only be the last in the list of returned messages
and there can only be a single interactive message in the list.

To request asking the end user questions,
return the following interactive message from any applicative webhook:

.. code-block:: javascript
    :caption: Example of questionnaire

    {
      "botkitVersion":"0.4.0",
      "messages":[
        {
          "_type":"QuestionnaireEvent",
          "questionnaireAnsweredHook":{
            "webhook":"roadside_assistance",
            "payload":{
              "more_info_to_attach_to_answers":123
            }
          },
          "questionnaireAbortedHook":{
            "webhook":"roadside_assistance",
            "payload":{
              "validation error?":321
            }
          },
          "questions":[
            {
              "_type":"EmailQuestion",
              "name":"email",
              "text":"I need to identify you, what is your email?"
            },
            {
              "_type":"MultiChoiceQuestion",
              "text":"What happened?",
              "name":"what_happened",
              "choices":[
                "Accident",
                "Mechanical problem",
                "Other"
              ]
            },
            {
              "_type":"OpenQuestion",
              "name":"details",
              "text":"I need a string that starts with 'a' and is 3 or more letters",
              "validationRegex":"a.{2}"
            }
          ]
        }
      ]
    }

The "_type" of the message is always: "QuestionnaireEvent"

"questionnaireAnsweredHook" is an enumeration of the webhook to call when the questions have all been answered.
"payload" is an object that will be added to the payload of the "questionnaireAnsweredHook".

"questionnaireAbortedHook" has the same structure of a "questionnaireAnsweredHook". 
A "questionnaireAbortedHook" will be called if the validation of an "OpenQuestion" fails two times. 
This key is optional.

Send 1 or more questions, of any of the supported types in the list of "questions". 
In this example there are 3 questions. 
Each question has a "name" which will be the key of the result in the payload to be delivered to the "questionnaireAnsweredHook".

The 1st question in the example is an EmailQuestion.
The open reply will be validated using a built-in regular expression for email addresses.


.. note::

   Eva will then send out an email to the designated address to make sure the submitted email is valid and owned by the end user!

The 2nd question in the example is a multiple choice question, typed "MultiChoiceQuestion" with 3 choices.

The 3rd question in the example is an open question for which you may request a validation regular expression.



Inverse Webhooks
================

Eva supports inverse webhooks to allow your application to send asynchronous messages to end users.
Common use cases are sending applicative notifications to the end users, such as "Your flight is now boarding at gate D3".

There are 2 types of notifications - unicast and subscription based multicast.
Unicast messages are sent to a single conversation,
while subscription based multicast messages are sent to a subscription list of conversations.
As usual, Eva handles all the formatting and glue logic for you, so you can send simple messages and the BotKit will reformat
Them as needed for the specific messaging platforms.

The format of the messages is the same as the reply from the applicative webhooks.

Unicast messages are sent to the following URL:

https://chat.evature.com/send_botkit_message

Subscription Multicast messages are sent to the following URL:

http://chat.evature.com/update_subscription

All inverse webhooks are HTTPS posts with a JSON payload.
The payload is a simple JSON object with a "siteCode" key and the "apiKey" secret.


.. code-block:: javascript
    :caption: Single Text message sent as a Notification

    {
      "botkitVersion": "0.4.0",
      "siteCode": "your_site_code",
      "apiKey": "your_api_key",
      "chatKey": "3648b2a2-1aee-4d5a-7ef4-13a0aa441c21",
      "messages": [
        {
          "_type": "TextMessage",
          "text": "Good Morning!"
        }
      ]
    }


to send a message to an existing subscription:


.. code-block:: javascript
    :caption: Notification Group Message, sent as a Notification

    {
      "botkitVersion": "0.4.0",
      "siteCode": "your_site_code",
      "apiKey": "your_api_key",
      "requestType": "send_message",
      "subscriptionId": "Flight UA-123 January 10th",
      "messages": [
          {
            "_type": "TextMessage",
            "text": "Your flight has been delayed but here is a picture of a cute dog:"
          },
          {
            "_type": "ImageMessage",
            "imageUrl": "https://storage.googleapis.com/linebot-1275.appspot.com/monaka1.jpg"
          }
      ]
    }


To remove an existing subscription (delete and unsubscribe all end users) send the following:


.. code-block:: javascript
    :caption: Delete subscription list, sent as a Notification

    {
      "siteCode": "your_site_code",
      "apiKey": "your_api_key",
      "requestType": "remove_subscription",
      "subscriptionId": "subscription_id",
    }

Secure Invitations
==================

Secure Invitations allow a Bot to invite known non-bot users to use the bot while maintaining their identity.
If you already have a login-protected webpage for all end users,
you may wish to use the `Interactive Message - Logging In End Users - OAuth`_   

Secure Invitations (simplified version) consist of 3 steps:

1. Request a secure invitation for an end user.
You provide your credentials and the internal-identity of the end user you wish to invite.
We reply with a secure token.

HTTPS Post to "https://chat.evature.com/generate_secure_invitation" with this JSON payload:


.. code-block:: javascript
    :caption: Example JSON Secure Invitation Request

    {
      "site_code": "my_site_code",
      "api_key": "my_api_key",
      "api_key": "my_api_key",
      "facebook_page_id": "my_facebook_page_id",
      "telegram_channel_id": "my_telegram_channel_id",
      "private_id": "private_id_of_an_end_user",
      "already_authenticated": true,
    }

.. note::

     You can only request one of ``facebook_page_id`` and ``telegram_channel_id`` at a time


.. code-block:: javascript
    :caption: Example JSON Response for Telegram

    {
      "referral": "some_random_string",
      "referralUrl": "https://telegram.me/EvatureHotelsBot?start=some_random_string",
    }



.. code-block:: javascript
    :caption: Example JSON Response for Facebook Messenger

    {
      "referral": "some_random_string",
      "referralUrl": "https://m.me/1749750371937776?ref=some_random_string",
    }


2. Email or SMS the referral link to end users.

3. When the end user clicks on the link, Facebook Messenger opens, with a privacy message, such as
"You opened this conversation with m.me/eva.tech.demo. eva.ai can see that you used their link."
- This comes from Facebook, not from us, and cannot be customized.

Telegram Bots present the user with a "Start" button.
- This comes from Telegram, not from us, and cannot be customized.

The Bot tells the user:
"You have now successfully authenticated!"

Every subsequent webhook call in the interaction with this specific end user will have the private internal ID
of the person in the payload: 

.. code-block:: javascript
    :caption: Simplified Payload-Part After A Successful Secure Invitation 

    {
      "user": {
        "privateId": "private_id_of_an_end_user",
      }
    }

So when this user says "Show me my boarding pass", we notify you and you know what data to return. 

