<template>
  <div
    class="Character"
    :style="{
      left: (y/length) * 100 + 3 + '%',
      top: (x/width) * 100 + 3 + '%',
      width: (1/length) * 80 + '%',
      height: (1/width) * 60 + '%'
    }"
  >
    character -- {{state}}
  </div>
</template>

<script>
export default {
  name: 'Character',
  props: {
    type: String,
    x: String,
    y: String,
    state: String,
    width: String,
    length: String,
  },
};
</script>

<style>
.Character {
  position: absolute;
  padding: '15px';
  background-color: white;
}
</style>
