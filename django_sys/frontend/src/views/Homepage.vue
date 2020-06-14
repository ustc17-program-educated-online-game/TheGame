<template>
  <div class="home">
    <cards></cards>
  </div>
  <!---->
</template>

<script>
// @ is an alias to /src
import Cards from '../components/Homepage/Cards.vue';

export default {
  name: 'HomePage',
  components: {
    Cards,
  },
};
</script>
