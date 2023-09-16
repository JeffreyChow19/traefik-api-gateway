# Traefik API Gateway: A Guide

Welcome to the guide for our Traefik API Gateway. This gateway serves as a conduit for two distinct services: `Numbers` and `Quotes`. Each service is built using a different framework and offers unique endpoints.

## Services Overview

### 1. Numbers Service

The Numbers service is crafted using the JavaScript Express framework. It provides two endpoints:

- `'/'`: The root endpoint.
- `'/random'`: This endpoint generates random numbers.

### 2. Quotes Service

The Quotes service is built with the Python Flask framework and also offers two endpoints:

- `'/'`: The root endpoint.
- `'/quote'`: This endpoint generates a random quote.

## Building and Running the API Gateway

Follow these steps to build the images for each service and run the API Gateway:

1. **Build the Quotes Image**

Navigate to the `flask-quotes` directory and build the image with Docker:

```bash
cd flask-quotes
docker build -t quotes .
```

2. **Build the Numbers Image**

Next, navigate to the `express-numbers` directory and directory and build this image:

```bash
cd ../express-numbers
docker build -t numbers .
```

3. **Run the API Gateway**

Finally, return to the root directory and start the API Gateway with Docker Compose:

```bash
cd ..
docker-compose up -d
```

## Accessing the API Gateway

Once the API Gateway is up and running, you can access each service by navigating to ` http://localhost/{service}` in your web browser or API testing tool. e.g. `http://localhost/numbers/random`

## Author

- [Jeffrey Chow](https://github.com/JeffreyChow19)
- [Rachel Gabriela Chen](https://github.com/chaerla)
