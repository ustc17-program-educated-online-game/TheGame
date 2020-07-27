<template>
  <div class="card card-info intro-card" v-if="visible">
    <div class="card-header">
      <h5 class="card-title">{{this.levelid}}</h5>
    </div>
    <div class="card-body">
      <h5 class="card-title">{{this.title}}</h5>
      <div class="card-text" v-html="this.message"></div>
      <a @click="visible=false" class="btn btn-outline-danger close-info">关闭</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StageInfo',
  props: {
    hint: String,
  },
  data() {
    return {
      visible: false,
      title: '关卡标题',
      message: '关卡信息',
      levelid: '第x关',
    };
  },
};
</script>

<style>
.intro-card {
  position: absolute;
  text-align: left;
  top: 0%;
  left: 0%;
  width: 0%;
  height: 100%;
  box-shadow: 4px 4px 2px rgb(55, 97, 27);
}
.close-info {
  margin-top: 20px;
}
</style>
