const bodyParser = require('body-parser')
const express = require('express')
const path = require('path')
const app = express()
const port = 3000

const ps5gold_id = "7ca9719d-bb05-419e-9a8e-f7fa96055689";
const ps5gold_price = 10000;

function getPrice(res, id, coupon) {
  if (typeof(id) !== 'string') { res.status(400).type('text').send('item not valid'); return false}
  if (typeof(coupon) !== 'string') { res.status(400).type('text').send('coupon not valid'); return false}

  id = id.trim().toLowerCase();
  coupon = coupon.trim();

  if (id !== ps5gold_id) { res.status(404).type('text').send('product not found'); return false}
  if (coupon.length > 0) {
    const coupon_value = coupon.match(/^piday(\d.\d\d)$/);
    if (coupon_value === null || coupon_value.length !== 2) { res.status(400).type('text').send('coupon does not match regex'); return false}
    const leftover_price = ps5gold_price - parseFloat(coupon_value[1])
    if (leftover_price < 0) { res.status(409).type('text').send('cannot use coupon which exceeds total price'); return false}
    return leftover_price;
  } else {
    return ps5gold_price;
  }
}

// Parse JSON & URL-encoded body
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

// Serve everything from 'public' folder as-is
app.use(express.static(path.join(__dirname, 'public')))

// Show homepage
app.get('/', (req, res, next) => {
  res.sendFile(path.join(__dirname, 'templates', 'index.html'));
})

// Show cart
app.get('/shop', (req, res, next) => {
  res.sendFile(path.join(__dirname, 'templates', 'shop.html'));
})

// API endpoint to calculate cart price
app.post('/calc-cart-price', (req, res) => {
  let id = req.body.item;
  let coupon = req.body.coupon;
  const leftover_price = getPrice(res, id, coupon);
  if (leftover_price === false) return;
  res.status(200).type('text').send(leftover_price.toString())
})

// API endpoint to get flag
app.post('/buy', (req, res) => {
  let id = req.body.item;
  let coupon = req.body.coupon;
  let suggested_price = req.body.price;
  if (typeof(suggested_price) !== 'string') { res.status(400).type('text').send('suggested_price not valid'); return false}
  suggested_price = parseFloat(suggested_price);
  const leftover_price = getPrice(res, id, coupon);
  if (suggested_price !== leftover_price) { res.status(409).type('text').send('Price does not match coupon value. Please apply your coupon.'); return false}
  if (leftover_price === false) return;
  if (leftover_price === 0) {
    let flag = "you got the flag! run with correct ENV variable to get the real flag";
    if (process && process.env && process.env.UHCTF_FLAG) flag = process.env.UHCTF_FLAG;
    res.status(200).type('text').send(flag);
  } else {
    res.status(200).type('text').send('/images/pay.png');
  }
})

app.get('*', function(req, res){
  res.type('txt').status(404).send("404");
});


app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`)
})