import Vue from 'vue';
import App from './App.vue';
import store from './store/store';
Vue.config.productionTip = process.env.NODE_ENV === 'development'

new Vue({
  store,
  render: h => h(App),
}).$mount('#app');
