fetch('https://ipapi.co/ip/')
.then(function(response) {
  response.text().then(txt => {
    document.getElementById("ip").value=txt
  });
})
.catch(function(error) {
  console.log(error)
});

      //document.getElementById("ip").value=data.ip