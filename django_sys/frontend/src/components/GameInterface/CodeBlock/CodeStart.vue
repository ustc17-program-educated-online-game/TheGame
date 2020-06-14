<template>
  <div class="row CodeBlock">
    <div class="">
      <draggable
        class="dragArea list-group"
        :list="list1"
        :group="{ name: 'people', pull: 'clone', put: false }"
        tag="ul"
        :clone="cloneCode"
        @change="log"
      >
        <div
          class="list-group-item list-group-item-info"
          v-for="element in list1"
          :key="element.id"
        >
          {{ element.name }}
        </div>
      </draggable>
    </div>

    <vue-custom-scrollbar
      class="scroll-area"
      :settings="settings"
    >
      <div class="row PlayerCode">
        <div class="CodeArea bg-info">
          <nested-draggable :tasks="list" id="codes"/>
        </div>
      </div>
    </vue-custom-scrollbar>

    <button
      type="button"
      class="btn btn-primary btn-start"
      @click="getAllCodes('continue')"
    >
      Start
    </button>
    <button
      type="button"
      class="btn btn-danger btn-single"
      @click="getAllCodes('onestep')"
    >
      单步执行
    </button>
    <button
      type="button"
      class="btn btn-warning btn-clear"
      @click="clear()"
    >
      清空
    </button>
  </div>
</template>

<script>
import draggable from 'vuedraggable';
import vueCustomScrollbar from 'vue-custom-scrollbar';
import nestedDraggable from './NestedDraggable.vue';
import testJSON from '../Interface/test.json';

let idGlobal = 0;

