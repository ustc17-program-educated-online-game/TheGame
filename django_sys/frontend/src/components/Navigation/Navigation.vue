<template>
    <div>

        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="/">编程教育游戏</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item href="/">首页</b-nav-item>
                    <b-nav-item href="/#/StageSelect">关卡选择</b-nav-item>
                    <b-nav-item href="/#/MapEditor">地图编辑器</b-nav-item>
                    <b-nav-item href="/#/Community">玩家社区</b-nav-item>
                </b-navbar-nav>

                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    <!--<b-nav-form>
                        <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                    </b-nav-form>-->
                    <div v-show = "DataSet.state === 1">
                        <b-nav-item>欢迎玩家{{DataSet.username}}</b-nav-item>
                    </div>
                    <!-- <div>欢迎</div> -->
                    <b-nav-item href="/register/">注册新账号</b-nav-item>
                    <div v-show = "DataSet.state === 0">
                        <b-nav-item href="/login/">登录</b-nav-item>
                    </div>
                    <div v-show = "DataSet.state === 1">
                        <b-nav-item-dropdown right>
                        <!-- Using 'button-content' slot -->
                            <template v-slot:button-content>
                                我的账号
                            </template>
                            <b-dropdown-item
                              @click="ShowUserInfo"
                              >账号信息</b-dropdown-item>
                            <b-dropdown-item href="/logout/">退出登录</b-dropdown-item>
                        </b-nav-item-dropdown>
                    </div>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
        <user-info
          ref="UserInfo"
          :username="DataSet.username"
          :usersex="DataSet.usersex"
          :useremail="DataSet.useremail"
          :usermobile="DataSet.usermobile"></user-info>
    </div>
</template>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
import axios from 'axios';
import LoginTest from './LoginTest.json';
import UserInfo from './UserInfo.vue'

export default {
  name: 'Navigation',
  data() {
    return {
      DataSet: {
        //user_id: Number,
        username: String,
        usersex: String,
        useremail: String,
        usermobile: String,
        state: Number,
      },
    };
  },
  components: {
    UserInfo,
  },
  mounted() {
    const url = '/userState/';
    this.$http({
        url: url,
        method: 'get',
        headers: { 'X-CSRFToken': this.getCookie('csrftoken') },
      }).then((response) => {
        var result = response.data;
        console.log(result);
        this.DataSet = result;
      }).catch((error) => {
        console.log(error);
      });
  },
  methods: {
    getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
      return null;
    },
    ShowUserInfo(){
      this.$refs.UserInfo.visible = true;
    }
  }
  /*mounted() {
    //console.log(LoginTest);
    this.DataSet = LoginTest;
    console.log(this.DataSet.state);
  },
  components: {
    LoginTest,
  }, */
};
</script>
