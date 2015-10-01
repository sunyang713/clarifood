/**
 * Map locations using Google Maps API
 */

var mapStyles = [
  {
    "featureType": "water",
    "elementType": "geometry",
    "stylers": [
      { "color": "#e9e9e9" },
      { "lightness": 17 }
    ]
  },{
    "featureType": "landscape",
    "elementType": "geometry",
    "stylers": [
      { "color": "#f5f5f5" },
      { "lightness": 20 }
    ]
  },{
    "featureType": "road.highway",
    "elementType": "geometry.fill",
    "stylers": [
      { "color": "#ffffff" },
      { "lightness": 17 }
    ]
  },{
    "featureType": "road.highway",
    "elementType": "geometry.stroke",
    "stylers": [
      { "color": "#ffffff" },
      { "lightness": 29 },
      { "weight": 0.2 }
    ]
  },{
    "featureType": "road.arterial",
    "elementType": "geometry",
    "stylers": [
      { "color": "#ffffff" },
      { "lightness": 18 }
    ]
  },{
    "featureType": "road.local",
    "elementType": "geometry",
    "stylers": [
      { "color": "#ffffff" },
      { "lightness": 16 }
    ]
  },{
    "featureType": "poi",
    "elementType": "geometry",
    "stylers": [
      { "color": "#f5f5f5" },
      { "lightness": 21 }
    ]
  },{
    "featureType": "poi.park",
    "elementType": "geometry",
    "stylers": [
      { "color": "#dedede" },
      { "lightness": 21 }
    ]
  },{
    "elementType": "labels.text.stroke",
    "stylers": [
      { "visibility": "on" },
      { "color": "#ffffff" },
      { "lightness": 16 }
    ]
  },{
    "elementType": "labels.text.fill",
    "stylers": [
      { "saturation": 36 },
      { "color": "#333333" },
      { "lightness": 40 }
    ]
  },{
    "elementType": "labels.icon",
    "stylers": [
      { "visibility": "off" }
    ]
  },{
    "featureType": "transit",
    "elementType": "geometry",
    "stylers": [
      { "color": "#f2f2f2" },
      { "lightness": 19 }
    ]
  },{
    "featureType": "administrative",
    "elementType": "geometry.fill",
    "stylers": [
      { "color": "#fefefe" },
      { "lightness": 20 }
    ]
  },{
    "featureType": "administrative",
    "elementType": "geometry.stroke",
    "stylers": [
      { "color": "#fefefe" },
      { "lightness": 17 },
      { "weight": 1.2 }
    ]
  }
];
var mapOptions = {
  center: { lat: 40.7577, lng: -73.9857 },
  zoom: 12,
  disableDefaultUI: true,

  zoomControl: true,
  zoomControlOptions: {
    style: google.maps.ZoomControlStyle.SMALL
  },

  styles: mapStyles
};

var MAP_ICON = {
  path: fontawesome.markers.MAP_MARKER,
  scale: 0.5,
  anchor: new google.maps.Point(20, -5),
  strokeOpacity: 0,
  fillColor: '#f00',
  fillOpacity: .6
};

var map;
var infoBox;

function map() {
  map = new google.maps.Map(document.getElementById('map'), mapOptions);
  if (locations.length > 0) {
    bounds = new google.maps.LatLngBounds();

    for (var i = 0; i < locations.length; i++) {
      loc = locations[i];
      // add each location to map as a marker
      var marker = new google.maps.Marker({
        map: map,
        icon: MAP_ICON,
        position: {lat: loc.location.lat, lng: loc.location.lng}
      });
      // attach event listener to marker
      attachInfo(marker, loc);
      // extend bounds of map view
      bounds.extend(new google.maps.LatLng(loc.location.lat, loc.location.lng));
    }
  }
}

/*
 * Attaches info box and event handler for when a marker is clicked.
 * 'marker' is a google.maps.Marker object
 * 'place' is an object containing info on the place
 */
function attachInfo(marker, place) {
  // Add info box
  var contentString = '';
  if (place) {
    contentString = '<div class="infobox">' + 
      '<b>' + place.name + '</b><br>' +
      place.address + '</div>';
      addMarkListener(marker, contentString);
  }
}

/*
 * Adds a listener to a given marker
 */
function addMarkListener(marker, content) {
  marker.info = content;

  google.maps.event.addListener(marker, 'click', function () {
    // Info box appears when marker clicked
    infoBox.setContent(marker.info);
    infoBox.open(map, marker);
  });
}


function initialize() {
  map();

  infoBox = new google.maps.InfoWindow({ maxWidth: 230 });
}

// load after page has loaded
google.maps.event.addDomListener(window, 'load', initialize);