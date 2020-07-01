<template>
  <div class="position-setter" :class="inputType">
    <label><slot></slot></label>
    <div class="position-block">
      <label> x </label>
      <input :id="inputType" v-model.number="position.x" placeholder="0">
    </div>
    <div class="position-block">
      <label> y </label>
      <input :id="inputType" v-model.number="position.y" placeholder="0">
    </div>
  </div>
</template>

<script>
export default {
  name: 'PositionSetter',
  data() {
    return {
      position: {
        x: undefined,
        y: undefined,
      },
    };
  },
  props: {
    inputType: {
      type: String,
      default: 'start',
    },
  },
  watch: {
    position: {
      handler() {
        if (this.position.x > 7) this.position.x = 7;
        else if (this.position.x < 0) this.position.x = 0;
        if (this.position.y > 7) this.position.y = 7;
        else if (this.position.y < 0) this.position.y = 0;
        this.$emit('set-point', this.inputType, this.position);
      },
      deep: true,
    },
  },
};
</script>

<style scoped>
.position-setter {
  margin: 10px 0 10px 10px;
  padding: 0;
  background: #ffffff;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  display: inline-block;
}

input {
  width: 40px;
  display: inline-block;
  border: none;
  font-size: 16px;
  font-family: PingFangSC-Regular, "PingFang SC", sans-serif;
}

label {
  position: relative;
  text-align: center;
  left: 0;
  width: 80px;
  font-family: PingFangSC-Regular, "PingFang SC", sans-serif;
  color: #222222;
  display: inline-block;
}

::-webkit-input-placeholder {
  color: #afafaf;
}

:-ms-input-placeholder {
  color: #afafaf;
}

:-moz-placeholder {
  color: #afafaf;
}

::-moz-placeholder {
  color: #afafaf;
}
</style>
