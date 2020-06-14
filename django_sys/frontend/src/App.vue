<template>
  <div id="app">
    <div id="nav">
      <!-- The followings are the navigations in the top of our website -->
      <navigation></navigation>
      <!-- <navigation-background></navigation-background>
      <navigation-bar></navigation-bar>
      <logo></logo>
      <link-button address="/" content="主页" left="35%"></link-button>
      <link-button address="/GameInterface" content="游戏" left="45%"></link-button>
      <link-button address="/MapEditor" content="地图编辑器" left="55%"></link-button>
      <link-button address="/" content="注册" left="80%"></link-button>
      <link-button address="/" content="登录" left="90%"></link-button> -->
    </div>
    <router-view/>
  </div>
</template>

<script>
// the followings are importng part of the navigation part
// import NavigationBackground from './components/Navigation/NavigationBackground.vue';
// import NavigationBar from './components/Navigation/NavigationBar.vue';
import Navigation from './components/Navigation/Navigation.vue';
// import Logo from './components/Navigation/Logo.vue';
// import LinkButton from './components/Navigation/LinkButton.vue';

export default {
  name: 'App',
  components: {
    // NavigationBackground,
    // NavigationBar,
    // Logo,
    // LinkButton,
    Navigation,
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
  top: 0%;
  margin: 0%;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

#nav a.router-link-exact-active {
  color: #e24b25;
}

#nav a:hover {
  color: #e24b25;
  background: #39db6f;
}

.navigation#homepage {
  position: absolute;
  left: 30%;
  top: 0%;
  z-index: -9;
}

.navigation#game {
  position: absolute;
  left: 0%;
  top: 0%;
  z-index: -10;
}

.navigation#map {
  position: absolute;
  left: 60%;
  top: 0%;
  z-index: -10;
}

#HomepageRouter {
  font-family: 'Courier New', Courier, monospace;
  font-size: 200%;
  position: absolute;
  top: 5%;
  z-index: 0;
  left: 44%;
}

#GameRouter {
  font-family: 'Courier New', Courier, monospace;
  font-size: 200%;
  position: absolute;
  top: 5%;
  z-index: 0;
  left: 8%;
}

#MapRouter {
  font-family: 'Courier New', Courier, monospace;
  font-size: 200%;
  position: absolute;
  top: 5%;
  z-index: 0;
  left: 77%;
}
</style>
