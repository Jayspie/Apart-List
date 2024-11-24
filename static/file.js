//Get users ip for folder
fetch("https://ipapi.co/ip/")
  .then(function (response) {
    response.text().then((txt) => {
      document.getElementById("ip").value = txt;
    });
  })
  .catch(function (error) {
    console.log(error);
  });
