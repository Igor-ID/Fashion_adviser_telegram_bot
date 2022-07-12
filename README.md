# Fashion advisor telegram bot

## Summary

This telegram bot is intended to give an answer to the user query based on information retrieved from an image database. This bot was implemented for the fashion domain, but designed to be a domain agnostic. To switch to another domain, the appropriate dataset must be taken into account. For the current implementation, [the Polyvore dataset (2017)](https://github.com/xthan/polyvore-dataset) containing the images of 33,375 outfits was selected.

## Implementation
For the implementation to work, the dataset with element attributes has to be obtained. This project assumes that data (relating to any domain) has been collected in any possible way, whether it be a ready-to-use dataset, a specific image dataset, a personal dataset, etc. This implementation utilizes [the dataset](https://drive.google.com/file/d/12x-Q_Q1XhbAcb4amCD4ZxKmof_GHZEWu/view?usp=sharing) which was preprocessed using [Scene Graph Benchmark](https://github.com/microsoft/scene_graph_benchmark) VinVL pre-trained model.
The attribute embeddings have been added to the dataset using [SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://github.com/princeton-nlp/SimCSE). See the implementation along with the initial dataset obtained from VinVL in the [preprocessing folder](https://github.com/Igor-ID/Fashion_adviser_telegram_bot/tree/main/preprocessing)

## Instructions
:whale: Docker `20.10+` and Docker Desktop `4.0+` are required. A container is used to manage other requirements.

1. Use the pre-built docker image - "igordedkov/fashion_advisor_bot", and run it on your computer. To pull the image down use the "docker pull" or "docker run" commands

2. 
-- Clone the repository.

-- Run the bot locally by executing the bot.py file.

-- or create a new docker image. Go to the directory where you place bot.py, Dockerfile and execute the next steps:

* docker build --tag <BOT_NAME> .
* docker run <YOUR_BOT_NAME>
* Docker image can be pushed to the docker hub by the following commands:

a. docker image tag <BOT_NAME> <DOCKER_ID>/<BOT_NAME>

b. docker push <DOCKER_ID>/<BOT_NAME>


All of the above cases require you to provide TOKEN env variable. You can get it from system Telegram Bot called BotFather. 

![image](https://user-images.githubusercontent.com/69838126/178476183-02d8b901-d80b-42ed-8475-5dc3289173e7.png)



Add the token to docker environmental variables or provide it to ENV variables on your machine.

![Screenshot 2022-07-11 220602](https://user-images.githubusercontent.com/69838126/178476694-07322a04-b16f-45d4-b727-4a78935739cd.png)



When your bot is running type '/help' for instructions

![image](https://user-images.githubusercontent.com/69838126/178483325-e8bca5d7-9dde-4bb0-8992-21e7801641bf.png)


In order for the bot to start responding after the very first query, you need to wait 5-7 minutes until the docker downloads and processes all the requirements. After that, the next and subsequent requests will work instantly.

![Screenshot 2022-07-11 222256](https://user-images.githubusercontent.com/69838126/178476910-4ba63d24-b5fa-486f-8a04-d81a61ee3493.png)


