var map;
var view;

function ourLoc(){
  map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view: view
  });
}

function initMap(){
  view.animate({
    center: map,
    duration: 2000
  });
}



var map, heatmap;

      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 13,
          center: {lat: 37.775, lng: -122.434},
          mapTypeId: 'satellite'
        });

        heatmap = new google.maps.visualization.HeatmapLayer({
          data: getPoints(),
          map: map
        });
      }

      function Heatmap() {
        heatmap.setMap(heatmap.getMap() ? null : map);
      }

      map = new google.maps.Map(document.getElementById('map_canvas'),
      mapOptions);

      pointArray = new google.maps.MVCArray(taxidata);

      heatmap= new google..maps.visualization.HeatmapLayer({
        data.pointArray
      });
      heatmap.setMap(map);
    }

    function toggleHeatmap(){
      heatmap.setMap(heatmap.getMap() ? null : map);
    }


      function changeHue() {
        var hue = [
          'rgba(0, 255, 255, 0)',
          'rgba(0, 255, 255, 1)',
          'rgba(0, 191, 255, 1)',
          'rgba(0, 127, 255, 1)',
          'rgba(0, 63, 255, 1)',
          'rgba(0, 0, 255, 1)',
          'rgba(0, 0, 223, 1)',
          'rgba(0, 0, 191, 1)',
          'rgba(0, 0, 159, 1)',
          'rgba(0, 0, 127, 1)',
          'rgba(63, 0, 91, 1)',
          'rgba(127, 0, 63, 1)',
          'rgba(191, 0, 31, 1)',
          'rgba(255, 0, 0, 1)'
        ]
        heatmap.set('hue', heatmap.get('hue') ? null : hue);
      }

      function changeRadius() {
        heatmap.set('radius', heatmap.get('radius') ? null : 20);
      }

      // Heatmap data: 500 Points
      function getPoints() {
        return [
          new google.maps.LatLng(37.782, -122.447),
          new google.maps.LatLng(37.782, -122.445),
          new google.maps.LatLng(37.782, -122.443),
          new google.maps.LatLng(37.782, -122.441),
          new google.maps.LatLng(37.782, -122.439),
          new google.maps.LatLng(37.782, -122.437),
          new google.maps.LatLng(37.782, -122.435),
          new google.maps.LatLng(37.785, -122.447),
          new google.maps.LatLng(37.785, -122.445),
          new google.maps.LatLng(37.785, -122.443),
          new google.maps.LatLng(37.785, -122.441),
          new google.maps.LatLng(37.785, -122.439),
          new google.maps.LatLng(37.785, -122.437),
          new google.maps.LatLng(37.785, -122.435)
        ];
      }

      function initialize(){
        var mapOtions = {
          zoom: 13,
          center: new google.maps.LatLng(37.782, -122.445),
          mapTypeId: google.maps.MapTypeId.SATELLITE
        };
        map = new google.maps.Map(document.getElementById('map_canvas'),
      mapOptions);

      pointArray = new google.maps.MVCArray(taxidata);

      heatmap= new google..maps.visualization.HeatmapLayer({
        data.pointArray
      });
      heatmap.setMap(map);
      }
      google.maps.event.addDomListener(window, 'load', initialize); 
    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?libraries=visualization&callback=initMap">
    </script>

  </body>

</html>
