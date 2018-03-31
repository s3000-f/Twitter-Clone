<template>
    <div class="field">
      <!--  the right side icon will change accordingly if username exist in
            database or not -->
      <div class="control has-icons-left has-icons-right">
        <input
         v-model="username"
         v-on:keyup.enter="login(username, password)"
         type="text"
         name="username"
         class="input"
         placeholder="Enter your username">

        <span class="icon is-small is-left">
          <i class="fa fa-user"></i>
        </span>
      </div>
      <div class="control has-icons-left">
        <input v-on:keyup.enter="login(username, password)"
         v-model="password"
         class="input"
         type="password"
         name="password"
         placeholder="Enter your password">
        <span class="icon is-small is-left">
          <i class="fa fa-lock"></i>
        </span>
      </div>
        <button v-on:click="login(username, password)" class="button is-link">
          <span class="icon is-small">
          <i class="fa fa-sign-in"></i>
          </span>
          <span> Login </span>
        </button>

    </div>

</template>



<script>
import axios from 'axios'
import qs from 'qs'
let ax = axios.create({
  baseURL: 'http://localhost:5000/api/',
  timeout: 5000,
  headers: {'Content-type': 'application/x-www-form-urlencoded'}
})
export default {
  name: 'LoginComponent',
  data () {
    return {
      username: 'sdfsadfad',
      password: 'asdfsdaf'
    }
  },
  methods: {
    login: function () {
      if (this.username && this.password) {
        ax.post('login',
          qs.stringify({'username': this.username}) + '&' + qs.stringify({'password': this.password})

        )
          .then(function (response) {
            console.log(response)
          })
          .catch(function (error) {
            console.error(error)
          })
      }
    }
  }
}
</script>



<style>

</style>
