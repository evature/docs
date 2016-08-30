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

      For **free** API access please register here: https://www.evature.com/registration/form

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

   Select Full AI.

   Type in your Telegram HTTP API token.


#. **Say hi to Eva on Telegram!**

   Now try chatting with your new bot in Telegram! Go ahead - try typing "hi" and "Who are you?"


Line integration
----------------

#. **Create a new Line Bot**

   Create a Line BOT API account from the LINE Business Center.
   You need to have a business account - https://business.line.me

   Register for a BOT API Trial Account - https://business.line.me/en/products/4/introduction

   Once you have the bot, note the following -

   * Channel ID, e.g. "1476248720"
   * Channel Secret, e.g. "0a1b2427f865b36aebf6f18d2a7b2a19"
   * MID, e.g. "u6693abde9913e0bb699d29da0b632de0"

   You will need to copy those to Eva in the line integration.

#. **Create a new Line Integration**

   Head back to https://chat.evature.com/botkit and (after logging in if needed), click on the **Add Chat Integration** button.

   Choose Type = Line.

   Select Full AI.

   Fill in your Channel ID, Channel Secret and MID.

#. **Configure Eva as the Line Bot**

   Set the Callback URL to "https://chat.evature.com:443/line"

   See the `detailed Line docs <https://developers.line.me/bot-api/getting-started-with-bot-api-trial#register_callback_url>`_

#. **Say hi to Eva on Line!**

   Now try chatting with your new bot in Line. Go ahead - try typing "hi" and "Who are you?"


Facebook integration
--------------------

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

   Select Full AI.

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

   Select Full AI.

   Fill in the username and API Key generated in the previous step.

   Click Save.


#. **Say hi to Eva on Kik!**

   Now try chatting with your new bot in Kik. Go ahead - try typing "hi" and "Who are you?"



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

All DateTimes are in ISO 8601 format https://en.wikipedia.org/wiki/ISO_8601 .
DateTimes that are ranges (e.g. 'next week', or 'July') are expressed as a combination of 2 DateTimes - a "Min" and a "Max".
DateTimes that are NOT ranges are expressed as a combination of 2 IDENTICAL DateTimes.

Here is the minimal webhook reply with a single text message:

.. code-block:: javascript
    :caption: Webhook Reply with single Text message

    {
      "botkitVersion": "0.3.0", // Without this key the content is considered a Raw message and is passed as-is
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
      "botkitVersion": "0.3.0",
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
      "botkitVersion": "0.3.0",
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
      "botkitVersion": "0.3.0", // Without this key the content is considered a Raw message and is passed as-is
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
      "botkitVersion": "0.3.0", // Without this key the content is considered a Raw message and is passed as-is
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

    {  "botkitVersion": "0.3.0",
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

    {  "botkitVersion": "0.3.0",
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
      "botkitVersion":"0.3.0"
    }


Here is a generic, all inclusive example of a webhook reply that is returned by the implementation:

.. code-block:: javascript
    :caption: Generic Webhook Reply

    {
      "botkitVersion": "0.3.0",
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

Override the greeting to the user


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


Log Messages between Eva and User
---------------------------------

Allows logging of all communication between Eva to the end user and helpful debug information regarding the integration.  

Eva BotKit logs all activity to this Webhook as simple JSON HTTP POSTs.  

.. tip::

   To set up a simple view for this log, head over to https://hyperdev.com  
   
   * Log in to GitHub.  
   
   * Start a new project.  
   
   * Click on the project name, `Advanced Options`, `Import from Github` and input 'iftahh/bot_logger'.  
   
   * Click on `Show` and you will see a scrolling list of logs from the BotKit.  
   
   Enter "Hi" to Eva in any messenger to see some logs.  


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
      "botkitVersion": "0.3.0", 
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
applicative webhook calls as a new key called `loginData`.

Interactive Message - Transfer chat to a Human Agent
----------------------------------------------------

When this message is returned from an applicative webhook, Eva will attempt to transfer the chat to a human agent.
This assumes that an Agency of Human Agents has been set up in advance. The message looks like this:

.. code-block:: javascript
    :caption: Transfer Chat to Human Agent Reply Example

    {
      "botkitVersion": "0.3.0", 
      "messages": [
        {
          "_type": "HandoffToHumanEvent", 
        }
      ]
    }

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
      "botkitVersion": "0.3.0", 
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
      "botkitVersion": "0.3.0", 
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
      "botkitVersion": "0.3.0", 
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
      "botkitVersion": "0.3.0",
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
      "botkitVersion": "0.3.0",
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
      "botkitVersion": "0.3.0",
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

 