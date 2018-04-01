<template>
    <div class="field">
      <!--  the right side icon will change accordingly if username exist in
            database or not -->
      <div class="control has-icons-left has-icons-right">
        <input
         v-model="username"
         v-on:keyup.enter="signup(username, password)"
         type="text"
         name="username"
         class="input"
         placeholder="Enter your username">
        <span class="icon is-small is-left">
          <i class="fa fa-user"></i>
        </span>
        <p v-if="usernameExistFlag" class="help is-danger">
        user already exist
        </p>
      </div>
      <div class="control has-icons-left">
        <input v-on:keyup.enter="signup(username, password)"
         v-model="password"
         class="input"
         type="password"
         name="password"
         placeholder="Enter your password">
        <span class="icon is-small is-left">
          <i class="fa fa-lock"></i>
        </span>
      </div>
        <button v-on:click="signup(username, password)" class="button is-link">
          <span> Sign Up! </span>
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
    nme: 'SignupComponent',
    data () {
      return {
        username: '',
        password: '',
        usernameExistFlag: false
      }
    },
    methods: {
      signup: function (u, p) {
        if (u && p) {
          ax.post('signup',
            qs.stringify({'username': this.username}) + '&' + qs.stringify({'password': this.password})
  
          )
            .then( (response) => {
	            if (response.data.ans.indexOf('Already Registered') !== -1) {
	              console.log(this.$data.usernameExistFlag);
	              this.$data.usernameExistFlag = true;
	              console.log(this.$data.usernameExistFlag);
              }
              else {
	            	this.$parent.$parent.$data.token = response.data.ans;
                console.log(this.$parent.$parent.$data.token)
                this.$router.push('Home')
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
