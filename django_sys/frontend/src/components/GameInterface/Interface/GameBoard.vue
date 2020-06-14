<template>
  <div class="GameBoard border border-primary rounded">
    <div v-for="(states, index1) in DataSet.map.state" :key="index1">
      <div v-for="(state, index2) in states" :key="index2">
        <map-block
          :state=state
          :length=DataSet.map.length
          :width=DataSet.map.width
          :x=index1
          :y=index2
          :start=DataSet.map.start
          :end=DataSet.map.end
          :character=DataSet.map.character
        >
        </map-block>
      </div>
    </div>
  </div>
</template>

<script>
import TestJson from './test.json';
import MapBlock from './GameBoard/MapBlock.vue';

export default {
  name: 'GameBoard',
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
    };
  },
  created() {
    this.DataSet = JSON.parse(JSON.stringify(TestJson));
  },
  components: {
    MapBlock,
  },
  methods: {
    getMap(mapid) {
      const ThisComponent = this;
      const MapDatabaseQueryPath = '';
      ThisComponent.$http.get(MapDatabaseQueryPath + mapid).then((response) => {
        ThisComponent.DataSet = JSON.parse(response.body);
      });
    },
    setMap(mapid) {
      this.map = {
        id: mapid,
      };
    },
    takeAction(action) {
      if (action === 'goUp') {
        this.DataSet.map.character.x = String(Number(this.DataSet.map.character.x) - 1);
      } else if (action === 'goDown') {
        this.DataSet.map.character.x = String(Number(this.DataSet.map.character.x) + 1);
      } else if (action === 'goLeft') {
        this.DataSet.map.character.y = String(Number(this.DataSet.map.character.y) - 1);
      } else if (action === 'goRight') {
        this.DataSet.map.character.y = String(Number(this.DataSet.map.character.y) + 1);
      } else if (action === 'turnLeft') {
        if (this.DataSet.map.character.state === 'u') {
          this.DataSet.map.character.state = 'l';
        } else if (this.DataSet.map.character.state === 'r') {
          this.DataSet.map.character.state = 'u';
        } else if (this.DataSet.map.character.state === 'd') {
          this.DataSet.map.character.state = 'r';
        } else if (this.DataSet.map.character.state === 'l') {
          this.DataSet.map.character.state = 'd';
        }
      } else if (action === 'turnRight') {
        if (this.DataSet.map.character.state === 'u') {
          this.DataSet.map.character.state = 'r';
        } else if (this.DataSet.map.character.state === 'r') {
          this.DataSet.map.character.state = 'd';
        } else if (this.DataSet.map.character.state === 'd') {
          this.DataSet.map.character.state = 'l';
        } else if (this.DataSet.map.character.state === 'l') {
          this.DataSet.map.character.state = 'u';
        }
      } else if (action === 'collectSuccess') {
        // eslint-disable-next-line no-console
        console.log('success');
      } else if (action === 'collectFail') {
        // eslint-disable-next-line no-console
        console.log('success');
      }
    },
    clear() {
      this.DataSet = JSON.parse(JSON.stringify(TestJson));
    },
  },
};
</script>

<style>
.GameBoard {
  position: absolute;
  top: 1.4%;
  left: 7.5%;
  width: 55%;
  height:90%;
  box-shadow: 6px 6px 3px #888888;
}
</style>
