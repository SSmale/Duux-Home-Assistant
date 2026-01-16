import fs from "fs";

const notes = process.argv[2];

const HEADER = `# Changelog

All notable changes to this project will be documented in this file.
`;

const file = "CHANGELOG.md";
const existing = fs.existsSync(file) ? fs.readFileSync(file, "utf8") : HEADER;

if (!existing.startsWith(HEADER)) {
    throw new Error("CHANGELOG.md header was modified or missing");
}

const rest = existing.slice(HEADER.length).trimStart();

const updated =
    `${HEADER}

${notes.trim()}

${rest ? "\n" + rest : ""}
`;

fs.writeFileSync(file, updated);
