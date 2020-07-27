<template>
  <div class="card card-info" id="userinfo" v-if="visible">
    <div class="card-header">
      账号信息
    </div>
    <div class="card-body">
      <div
      class="card-text"
      >
      name:{{username}}</div>
      <div
      class="card-text"
      >
      email:{{useremail}}</div>
      <div
      class="card-text"
      >
      sex:{{usersex}}</div>
      <div
      class="card-text"
      >
      mobile:{{usermobile}}</div>
      <a @click="visible=false" class="btn btn-outline-danger close-info" id="closeuser">关闭</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserInfo',
  props: {
    username: String,
    useremail: String,
    usersex: String,
    usermobile: String,
  },
  data() {
    return {
      visible: false,
    };
  },
};
</script>

<style>
#userinfo {
  z-index: 100;
  box-shadow: 2px 2px 1px gray;
}
</style>
