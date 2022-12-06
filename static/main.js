var map = L.map('map',{
}).setView([38.8610,  71.2761],7);
map.zoomControl.setPosition('topright')

var osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var waterMap = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
subdomains: 'abcd',
minZoom: 1,
maxZoom: 16,
ext: 'jpg'
});

var googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
maxZoom: 20,
subdomains:['mt0','mt1','mt2','mt3']
});

var googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
maxZoom: 20,
subdomains:['mt0','mt1','mt2','mt3']
});

var marker = L.marker([38.8610,  71.2761]).addTo(map)
.bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
.openPopup();

// adding map scale
L.control.scale({position:'bottomleft'}).addTo(map)

//showing coodinates om mousehover 

map.on('mousemove',function(e){
console.log(e)
$('#coordinate').html(`lat:${e.latlng.lat} long:${e.latlng.lng}`)
})


//adding geoJSON file
L.geoJSON(nepalData).addTo(map);


//adding basemap

var baseMap = {
    'OSM':osm,
    'WATERMAP':waterMap,
    'GOOGLE STREET':googleStreets,
    'GOOGLE SATELITE':googleSat
};



