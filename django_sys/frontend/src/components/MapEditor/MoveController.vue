<template>
  <div class="move-controller">
      MoveController
      <button class="btn btn-move-left btn-secondary" @click="MoveElement('left')">left</button>
      <button class="btn btn-move-right btn-secondary" @click="MoveElement('right')">right</button>
      <button class="btn btn-move-up btn-secondary" @click="MoveElement('up')">up</button>
      <button class="btn btn-move-down btn-secondary" @click="MoveElement('down')">down</button>
  </div>
</template>

<script>
export default {
  name: 'MoveController',
  methods: {
    MoveElement(direction) {
      this.$emit('move-element', direction);
    },
  },
};
</script>

<style>
.btn-move-left{
position: absolute;
  top: 40%;
  left: 15%;
  width: 30%;
  height: 10%;
}

.btn-move-right{
position: absolute;
  top: 40%;
  right: 15%;
  width: 30%;
  height: 10%;
}

.btn-move-up{
position: absolute;
  top: 20%;
  left: 35%;
  width: 30%;
  height: 10%;
}

.btn-move-down{
  position: absolute;
  top: 60%;
  right: 35%;
  width: 30%;
  height: 10%;
}

.move-controller {
  position: absolute;
  top: 5%;
  right: 5%;
  width: 35%;
  height: 50%;
  background-color: white;
  border: 2px groove rgb(33, 204, 247);
  box-shadow: 2px 2px 2px rgb(3, 149, 160);
}
</style>
