=================
API - The Request
=================

All text requests are handled by a Web API server, available at `http://freeapi.evature.com/vX.Y`

Please register here to get started for free: http://www.evature.com/registration/form 

Here is an example of a text request:

`http://freeapi.evature.com/v1.0?site_code=<your site_code>&api_key=<your api_key>&input_text=chicago+monday`                                 

The text request is sent as an HTTP GET method with the following parameters:

input_text
==========

The input query string in URL format and UTF-8 encoded.

There may be more than a single input text, for example when the source of the text is the hypotheses of a
speech recognition engine. In this case see: :ref:`multiple_input_text`.

.. _site_code and api_key:

site_code and api_key
=====================

Designated username/password credentials provided by Evature per customer site or application using the Web API or the Mobile SDKs.

Users receive the credentials after registration.  

Mandatory fields.

.. _uid:

uid
===

A unique identifier to help Eva track the end user across sessions, see :ref:`metasessions`. 
This field, while not mandatory, is very important, as it is the only way Eva can group users across sessions
which allows for better understanding.
On Android if you have the READ_PHONE_STATE permissions for your application you can use the deviceId

.. code-block:: java
    :caption: Java snippet

    public String getDeviceId() {
      if (this.deviceId == null) {
        try {
          TelephonyManager telephonyManager = (TelephonyManager) activity.getSystemService(Context.TELEPHONY_SERVICE);
          deviceId=telephonyManager.getDeviceId();
        }
        catch(SecurityException e) {
           Log.e(TAg, "Can't read the Device Id because of missing READ_PHONE_STATE permission");
        }
      }
      return deviceId;
    }

Another alternative may be to to use the Google Advertisement ID:

https://support.google.com/googleplay/android-developer/answer/6048248?hl=en


or to generate a random string and save it to preferences.

http://stackoverflow.com/a/17625641

Then add it to the URL:

.. code-block:: java
    :caption: Java snippet

    evatureUrl += "&uid=" +getDeviceId();        

This parameter is automatically handled by :ref:`the_mobile_sdks`.


.. _scope:

scope
=====

Defines the types of travel services are provided by the application/web site.

The value is a concatenated string with a single letter representing each of the travel services available:
	
f - flights

h - hotels

v - flight and hotel vacation packages

c - car rental

r - cruise

s - ski

e - explore (inspiration search / tours and activities within a location)

t - trains

p - airports

If for example an application offers hotels only, you should send: scope=h,
while a web site for flights and cruises should send: scope=fr.

.. _context:

context
=======

Defines the **current** state of the site/application.

The value is a single letter representing current context, with the same enumeration as `scope`_.

For example: if an app/site supports both flights and hotels, and a user is currently viewing the flights page,
the app/site should send "&context=f" and while the user is viewing hotels - "&context=h".

The result is that if the user says "New York" while in the flights context
Eva would interpret this utterance as a **flight** request, either to or from New York, while if in the hotel context
the same input would mean **hotel** in New York.  

locale
======

Receives one of the values: UK, US, IL -
specifying the date notation (10/3/2010 is March 10th in UK/IL and October 3rd in the US)
and the days of the weekend (Sat-Sun in UK/US, Fri-Sat in IL).

This parameter is automatically handled by :ref:`the_mobile_sdks`.
	
bias
====

Specify a list of locations to be biased as the home location of the user. Values are the location Geoname IDs.

Example: bias=3017382,2510769 

Represents bias to France or Spain. Bias means that the departure of any trip would always be from within the bias locations.

For example: "NY London Monday" would mean a flight from NY to London on Monday, but if bias was set to be UK, the same input would be interpreted as flight from London to NY on Monday.

It is highly important to set bias in sites that imply the origin of the trip, for example sites that sell vacation packages originating in the UK.

Note: If you define both "home" and "bias" - home must be a location within the bias (For example London and UK).

home
====

The home of the end user sending the request, if specifically known to our client (for example through registration).

