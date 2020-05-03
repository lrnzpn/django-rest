<template lang="pug">
  .container
    .content-wrapper
        h1 {{message}}
        h3 What is your agenda for today?
        .list-wrapper(v-if="todoList && todoList.length")
            .list-item(v-for="item in todoList")
                h1 {{item.name}}
                routerLink.btn(:to="`/edit/${item.todo_id}`") Edit
                button.btn(v-on:click="remove(item)") Delete

        .list-wrapper(v-else)
            span None
        
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import axios from "axios";

export default {
  name: 'Home',
  components: {
    
  },
  data() {
      return {
          message: 'Hello world!',
          todoList: [],
      }
  },
  methods: {
      all() {
          axios.get('http://127.0.0.1:8888/api/todo/').then(res=> {
                    this.todoList = res.data;
                })
      },
      remove(item) {
          axios.delete(`http://127.0.0.1:8888/api/todo/${item.todo_id}`)
          .then(res => {
            this.all();
          });
      }
  },
  created() {
      this.all()
  }
}
</script>

<style lang="scss">

.list-wrapper {
    span {
        color: red;
        font-size: 5em;
    }

    .list-item {

        .btn {
            text-decoration: none;
            padding: 5px 10px;
            font: inherit;
            cursor: pointer;
            margin-right: 10px;
            border-radius: 10px;
        }

        a {
            border: 1px solid aquamarine;
            background-color: aquamarine;
            color: black
        }

        button {
            border: 1px solid maroon;
            background-color: maroon;
            color: white;
        }
    }
}
</style>
