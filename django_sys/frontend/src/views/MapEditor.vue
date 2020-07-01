/* eslint-disable no-alert */
<template>
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
    <game-board
      ref="GameBoard"
    >
    </game-board>
    <check-point-info ref="CheckInfo"></check-point-info>
    <code-start
      @takeAction="test($event)"
      ref="code-block"
    >
    </code-start>
    <button type="button" class="btn btn-back btn-secondary" @click="EditMap"
        >返回</button>
    <button type="button" class="btn btn-upload btn-secondary" @click="UploadMap"
        >提交</button>
  </div>

</template>

<script>
import MapBoard from '../components/MapEditor/MapBoard.vue';
import ElementBoard from '../components/MapEditor/ElementBoard.vue';
import GameBoard from '../components/GameInterface/Interface/GameBoard.vue';
import CheckPointInfo from '../components/GameInterface/Interface/CheckPointInfo.vue';
import CodeStart from '../components/GameInterface/CodeBlock/CodeStart.vue';

export default {
  name: 'MapEditor',
  components: {
    MapBoard,
    GameBoard,
    CheckPointInfo,
    ElementBoard,
    CodeStart,
  },
  data() {
    return {
      state: 'edit',
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
      this.state = 'test';
    },
    TestMap() {
      this.state = 'test';
    },
    EditMap() {
      this.state = 'edit';
    },
    UploadMap() {
      this.state = 'edit';
    },
    test(event) {
      this.$refs.GameBoard.takeAction(event);
    },
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
