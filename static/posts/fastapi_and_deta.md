---
title: A beginner's guide to developing and hosting APIs using FastAPI and Deta.sh
date: 9/5/22
tags:
  - API
  - python
  - Cloud
slug : fastapi_and_deta
postno: 2
---

# A beginner's guide to developing and hosting APIs using FastAPI and Deta.sh

In this guide, I’ll show you how to create an **API** using python’s **[FastAPI](https://fastapi.tiangolo.com/)** web framework, use **[Deta](https://www.deta.sh/)** cloud to deploy the same, and use their unlimited production-grade NoSQL database for storing our data (yes, you heard it right, they provide unlimited storage and that too for free).

Let’s first look at the basics.

## What is an API?

API stands for Application Programming Interface. In simpler words, it is an interface through which two applications communicate with each other ( usually, it is used by a client-facing application to speak to the backend server and retrieve data from a backend database). There are different types of APIs. The one we will be creating is called REST API (The most popular one).

The four most common types of HTTP methods used in developing a REST API are GET, POST, PUT, and DELETE.

**GET**: Used for retrieving data from a server.

**POST**: Used for sending data to a server at some specified resource.

**PUT**: Used to update already existing server data at some specified resource.

**DELETE**: Used for deleting the data from a server at some specified resource.

We will now develop a simple notes API that can perform all these operations and deploy it on the web.

Developing the API
Prerequisites: Make sure you have Python 3.6 or above installed in your system

Open up the terminal and create a folder for the API. Change the working directory to that folder using the cd command.


    mkdir fastapi-tutorial
    cd fastapi-tutorial



Install the python virtual environment in the folder and activate it ( these commands work for windows. For macOS and Linux, look up the respective commands)


    python -m venv venv
    venv\Scripts\activate


Install FastAPI by pip


    pip install "fastapi[all]"


The “all” keyword installs the respective dependencies automatically, such as uvicorn. ( The ASGI implementation for python).

Create a file called main.py inside your folder and copy the below code


<script src="https://gist.github.com/utk61198/0ca758ff9d05d8e6e7942808dbf6368f.js"></script>


run the file inside the terminal with the following command

    uvicorn main:app --reload

Now go to http://127.0.0.1:8000/, and you will see the below output

!["index page"](https://miro.medium.com/max/700/1*pfRGGw6WryGCRDU6_aeW7A.png)

You can visit http://127.0.0.1:8000/docs to see the Swagger UI for your API and test it.

!["iSwagger UI"](https://miro.medium.com/max/700/1*8PPfDKiaRqcELKw8gB9b1w.png)

Click on Execute, and you will see the response HTTP status code as 200 (meaning the request was successful)


![](https://miro.medium.com/max/700/1*8cz0VJE7qigD0JUgnaIenQ.png)

## A little explanation:-

In main.py, we imported the FastAPI module and created an app with that module ( line number 3). Now @app.get('/') means, we are using a GET method on the index page of our application. This method returns the dictionary. 

    {"message":"This is the index page of the notes API"}

Now let’s add the functionality to add notes through our API.

For this, we need a database to store our notes. Sign up to Deta Cloud and create a project and retrieve the project key. It should be pretty straightforward.

Install deta through pip

    pip install deta

Modify the main.py as shown below

<script src="https://gist.github.com/utk61198/f4ec4b876cb61600748fd978aedfdf33.js"></script>

Here we have created a addnote URL route that takes in an id and note string.

Let’s test our API endpoint in the Swagger UI. Go to http://127.0.0.1:8000/docs

![](https://miro.medium.com/max/700/1*jwssvoXPLkE_AkepNuF7XQ.png)

Click on the post dropdown and execute the post request with id and string parameter.

![](https://miro.medium.com/max/700/1*5zdW2eM1yNu6R3ID6M6LNQ.png)

We can also see the notes database in the Deta Dashboard.

![](https://miro.medium.com/max/700/1*vraxf4h0vjG4eQljgs0-iA.png)

Similarly, we will create methods to view notes, delete notes and update a note.

modify the main.py as below

<script src="https://gist.github.com/utk61198/6b80d2c5866915f378e907acbd3e75e5.js"></script>



test your API by visiting http://127.0.0.1:8000/docs

![](https://miro.medium.com/max/700/1*34ZC79yeo6lmJ-7lBwn57w.png)

The getnotes route will display all the notes stored in the Deta cloud.

![](https://miro.medium.com/max/700/1*hES6OtYNcAdUpbRpZGxYeA.png)


# Deploying the API
Now we have a fully working API that can perform all the operations. Let’s deploy it on the cloud. We will use Deta Micros for hosting our API. It allows for unlimited app hosting and is highly scalable.

Create a `requirements.txt` file in the same folder where `main.py` is located and modify the file as given below.


![](https://miro.medium.com/max/437/1*n4R3-HOHZs_rnWiVn5C15g.png)"

Open Windows PowerShell and install the Deta CLI with the following command. Use the command `deta login` to authenticate the cli through browser


    iwr https://get.deta.dev/cli.ps1 -useb | iex
    deta login
For macOS and Linux, follow this to install the CLI

Using PowerShell, navigate to the folder containing main.py and requirements.txt and use the below command to deploy your API.

    deta new

![](https://miro.medium.com/max/700/1*i4KhDMuxXIyNl2O3QuXEtw.png)

Yes, it is that simple. Go to the endpoint displayed in the terminal, and your API will be live. You can also configure custom domains by logging into your Deta dashboard. I have configured mine as https://fastapi-tutorial.deta.dev/.

![](https://miro.medium.com/max/597/1*KY-Fk2xYFh5e2ZwFYbBZkQ.png)

Test your live API by going to the /docs route

![](https://miro.medium.com/max/700/1*g0c0t_DsT5Fm1tilcds81g.png)


Swagger UI for the live API
If there are any changes to your code, use the command **deta deploy** to deploy the API again.

That is all for this tutorial. We successfully developed and hosted an API on the web.

Cheers:)