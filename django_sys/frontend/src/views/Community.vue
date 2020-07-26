<template>
  <div>
    <div class="card-group">
      <div v-for="(item,index) in DataSet.data" :key="index">
        <div v-show = "item.message === 'success'" class="card">
          <div class="card-header">
            地图编号：{{item.map_id}}
          </div>
          <div class="card-body">
            <h5 class="card-title">{{item.map_name}}</h5>
            <p class="card-text">作者：{{item.user_name}}</p>
            <button href="/#/" class="btn btn-primary">开始游戏</button>
            <!-- 这里还要根据地图编号增加对应的开始游戏链接 -->
          </div>
          <div class="card-footer text-muted">
            {{index}}
          </div>
        </div>
      </div>
    </div>
    <div>
      <b-progress :value="id" :max="DataSet.maxid" class="mb-3">
      </b-progress>
    </div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <button @click="FirstPage()" class="btn btn-primary">第一页</button>
      <button @click="PreviousPage()" class="btn btn-primary">上一页</button>
      <button @click="NextPage()" class="btn btn-primary">下一页</button>
      <button @click="LastPage()" class="btn btn-primary">最后一页</button>
    </nav>
  </div>
</template>

<script>
import CommunityTest from './CommunityTest.json';

export default {
  name: 'Community',
  data() {
    return {
      id: Number, // 查询的地图编号的下界，一次查询的地图数根据页面待定
      cnt: Number, // 一页显示的地图数
      DataSet: {
        maxid: Number, // 最大的地图编号，用来防止越界，向后端查询
        data: [],
      },
    };
  },
  created() {
    this.id = 1; // 实际开始的编号要根据玩家自定义地图的最小编号来确定,修改时下面的跳转第一面也要改
    this.cnt = 10;
  },
  mounted() {
    this.DataSet = CommunityTest;
  },
  methods: {
    FirstPage() { // 跳转到第一面
      this.id = 1;
    },
    PreviousPage() { // 前一面
      if (this.id - this.cnt > 0) {
        this.id -= this.cnt;
      }
      // console.log(this.id);
    },
    NextPage() { // 后一面
      if (this.id + this.cnt < this.DataSet.maxid) {
        this.id += this.cnt;
      }
      // console.log(this.id);
      // console.log(this.DataSet.maxid);
    },
    LastPage() { // 最后一面
      this.id = Math.floor((this.DataSet.maxid - 1) / this.cnt) * this.cnt + 1;
    },
  },
};
</script>
