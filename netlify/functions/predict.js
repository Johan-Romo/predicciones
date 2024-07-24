const { spawn } = require('child_process');

exports.handler = async function(event, context) {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  const data = JSON.parse(event.body);

  return new Promise((resolve, reject) => {
    const python = spawn('python', ['predict.py', JSON.stringify(data)]);
    
    let output = '';
    python.stdout.on('data', (data) => {
      output += data.toString();
    });

    python.on('close', (code) => {
      resolve({
        statusCode: 200,
        body: JSON.stringify({ prediccion: output.trim() })
      });
    });

    python.on('error', (error) => {
      reject({ statusCode: 500, body: JSON.stringify({ error: error.message }) });
    });
  });
};