<template>
  <div class="element-board">
      <element-list @select-element="SelectElement"></element-list>
      <move-controller @move-element="MoveElement"></move-controller>
      <point-set @set-point="SetPoint" @rotate-character="RotateCharacter"></point-set>
      <button @click="ResetBoard" class="btn btn-reset btn-warning">重置</button>
      <button @click="RemoveElement" class="btn btn-remove btn-danger">删除</button>
  </div>
</template>

<script>
import ElementList from './ElementList.vue';
import MoveController from './MoveController.vue';
import PointSet from './PointSet.vue';

export default {
  name: 'ElementBoard',
  components: {
    ElementList,
    MoveController,
    PointSet,
  },
  methods: {
    SetPoint(msg) {
      this.$emit('set-point', msg);
    },
    SelectElement(msg) {
      this.$emit('select-element', msg);
    },
    MoveElement(msg) {
      this.$emit('move-element', msg);
    },
    ResetBoard() {
      this.$emit('reset-board');
    },
    RemoveElement() {
      this.$emit('remove-element');
    },
    RotateCharacter() {
      this.$emit('rotate-character');
    },
  },
};
</script>

<style>
.element-board {
  position: absolute;
  top: 1.4%;
  right: 5%;
  width: 30%;
  height: 80%;
  background-color: white;
  border: 2px groove rgb(33, 204, 247);
  box-shadow: 2px 2px 2px rgb(3, 149, 160);
}

.btn-reset {
  position: absolute;
  top: 80%;
  left: 70%;
  width: 20%;
  height: 10%;
}

.btn-remove {
  position: absolute;
  top: 65%;
  left: 70%;
  width: 20%;
  height: 10%;
}

</style>
