# Use Node.js LTS version
FROM node:lts

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install

# Copy app code
COPY . .

# Build app
RUN npm run build

# Expose port 3000 for the app
EXPOSE 3000

# Start app
CMD [ "npm", "run", "dev" ]
