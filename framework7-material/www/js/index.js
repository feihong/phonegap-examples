var myApp = new Framework7({
  material: true,   // Enable Material theme
  modalTitle: 'This is a modal',
})

var $$ = Dom7

var mainView = myApp.addView('.view-main', {})

function initIndexPage() {
  $$('.alert-button').on('click', function() {
    myApp.alert('Woo hoo!')
  })

  var info = {
    'Cordova version': device.cordova,
    'Platform': device.platform,
    'Device model': device.model,
    'Platform version': device.version,
    // 'UUID': device.uuid,
  }

  for (var key in info) {
    var val = info[key]
    $$('.device-info-list').append(
      '<li><div class="item-content"><div class="item-inner"><div class="item-title">' + key + '</div><div class="item-after">' + val + '</div></div></div></li>'
    )
  }

  $$('.uuid').html(device.uuid)
}

var isPhoneGap = navigator.userAgent.match(/(iPhone|iPod|iPad|Android|BlackBerry|IEMobile)/)
if (isPhoneGap) {
  document.addEventListener("deviceready", initIndexPage, false)
} else {
  var device = {
    cordova: 'N/A',
    platform: 'browser',
    model: 'N/A',
    version: 'N/A',
    uuid: 'N/A',
  }
  initIndexPage()
}
