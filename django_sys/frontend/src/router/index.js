import Vue from 'vue';
import VueRouter from 'vue-router';
import Homepage from '../views/Homepage.vue';
import GameInterface from '../views/GameInterface.vue';
import MapEditor from '../views/MapEditor.vue';
import StageSelect from '../views/StageSelect.vue';
import GameHelp from '../views/GameHelp.vue';
import Community from '../views/Community.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Homepage,
  },
  {
    path: '/GameInterface/10001',
    name: '游戏界面',
    component: GameInterface,
  },
  {
    path: '/GameInterface/10002',
    name: '游戏界面',
    component: GameInterface,
  },
  {
    path: '/GameInterface/10003',
    name: '游戏界面',
    component: GameInterface,
  },
  {
    path: '/GameInterface/10004',
    name: '游戏界面',
    component: GameInterface,
  },
  {
    path: '/GameInterface/10005',
    name: '游戏界面',
    component: GameInterface,
  },
  {
    path: '/GameInterface/10006',
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
  {
    path: '/GameHelp',
    name: '游戏帮助',
    component: GameHelp,
  },
  {
    path: '/Community',
    name: '玩家社区',
    component: Community,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
