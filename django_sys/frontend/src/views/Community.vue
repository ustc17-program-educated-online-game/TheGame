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
            <b-button href="/#/" class="card-link">开始游戏</b-button>
            <!-- 这里还要根据地图编号增加对应的开始游戏链接 -->
          </div>
          <div class="card-footer text-muted">
            {{index}}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CommunityTest from './CommunityTest.json';

export default {
  name: 'Community',
  data() {
    return {
      id: Number, // 查询的地图编号的下标，一次查询的地图数根据页面待定
      cnt: Number, // 一页显示的地图数
      maxid: Number, // 最大的地图编号，用来防止越界，向后端查询
      DataSet: {
        data: [],
      },
    };
  },
  mounted() {
    // console.log(LoginTest);
    this.DataSet = CommunityTest;
    // console.log(this.DataSet.state);
  },
  methods: {
    PreviousPage() {
      if (this.id - this.cnt > 0) {
        this.id -= this.cnt;
      }
    },
    NextPage() {
      if (this.id + this.cnt > this.maxid) {
        this.id += this.cnt;
      }
    },
  },
};
</script>
