# Instructions

The goal of the exercise is to audit the source code of this application and report security vulnerabilities.
There are 3 injection vulnerabilities to find. All of them are exploitable.

Find at least one vulnerability and add it to the WRITE-UP.md file in your own words.
Imagine that you are reporting the issue to the developer who wrote the application. This person is an experienced developer but lacks some basic web security expertise.

Once you are done, send your WRITE-UP.md file by email.

# Requirements

You need to install [Docker](https://docs.docker.com/get-docker/) to run the application.

# Context

This application allows users to register one or multiple accounts with a unique username and link a public avatar to this username.
All pages are meant to be public except the page to edit an avatar.

# Scope

Here is a list of potential security problems in this application that you should *not* report:
* Application only accessible through HTTP
* Vulnerabilities in dependencies or the Docker image itself
* Missing security headers
* Missing brute force protection, rate limiting, or captchas
* User enumeration
* Hard-coded credentials
* Publicly accessible pages

# The Vulnerabilities i found

1- First one is XSS or Cross-Site Scripting

![Image of mahmoudashraf1344](https://github.com/0x1mahmoud/SonarSource-AppSec-Practice/blob/main/XSS.png)

Payload: <img src=x onerror alert(document.cookie)>

2- Second one is Path Injection

3- Third one is SSTI or Server-Side Tamplate Injection

![Image of mahmoudashraf1344](https://github.com/0x1mahmoud/SonarSource-AppSec-Practice/blob/main/SSIT.png)



