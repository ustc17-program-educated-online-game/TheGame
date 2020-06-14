<template>
  <div class="GameInterface">
    <game-board
      ref="GameBoard"
    >
    </game-board>
    <check-point-info ref="CheckInfo"></check-point-info>
    <hint-info ref="HintInfo"></hint-info>
    <code-start
      @takeAction="takeAction($event)"
      @clear="clear()"
      ref="code-block"
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
import CodeStart from '../components/GameInterface/CodeBlock/CodeStart.vue';

export default {
  name: 'GameInterface',
  components: {
    CodeStart,
    GameBoard,
    CheckPointInfo,
    HintInfo,
  },
  methods: {
    takeAction(event) {
      this.$refs.GameBoard.takeAction(event);
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
