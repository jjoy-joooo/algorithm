const fs = require("fs");
const filePath = "./data.txt";

function readDataSync() {
  try {
    const data = fs.readFileSync(filePath, "utf8");
    return data;
  } catch (error) {
    console.error(`Error reading file: ${error}`);
    return null;
  }
}

const fileData = readDataSync();
console.log(fileData);
module.exports = fileData;
