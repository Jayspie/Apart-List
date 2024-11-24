import express from "express";
import path from "path";
import { fileURLToPath } from "url";
import { spawn } from "child_process";
// Two because there's was some "Overload" issues
import apple from "node:fs";
import test from "node:fs";

const app = express();
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.use(express.urlencoded({ extended: true }));
app.use(express.json()); //// Parses JSON data in request bodies

// Serves static files
app.use(express.static(path.join(__dirname, "view")));
app.use(express.static(path.join(__dirname, "test")));
app.use("/static", express.static("./static/"));
app.use("/status", express.static("./status/"));

function countOccurrences(string, subString) {
  // Counts occurrences of a substring within a string
  return string.split(subString).length - 1;
}

app.get("/", async (req, res) => {
  // Displays the homepage at "/"
  res.sendFile(path.join(__dirname, "view", "index.html"));
});

app.post("/getid", async (req, res) => {
  bud = id.push(Object.values(req.body).toString());
  console.log(id);
});

app.post("/link", async (req, res) => {
  /// Processes link, validates it, and executes Python script if valid
  const link = req.body.link;
  const subString = "apartments";

  if (countOccurrences(link, subString) == 2) {
    if (link.includes("house" || "condos" || "townhomes")) {
      return res.status(400).sendFile(__dirname + "/status" + "/400.html");
    } else {
      console.log("vaild link");
    }
  } else {
    return res.status(400).sendFile(__dirname + "/status" + "/400.html");
  }

  const ip = req.body.ip;
  console.log(ip);
  console.log("link sent");

  const folderName = `\_${ip}`;

  if (!apple.existsSync(folderName)) {
    apple.mkdirSync(folderName); // Creates new folder if not existing
  } else if (apple.existsSync(folderName)) {
    // Deletes folder if it exists, then recreates after a delay
    apple.rm(folderName, { recursive: true }, (err) => {
      if (err) {
        throw err;
      }

      setTimeout(() => {
        apple.mkdirSync(folderName);
      }, 2000);
    });
  }

  const py_process = spawn("python3", ["python/filexe.py", link, ip]);

  py_process.stdout.on("data", (data) => {
    var respond = data.toString().trim();
    if (respond == "stop") {
      return res.status(500).sendFile(__dirname + "/status" + "/400.html");
    }
  });

  py_process.stderr.on("data", (data) => {
    return res.status(500).sendFile(__dirname + "/status" + "/500.html");
  });

  const path = `_${ip}/apartment_list.xlsx`; // Path to the file you want to monitor

  async function checkFileExists() {
    // Checks if the file exists
    if (test.existsSync(path)) {
      return true;
    } else if (!test.existsSync(path)) {
      console.log("false");
      return false;
    }
  }

  const interval = 60000; // Sets interval to check file every 60 seconds
  const intervalId = setInterval(async () => {
    const result = await checkFileExists();
    if (result) {
      clearInterval(intervalId); // Stops checking once the file is found
      res.redirect(`/succes`);
    }
  }, interval);
});

app.get("/succes", async (req, res) => {
  // Displays "suc.html" for download confirmation
  res.sendFile(__dirname + "/test" + "/suc.html");
});

app.get("/file", async (req, res) => {
  // Provides downloadable file based on user's IP address
  fetch("https://ipapi.co/ip/")
    .then(function (response) {
      response.text().then((txt) => {
        const excelFilePath = path.join(
          __dirname,
          `_${txt}/apartment_list.xlsx`
        );
        res.sendFile(excelFilePath, (err) => {
          if (err) console.log(err);
        });
      });
    })
    .catch(function (error) {
      console.log(error);
    });
});

app.get("/download/:ip", (req, res) => {
  // Allows file download using IP from URL parameter
  const txt = req.params.ip.replace(":", "");
  console.log(txt);
  const filePath = path.join(__dirname, `_${txt}`, "apartment_list.xlsx");

  res.download(filePath, `apartment_list.xlsx`, (err) => {
    if (err) {
      console.error("File download failed:", err);
      res.status(500).send("Error downloading file");
    }
  });
});

app.get("/id", async (req, res) => {
  fetch("https://ipapi.co/ip/").then(function (response) {
    response
      .text()
      .then((txt) => {
        console.log(txt);
      })
      .catch(function (error) {
        console.log(error);
      });
  });
});

app.listen(80, () => {
  console.log("[server] Application started!");
});

function sleep(ms) {
  // Utility function to delay for a specified time
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function getFolders(dirPath) {
  // Gets list of directories within a specified path
  const entries = apple.readdirSync(dirPath, { withFileTypes: true });

  const folders = entries
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name);

  return folders;
}

const directoryPath = "./"; // Replace with the directory you want to search

// Continuously cleans up folders every 12 hours
while (true) {
  await sleep(43200000); // Waits for 12 hours
  const folders = getFolders(directoryPath);

  for (let i = 0; i < folders.length; i++) {
    var to_number = Number(folders[i][1]);
    if (Number.isInteger(to_number) == true) {
      apple.readdir(`./${folders[i]}`, (err, files) => {
        if (err) {
          console.error("Error reading directory:", err);
          return;
        }
        if (files.length > 0) {
          apple.rm(`./${folders[i]}`, { recursive: true }, (err) => {
            if (err) {
              throw err;
            }
          });
        } else {
          console.log("noo");
        }
      });
    }
  }
}
