var map = L.map('map',{
}).setView([28.2096,  83.9856],7);
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

var marker = L.marker([28.2096,  83.9856]).addTo(map)
.bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
.openPopup();

// adding map scale
L.control.scale({position:'bottomleft'}).addTo(map)
//adding fullscreen function
var mapid=document.getElementById('map');
function fullScreenView(){
    if(document.fullscreenElement)
    document.exitFullscreen();
    else
    mapid.requestFullscreen();
}
//showing coodinates om mousehover 

map.on('mousemove',function(e){
console.log(e)
$('#coordinate').html(`lat:${e.latlng.lat} long:${e.latlng.lng}`)
})
//map print
// $('#map-print').click(function(){
//     window.print();
// });
L.control.browserPrint({position:'topright'}).addTo(map);

//adding geoJSON file
L.geoJSON(nepalData).addTo(map);
//adding search bar
L.Control.geocoder().addTo(map);
// measure in map
L.control.measure({
    primaryLengthUnit: 'kilometers',
    secondaryLengthUnit: 'meters',
    primaryAreaUnit: 'sqmeters',
    secondaryAreaUnit: undefined 
}).addTo(map);
//adding basemap

var baseMap = {
    'OSM':osm,
    'WATERMAP':waterMap,
    'GOOGLE STREET':googleStreets,
    'GOOGLE SATELITE':googleSat
}
var layerMarker = {
    'MARKER':marker
}

L.control.layers(baseMap,layerMarker,{collapsed:false,position:'topleft'}).addTo(map);

//adding zoom to layer

$('#zoomToLayer').click(function(){
map.setView([28.2096,  83.9856],7)
})