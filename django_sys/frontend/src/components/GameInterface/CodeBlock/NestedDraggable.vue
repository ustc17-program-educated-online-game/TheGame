<template>
  <draggable class="dragArea" tag="ul" :list="tasks" :group="{ name: 'people' }">
    <li v-for="el in tasks" :key="el.id">
      <div class="container">
        <div class="row name-box">
          <p
            :style="(el.embeded || el.extrainfo)? embeded : normal"
            class="list-group-item list-group-item-success name"
          >
            {{ el.name }}
          </p>
          <div
            class="list-group-item list-group-item-secondary condition col-8"
            v-if="el.embeded"
          >
            <div class="inspect">
              前方
            </div>
            <select id="relation" class="relation">
              <option selected value="1">==</option>
              <option value="2">!=</option>
            </select>
            <select id="val" class="right-value">
              <option selected value="1">空地</option>
              <option value="2">障碍</option>
              <option value="3">宝藏</option>
              <option value="4">边缘</option>
            </select>
          </div>
          <div
            class=""
            v-else-if="el.extrainfo"
          >
            <input type="text" class="extrainfo" value="1">
          </div>
        </div>
      </div>
      <nested-draggable :tasks="el.tasks" v-if="el.embeded"/>
    </li>
  </draggable>
</template>
<script>
import draggable from 'vuedraggable';

export default {
  props: {
    tasks: {
      required: true,
      type: Array,
    },
  },
  data() {
    return {
      normal: {
        width: '200px',
        padding: '0',
        margin: '0',
        height: '45px',
      },
      embeded: {
        width: '100px',
        padding: '0',
        margin: '0',
        height: '45px',
      },
    };
  },
  components: {
    draggable,
  },
  name: 'nested-draggable',
};
</script>
<style scoped>
.dragArea {
  min-height: 45px;
  width: 400px;
}
.condition {
  left: 0px;
  height: 45px;
  padding: 0px;
  width: 300px;
}
.inspect {
  position: absolute;
  top: 20%;
  width: 20%;
  left: 5%;
}
.relation {
  position: absolute;
  top: 20%;
  left: 25%;
  width: 20%;
  height: 60%;
}
.right-value {
  position: absolute;
  top: 20%;
  left: 50%;
  width: 41%;
  height: 60%;
}
.extrainfo {
  position: relative;
  left: 0%;
  height: 45px;
  width:100px;
}
.name {
  background: rgba(245, 222, 179, 0.945);
  border-radius: 3px;
  text-align: center;
}
</style>
