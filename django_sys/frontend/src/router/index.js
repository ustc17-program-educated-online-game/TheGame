import Vue from 'vue';
import VueRouter from 'vue-router';
import Homepage from '../views/Homepage.vue';
import GameInterface from '../views/GameInterface.vue';
import MapEditor from '../views/MapEditor.vue';
import StageSelect from '../views/StageSelect.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Homepage,
  },
  {
    path: '/GameInterface',
    name: '游戏界面',
    component: GameInterface,
  },
  {
    path: '/MapEditor',
    name: '地图编辑器',
    component: MapEditor,
  },
  {
    path: '/StageSelect',
    name: '关卡选择',
    component: StageSelect,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
