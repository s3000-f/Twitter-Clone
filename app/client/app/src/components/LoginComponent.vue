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
      username: '',
      password: '',
      wrongPasswordFlag: false,
      wrongUserFlag: false,
      alreadyLoggedinFlag: false
    }
  },
  methods: {
    login: function () {
      if (this.username && this.password) {
      	this.$data.wrongUserFlag = false;
      	this.$data.alreadyLoggedinFlag = false;
      	this.$data.wrongPasswordFlag = false;
        ax.post('login',
          qs.stringify({'username': this.username}) + '&' + qs.stringify({'password': this.password})

        )
          .then((response) => {
          	console.log(response.data.ans);
            if(response.data.ans.indexOf("Not Registered") !== -1){
            	this.$data.wrongUserFlag = true
            }
            else if(response.data.ans.indexOf("Already Logged In") !== -1){
            	this.$data.alreadyLoggedinFlag = true
            }
            else if(response.data.ans.indexOf("Wrong Password") !== -1){
            	this.$data.wrongPasswordFlag = true
            }
            else {
            	this.$parent.$parent.$data.token = response.data.ans;
            	this.$router.push('home');
            }
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
