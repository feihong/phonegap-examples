(function() {
  var ua = navigator.userAgent.toLowerCase()
  if (ua.match('android') || !ua.match('chrome')) {
    document.write('<script type="text/javascript" src="cordova.js"></script>')
  }
})()
