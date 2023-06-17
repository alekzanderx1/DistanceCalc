# Distance Calculator 

A web app that calculates the air distance between two points, given longitude and latitude. Also includes utility which converts given address to geo-location using Google Maps API.

Although the apps functionality is very trivial, it mainly demonstrates how easy it is to utilize Vercel and Flask to host an application with APIs, templated HTML pages, and static content with minimal setup required. Moreover you get automatic builds on new commits, automatic deployments, logs collection, and usage analytics in addition to so many more useful features.

> App Demo available here until account limits are reached: https://distance-calc.vercel.app/ 

---

As we will see below, with the code already in place, setup should not take more than 10 minutes, demostrating how easy it is to host your own web app online. Moreover, as you push new changes, the app will be automatically redeployed with the new changes.

---

##  Prerequisites

* Obtain Google Maps API key [here](https://developers.google.com/maps/get-started) 

## Intructions to run application locally

Navigate to Project root and follow below steps:

1. Setup a User Environment Variable `GMAPS_API_KEY` with value as API key obtained above.

2. Install dependencies by running `pip install -r requirements.txt`

3. Launch Flask app by running `flask --app index run`

> App should be available at http://127.0.0.1:5000 

## Instructions for deploying application on Vercel

1. Signup for Vercel using own Github account

2. Fork this repository to your own account

3. Create new Vercel project by Importing git repository forked in Step 2, choose all default settings

4. In Project settings, create new environment variable `GMAPS_API_KEY` with value as API key obtained above

> The Flask app should should be deployed automatically and public link available for you to use
