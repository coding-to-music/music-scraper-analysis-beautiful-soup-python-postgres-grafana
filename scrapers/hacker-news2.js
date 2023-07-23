const puppeteer = require("puppeteer");

const scrapeHackerNews = async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  await page.goto("https://news.ycombinator.com/", {
    waitUntil: "domcontentloaded",
  });

  await page.waitForSelector(".athing");

  // Debug: Check the number of postElements found
  const postElements = await page.$$(".athing");
  console.log("Number of postElements found:", postElements.length);

  const topPosts = await page.evaluate(() => {
    const posts = [];
    const postElements = document.querySelectorAll(".athing");

    postElements.forEach((element) => {
      console.log(element); // Debug: Log each element

      const titleElement = element.querySelector(".storylink");
      const title = titleElement ? titleElement.textContent : "";

      const url = titleElement ? titleElement.href : "";

      const authorElement = element.nextElementSibling.querySelector(".hnuser");
      const author = authorElement ? authorElement.textContent : "";

      posts.push({ title, url, author });
    });

    return posts;
  });

  await browser.close();
  return topPosts;
};
