import https from "https";
import fs from "fs";
import "dotenv/config";

// const docId = process.env.DOC_ID as string;
// const sheetId = process.env.SHEET_ID as string;
// const format = "json";
// const url = `https://docs.google.com/spreadsheets/d/${docId}/gviz/tq?tqx=out:${format}&tq&gid=${sheetId}`;

// console.log(`Downloading Google sheet at ${url}...`);

// const startToRemove = "/*O_o*/\ngoogle.visualization.Query.setResponse(";
// const endToRemove = ");";

// let response = await fetch(url);
// let result = await response.text();
// result = result.substring(startToRemove.length);
// result = result.slice(0, -endToRemove.length);

let result = fs.readFileSync("./sheet.json", "utf8");
let data = JSON.parse(result);

const firstRow = data.table.rows[0].c;
const aiHubSheetRow = {
  url: firstRow[0]?.v,
  downloadCounter: firstRow[1]?.v,
  modelName: firstRow[2]?.v,
  filename: firstRow[3]?.v,
  fileSize: firstRow[4]?.v,
  md5Hash: firstRow[5]?.v,
  rvcVersion: firstRow[6]?.v,
  altUrl1: firstRow[7]?.v,
  altUrl2: firstRow[8]?.v,
  altUrl3: firstRow[9]?.v,
  altUrl4: firstRow[10]?.v,
  altUrl5: firstRow[11]?.v,
  altUrl6: firstRow[12]?.v,
  altUrl7: firstRow[13]?.v,
  altUrl8: firstRow[14]?.v,
  altUrl9: firstRow[15]?.v,
  altUrl10: firstRow[16]?.v,
  altUrl11: firstRow[17]?.v,
  altUrl12: firstRow[18]?.v,
  altUrl13: firstRow[19]?.v,
  altUrl14: firstRow[20]?.v,
  altUrl15: firstRow[21]?.v,
  altUrl16: firstRow[22]?.v,
  altUrl17: firstRow[23]?.v,
  altUrl18: firstRow[24]?.v,
  altUrl19: firstRow[25]?.v,
};

console.log(aiHubSheetRow);

// TODO: write mutations to add the Model records

fs.writeFileSync("./sheet.json", result);
