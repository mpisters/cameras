<template>
  <table id="cameraTableContainer">
    <tbody v-if="cameras">
    <tr>
      <td>
        <table id="column3">
          <thead>
          <tr>
            <th colspan="4">Cameras 3</th>
          </tr>
          <tr>
            <th>Number</th>
            <th>Name</th>
            <th>Latitude</th>
            <th>Longitude</th>
          </tr>
          </thead>
          <tbody>

          <camera-line v-for="camera in getCameras3()"
                       :key="camera.row_number"
                       :camera="camera">
          </camera-line>
          </tbody>
        </table>
      </td>
      <td>
        <table id="column5">
          <thead>
          <tr>
            <th colspan="4">Cameras 5</th>
          </tr>
          <tr>
            <th>Number</th>
            <th>Name</th>
            <th>Latitude</th>
            <th>Longitude</th>
          </tr>
          </thead>
          <tbody>
          <camera-line v-for="camera in getCameras5()"
                       :key="camera.row_number"
                       :camera="camera">
          </camera-line>
          </tbody>
        </table>
      </td>
      <td>
        <table id="column15">
          <thead>
          <tr>
            <th colspan="4">Cameras 3 &amp; 5</th>
          </tr>
          <tr>
            <th>Number</th>
            <th>Name</th>
            <th>Latitude</th>
            <th>Longitude</th>
          </tr>
          </thead>
          <tbody>
          <camera-line v-for="camera in getCameras3And5()"
                       :key="camera.row_number"
                       :camera="camera">
          </camera-line>
          </tbody>
        </table>
      </td>
      <td>
        <table id="columnOther">
          <thead>
          <tr>
            <th colspan="4">Cameras Overig</th>
          </tr>
          <tr>
            <th>Number</th>
            <th>Name</th>
            <th>Latitude</th>
            <th>Longitude</th>
          </tr>
          </thead>
          <tbody>
          <camera-line v-for="camera in getOtherCameras()"
                       :key="camera.row_number"
                       :camera="camera">
          </camera-line>
          </tbody>
        </table>
      </td>
    </tr>
    </tbody>
    <tbody v-else>
    <p>No cameras could be found</p>
    </tbody>
  </table>
</template>

<script>
import {mapGetters} from 'vuex';
import CameraLine from '@/components/CameraLine';

export default {
  name: 'CameraOverview',
  computed: {
    ...mapGetters({cameras: 'getCameras'}),
  },
  components: {
    cameraLine: CameraLine,
  },
  methods: {
    getCameras3() {
      return this.cameras.filter((camera) => parseInt(camera.number) % 3 === 0);
    },
    getCameras5() {
      return this.cameras.filter((camera) => parseInt(camera.number) % 5 === 0);
    },
    getCameras3And5() {
      return this.cameras.filter((camera) => parseInt(camera.number) % 5 === 0 || parseInt(camera.number) % 3 === 0);
    },
    getOtherCameras() {
      return this.cameras.filter((camera) => !(parseInt(camera.number) % 5 === 0 || parseInt(camera.number) % 3 === 0));
    },

  },
};
</script>

<style scoped>

</style>
