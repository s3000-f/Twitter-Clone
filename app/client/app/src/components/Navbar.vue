<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
        <div class="navbar-item">
          <img src="../assets/img/logo.png">
        </div>
      <a class="navbar-item" v-on:click="goToHome">
        Home
      </a>
      <router-link class="navbar-item" activeClass='is-active' :to="{ path: 'search'}">Search</router-link>
      <div class="navbar-end">
      
      </div>
    </div>
    <div class="navbar-menu">
      <div class="navbar-end">
        <a class="navbar-item is-size-7" v-on:click="logout">Log Out</a>
      </div>
    </div>
  </nav>
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
  name: 'Navbar',
  data () {
    return {
    }
  },
  methods: {
	  logout: function () {
		  ax.post('logout',
			  qs.stringify({'token': this.$parent.$data.token})//
		  ).then(response => {
			  if (response.data.ans.indexOf('User Not Logged-in') !== -1) {
				  alert("USER IS NOT LOGGED IN")
				  this.$router.push('/')
			  }
			  else {
				  console.log('user', this.$parent.$data.token, 'has logged out');
				  this.$parent.$data.token = ""
				  this.$router.push('/')
			  }
		  })
	  },
    goToHome: function () {
      if (this.$parent.$data.token.length >0)
      {
      	this.$router.push('/home')
      }
      else {
      	this.$router.push('/')
      }
    }
  }
}
</script>

<style lang="sass" scoped>

nav.navbar
  min-height: none
  background-color: $nav-background
  border-bottom: solid 1px #dbdbdb

.navbar-brand > .navbar-item
  padding-left: 10px

  img
    height: 15px

</style>
