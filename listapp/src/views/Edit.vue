<template lang="pug">
    form.container(method="post" @submit.prevent="edit")
        .form-group
            label(for="name") Task: 
            input#name(type="text" placeholder="Enter task" name="name" v-model="todo.name")

        button(type="submit") Submit
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            todo: {
                name: ""
            }
        }
    }, 
    methods: {
        edit(e) {
            axios.put(`http://127.0.0.1:8888/api/todo/${this.todo.todo_id}/`, this.todo)
            .then(res => {
                this.$router.push("/");
            })
            .catch(err => {console.log(err)})
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8888/api/todo/' + this.$route.params.id)
        .then(res=> {
            this.todo = res.data;
        })
    }
}
</script>

<style lang="scss" scoped>
input {
    padding: 5px;
    margin-right: 10px;
}

button {
    border: 1px solid black;
    background-color: lawngreen;
    color: black;
    border-radius: 10px;
    font: inherit;
    cursor: pointer;
}
</style>