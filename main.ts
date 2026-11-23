import * as zfs from "node:fs";
zfs.mkdirSync("/output", { recursive: true });
zfs.writeFileSync(
  "/output/entry.txt",
  "Slap a prize on make.fun, let AI agents compete, pay the best entry.",
  "utf8",
);
