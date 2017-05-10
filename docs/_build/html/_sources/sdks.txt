.. _the_mobile_sdks:

===============
The Mobile SDKs
===============

.. highlight:: none


Overview
========
The mobile SDKs bundle Eva's Natural Language Understanding and Dialog Management features
with robust cloud based Speech Recognition and a Voice Chat Overlay user interface.
Furthermore, the Eva API reply is automatically parsed and handled and the application is only called upon
to implement applicative directives, such as *ShowBoardingPass* or *PerformFlightSearch*.

Integration on all platforms consists of the following steps:

#. **Import**
   
   Download the code and place it in your project.
   The detailed instructions include a validation test to make sure the application can properly connect to the SDK. 

#. **Initialize and Configure**
   
   Initialize the Eva singleton component and pass along the applicative configuration.
   The default configuration is usually sufficient to proceed with the integration
   yet there are many configurations which change the behavior of the Voice interface and
   the developer / product manager are encouraged to fiddle with them later.
   For this phase you will need the credentials you received from Evature.

   In the logs you will be able to see that the application was successfully authenticated by Eva.

#. **Add the microphone button!**
   
   Add a single line of code to each *screen* (e.g. Activity on Android) to add a floating microphone action-button.
   Best practice is to add a voice interface to each *screen* to enable the full power of Voice in the application.

#. **Mini Integration Test - Say Hi!**
   
   At this point you will be able to open the application, press the microphone button and say Hi to Eva.
   Eva will politely respond.
   
   A successful integration means that Speech Recognition, Natural Language Understanding and Dialog Management are working,
   but Eva doesn’t yet know anything about your application!
   
   **Total estimate time of getting to this point - 1 hour**.

#. **Implement applicative callbacks**
   
   Eva defines many callback functions for applicative requests that may be queried by the end users.
   This is usually existing functionality within the application that the developer
   needs to "wire" to the corresponding callback function.
   
   Here are some examples:

   * Perform Flight Search
   * Perform Hotel Search
   * Show Boarding Pass
   * Show Itinerary
     
   Obviously if the application does not support such functionality you can simply ignore the non-applicable callbacks.

#. **Customization**
   
   All static content used within the SDK is fully configurable.
   Strings, icons, colors, images, layouts and sounds are collected in the platform designated locations for easy access.
   This allows the developers to integrate Voice functionality while maintaining the look and feel
   of the application.

#. **Platform Specific integrations**

   Some functionality is unique to a specific platform.
   An example of this is the "OK Google" integration on Android devices.
   End-users will be able to say to their phone (on any screen!)::

       User: "OK Google. Search for New York to Tokyo on MyTravelApp"

   And Android will automatically launch the MyTravelApp application and start a chat with Eva searching for "New York to Tokyo" !


VoiceKit for iOS
====================

A native Objective C integration of the Eva service, cloud based Speech Recognition, text-to-speech
and a customizable iOS friendly animated chat overlay.

VoiceKit for iOS lives here: 
https://github.com/evature/ios

VoiceKit for Android
========================

A native Java integration of the Eva service, cloud based Speech Recognition, text-to-speech
and a customizable Android Material Design animated chat overlay.

VoiceKit for Android lives here: 
https://github.com/evature/android

VoiceKit for PhoneGap (Apache Cordova)
======================================

A Javascript, HTML and CSS integration of the Eva service, cloud based Speech Recognition, text-to-speech
and a customizable animated chat overlay.

VoiceKit for PhoneGap (Apache Cordova) lives here: 
https://github.com/evature/voicekit-cordova


.. note::

   The PhoneGap VoiceKit currently supports only the Android platform. iOS support is coming soon.
   
   VoiceKit on pure mobile websites will **NOT** be supported due to the inability to consistently
   access the microphone from the mobile web browser. 


