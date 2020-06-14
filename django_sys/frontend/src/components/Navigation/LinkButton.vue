<template>
  <router-link :to="address" :style="{left: left}" class="LinkButton">
    <div class="content">{{content}}</div>
  </router-link>
</template>

<script>
export default {
  name: 'LinkButton',
  props: ['address', 'content', 'left'],
};
</script>

<style>
.LinkButton {
  font-family: 'Courier New', Courier, monospace;
  position: absolute;
  top: 0%;
  height: 6.35%;
  width: 8%;
  background-color: blanchedalmond;
  color: white;
  padding: 14px 14px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

.content {
  position: relative;
  top: 28%;
}
</style>
