const express = require('express');
const fs = require('fs');
const app = express();

app.use(express.json());

const readData = (callback) => {
  fs.readFile('file.json', (err, data) => {
    if (err) {
      console.error('Error reading data from file:', err);
      return callback(err, null);
    }
    try {
      const jsonData = JSON.parse(data);
      callback(null, jsonData);
    } catch (parseErr) {
      console.error('Error parsing JSON:', parseErr);
      callback(parseErr, null);
    }
  });
};

const writeData = (jsonData, callback) => {
  fs.writeFile('file.json', JSON.stringify(jsonData, null, 2), (err) => {
    if (err) {
      console.error('Error writing data to file:', err);
      return callback(err);
    }
    callback(null);
  });
};

app.get('/getdata', (req, res) => {
  readData((err, data) => {
    if (err) {
      return res.status(500).send('Internal Server Error');
    }
    res.json(data);
  });
});

app.post('/adddata', (req, res) => {
  const newData = req.body;
  readData((readErr, existingData) => {
    if (readErr) {
      return res.status(500).send('Internal Server Error');
    }
    existingData.push(newData);
    writeData(existingData, (writeErr) => {
      if (writeErr) {
        return res.status(500).send('Internal Server Error');
      }
      res.status(201).send('Data added successfully');
    });
  });
});

function processJsonData(dataArray) {
  return new Promise((resolve, reject) => {
      // Iterate over each item in the array
      function processItem(index) {
          if (index >= dataArray.length) {
              
          } else {
              const currentItem = dataArray[index];
              console.log(currentItem);
              setTimeout(() => {
                  const processingSuccessful = true;
                  if (processingSuccessful) {
                      processItem(index + 1);
                  } else {
                      reject('Error processing item');
                  }
              }, 1000);
          }
      }
      processItem(0);
  });
}
app.get('/processData', (req, res) => {
  // Read data from JSON file
  fs.readFile('file.json', 'utf8', (err, data) => {
      if (err) {
          console.error(err);
          return res.status(500).json({ error: 'Error reading data from file' });
      }
      const jsonData = JSON.parse(data);
      processJsonData(jsonData)
          .then(result => {
              res.json({ message: 'Data processed successfully' });
          })
          .catch(error => {
              console.error(error);
              res.status(500).json({ error: 'Error processing data' });
          });
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
