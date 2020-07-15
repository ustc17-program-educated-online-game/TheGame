<template>
  <div>
    <!--<div>
        <b-card-group deck>
            <b-card overlay img-src="https://placekitten.com/1000/400" img-alt="Card image" img-bottom>
                <b-card-text>
                <a href="/#/GameInterface" class="card-link">开始游戏</a>
                </b-card-text>
            </b-card>

            <b-card overlay img-src="https://placekitten.com/1000/400" img-alt="Card image" img-bottom>
                <b-card-text>
                <a href="#" class="card-link">背景故事</a>
                在这里填写背景故事简述
                </b-card-text>
            </b-card>
        </b-card-group>
    </div>
    <div>
        <b-card-group deck>
            <b-card overlay img-src="https://placekitten.com/1000/400" img-alt="Card image" img-bottom>
                <b-card-text>
                <a href="/#/GameInterface" class="card-link">游戏帮助</a>
                </b-card-text>
            </b-card>

            <b-card overlay img-src="https://placekitten.com/1000/400" img-alt="Card image" img-bottom>
                <b-card-text>
                <a href="#" class="card-link">游戏设置</a>
                点我可以调整游戏的设置
                </b-card-text>
            </b-card>
        </b-card-group>
    </div>
    -->
    <div>
        <b-card-group deck>
            <b-card title="开始游戏" img-src="" img-alt="Image" img-top>
            <b-card-text>
                点击下面的按钮开始游戏
            </b-card-text>
            <b-button href="/#/GameInterface" class="card-link">点我开始</b-button>
            <img src="../../img/card1.jpg" class="picture">
            </b-card>

            <b-card title="关卡选择" img-src="" img-alt="Image" img-top>
            <b-card-text>
                选择想要的关卡开始游戏吧
            </b-card-text>
            <b-button href="/#/StageSelect" class="card-link">关卡选择</b-button>
            <img src="../../img/card2.jpg" class="picture">
            </b-card>

            <b-card title="游戏帮助" img-src="" img-alt="Image" img-top>
            <b-card-text>
                可以查看游戏的玩法和一些小技巧
            </b-card-text>
            <b-button href="/#/GameInterface" class="card-link">查看帮助</b-button>
            <img src="../../img/card3.jpg" class="picture">
            </b-card>

            <b-card title="游戏设置" img-src="" img-alt="Image" img-top>
            <b-card-text>
                可以在这里调整游戏的设置
            </b-card-text>
            <b-button href="/#/GameInterface" class="card-link">调整设置</b-button>
            <img src="../../img/card4.jpg" class="picture">
            </b-card>
        </b-card-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cards',
};
</script>

<style>
.picture{
    width: 90%;
    height: 300%;
}
</style>
