import https from "https";
import fs from "fs";
import "dotenv/config";

import { testing } from "./util/parse-google-sheet.js";

const realtimeArchiveUrl = process.env.REALTIME_ARCHIVE_URL as string;
// console.log(realtimeArchiveUrl);
// let ans = await fetchGoogleSheet(realtimeArchiveUrl);
let ans = testing();
// console.log(ans);
