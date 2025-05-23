# Base node image
FROM node:18

# Create app directory
WORKDIR /app

# Install dependencies
COPY frontend/package.json .
RUN npm install

# Copy the rest of the frontend code
COPY frontend/ .

# Start the React app
CMD ["npm", "start"]
