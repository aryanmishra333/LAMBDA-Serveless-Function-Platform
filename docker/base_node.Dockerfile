FROM node:18-slim
WORKDIR /app
COPY code.js /app/code.js
CMD ["node", "/app/code.js"]
