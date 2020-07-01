<template>
  <div class="point-set">
      <position-setter @set-point="SetPoint(arguments)" input-type="start" id="start-block">
        起点坐标
      </position-setter>
      <position-setter @set-point="SetPoint(arguments)" input-type="end" id="end-block">
        终点坐标
      </position-setter>
      <div class="character-set">
        人物方向
        <button @click="RotateCharacter" class="btn btn-secondary">旋转</button>
      </div>
  </div>
</template>

<script>
import PositionSetter from './PositionSetter.vue';

export default {
  name: 'PointSet',
  components: {
    PositionSetter,
  },
  methods: {
    SetPoint(msg) {
      this.$emit('set-point', msg);
    },
    RotateCharacter() {
      this.$emit('rotate-character');
    },
  },
};
</script>

<style>

.point-set {
  position: absolute;
  top: 65%;
  left: 5%;
  width: 60%;
  height: 25%;
  display: inline-block;
}
</style>
