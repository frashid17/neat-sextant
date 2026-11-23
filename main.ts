import * as qfs from "node:fs";
qfs.mkdirSync("/output", { recursive: true });
qfs.writeFileSync(
  "/output/entry.txt",
  "Park a bounty on make.fun with real cash, let AI agents compete, pay the winner.",
  "utf8",
);
