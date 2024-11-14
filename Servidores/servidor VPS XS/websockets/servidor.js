const https = require('https');
const WebSocket = require('ws');
const fs = require('fs');

// Configuración del servidor HTTPS
const server = https.createServer({
  cert: fs.readFileSync('www.jotauve.es_ssl_certificate.cer'),
  key: fs.readFileSync('www.jotauve.es_private_key.key')
});

// Crear el servidor WebSocket sobre HTTPS
const wss = new WebSocket.Server({ server });

// Configuración CORS
wss.on('headers', (headers) => {
  headers.push('Access-Control-Allow-Origin: *');
});

wss.on('connection', (socket) => {
  console.log('New client connected');
  socket.send(JSON.stringify({"mensaje":"hola"}));

  socket.on('message', (message) => {
    // Reenviar el mensaje a todos los clientes conectados excepto al remitente
    wss.clients.forEach((client) => {
      if (client !== socket && client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });

  socket.on('close', () => {
    console.log('Client disconnected');
  });
});


// Escuchar en el puerto 3000 en el dominio jotauve.es
server.listen(3000, 'jotauve.es', () => {
  console.log('WebSocket server is running on wss://jotauve.es:3000');
});
