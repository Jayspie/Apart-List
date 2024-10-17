const express = require('express');
const path = require('path');
const bodyParser = require('body-parser')
const spawner=require('child_process').spawn
const fs = require('fs').promises;
const apple = require('node:fs');
const test = require('node:fs');

const app = express();

app.use(express.urlencoded())
app.use(express.json());
app.use(express.static(path.join(__dirname, 'view')));
app.use(express.static(path.join(__dirname, 'test')));
app.use("/static", express.static('./static/'));
app.use("/status", express.static('./status/'));

function countOccurrences(string, subString) {
  // Split the string by the subString and count the resulting array length minus one
  return string.split(subString).length - 1;
}


app.get('/', async(req, res) => {//shows index.html/ home page
  res.sendFile(path.join(__dirname, 'view', 'index.html'));
});


app.post('/getid', async(req, res) => {
  bud = id.push(Object.values(req.body).toString())
  console.log(id);
})


app.post("/link", async(req, res) => {//prossces the link to py file and take user to suc.html
  const link=req.body.link
  const subString = "apartments";
  if(countOccurrences(link, subString)==2){
  if(link.includes('house'|| "condos"||"townhomes")){
    return res.status(400).sendFile(__dirname+'/status'+'/400.html')
  }else{
    console.log("vaild link")
  }
}else{
  return res.status(400).sendFile(__dirname+'/status'+'/400.html')
}
  const ip=req.body.ip
  console.log(ip)
  console.log("link sent")

  const folderName = `\_${ip}`;

    if (!apple.existsSync(folderName)) {
      apple.mkdirSync(folderName);
    }
    else if (apple.existsSync(folderName)){
      apple.rm(folderName,{ recursive: true}, err => {
        if (err) {
          throw err;
        }
        
        setTimeout(() => { apple.mkdirSync(folderName) }, 2000)
      });
    }
  const py_process= spawner('python3',['python/filexe.py',link,ip])
  py_process.stdout.on('data', (data) => {
    var respond=data.toString().trim()
    if(respond=="stop"){
      return res.status(500).sendFile(__dirname+'/status'+'/400.html')
    }
    })
  py_process.stderr.on('data', (data) => {
    return res.status(500).sendFile(__dirname+'/status'+'/500.html')
})

  const path = `_${ip}/apartment_list.xlsx`; // Path to the file you want to monitor
  async function checkFileExists() {

    if (test.existsSync(path)) {
      return true
    }
    else if (!test.existsSync(path)){
      console.log('false')
      return false
      
    }}
  // Check every 5 seconds
  const interval = 60000;
  const intervalId = setInterval(async () => {
  const result = await checkFileExists();
  if (result) {
    clearInterval(intervalId); // Stop checking when file is found
    res.redirect(`/succes`)
  }
  }, interval);

   
});


app.get('/succes', async(req, res) =>{// shows suc.html and user can dowload
  /*const what= spawner('python',['./linkget.py'])
  what.stdout.on('data', (data) => {
      console.log(data)
  })*/
  res.sendFile(__dirname+'/test'+'/suc.html')

})

app.get("/file", async (req, res) => {// file able to download for user 
  fetch('https://ipapi.co/ip/')
  .then(function(response) {
    response.text().then(txt => {
      const excelFilePath = path.join(__dirname, `_${txt}/apartment_list.xlsx`);
      res.sendFile(excelFilePath, (err) => {
    if (err) console.log(err);
  });
    });
  })
  .catch(function(error) {
    console.log(error)
  });
  
});

app.get('/download/:ip', (req, res) => {
  const txt=req.params.ip.replace(":", '')
  console.log(txt)
  const filePath = path.join(__dirname, `_${txt}`, 'apartment_list.xlsx');
  
  res.download(filePath, `apartment_list.xlsx`, (err) => {
        if (err) { 
            console.error('File download failed:', err);
            res.status(500).send('Error downloading file');
        }
    })
  
});

app.get("/id", async (req, res) => {
  fetch('https://ipapi.co/ip/')
  .then(function(response) {
    response.text().then(txt => {
      console.log(txt)
  })
  .catch(function(error) {
    console.log(error)
  });
})
})

app.listen(8080, () => {
    console.log('[server] Application started!')
});