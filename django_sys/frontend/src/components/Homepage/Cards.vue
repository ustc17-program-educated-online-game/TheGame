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
            <b-card title="开始游戏" img-src="https://placekitten.com/g/300/450" img-alt="Image" img-top>
            <b-card-text>
                点击下面的按钮开始游戏
            </b-card-text>
            <a href="/#/GameInterface" class="card-link">点我开始</a>
            </b-card>

            <b-card title="背景故事" img-src="https://placekitten.com/g/300/450" img-alt="Image" img-top>
            <b-card-text>
                在这里写游戏背景的简述
            </b-card-text>
            <a href="#" class="card-link">详细了解</a>
            </b-card>

            <b-card title="游戏帮助" img-src="https://placekitten.com/g/300/450" img-alt="Image" img-top>
            <b-card-text>
                可以查看游戏的玩法和一些小技巧
            </b-card-text>
            <a href="#" class="card-link">查看帮助</a>
            </b-card>

            <b-card title="游戏设置" img-src="https://placekitten.com/g/300/450" img-alt="Image" img-top>
            <b-card-text>
                可以在这里调整游戏的设置
            </b-card-text>
            <a href="#" class="card-link">调整设置</a>
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
</style>
