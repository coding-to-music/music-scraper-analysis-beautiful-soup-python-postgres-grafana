const puppeteer = require("puppeteer");

const scrapeHackerNews = async () => {
  //   const browser = await puppeteer.launch({ headless: true });
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto("https://news.ycombinator.com/", {
    waitUntil: "domcontentloaded",
  });

  await page.waitForSelector(".athing");

  console.log("before loop");

  const topPosts = await page.evaluate(() => {
    const posts = [];
    const postElements = document.querySelectorAll(".athing");
    console.log(postElements);

    postElements.forEach((element) => {
      console.log(element);
      const titleElement = element.querySelector(".storylink");
      const title = titleElement ? titleElement.textContent : "";

      const url = titleElement ? titleElement.href : "";

      const authorElement = element.nextElementSibling.querySelector(".hnuser");
      const author = authorElement ? authorElement.textContent : "";

      console.log(title);
      console.log(url);
      console.log(author);
      posts.push({ title, url, author });
    });

    return posts;
  });

  await browser.close();
  return topPosts;
};

console.log("after loop");

scrapeHackerNews()
  .then((topPosts) => {
    console.log("Top posts on Hacker News:");
    console.log(topPosts);
  })
  .catch((err) => {
    console.error("Error while scraping:", err);
  });

// const puppeteer = require('puppeteer');

// puppeteer.launch({ headless: true, args: ['--user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36"] }).then(async)

// const page = await puppeteer.Browser.newPage();
// await page.goto("https://news.ycombinator.com/");
// await page.waitForSelector('body');

// var rposts = await page.evaluate(() -> {

// });

// console.log(rposts);
// await puppeteer.Browser.close();
// ]
// }).catch(function(error)) {
//     console.error(error);
// });

// postItems = [];

// posts.array.forEach((element) => {
//   // row 1

//   let title = "";
//   let link = "";

//   try {
//     title = item.querySelector(".storylink").innerText;
//     if (title != "") {
//       // first row
//       link = item.querySelector(".storylink").href;

//       postItems.push({ title: title, link: link });
//     }
//   } catch (error) {}
// });

// return postItems;

// Web Scraping Hacker News with Puppeteer | Proxies API
// https://www.youtube.com/watch?v=qQ-3fHopU20&ab_channel=ProxiesAPI
// Web Scraping Hacker News with Puppeteer.
// Here is the link to the rotating Proxies API service mentioned in the video:- https://www.proxiesapi.com/
// We have also launched our Brand New Cloud Based Web Crawling service at https://www.teracrawler.io/
// We have a running offer of 1000 API calls completely free. Register and get your free API Key here.
