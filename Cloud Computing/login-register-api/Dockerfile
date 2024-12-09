# Gunakan image Node.js
FROM node:16

# Tentukan direktori kerja di dalam container
WORKDIR /app

# Salin file package.json dan package-lock.json ke dalam container
COPY package*.json ./

# Install dependencies
RUN npm install

# Salin seluruh folder src ke dalam container
COPY src/ ./src

# Expose port yang digunakan aplikasi (misalnya port 3000)
EXPOSE 8080

# Jalankan aplikasi dengan file index.js
CMD ["node", "src/index.js"]
