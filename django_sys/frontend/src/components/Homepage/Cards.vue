<template>
  <div>
    <div>
        <div class="card-group ">
            <div class="card bg-dark text-white ">
                <img src="../../img/card1.jpg" class="card-img">
                <div class="card-img-overlay">
                    <h5 class="card-title">开始游戏</h5>
                    <p class="card-text">
                        点击下面的按钮开始游戏
                    </p>
                    <b-button href="/#/GameInterface" class="card-link">点我开始</b-button>
                </div>
            </div>

            <div class="card bg-dark text-white ">
                <img src="../../img/card2.jpg" class="card-img">
                <div class="card-img-overlay">
                    <h5 class="card-title">关卡选择</h5>
                    <p class="card-text">
                        选择想要的关卡开始游戏吧
                    </p>
                    <b-button href="/#/StageSelect" class="card-link">关卡选择</b-button>
                </div>
            </div>

            <div class="card bg-dark text-white ">
                <img src="../../img/card3.jpg" class="card-img">
                <div class="card-img-overlay">
                    <h5 class="card-title">游戏帮助</h5>
                    <p class="card-text">
                        可以查看游戏的玩法和一些小技巧
                    </p>
                    <b-button href="/#/GameHelp" class="card-link">查看帮助</b-button>
                </div>
            </div>

            <div class="card bg-dark text-white ">
                <img src="../../img/card4.jpg" class="card-img">
                <div class="card-img-overlay">
                    <h5 class="card-title">游戏设置</h5>
                    <p class="card-text">
                        可以在这里调整游戏的设置
                    </p>
                    <b-button href="/#/GameInterface" class="card-link">调整设置</b-button>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cards',
};
</script>

<style>
</style>
