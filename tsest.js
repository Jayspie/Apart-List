//const fs = require('fs').promises;
import apple from 'node:fs';
//const { join } = require('path');
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
  //const fs = require('fs');
  //const path = require('path');
  
  /*function getFolders(dirPath) {
    const entries = fs.readdirSync(dirPath, { withFileTypes: true });
  
    const folders = entries.filter(entry => entry.isDirectory()).map(entry => entry.name);
  
    return folders;
  }
  
  const directoryPath = './'; // Replace with the directory you want to search
  const folders = getFolders(directoryPath);
  
  var numbers=Number(folders[2][1])
  if (Number.isInteger(numbers)==true)(
    console.log("true")
  )

  for (let i = 0; i<folders.length; i++) {
    var to_number= Number(folders[i][1])
    if (Number.isInteger(to_number)==true)(
      apple.rm(`./${folders[i]}`,{ recursive: true}, err => {
        if (err) {
          throw err;
        }
      })
    )
  }*/

    apple.readdir('./_df', (err, files) => {
      if (err) {
        console.error('Error reading directory:', err);
        return;
      }
      if(files.length>0){
        console.log("yes")
      }else{
        console.log("noo")
      }
    });

    for (let i = 0; i<1; i--) {
      var count = 1
      count+=1
      console.log(count)
    }


