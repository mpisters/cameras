<template>
  <div id="mapid" v-if="cameras"></div>
  <div v-else><p>No cameras found for map</p></div>
</template>

<script>
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import {mapGetters} from 'vuex';

export default {
  name: 'CameraMap',
  computed: {
    ...mapGetters({cameras: 'getCameras'}),
  },
  data() {
    return {map: null};
  },
  async mounted() {
    await this.initiatalizeMap();
    this.addMarkers();
  },
  methods: {
    async initiatalizeMap() {
      this.map = L.map('mapid').setView([52.0914, 5.1115], 13);
      L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoibXBpc3RlcnMiLCJhIjoiY2tlcXd5eDg0MHdvMDJ5b2V2dHlwenNpZyJ9.nAiAL_TYNH-pC864Cmtciw',
      }).addTo(this.map);
    },
    addMarkers() {
      this.cameras.map((camera) => {
        if (camera.Latitude && camera.Longitude) {
          L.marker([parseFloat(camera.Latitude), parseFloat(camera.Longitude)]).addTo(this.map);
        }
      });
    },
  },
  beforeDestroy() {
    if (this.map) {
      this.map.remove();
    }
  },
};
</script>

<style scoped>
#mapid {
  margin: auto;
  height: 500px;
  width: 100%;
}
</style>