export default {
  name: 'CodeStart',
  components: {
    draggable,
    nestedDraggable,
    vueCustomScrollbar,
  },
  data() {
    return {
      step: 0,
      actions: null,
      settings: {
        maxScrollbarLength: 160,
      },
      list1: [
        {
          id: 1,
          name: '如果',
          tasks: [],
          embeded: true,
          extrainfo: false,
        },
        {
          id: 2,
          name: '当',
          tasks: [],
          embeded: true,
          extrainfo: false,
        },
        {
          id: 3,
          name: '走',
          tasks: [],
          embeded: false,
          extrainfo: true,
        },
        {
          id: 4,
          name: '向左转',
          tasks: [],
          embeded: false,
          extrainfo: false,
        },
        {
          id: 5,
          name: '向右转',
          tasks: [],
          embeded: false,
          extrainfo: false,
        },
        {
          id: 6,
          name: '打开',
          tasks: [],
          embeded: false,
          extrainfo: false,
        },
      ],
      list: [],
    };
  },
  methods: {
    log(evt) {
      window.console.log(evt);
    },
    cloneCode({ name, embeded, extrainfo }) {
      idGlobal += 1;
      return {
        id: idGlobal,
        name,
        tasks: [],
        embeded,
        extrainfo,
      };
    },
    getCodes(object, codeslist) {
      let newcodes = codeslist;
      if (object.className === 'list-group-item list-group-item-success name') {
        if (newcodes !== '') {
          newcodes += ',{';
        } else {
          newcodes = '{';
        }
        if (object.innerText === '如果') {
          newcodes += '"condition":{';
          // add relation to newcodes
          newcodes += '"expression":';
          let relation = object.nextSibling.children[1];
          relation = relation.options[relation.selectedIndex].value;
          newcodes += relation;
          // add relation val to newcodes
          newcodes += ',"val":';
          let val = object.nextSibling.children[2];
          val = val.options[val.selectedIndex].value;
          newcodes += val;
          // add codes part to newcodes
          newcodes += ',"codes":[';
          let codes = object.parentNode.parentNode.nextSibling;
          // eslint-disable-next-line prefer-destructuring
          codes = codes.children[0].children[0].children[0].children[0];
          codes = this.getCodes(codes, '');
          newcodes += codes;
          newcodes += ']}';
          newcodes += '}';
        } else if (object.innerText === '当') {
          newcodes += '"circulate":{';
          // add relation to newcodes
          newcodes += '"expression":';
          let relation = object.nextSibling.children[1];
          relation = relation.options[relation.selectedIndex].value;
          newcodes += relation;
          // add relation val to newcodes
          newcodes += ',"val":';
          let val = object.nextSibling.children[2];
          val = val.options[val.selectedIndex].value;
          newcodes += val;
          // add codes part to newcodes
          newcodes += ',"codes":[';
          let codes = object.parentNode.parentNode.nextSibling;
          // eslint-disable-next-line prefer-destructuring
          codes = codes.children[0].children[0].children[0].children[0];
          codes = this.getCodes(codes, '');
          newcodes += codes;
          newcodes += ']}';
          newcodes += '}';
        } else if (object.innerText === '走') {
          newcodes += '"go":"';
          // eslint-disable-next-line no-console
          newcodes += object.nextSibling.children[0].value;
          newcodes += '"}';
        } else if (object.innerText === '向左转') {
          newcodes += '"turnleft": "1"}';
        } else if (object.innerText === '向右转') {
          newcodes += '"turnright": "1"}';
        } else if (object.innerText === '打开') {
          newcodes += '"open": "1"}';
        }
        let next = object.parentNode.parentNode.parentNode.nextSibling;
        if (next !== null) {
          // eslint-disable-next-line prefer-destructuring
          next = next.children[0].children[0].children[0];
          newcodes = this.getCodes(next, newcodes);
        }
      }
      return newcodes;
    },
    getAllCodes(mode) {
      let FirstSentence = document.getElementById('codes').children[0];
      // eslint-disable-next-line prefer-destructuring
      FirstSentence = FirstSentence.children[0].children[0].children[0];
      let codesstring = this.getCodes(FirstSentence, '');
      codesstring = `{"codes":[${codesstring}]}`;
      // eslint-disable-next-line no-console
      console.log(codesstring);
      const codes = JSON.parse(codesstring);
      // eslint-disable-next-line no-console
      console.log(codes);
      this.getActions(mode);
    },
    getActions(mode) {
      let i = this.step;
      const actions = testJSON.actionList;
      if (mode === 'continue') {
        const loop = setInterval(() => {
          if (actions[i] !== 'endMissionSuccess' && actions[i] !== 'endMissionFail') {
            while (actions[i] === 'isBlank' || actions[i] === 'isObstacle' || actions[i] === 'isTreasure' || actions[i] === 'isEdge') {
              i += 1;
            }
            this.takeActions(actions[i]);
            i += 1;
          } else {
            clearInterval(loop);
            if (actions[i] === 'endMissionSuccess') {
              // eslint-disable-next-line no-console
              console.log('success');
            } else if (actions[i] === 'endMissionFail') {
              // eslint-disable-next-line no-console
              console.log('fail');
            }
          }
        }, 1000);
      } else if (mode === 'onestep') {
        this.takeActions(actions[this.step]);
        this.step += 1;
        if (actions[this.step] === 'endMissionSuccess') {
          // eslint-disable-next-line no-console
          console.log('success');
        } else if (actions[this.step] === 'endMissionFail') {
          // eslint-disable-next-line no-console
          console.log('fail');
        }
      }
    },
    takeActions(action) {
      this.$emit('takeAction', action);
    },
    clear() {
      this.list = [];
      this.step = 0;
      this.$emit('clear');
    },
  },
};
</script>
<style>
.PlayerCode {
  width: 500%;
  height: 500%;
}
.CodeArea {
  width: 200%;
  height: 100%;
}
.CodeBlock {
  position: absolute;
  top: 0%;
  left: 66%;
  width: 34%;
  height: 100%;
  margin: 0%;
}
.btn-start {
  position: absolute;
  left: -1%;
  bottom: 5px;
  width: 18%;
}
.btn-single {
  position: absolute;
  left: -1%;
  bottom: 44px;
  width: 18%;
}
.btn-clear {
  position: absolute;
  left: -1%;
  bottom: 84px;
  width: 18%;
}
.scroll-area {
  width: 79%;
  height: 100%;
  background-color: rgb(87, 180, 187);
  border-radius: 3px;
}
</style>
