<template>
  <nav>
    <nav class="tabs is-small">
      <ul>
        <router-link tag="li" activeClass='is-active' :to="{ path: 'home'}"><a>Home</a></router-link>
        <router-link tag="li" activeClass='is-active' :to="{ path: 'users'}"><a>Users</a></router-link>
        <router-link tag="li" activeClass='is-active' :to="{ path: 'logs'}"><a>Show Log</a></router-link>
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
  }
}
</script>

<style lang="sass" scoped>

.tabs
	background-color: darken($background, 2)

</style>
