# FitJourney Login-Register API

This repository contains the Login-Register API for FitJourney, a fitness and nutrition tracking application. The API handles user authentication and account management using Node.js, MongoDB Atlas, and JSON Web Tokens (JWT).

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
   PORT=3000
   MONGO_URI=<your-mongodb-atlas-connection-string>
   JWT_SECRET=<your-secret-key>
   ```

4. Start the server:
   ```bash
   npm start
   ```

   The API will run at `http://localhost:8080`

## Security
- Passwords are hashed using [bcrypt](https://github.com/kelektiv/node.bcrypt.js).
- JWT is used for secure authentication.

## Deployment
This API can be deployed on any platform that supports Node.js. For cloud-based deployment, consider using [GCP Cloud Run](https://cloud.google.com/run) or other similar services.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or bug fixes.
