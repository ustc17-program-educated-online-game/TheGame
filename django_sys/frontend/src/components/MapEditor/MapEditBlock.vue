<template>
  <div class="BackDiv" :class="{active : select.state == true && x == select.x && y == select.y}"
  :style="BlockPosition" @click="SelectBlock">
    <div class="Empty" v-if="state == 1">
      <div class="Character-show" v-if="x == character.x && y == character.y">
        <img src="../../img/character.jpg">
      </div>
      <span class="decription"
      v-if="x == end.x && y == end.y">
        Destination
      </span>
      <span class="decription"
      v-else-if="x == start.x && y == start.y">
        Start
      </span>
    </div>
    <div class="Obstacle"
    v-else-if="state == 2">
      Obstacle
    </div>
    <div class="Treasure" v-else>
      <span v-if="x == end.x && y == end.y">
        Destination
      </span>
      <span v-else-if="x == start.x && y == start.y">
        Start
      </span>
      <span v-else>
        Treasure
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MapEditBlock',
  props: {
    state: Number,
    length: String,
    width: String,
    x: Number,
    y: Number,
    start: {
      x: String,
      y: String,
    },
    end: {
      x: String,
      y: String,
    },
    character: {
      type: String,
      x: String,
      y: String,
      state: String,
    },
    select: {
      state: Boolean,
      x: Number,
      y: Number,
    },
  },
  data() {
    const valueLeft = `${(this.x / this.width) * 100}%`;
    const valueRight = `${(this.y / this.length) * 100}%`;
    return {
      BlockPosition: {
        position: 'absolute',
        left: valueRight,
        top: valueLeft,
        width: '12.5%',
        height: '12.5%',
        padding: '0',
      },
    };
  },
  methods: {
    SelectBlock() {
      this.$emit('select-changed', this.x, this.y);
    },
  },
};
</script>

<style>
.active {
  border: 5px solid rgb(0, 204, 255);
}

</style>
