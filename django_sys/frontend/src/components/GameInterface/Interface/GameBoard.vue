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
          :treasureOpen=treasureOpen
        >
        </map-block>
      </div>
    </div>
  </div>
</template>

<script>
import MapBlock from './GameBoard/MapBlock.vue';

export default {
  name: 'GameBoard',
  data() {
    return {
      initialization: null,
      treasureOpen: false,
      DataSet: {
        state: String,
        message: String,
        map: {
          character: {
            type: Number,
            x: Number,
            y: Number,
            state: String,
          },
          end: {
            x: Number,
            y: Number,
          },
          id: Number,
          length: Number,
          name: String,
          start: {
            x: Number,
            y: Number,
          },
          state: null,
          treasure: {
            x: Number,
            y: Number,
            collected: Boolean,
          },
          width: Number,
        },
        actionList: null,
      },
    };
  },
  components: {
    MapBlock,
  },
  methods: {
    getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
      return null;
    },
    getMap(mapid) {
      const MapDatabaseQueryPath = '/mapInfo/';
      this.$http({
        url: MapDatabaseQueryPath,
        method: 'post',
        data: {
          id: mapid,
        },
        headers: { 'X-CSRFToken': this.getCookie('csrftoken') },
        credentials: 'include',
      }).then((response) => {
        console.log(response);
        this.DataSet.map = response.data.map;
        this.initialization = JSON.parse(JSON.stringify(this.DataSet));
      }).catch((error) => {
        console.log(error);
      });
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
        this.treasureOpen = true;
      } else if (action === 'collectFail') {
        document.alert('打开失败');
      }
    },
    clear() {
      this.DataSet = JSON.parse(JSON.stringify(this.initialization));
      this.treasureOpen = false;
    },
  },
  mounted() {
    const mapidpath = this.$route.path;
    const mapid = mapidpath.replace('/GameInterface/', '');
    console.log(mapid);
    this.getMap(Number(mapid));
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
