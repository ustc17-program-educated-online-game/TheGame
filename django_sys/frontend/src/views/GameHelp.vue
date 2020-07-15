<template>
  <div>
        <b-card-group deck>
            <b-card title="背景故事" img-src="" img-alt="Image" img-top>
                <b-card-text class="storytext">
                    <p>&nbsp;&nbsp;&nbsp;&nbsp;马大叔是一名大龄程序员，虽然生活有着诸多不顺，可是他却始终却没有放弃自己小时候的梦想——在星海中漫步。
                    今夜，他终于得到了幸运女神的垂青。在下班回家的路上，马大叔遇到了神秘的飞船和男孩，一场奇妙的太空探险就此展开。。。<br>
                    </p>
                </b-card-text>
                <b-button href="/#/GameInterface" class="card-link">开始游戏</b-button>
            </b-card>

            <b-card title="游戏目标" img-src="" img-alt="Image" img-top>
                <b-card-text>
                    游戏的目标很简单，操纵宇宙飞船去寻找宝藏吧！
                </b-card-text>
            </b-card>

        </b-card-group>
        <b-card-group deck>
            <b-card title="游戏帮助" img-src="" img-alt="Image" img-top>
                <b-card-text>
                    <p>为了让宇宙飞船送我们去埋藏宝藏的地方，我们需要一些特别的方法来控制它前进。<br>
                        在旅途中我们总是会遇到许多阻碍，地图上的这些障碍就阻挡了我们前进的步伐。因此我们需要小心控制飞船前进(配障碍图一张)<br>
                        右边的区域是我们的飞船控制区，我们可以拖动命令方块到右边的区域中，并通过合理的选择它们的顺序与结构，让飞船正确的前进吧。<br>
                        //（此处应有配图一张）
                    </p>

                    <h5><b>1.顺序执行</b></h5>
                        （顺序执行的介绍，结合关卡图片）
                    <p></p>
                    <h5><b>2.条件判断</b></h5>
                        （条件判断的介绍，结合关卡图片）
                    <p></p>
                    <h5><b>3.循环执行</b></h5>
                        （循环执行的介绍，结合关卡图片）
                    <p></p>
                    <h5><b>4.其他技巧</b></h5>
                        （其他技巧的介绍，结合关卡图片）
                    <p></p>
                </b-card-text>
            </b-card>
        </b-card-group>
  </div>
  <!---->
</template>

<script>
// @ is an alias to /src
// import Cards from '../components/Homepage/Cards.vue';

export default {
  name: 'GameHelp',
  components: {
    // Cards,
  },
};
</script>

<style>
.picture{
    width: 90%;
    height: 300%;
}
.storytext{
    text-align: left;
}
</style>
