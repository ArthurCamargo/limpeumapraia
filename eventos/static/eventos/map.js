var map = L.map('map', {
    center: [20.0, 5.0],
    minZoom: 2,
    zoom: 2,
});

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a','b','c']
}).addTo( map );


function addMarker(name, date, coord, map){
    coord = coord.split(",");
    console.log(coord);
    var marker = L.marker([parseFloat(coord[0]), parseFloat(coord[1])]).addTo(map);
    marker.bindPopup(name + " " + date).openPopup();
    map.setView([parseFloat(coord[0]), parseFloat(coord[1])], 13);
    return marker
}

function zoom(coord, map, zoom) {
    coord = coord.split(",");
    coord = [parseFloat(coord[0]), parseFloat(coord[1])]
    map.setView(coord, zoom);
}
