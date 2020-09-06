import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const state = {
  cameras: [],
};

const getters = {
  getCameras: state => {
    return state.cameras;
  },
};

const actions = {
  getCameras: ({commit}) => {
    return axios.get('/api/camera/').then((response) => {
      commit('updateCameras', response.data);
      return response.data;
    });
  },
};

const mutations = {
  updateCameras: (state, payload) => {
    state.cameras = [...payload];
  },
};

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
});
