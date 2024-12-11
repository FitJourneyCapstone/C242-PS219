# FitJourney Login-Register API

This repository contains the Login-Register API for FitJourney, an application designed to provide food recommendations based on user input. The API handles user authentication and account management using Node.js, MongoDB Atlas, and JSON Web Tokens (JWT).

## Features
- User Registration
- User Login
- Password Hashing
- JWT-Based Authentication
- MongoDB Atlas for Account Data Storage

## Requirements
Ensure you have the following installed:
- [Node.js](https://nodejs.org/) (version 16 or higher recommended)
- [npm](https://www.npmjs.com/)
- A [MongoDB Atlas](https://www.mongodb.com/atlas/database) cluster

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure environment variables by creating a `.env` file in the root directory:
   ```env
   PORT=8080
   MONGO_URI=<your-mongodb-atlas-connection-string>
   JWT_SECRET=<your-secret-key>
   ```

4. Start the server:
   ```bash
   npm start
   ```

   The API will run at `http://localhost:8080` by default.

## Security
- Passwords are hashed using [bcrypt](https://github.com/kelektiv/node.bcrypt.js).
- JWT is used for secure authentication.

## Deployment
This API is deployed on [Google Cloud Platform (GCP)](https://cloud.google.com/) for scalability and reliability. To deploy, use services like GCP Cloud Run or App Engine for seamless integration.

## Contributions
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or bug fixes.
