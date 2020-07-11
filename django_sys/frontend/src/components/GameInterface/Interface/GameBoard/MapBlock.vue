<template>
  <div class="BackDiv" :style="BlockPosition">
    <div class="Empty" v-if="state == 1">
      <div class="Character-show" v-if="x == character.x && y == character.y">
        <div v-if="character.state == 'u'">
          <img src="../../../../img/character_u.jpg">
        </div>
        <div v-if="character.state == 'd'">
          <img src="../../../../img/character_d.jpg">
        </div>
        <div v-if="character.state == 'l'">
          <img src="../../../../img/character_l.jpg">
        </div>
        <div v-if="character.state == 'r'">
          <img src="../../../../img/character_r.jpg">
        </div>
      </div>
      <span class="decription" v-if="x == end.x && y == end.y">
        Destination
      </span>
      <span class="decription" v-else-if="x == start.x && y == start.y">
        Start
      </span>
    </div>
    <div class="Obstacle" v-else-if="state == 2">
      Obstacle
    </div>
    <div class="Treasure" v-else>
      <div class="Character-show" v-if="x == character.x && y == character.y">
        <div v-if="character.state == 'u'">
          <img src="../../../../img/character_u.jpg">
        </div>
        <div v-if="character.state == 'd'">
          <img src="../../../../img/character_d.jpg">
        </div>
        <div v-if="character.state == 'l'">
          <img src="../../../../img/character_l.jpg">
        </div>
        <div v-if="character.state == 'r'">
          <img src="../../../../img/character_r.jpg">
        </div>
      </div>
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
  name: 'MapBlock',
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
  },
  data() {
    const valueLeft = `${(this.x / this.width) * 100}%`;
    const valueRight = `${(this.y / this.length) * 100}%`;
    return {
      BlockPosition: {
        position: 'absolute',
        left: valueRight,
        top: valueLeft,
        width: '10%',
        height: '10%',
        padding: '0',
      },
    };
  },
};
</script>

<style>
.Empty,
.Obstacle,
.Treasure {
  width: 100%;
  height: 100%;
}
.Character-show {
  position: absolute;
  top: 25%;
  left: 30%;
  width: 40%;
  height: 50%;
}
.Empty {
  background: url("../../../../img/grass.jpg") no-repeat;
  background-size: cover;
}
.Obstacle {
  background-color: rgb(99, 74, 21);
}
.Treasure {
  background-color: rgb(255, 215, 83);
}
.Destination {
  background-color: rgb(80, 214, 39);
}
img {
  width:100%;
  height: 100%;
}
</style>
