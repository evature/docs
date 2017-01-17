============
Introduction
============

.. highlight:: none

What is Eva?
======================
Eva is an AI system designed to communicate with people in natural language using text or voice.
The Eva engine was trained with data in the Travel domain, specializing in Flights, Hotels and Car Rentals.

Eva supports formal language queries, such as:: 

   User: "I am looking for a weekend in Rome for less than $250 per person"

as well as queries written in "Search Language", such as::
	 
   User: "NYC LV next Monday"


Eva converts those requests into a structured search query with various parameters, such as:

.. code-block:: javascript
    :caption: Simplified Eva API Reply

    {
        "travelers":
        {
            "adult": 2
        }
    }

which can then be programmatically used to perform a database search.  

Eva completely manages the conversation, asking questions when needed:

.. code-block:: javascript
    :caption: Simplified Eva API Reply

	"api_reply": {
	    "Flow": [
	      {
	        "Type": "Question", 
	        "SayIt": "When would you like to return from Dallas Texas to Rome Italy?"
	      }
	    ]

Eva maintains a natural, non-linear conversation, so that the reply to the above question can be any of these::

    User: "Tomorrow morning, returning on Friday"
    User: "Flight from DFW as late as possible on the 15th"
    User: "One way flight only"

Evature provides low level access to the Eva web service as an HTTPS RESTful API
as well as fully customizable open source SDKs which bundle Eva with a speech recognition engine
and a ready-made user interface.

Audience
========
This document is intended for mobile developers who wish to voice-enable their Travel application,
Bot developers who wish to add a personalized AI travel assistant to any messaging platform 
as well as any developers who would like to simply "understand" natural language in the Travel domain. 
The documentation provides an introduction to using the web service as well as the mobile SDKs and the BotKit,
providing examples and complete reference materials on the available parameters.

Usage Limits
============
Usage of the Eva Travel API is subject to limitations defined by the Evature License Agreement and may be limited
in the number of requests per day.
You can get started with Eva for free. 

.. note::
   For FREE API access please register here: http://w.evature.com/registration/form

If you need a larger quota to support a prototype or a product please do not hesitate to contact us.
 

Which should I use?
===================
If you are adding voice to a new or existing mobile applications use :ref:`the_mobile_sdks`.
The SDKs provide the simplest integrations and the fastest time-to-market, while being fully flexible and customizable.

If you are building a text based Bot use :ref:`eva_botkit`.
The BotKit provides seamless integration with all available messaging platforms, enabling applicative DRY integration. 

For anything else use :ref:`rest_api`.

The Platform
============
Eva runs on top of the AWS cloud in multiple availability zones across 2 regions.
It utilizes many Amazon components from EC2 servers to Lambda functions
and from DynamoDB to RDS in a micro-services architecture.
Evature R&D practices continuous integration and continuous deployment,
backed up by an extensive testing and validation platform allowing upgrades to be seamless and risk-free.
Evature's current velocity is 20 deployments per week.