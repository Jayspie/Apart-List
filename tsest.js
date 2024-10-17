const fs = require('fs').promises;
const apple = require('node:fs');
const { join } = require('path');
/*function getFilesizeInBytes(filename) {
  var stats = fs.statSync(filename);
  var fileSizeInBytes = stats.size;
  return fileSizeInBytes
}
console.log(typeof(getFilesizeInBytes('apartment_list.xlsx')))
if (getFilesizeInBytes('apartment_list.xlsx')<6000){
  console.log('low')
}
else{
  console.log('high')
}*/
/*const path = `_2600:100d:b068:9c1e:401b:e098:61d8:1ebc/apartment_list.xlsx`; // Path to the file you want to monitor
 async function checkFileExists() {

  if (apple.existsSync(path)) {
    return true
  }
  else if (!apple.existsSync(path)){
    console.log('false')
    return false
    
  }}

  // Check every 5 seconds
  const interval = 5000;
  const intervalId = setInterval(async () => {
  const result = await checkFileExists();
  if (result) {
    clearInterval(intervalId); // Stop checking when file is found
    console.log('yo')
  }
  }, interval);*/
  fetch/*Ruff Ruffman*/('https://ipapi.co/ip/')
  .then(function(response) {
      response.text().then(txt => {
// Dynamically create the <a> tag and set the href
console.log(txt)
});
})
.catch(function(error) {
console.log(error)
});