import https from "https";
import fs from "fs";
import "dotenv/config";

const docId = process.env.DOC_ID as string;
const sheetId = process.env.SHEET_ID as string;
const format = "json";
const url = `https://docs.google.com/spreadsheets/d/${docId}/gviz/tq?tqx=out:${format}&tq&gid=${sheetId}`;

console.log(`Downloading Google sheet at ${url}...`);

const startToRemove = "/*O_o*/\ngoogle.visualization.Query.setResponse(";
const endToRemove = ");";

let response = await fetch(url);
let data = await response.text();
data = data.substring(startToRemove.length);
data = data.slice(0, -endToRemove.length);
fs.writeFileSync("./sheet.json", data);
