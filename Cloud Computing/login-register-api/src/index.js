const Hapi = require('@hapi/hapi');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const { MongoClient } = require('mongodb');
require('dotenv').config();

const JWT_SECRET = process.env.JWT_SECRET;
const MONGO_URI = process.env.MONGO_URI;

console.log('Mongo URI:', MONGO_URI);

let db;

// Fungsi untuk menghubungkan ke database MongoDB
const connectToDatabase = async () => {
    try {
        const client = new MongoClient(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });
        await client.connect();
        db = client.db('login-register'); // Nama database yang sesuai
        console.log('Connected to MongoDB');
    } catch (error) {
        console.error('Failed to connect to MongoDB', error);
    }
};

const init = async () => {
    const server = Hapi.server({
        port: process.env.PORT || 8080,
        host: '0.0.0.0',
    });

    // Route untuk register
    server.route({
        method: 'POST',
        path: '/register',
        handler: async (request, h) => {
            const { username, password } = request.payload;

            // Cek apakah username sudah digunakan
            const existingUser = await db.collection('users').findOne({ username });
            if (existingUser) {
                return h.response({ message: 'Username already exists' }).code(400);
            }

            // Hash password
            const hashedPassword = await bcrypt.hash(password, 10);
            await db.collection('users').insertOne({ username, password: hashedPassword });

            return h.response({ message: 'User registered successfully' }).code(201);
        },
    });

    // Route untuk login
    server.route({
        method: 'POST',
        path: '/login',
        handler: async (request, h) => {
            const { username, password } = request.payload;

            // Cek apakah username ada
            const user = await db.collection('users').findOne({ username });
            if (!user) {
                return h.response({ message: 'Invalid username or password' }).code(401);
            }

            // Verifikasi password
            const isValid = await bcrypt.compare(password, user.password);
            if (!isValid) {
                return h.response({ message: 'Invalid username or password' }).code(401);
            }

            // Buat token JWT
            const token = jwt.sign({ username }, JWT_SECRET, { expiresIn: '1h' });

            return h.response({ message: 'Login successful', token }).code(200);
        },
    });

    await server.start();
    console.log('Server running on %s', server.info.uri);
};

process.on('unhandledRejection', (err) => {
    console.log(err);
    process.exit(1);
});

connectToDatabase().then(init).catch(console.error);
