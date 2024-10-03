FROM node:14

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy everything from the current directory into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 8080

# Command to start the app
CMD ["node", "app.js"]
