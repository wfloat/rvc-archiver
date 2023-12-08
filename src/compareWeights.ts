// import { promises as fs } from "fs";

// // Function to read the first n bytes of a file
// const readFirstNBytes = async (
//   filePath: string,
//   n: number
// ): Promise<Buffer> => {
//   const fileHandle = await fs.open(filePath, "r");
//   try {
//     const buffer = Buffer.alloc(n);
//     const { bytesRead } = await fileHandle.read(buffer, 0, n, 0);
//     return buffer.slice(0, bytesRead);
//   } finally {
//     await fileHandle.close();
//   }
// };

// // Function to compare the first n bytes of two files
// const compareFiles = async (
//   filePath1: string,
//   filePath2: string,
//   n: number
// ): Promise<boolean> => {
//   const data1 = await readFirstNBytes(filePath1, n);
//   const data2 = await readFirstNBytes(filePath2, n);
//   return data1.equals(data2);
// };

// // Example usage
const filePathA =
  "/home/mitch/dev/wfloat/rvc-archiver/omniman_a/OmniMan_e300_s1800.pth";
const filePathB = "/home/mitch/dev/wfloat/rvc-archiver/omniman_b/model.pth";
const filePathC =
  "/home/mitch/dev/wfloat/rvc-archiver/omniman_c/Omni-Man_MK1.pth";
// const n = 1167671680; // Number of bytes to compare

// compareFiles(filePathA, filePathB, n)
//   .then((areSame) =>
//     console.log(`The files are ${areSame ? "the same" : "different"}`)
//   )
//   .catch((error) => console.error("An error occurred:", error));

import { createReadStream } from "fs";
import { createHash } from "crypto";
import { promises as fsPromises } from "fs";

async function hashFile(filePath: string) {
  try {
    const hash = createHash("sha256");
    const stream = createReadStream(filePath);

    for await (const chunk of stream) {
      hash.update(chunk);
    }

    return hash.digest("hex");
  } catch (err) {
    console.error("Error hashing file:", err);
    throw err;
  }
}

let fileHash = await hashFile(filePathC);
console.log(`SHA256 ${fileHash}`); // The SHA-256 hash of the file

// A: 3e2badeacdc9af3f5fd76f007f77c2236dcf40be9ee3fc724b4a0e67284a275e
// B: 3e2badeacdc9af3f5fd76f007f77c2236dcf40be9ee3fc724b4a0e67284a275e
// C: 5dd2e9eff5e2f3755d3522b62acf57122d4e08500bca3c8f3a7d2b2691fe3475\

// D: 26d46d3ab00691e0dd7c1d8407d4f5ab

async function hashFileMD5(filePath: string) {
  try {
    const hash = createHash("md5"); // Using MD5 here
    const stream = createReadStream(filePath);

    for await (const chunk of stream) {
      hash.update(chunk);
    }

    return hash.digest("hex");
  } catch (err) {
    console.error("Error hashing file:", err);
    throw err;
  }
}

fileHash = await hashFileMD5(filePathA);
console.log(`${fileHash}`); // The MD5 hash of the file
fileHash = await hashFileMD5(filePathB);
console.log(`${fileHash}`); // The MD5 hash of the file
fileHash = await hashFileMD5(filePathC);
console.log(`${fileHash}`); // The MD5 hash of the file
