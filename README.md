# Fashion advisor telegram bot

## Summary

This telegram bot is designed to respond to a user query based on information obtained from the database. This bot has been implemented for the fashion domain, but is designed to be a domain agnostic. To switch to a different domain, the appropriate dataset must be taken into account.

## Implementation
For the current implementation, [the Polyvore dataset (2017)](https://github.com/xthan/polyvore-dataset) containing images of 33,375 outfits was selected. The garments with their attributes were extracted from the dataset using a pre-trained VinVL model from [Scene Graph Benchmark](https://github.com/microsoft/scene_graph_benchmark).
The core of the project based on embeddings - numerical representations of real-world objects and relationships, expressed as a vector. The embeddings have been added to the initial dataset using [SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://github.com/princeton-nlp/SimCSE). The implementation, along with the initial dataset obtained using VinVL can be found in the [preprocessing folder](https://github.com/Igor-ID/Fashion_adviser_telegram_bot/tree/main/preprocessing)

## Instructions
:whale: `Docker 20.10+` and `Docker Desktop 4.0+` are required. A container is used to manage other requirements.

There are two ways to run the bot:

1. Use the pre-built docker image `igordedkov/fashion_advisor_bot`, and run it on your computer. To pull the image down use the `docker pull` or `docker run` commands.

2. Run the bot using the code from this repository:
* Clone the repository.

* Get the dataset and add it to the project directory. There are two ways to get the dataset. First, by running [the notebook](https://github.com/Igor-ID/Fashion_adviser_telegram_bot/blob/main/preprocessing/Data_Preprocessing_Embeddings.ipynb) (if running in colab with GPU, the whole process should take ~15 minutes). Second, download [the dataset](https://drive.google.com/file/d/12x-Q_Q1XhbAcb4amCD4ZxKmof_GHZEWu/view?usp=sharing) (size ~825MB).

* Run the bot locally by executing the bot.py file.

It is also possible to create a new docker image. Go to the directory where you place bot.py, Dockerfile and execute the next steps:

`docker build --tag <BOT_NAME> .`

`docker run --env TOKEN=<BOT_TOKEN> <BOT_NAME>`

The Docker image can be pushed to [docker hub](https://hub.docker.com/) with the following commands:

`docker image tag <BOT_NAME> <DOCKER_ID>/<BOT_NAME>`

`docker push <DOCKER_ID>/<BOT_NAME>`

<BOT_NAME> - choose name for your docker image (for example fashion_advisor)

<DOCKER_ID> - for Docker ID you have to have a [docker hub](https://hub.docker.com/) account

For all the above cases you have to create your own telegram bot and have your own TOKEN.
1. Start a chat with (https://telegram.me/BotFather)
2. Send the message `/newbot`
3. Choose the public name of your bot
4. Choose the name id of your bot (It must end in `bot`. Like this, for example: FashionBot or fashion_bot.)
5. Father bot will return you the token (API key)

![image](https://user-images.githubusercontent.com/69838126/178476183-02d8b901-d80b-42ed-8475-5dc3289173e7.png)



Add the token to docker environmental variables if using Docker Desktop or add the token to environmental variables on your machine if running locally.

![Screenshot 2022-07-11 220602](https://user-images.githubusercontent.com/69838126/178476694-07322a04-b16f-45d4-b727-4a78935739cd.png)



When your bot is running type '/help' for instructions

![image](https://user-images.githubusercontent.com/69838126/178483325-e8bca5d7-9dde-4bb0-8992-21e7801641bf.png)


In order for the bot to start responding after the very first query, you need to wait 5-7 minutes until Docker downloads and processes all the requirements. After that, next and subsequent requests will work instantly.

![Screenshot 2022-07-11 222256](https://user-images.githubusercontent.com/69838126/178476910-4ba63d24-b5fa-486f-8a04-d81a61ee3493.png)


