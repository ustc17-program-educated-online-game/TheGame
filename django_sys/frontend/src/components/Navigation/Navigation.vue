<template>
    <div>

        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="/">编程教育游戏</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item href="/">首页</b-nav-item>
                    <b-nav-item href="/#/GameInterface">开始游戏</b-nav-item>
                    <b-nav-item href="/#/StageSelect">关卡选择</b-nav-item>
                    <b-nav-item href="/#/MapEditor">地图编辑器</b-nav-item>
                    <b-nav-item href="/#/">玩家社区</b-nav-item>
                </b-navbar-nav>

                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    <b-nav-form>
                        <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                    </b-nav-form>
                    <div v-show = "DataSet.state === 1">
                        <b-nav-item>欢迎玩家{{DataSet.username}}</b-nav-item>
                    </div>
                    <!-- <div>欢迎</div> -->
                    <b-nav-item href="/#/">注册新账号</b-nav-item>
                    <div v-show = "DataSet.state === 0">
                        <b-nav-item href="/#/">登录</b-nav-item>
                    </div>
                    <div v-show = "DataSet.state === 1">
                        <b-nav-item-dropdown right>
                        <!-- Using 'button-content' slot -->
                            <template v-slot:button-content>
                                我的账号
                            </template>
                            <b-dropdown-item href="#">账号信息</b-dropdown-item>
                            <b-dropdown-item href="#">退出登录</b-dropdown-item>
                        </b-nav-item-dropdown>
                    </div>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
import LoginTest from './LoginTest.json';

export default {
  name: 'Navigation',
  data() {
    return {
      DataSet: {
        state: Number,
        username: String,
      },
    };
  },
  mounted() {
    // eslint-disable-next-line no-console
    console.log(LoginTest);
    this.DataSet = LoginTest;
    // eslint-disable-next-line no-console
    console.log(this.DataSet.state);
  },
  /* components: {
    LoginTest,
  }, */
};
</script>
