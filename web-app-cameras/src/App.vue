<template>
  <div id="app">
    <h1>Security cameras Utrecht</h1>
    <camera-map></camera-map>
    <div id="source">
      source:
      <a href="https://data.overheid.nl/data/dataset/camera-s">https://data.overheid.nl/data/dataset/camera-s</a>
    </div>
    <main>
      <camera-overview></camera-overview>
    </main>
  </div>
</template>

<script>
import CameraOverview from '@/components/CameraOverview';
import CameraMap from '@/components/CameraMap';

export default {
  name: 'App',
  components: {
    cameraOverview: CameraOverview,
    cameraMap: CameraMap
  },
  data(){
    return {cameras: []}
  },
  async beforeCreate() {
    await this.$store.dispatch('getCameras');
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
