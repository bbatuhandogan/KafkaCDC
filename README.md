# Kafka CDC

This project is a Change Data Capture (CDC) application that extracts new documents from a specific MongoDB collection and sends them as JSON messages to Apache Kafka. The application consists of two parts: the Message Producer Application (App A) and the Message Consumer Application (App B). Docker is used to set up the environment, including the applications and Apache Kafka.

## Project Structure

The project involves developing two applications, App A and App B, in the programming language of your choice:

- `Message Producer Application (App A)`: This application queries a specific MongoDB collection at regular intervals(10 sec) and identifies newly added documents since its last run. It then sends these new documents as JSON messages to Apache Kafka.
- `Message Consumer Application (App B)`: This application queries a specific MongoDB collection at regular intervals and identifies newly added documents since its last run. It then sends these new documents as JSON messages to Apache Kafka.

To facilitate the project, Docker is utilized. Docker Compose is used to build the necessary Docker images and run the application services, including App A, App B, and Apache Kafka.

## Requirements

To run the project, the following requirements must be fulfilled:

- Programming language and its version need to be specified.
- MongoDB connection details must be provided.
- Apache Kafka connection details are required.


## Installation and Execution

Follow the steps below to build and run the applications:

**1. Clone the repository:**

Clone the project from the GitHub repository. Use the following command to clone the project to your local machine:

```shell
git clone https://github.com/bbatuhandogan/KafkaCDC
```

**2. Navigate to the project directory:**

After cloning the project, navigate to the project directory:

```shell
cd KafkaCDC
```

**3. Build Docker images and run the services:**

Use Docker Compose to build the Docker images and run the application services. Execute the following command to start Docker Compose:

```shell
docker-compose up --build
```

This command will build the defined services and start them. Please note that building the images may take some time. Once completed, the applications will be up and running, and the data flow will commence.

**4. Start the data flow:**

To initiate the data flow, open a terminal and ensure you are in the project directory. Then, enter the following command to start the data producer:

```shell
python kafka-producer.py
```

This command will query new documents from a specific MongoDB collection and send them as JSON messages to Apache Kafka.

By following these steps, you can monitor the data flow in the terminal and observe the changes in Apache Kafka and MongoDB.

## Additional Notes

- Docker and Docker Compose should be installed. You can find installation instructions for Docker ['here'](https://www.docker.com/get-started) and for Docker Compose ['here'](https://docs.docker.com/compose/install/).
- Apache Kafka should be installed. You can find more information about Apache Kafka ['here'](https://kafka.apache.org/).
- MongoDB should be installed. You can find more information about MongoDB ['here'](https://www.mongodb.com/).

## Troubleshooting

If you encounter any issues or errors, please check the application logs located in the `'app/logs/'` directory for further details.

## Resources

- Docker: [https://www.docker.com/get-started](https://www.docker.com/get-started)
- Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
- Apache Kafka: [https://kafka.apache.org/](https://kafka.apache.org/)
- MongoDB: [https://www.mongodb.com/](https://www.mongodb.com/)

## Contribution

Pull requests are welcome for bug fixes and improvements to the project.