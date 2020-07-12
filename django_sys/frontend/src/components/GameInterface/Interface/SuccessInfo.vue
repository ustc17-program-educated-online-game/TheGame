<template>
  <div class="card card-info" v-if="visible">
    <div class="card-header">
      {{mapid}}
    </div>
    <div class="card-body">
      <h5 class="card-title"></h5>
      <div
      class="card-text"
      >
      打开宝箱并到达目的地，通关成功</div>
      <a @click="visible=false" class="btn btn-outline-danger close-info">关闭</a>
      <a class="btn btn-outline-danger close-info">下一关</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SuccessInfo',
  props: {
    mapid: String,
  },
  data() {
    return {
      visible: false,
    };
  },
};
</script>

<style>
.card-info {
  position: absolute;
  top: 20%;
  left: 35%;
  width: 300px;
  height: 250px;
  box-shadow: 4px 4px 2px rgb(55, 97, 27);
}
.close-info {
  margin-top: 20px;
}
</style>
