<template>
  <div class="element-list">
    ElementList
    <div class="Obstacle map-element" @click="SelectElement('obstacle')">
      Obstacle
    </div>
    <div class="Treasure map-element" @click="SelectElement('treasure')">
        Treasure
    </div>
  </div>
</template>
<script>

export default {
  name: 'ElementList',
  methods: {
    SelectElement(type) {
      this.$emit('select-element', type);
    },
  },
};
</script>

<style>
.map-element{
  margin: 10%;
  left: 10%;
  width: 80%;
  height: 30%;
}

.element-list {
  position: absolute;
  top: 5%;
  left: 5%;
  width: 50%;
  height: 50%;
  background-color: white;
  border: 2px groove rgb(33, 204, 247);
  box-shadow: 2px 2px 2px rgb(3, 149, 160);
}
</style>
