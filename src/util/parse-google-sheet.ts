import https from "https";

export function testing() {
  console.log("updated?");
}

// export async function fetchGoogleSheet(url: string) {
//   try {
//     const response = await new Promise((resolve, reject) => {
//       const req = https.request(url, (res) => {
//         const body = [];
//         let isStarted = false;

//         res.on("data", (chunk) => {
//           if (!isStarted && !String(chunk).startsWith("/*O_o*/"))
//             return resolve(null);
//           isStarted = true;

//           body.push(chunk);
//         });

//         res.on("end", () => {
//           const response = {
//             ok: true,
//             text: () => Buffer.concat(body).toString(),
//           };
//           resolve(response);
//         });
//       });

//       req.on("error", reject);
//       req.end();
//     });

//     return response;
//   } catch (error) {
//     console.error("Error fetching Google Sheet:", error);
//     return null;
//   }
// }
