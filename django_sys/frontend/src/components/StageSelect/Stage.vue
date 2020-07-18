<template>
  <div>
    <div class="stagegroup">
        <b-card-group columns>
            <b-card title="第一关" img-src="" img-alt="Image" img-top>
                <b-card-text>
                    <b>起飞</b>
                </b-card-text>
                <b-button href="#">开始游戏</b-button>
                <button type="button" class="btn btn-info btn-secondary"
                @click="ShowInfo(1)">背景故事</button>
                <stage-info ref="StageInfo1"></stage-info>
                <b-button href="#">讨论区</b-button>
                <img src="../../img/level1.png" class="picture">
            </b-card>

            <b-card title="第二关" img-src="" img-alt="Image" img-top>
                <b-card-text>
                    <b>冲出大气层</b>
                </b-card-text>
                <b-button href="#">开始游戏</b-button>
                <button type="button" class="btn btn-info btn-secondary"
                @click="ShowInfo(2)">背景故事</button>
                <stage-info ref="StageInfo2"></stage-info>
                <b-button href="#">讨论区</b-button>
                <img src="../../img/level2.png" class="picture">
            </b-card>

            <b-card title="第三关" img-src="" img-alt="Image" img-top>
                <b-card-text>
                    <b>太阳系漫游</b>
                </b-card-text>
                <b-button href="#">开始游戏</b-button>
                <button type="button" class="btn btn-info btn-secondary"
                @click="ShowInfo(3)">背景故事</button>
                <stage-info ref="StageInfo3"></stage-info>
                <b-button href="#">讨论区</b-button>
                <img src="../../img/level3.png" class="picture">
            </b-card>

        </b-card-group>
    </div>

    <div class="stagegroup">
        <b-card-group columns>
            <b-card title="第四关" img-src="" img-alt="Image" img-top>
                <b-card-text>
                    <b>新的旅程</b>
                </b-card-text>
                <b-button href="#">开始游戏</b-button>
                <button type="button" class="btn btn-info btn-secondary"
                @click="ShowInfo(4)">背景故事</button>
                <stage-info ref="StageInfo4"></stage-info>
                <b-button href="#">讨论区</b-button>
                <img src="../../img/level1.png" class="picture">
            </b-card>

            <b-card title="第五关" img-src="" img-alt="Image" img-top>
                <b-card-text>
                    <b>寻找宝藏</b>
                </b-card-text>
                <b-button href="#">开始游戏</b-button>
                <button type="button" class="btn btn-info btn-secondary"
                @click="ShowInfo(5)">背景故事</button>
                <stage-info ref="StageInfo5"></stage-info>
                <b-button href="#">讨论区</b-button>
                <img src="../../img/level2.png" class="picture">
            </b-card>

            <b-card title="第六关" img-src="" img-alt="Image" img-top>
                <b-card-text>
                    <b>最后的挑战</b>
                </b-card-text>
                <b-button href="#">开始游戏</b-button>
                <button type="button" class="btn btn-info btn-secondary"
                @click="ShowInfo(6)">背景故事</button>
                <stage-info ref="StageInfo6"></stage-info>
                <b-button href="#">讨论区</b-button>
                <img src="../../img/level3.png" class="picture">
            </b-card>

        </b-card-group>
    </div>
  </div>
</template>

<script>
import StageInfo from './Introduction.vue';

export default {
  name: 'Stage',
  components: {
    StageInfo,
  },
  methods: {
    ShowInfo(id) {
      switch (id) {
        case 1:
          this.$refs.StageInfo1.visible = true;
          this.$refs.StageInfo1.title = '起飞';
          this.$refs.StageInfo1.levelid = '第一关';
          this.$refs.StageInfo1.message = '&nbsp&nbsp&nbsp&nbsp马大叔已经全副武装，在飞来此处的路上，男孩已经把事情的经过告诉了他。'
          + '男孩名为陆飞，他们家族拥有着世界上最大的飞行物设计公司。'
          + '此次出发，正是为了寻找祖上流传下来的传说——名为'
          + '“one piece”的宇宙大秘宝。'
          + '他希望马大叔能和他一起，向着无垠的宇宙进发。<br>'
          + '&nbsp&nbsp&nbsp&nbsp“准备开始，起飞！”，随着机械女声响起，飞碟的发动机开始轰鸣'
          + '让我们一鼓作气，冲破大气层吧<br>';
          break;
        case 2:
          this.$refs.StageInfo2.visible = true;
          this.$refs.StageInfo2.title = '冲出大气层';
          this.$refs.StageInfo2.levelid = '第二关';
          this.$refs.StageInfo2.message = '&nbsp&nbsp&nbsp&nbsp在马大叔和陆飞的操作下，飞船终于冲出了大气层，'
          + '可问题还没有结束。一块卫星残骸正位于他们面前的轨道上，请你操纵人物，避开障碍，继续探险吧！';
          break;
        case 3:
          this.$refs.StageInfo3.visible = true;
          this.$refs.StageInfo3.title = '太阳系漫游';
          this.$refs.StageInfo3.levelid = '第三关';
          this.$refs.StageInfo3.message = '&nbsp&nbsp&nbsp&nbsp马大叔和陆飞来到了美丽的太阳系，远处是广阔而深邃的宇宙，身后是蔚蓝的地球。'
          + '曾经的梦想如今化为现实，年少的轻狂最后成为了眼前实景，请你操纵人物，在这美丽的星海中漫游吧';
          break;
        case 4:
          this.$refs.StageInfo4.visible = true;
          this.$refs.StageInfo4.title = '新的旅程';
          this.$refs.StageInfo4.levelid = '第四关';
          this.$refs.StageInfo4.message = '&nbsp&nbsp&nbsp&nbsp根据宇宙地图的指示，他们要寻找的秘宝，正位于一个名叫拉夫德鲁的星系中。'
          + '为了完成友人陆飞的梦想，让我们继续前进吧，笔直地冲出太阳系。';
          break;
        case 5:
          this.$refs.StageInfo5.visible = true;
          this.$refs.StageInfo5.title = '寻找宝藏';
          this.$refs.StageInfo5.levelid = '第五关';
          this.$refs.StageInfo5.message = '&nbsp&nbsp&nbsp&nbsp经历了漫长的航行，如今大秘宝已近在眼前。'
          + '克制住自己的冲动，谨慎地避开每一个障碍，到达那路途的尽头，梦想之地吧！';
          break;
        case 6:
          this.$refs.StageInfo6.visible = true;
          this.$refs.StageInfo6.title = '最后的挑战';
          this.$refs.StageInfo6.levelid = '第六关';
          this.$refs.StageInfo6.message = '正在制作中，敬请期待！';
          break;
        default:
          break;
      }
    },
  },
};

</script>

<style scoped>
.stagegroup{
  position: relative;
  left: 0%;
  width: 100%;
  height: 20%;
}
</style>>
