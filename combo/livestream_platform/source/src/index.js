const cookieParser = require('cookie-parser')
const bodyParser = require('body-parser')
const moment = require('moment-timezone')
const express = require('express')
const path = require('path')
const app = express()
const port = 3000

const {TwingEnvironment, TwingLoaderFilesystem} = require('twing');
let loader = new TwingLoaderFilesystem(path.join(__dirname, 'templates'));
let twing = new TwingEnvironment(loader);

const correctLoginCookie = "ad366fce4a77c331a91327c08ba6ff3f";
const timeOfLivestream = moment().tz('Europe/Brussels').hour(20).minute(0).second(0)

function escapeHtml(text) {
  var map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;'
  };
  
  return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}

// Parse URL-encoded body
app.use(bodyParser.urlencoded({ extended: false }))

// Parse cookies for easy use
app.use(cookieParser())

// Tell clients they should have timezone cookie set to 'Europe/Brussels'
app.use((req, res, next) => {
  if (!req.cookies.timezone || req.cookies.timezone !== 'Europe/Brussels') {
    res.cookie('timezone', 'Europe/Brussels', {
      maxAge: 86400,
      httpOnly: true,
    });
  }
  next();
});

// Check if client is authenticated
app.use((req, res, next) => {
  req.auth = (req.cookies.auth && req.cookies.auth === correctLoginCookie);
  next();
})

// Serve everything from 'public' folder as-is
app.use(express.static(path.join(__dirname, 'public')))

// Show homepage
app.get('/', (req, res, next) => {
  if (!req.auth) {
    res.redirect('/login');
  } else {
    res.sendFile(path.join(__dirname, 'templates/home.html'))
  }
})

// Show stream only if it has already started
// It starts at 20:00 'today' in client's local timezone
app.get('/stream', (req, res, next) => {
  if (!req.auth) {
    res.redirect('/login');
  } else {
    try {
      // Check which timezone client is in (based on cookie), assume 'Europe/Brussels' if none is set
      const requestedTime = moment().tz(`${req.cookies.timezone || 'Europe/Brussels'}`);
      if (requestedTime.format() > timeOfLivestream.format()) {
        res.sendFile(path.join(__dirname, 'templates/video.html'))
      } else {
        twing.render('too-soon.html', {
          'requestedTime': requestedTime.format('DD MMM YY - HH:mm:ss'),
          'targetTime': timeOfLivestream.format('DD MMM YY - HH:mm:ss'),
        }).then((output) => {
          res.end(output);
        });
      }
    } catch(e) {
      res.type('txt').status(500).send('500 - Something went wrong...')
    }
  }
})

app.post('/recover', (req, res) => {
  q1Correct = req.body.q1.trim().toLowerCase() === 'potvos.video';
  q2Correct = req.body.q2.trim().toLowerCase() === 'studio oranjeboom';
  q3Correct = req.body.q3.trim() === 'EDM-1.05a';
  if (q1Correct && q2Correct && q3Correct) {
    res.cookie('auth', correctLoginCookie, {
      maxAge: 86400,
      httpOnly: true,
    });
    res.redirect('/');
  } else {
    twing.render('recover.html', {
      'attempted': true,
      'q1Correct': q1Correct,
      'q2Correct': q2Correct,
      'q3Correct': q3Correct,
      'q1Value': escapeHtml(req.body.q1),
      'q2Value': escapeHtml(req.body.q2),
      'q3Value': escapeHtml(req.body.q3),
    }).then((output) => {
      res.end(output);
    });
  }
})

app.get('/recover', (req, res) => {
  twing.render('recover.html', {
    'attempted': false,
    'q1Correct': false,
    'q2Correct': false,
    'q3Correct': false,
    'q1Value': '',
    'q2Value': '',
    'q3Value': '',
  }).then((output) => {
    res.end(output);
  });
})

app.get('/login', (req, res) => {
  res.sendFile(path.join(__dirname, 'templates/signin.html'))
})

app.post('/login', (req, res) => {
  res.sendFile(path.join(__dirname, 'templates/signin-wrong.html'))
})

app.get('*', function(req, res){
  res.type('txt').status(404).send(`404 - We don't serve ${decodeURIComponent(req.path)}`);
});


app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`)
})