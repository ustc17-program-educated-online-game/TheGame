<template>
  <div class="GameInterface">
    <game-board
      ref="GameBoard"
    >
    </game-board>
    <check-point-info ref="CheckInfo"></check-point-info>
    <hint-info ref="HintInfo"></hint-info>
    <success-info
      ref="SuccessInfo"
      mapid="第一关"
      @nextStage="nextStage"
      :id=id></success-info>
    <fail-info
      ref="FailInfo"
      mapid="第一关"></fail-info>
    <code-start
      @takeAction="takeAction($event)"
      @execute="execute(arguments)"
      @clear="clear()"
      @MissionSuccess="ShowSuccessInfo"
      @MissionFail="ShowFailInfo"
      ref="CodeStart"
    >
    </code-start>
    <div class="btn-group info-group" role="group" aria-label="Basic example">
      <button type="button" class="btn btn-info btn-secondary"
        @click="ShowCheckInfo">关卡信息</button>
      <button type="button" class="btn btn-success btn-secondary"
        @click="ShowHintInfo">提示信息</button>
    </div>
    <span class="map-name">第一关：直来直往</span>
  </div>
</template>

<script>
import GameBoard from '../components/GameInterface/Interface/GameBoard.vue';
import CheckPointInfo from '../components/GameInterface/Interface/CheckPointInfo.vue';
import HintInfo from '../components/GameInterface/Interface/HintInfo.vue';
import SuccessInfo from '../components/GameInterface/Interface/SuccessInfo.vue';
import FailInfo from '../components/GameInterface/Interface/FailInfo.vue';
import CodeStart from '../components/GameInterface/CodeBlock/CodeStart.vue';

export default {
  name: 'GameInterface',
  data() {
    return {
      id: -1,
    };
  },
  components: {
    CodeStart,
    GameBoard,
    CheckPointInfo,
    HintInfo,
    SuccessInfo,
    FailInfo,
  },
  methods: {
    getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
      return null;
    },
    takeAction(event) {
      this.$refs.GameBoard.takeAction(event);
    },
    execute(arg) {
      const mapid = this.$refs.GameBoard.DataSet.map.id;
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
      this.$refs.GameBoard.clear();
    },
    ShowCheckInfo() {
      this.$refs.CheckInfo.visible = true;
    },
    ShowHintInfo() {
      this.$refs.HintInfo.visible = true;
    },
    ShowSuccessInfo() {
      this.$refs.SuccessInfo.visible = true;
      this.$refs.CodeStart.reset();
    },
    ShowFailInfo() {
      this.$refs.FailInfo.visible = true;
      this.$refs.CodeStart.reset();
    },
    nextStage() {
      const mapid = this.$refs.GameBoard.DataSet.map.id;
      this.id = mapid;
      const path = `#/GameInterface/${Number(mapid) + 1}`;
      this.$http({
        url: path,
        method: 'get',
        headers: { 'X-CSRFToken': this.getCookie('csrftoken') },
      });
    },
  },
};
</script>

<style>
.info-group {
  position: absolute;
  left: 51%;
  bottom: 5px;
  box-shadow: 1px 1px 1px #999999;
}
.GameInterface {
  position: absolute;
  top: 10%;
  left: 0;
  width: 100%;
  height: 90%;
}
.map-name {
  position: absolute;
  left: 7.5%;
  bottom: 5px;
  font-size:25px;
  color:rgb(87, 180, 187);
}
</style>
