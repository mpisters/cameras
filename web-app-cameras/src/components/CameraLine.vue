<template>
  <tr>
    <td>{{ camera.number }}</td>
    <td>{{ camera.Camera }}</td>
    <td>{{ camera.Latitude }}</td>
    <td>{{ camera.Longitude }}</td>
  </tr>
</template>

<script>
export default {
  name: 'CameraLine',
  props: {
    camera: {
      type: Object,
      default: () => {
      },
    },
  },
};
</script>

<style scoped>

</style>