The value can be either the Geoname ID for the home location (see http://www.geonames.org/) OR a string for the location name 

Example (Geoname ID): "home=5128581" means home is New York City - http://www.geonames.org/5128581.

Example (name string): "home=paris" means the home is Paris, France, or "home=paris TX" means home is Paris Texas.

ip_addr
=======

The end user's IP address, if known (e.g. extracted from the META REMOTE_ADDR HTTP request parameter).
The IP address will be used to identify the user's home location if no better coordinates are provided. 

If a specific 'home' was defined 'ip_addr' will be ignored.

Not needed if the end device (e.g. a mobile phone) is contacting Eva directly.

longitude and latitude
======================

The end user's current coordinates, when available.

This parameter is automatically handled by :ref:`the_mobile_sdks`.


time_zone
=========

Timezone - The end user's timezone in respect to the Coordinated Universal Time (UTC).
 
The timezone is very helpful in understanding expressions such as "tomorrow morning".
  
The value is a string representing the offset from UTC in the following format "+/-HH:MM".

HH represents the hour offset in the range -12 and 14

MM represents the minutes offset

Examples: 

"time_zone=+08:00" means the UTC+8 timezone.

"time_zone=-05:30" means the UTC-5:30 timezone.    

This parameter is automatically handled by :ref:`the_mobile_sdks`.

           			 
feedback
========

Enables to feedback Eva through the API regarding the parsing of a particular request.
This field should NOT be present in regular API calls.

Feedback requests should only include :ref:`credentials <site_code and api_key>`, an optional `comment`_ and
the :ref:`transaction_key <transaction_key>`.

Feedback requests do NOT get parsed and return a success message only.
The feedback is logged onto Eva for further learning and processing.

Feedback values can be:

0 - Parse failed.

1 - Parse was partly correct.

2 - Parse was correct.

comment
=======

Provide a text comment to a feedback. This will ONLY be reviewed in a request that includes the `feedback`_ field.

.. _session_id:

session_id
==========

A session identifier in order to maintain state for the end user. Enables Dialogs and multi-query inputs.

It is both an input to Eva and an output from Eva.

To start a new session send EVA a request with query parameter “session_id=1”. Eva will reply with a new session_id.
Maintain the session state by passing back the received session_id in the following requests to EVA,
much like an HTTP token or cookie.

A session may automatically be timed out after a few minutes of inactivity, or if specifically requested by the user.

For an overview see :ref:`maintaining_state`.

This parameter is automatically handled by :ref:`the_mobile_sdks`.

dialog_response
===============

When using sessions the dialog engine may present the end user with a multiple choice question. 
When the end user selects one of these responses using a GUI,
the application must return the choice to Eva in the *dialog_repsonse* request parameter.

This parameter is automatically handled by :ref:`the_mobile_sdks`.

.. _from_speech:

from_speech
===========

When the source of the text in the input_text is from a speech recognition engine,
please add `from_speech` to the request parameters.
This allows Eva to correctly overcome speech recognition blunders,
as well as disable text-specific processing such as a spell checker, resulting in a faster, more accurate reply.

This parameter is automatically handled by :ref:`the_mobile_sdks`.

android_ver
===========

If, for some reason you are integrating Eva into an Android device using the raw API,
it greatly helps Eva with analytics and debugging to know the Android OS version

.. code-block:: java
    :caption: Java snippet

    evatureUrl += "&android_ver=" +URLEncoder.encode(String.valueOf(android.os.Build.VERSION.RELEASE), "UTF-8");

This parameter is automatically handled by :ref:`the_mobile_sdks`.

device
======

If, for some reason you are integrating Eva into a mobile applications,
it greatly helps Eva with analytics and debugging to know the specific device

.. code-block:: java
    :caption: Java snippet

    evatureUrl += "&device=" +URLEncoder.encode(android.os.Build.MODEL, "UTF-8");

This parameter is automatically handled by :ref:`the_mobile_sdks`.

language
========

The input language per ISO 639-1.
 