const { chromium } = require(process.env.HOME + "/projects/torque-video/node_modules/playwright-core");
(async () => { const b = await chromium.launch({ channel: "chrome", headless: true }); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  for (const n of ["demo", "pitch"]) { await p.goto("file://" + __dirname + "/" + n + ".html"); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
    const fam = await p.evaluate(() => [...document.fonts].filter((f) => f.status === "loaded").map((f) => f.family + " " + f.weight).join(", "));
    await p.screenshot({ path: __dirname + "/" + n + ".png", clip: { x: 0, y: 0, width: 1280, height: 720 } }); console.log(n, "fonts:", fam); }
  await b.close(); })();
