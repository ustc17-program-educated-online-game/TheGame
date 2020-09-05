<template>
  <div class="MapBoard border border-primary rounded">
    <div v-for="(states, index1) in DataSet.map.state" :key="index1">
      <div v-for="(state, index2) in states" :key="index2">
        <map-edit-block
          :state=DataSet.map.state[index1][index2]
          :length=DataSet.map.length
          :width=DataSet.map.width
          :x=index1
          :y=index2
          :start=DataSet.map.start
          :end=DataSet.map.end
          :character=DataSet.map.character
          :select=SelectBlock
          @select-changed="ChangeSelectedBlock(arguments)"
          >
        </map-edit-block>
      </div>
    </div>
  </div>

</template>

<script>
import TestJson from './init.json';
import MapEditBlock from './MapEditBlock.vue';

export default {
  name: 'MapBoard',
  data() {
    return {
      DataSet: {
        state: String,
        message: String,
        map: {
          id: Number,
          name: String,
          length: Number,
          width: Number,
          state: null,
          start: {
            x: Number,
            y: Number,
          },
          end: {
            x: Number,
            y: Number,
          },
          treasure: {
            x: Number,
            y: Number,
            collected: Boolean,
          },
          character: {
            type: Number,
            x: Number,
            y: Number,
            state: String,
          },
        },
        actionList: null,
      },
      SelectBlock: {
        state: Boolean,
        x: Number,
        y: Number,
      },
    };
  },
  created() {
    this.DataSet = TestJson;
    this.SelectBlock = {
      state: true,
      x: 2,
      y: 1,
    };
  },
  components: {
    MapEditBlock,
  },
  methods: {
    getMap(mapid) {
      const ThisComponent = this;
      const MapDatabaseQueryPath = 'http://127.0.0.1:8000/mapInfo/';
      ThisComponent.$http.get(MapDatabaseQueryPath + mapid).then((response) => {
        ThisComponent.DataSet = response.data;
      });
    },
    saveMap(userid, username) {
      this.DataSet.map.id = userid;
      const ActionAnalyzePath = '/mapEditor/';
      const passData = {
        user_id: userid,
        user_name: username,
        map: this.DataSet.map,
      };
      this.$http({
        url: ActionAnalyzePath,
        method: 'post',
        data: passData,
        headers: { 'X-CSRFToken': this.getCookie('csrftoken') },
      }).then((response) => {
        console.log(response.data.message);
      }).catch((error) => {
        console.log(error);
      });
    },
    getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
      return null;
    },
    resetMap() {
      let i = 0;
      let j = 0;
      for (i = 0; i < 8; i += 1) {
        for (j = 0; j < 8; j += 1) {
          this.DataSet.map.state[i][j] = 1;
        }
      }
      this.SelectBlock = {
        state: false,
        x: 2,
        y: 1,
      };
      this.DataSet.map.treasure.x = '-1';
      this.DataSet.map.treasure.y = '-1';
      this.updateMap();
    },
    updateMap() {
      this.DataSet = {
        state: 'running',
        message: 'success',
        map: {
          id: '关卡编号',
          name: 'one',
          length: '8',
          width: '8',
          state: [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
          ],
          start: {
            x: '0',
            y: '0',
          },
          end: {
            x: '7',
            y: '7',
          },
          treasure: {
            x: '-1',
            y: '-1',
            collected: '0',
          },
          character: {
            type: '1',
            x: '0',
            y: '0',
            state: 'u',
          },
        },
        actionList: [
          'turnRight',
          'goUp',
          'turnRight',
          'goDown',
          'turnRight',
          'isBlank',
          'isObstacle',
          'turnLeft',
          'isTreasure',
          'isEdge',
          'goLeft',
          'turnRight',
          'goRight',
          'collectSuccess',
          'endMissionFail',
        ],
      };
      this.SelectBlock = {
        state: false,
        x: 2,
        y: 1,
      };
      this.DataSet = TestJson;
    },
    ChangeSelectedBlock(position) {
      const x = position[0];
      const y = position[1];
      this.SelectBlock.state = true;
      this.SelectBlock.x = x;
      this.SelectBlock.y = y;
    },
    MoveElement(direction) {
      if (this.SelectBlock.state === true) {
        if (direction === 'up' && this.SelectBlock.x > 0) this.SelectBlock.x -= 1;
        else if (direction === 'down' && this.SelectBlock.x < 7) this.SelectBlock.x += 1;
        else if (direction === 'left' && this.SelectBlock.y > 0) this.SelectBlock.y -= 1;
        else if (direction === 'right' && this.SelectBlock.y < 7) this.SelectBlock.y += 1;
      }
    },
    SetPoint(msg) {
      const type = msg[0];
      const position = msg[1];
      const { x: px, y: py } = position;
      if (type === 'start') {
        this.DataSet.map.start.x = px;
        this.DataSet.map.start.y = py;
        this.DataSet.map.character.x = px;
        this.DataSet.map.character.y = py;
      } else {
        this.DataSet.map.end.x = px;
        this.DataSet.map.end.y = py;
      }
    },
    SelectElement(msg) {
      if (this.SelectBlock.state === true) {
        if (msg === 'obstacle') {
          if (this.DataSet.map.start.x === this.SelectBlock.x && this.DataSet.map.start.y === this.SelectBlock.y) {
            alert('起点处不可以添加障碍物');
          } else if (this.DataSet.map.end.x === this.SelectBlock.x && this.DataSet.map.end.y === this.SelectBlock.y) {
            alert('终点处不可以添加障碍物');
          } else if (this.DataSet.map.state[this.SelectBlock.x][this.SelectBlock.y] === 3) {
            this.DataSet.map.treasure.x = '-1';
            this.DataSet.map.treasure.y = '-1';
          }
          this.DataSet.map.state[this.SelectBlock.x][this.SelectBlock.y] = 2;
        } else if (this.DataSet.map.treasure.x === '-1') {
          this.DataSet.map.state[this.SelectBlock.x][this.SelectBlock.y] = 3;
          this.DataSet.map.treasure.x = this.SelectBlock.x.toString();
          this.DataSet.map.treasure.y = this.SelectBlock.y.toString();
        } else {
          alert('最多有一个宝藏');
        }
      }
      this.updateMap();
    },
    RemoveElement() {
      if (this.SelectBlock.state === true) {
        if (this.DataSet.map.state[this.SelectBlock.x][this.SelectBlock.y] === 3) {
          this.DataSet.map.treasure.x = '-1';
          this.DataSet.map.treasure.y = '-1';
        }
        this.DataSet.map.state[this.SelectBlock.x][this.SelectBlock.y] = 1;
      }
      this.updateMap();
    },
    RotateCharacter() {
      console.log(this.DataSet.map.character.state);
      if (this.DataSet.map.character.state === 'u') {
        this.DataSet.map.character.state = 'l';
      } else if (this.DataSet.map.character.state === 'l') {
        this.DataSet.map.character.state = 'd';
      } else if (this.DataSet.map.character.state === 'd') {
        this.DataSet.map.character.state = 'r';
      } else {
        this.DataSet.map.character.state = 'u';
      }
      console.log(this.DataSet.map.character.state);
      this.updateMap();
      console.log(this.DataSet.map.character.state);
    },
  },
};
</script>

<style>
.MapBoard {
  position: absolute;
  top: 1.4%;
  left: 7.5%;
  width: 55%;
  height:90%;
  box-shadow: 6px 6px 3px #888888;
}
</style>
