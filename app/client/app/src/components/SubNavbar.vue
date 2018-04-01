<template>
  <nav>
    <nav class="tabs is-small">
      <ul>
        <router-link tag="li" activeClass='is-active' :to="{ path: 'home'}"><a>Home</a></router-link>
        <router-link tag="li" activeClass='is-active' :to="{ path: 'users'}"><a>Users</a></router-link>
        <router-link tag="li" activeClass='is-active' :to="{ path: 'log'}"><a>Show Log</a></router-link>
      </ul>
    </nav>
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
  name: 'SubNavbar',
  methods: {
  	logout: function () {
      ax.post('logout',
        qs.stringify({'token': this.$parent.$data.token})//
      ).then( response => {
	      if (response.data.ans.indexOf('User Not Logged-in') !== -1)
        {
        	alert("USER IS NOT LOGGED IN")
          this.$router.push('/')
        }
        else {
		      console.log('user', this.$parent.$data.token, 'has logged out');
		      this.$router.push('/')
	      }
      })
	  }
  }
}
</script>

<style lang="sass" scoped>

.tabs
	background-color: darken($background, 2)

</style>
