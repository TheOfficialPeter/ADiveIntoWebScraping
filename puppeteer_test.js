var puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('http://quotes.toscrape.com');
    
    // find all elements with the class 'quote'
    const quoteElements = await page.$$('.quote');

    for (const quoteElement of quoteElements) {
        const textProperty = await quoteElement.getProperty('innerText');
        const text = await textProperty.jsonValue();
        console.log(text);
    }

    await browser.close();
})();