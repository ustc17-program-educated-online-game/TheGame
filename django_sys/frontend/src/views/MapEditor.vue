/* eslint-disable no-alert */
<template>
  <div v-if="login===true">
    <div class="MapEditor" v-if="state==='edit'">
      <map-board ref="MapBoard"></map-board>
      <element-board ref="ElementBoard"
      @set-point="SetPoint"
      @select-element="SelectElement"
      @move-element="MoveElement"
      @reset-board="ResetBoard"
      @remove-element="RemoveElement"
      @rotate-character="RotateCharacter">
      </element-board>
      <button type="button" class="btn btn-save btn-secondary" @click="SaveMap"
          >保存</button>
      <button type="button" class="btn btn-test btn-secondary" @click="TestMap"
          >测试</button>
    </div>
    <div class="GameInterface" v-else>
      <test-board
        ref="TestBoard"
      >
      </test-board>
      <success-info
        ref="SuccessInfo"
        mapid="自定地图"></success-info>
      <fail-info
        ref="FailInfo"
        mapid="自定地图"></fail-info>
      <check-point-info ref="CheckInfo"></check-point-info>
      <code-start
        @takeAction="takeAction($event)"
        @execute="execute(arguments)"
        @clear="clear()"
        @MissionSuccess="ShowSuccessInfo"
        @MissionFail="ShowFailInfo"
        ref="CodeStart"
      >
      </code-start>
      <button type="button" class="btn btn-back btn-secondary" @click="EditMap"
          >返回</button>
      <button type="button" class="btn btn-upload btn-secondary" @click="ShareMap"
          >发布</button>
    </div>
  </div>
  <div v-else>
    请先登录再使用地图编辑器
  </div>

</template>

<script>
import axios from 'axios';
import MapBoard from '../components/MapEditor/MapBoard.vue';
import ElementBoard from '../components/MapEditor/ElementBoard.vue';
import TestBoard from '../components/MapEditor/TestBoard.vue';
import CheckPointInfo from '../components/GameInterface/Interface/CheckPointInfo.vue';
import CodeStart from '../components/GameInterface/CodeBlock/CodeStart.vue';
import SuccessInfo from '../components/MapEditor/SuccessInfo.vue';
import FailInfo from '../components/MapEditor/FailInfo.vue';

export default {
  name: 'MapEditor',
  components: {
    MapBoard,
    TestBoard,
    CheckPointInfo,
    ElementBoard,
    CodeStart,
    SuccessInfo,
    FailInfo,
  },
  data() {
    return {
      state: 'edit',
      login: false,
      DataSet: {
        user_id: Number,
        username: String,
        state: Number,
      },
    };
  },
  methods: {
    SetPoint(msg) {
      this.$refs.MapBoard.SetPoint(msg);
    },
    ResetBoard() {
      this.$refs.MapBoard.resetMap();
    },
    SelectElement(msg) {
      this.$refs.MapBoard.SelectElement(msg);
    },
    MoveElement(msg) {
      this.$refs.MapBoard.MoveElement(msg);
    },
    RemoveElement() {
      this.$refs.MapBoard.RemoveElement();
    },
    RotateCharacter() {
      this.$refs.MapBoard.RotateCharacter();
    },
    SaveMap() {
      this.$refs.MapBoard.saveMap(this.DataSet.user_id, this.DataSet.username);
      this.state = 'test';
    },
    TestMap() {
      this.state = 'test';
    },
    EditMap() {
      this.state = 'edit';
    },
    ShareMap() {
      this.state = 'edit';
    },
    getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
      return null;
    },
    takeAction(event) {
      this.$refs.TestBoard.takeAction(event);
    },
    execute(arg) {
      const mapid = this.$refs.TestBoard.DataSet.map.id;
      const passData = {
        id: mapid,
        type: arg[1],
        codeList: arg[0].codes,
      };
      const ActionAnalyzePath = '/game/';
      this.$http({
        url: ActionAnalyzePath,
        method: 'post',
        data: passData,
        headers: { 'X-CSRFToken': this.getCookie('csrftoken') },
      }).then((response) => {
        console.log(response.data.actionList);
        this.$refs.CodeStart.actions = response.data.actionList;
        this.$refs.CodeStart.getActions(passData.type);
      }).catch((error) => {
        console.log(error);
      });
    },
    clear() {
      this.$refs.TestBoard.clear();
    },
    ShowSuccessInfo() {
      this.$refs.SuccessInfo.visible = true;
      this.$refs.TestBoard.clear();
    },
    ShowFailInfo() {
      this.$refs.FailInfo.visible = true;
      this.$refs.TestBoard.clear();
    },
  },
  mounted() {
    const url = '/userState/';
    axios.get(url).then(
      (response) => {
        const result = response.data;
        console.log(result);
        this.DataSet = result;
        if (this.DataSet.user_id === null) {
          this.login = false;
        } else {
          this.login = true;
        }
      },
    ).catch(
      (error) => {
        console.log(error);
        alert('请先登陆');
      },
    );
  },
};
</script>

<style scoped>

.MapEditor {
  position: absolute;
  top: 10%;
  left: 0;
  width: 100%;
  height: 90%;
}

.btn-save,
.btn-back{
  position: absolute;
  top: 85%;
  left: 68%;
  width: 10%;
  height: 5%;
}

.btn-test,
.btn-upload{
  position: absolute;
  top: 85%;
  left: 82%;
  width: 10%;
  height: 5%;
}

.CodeBlock {
  position: absolute;
  top: 0%;
  left: 66%;
  width: 34%;
  height: 80%;
  margin: 0%;
}

</style>
