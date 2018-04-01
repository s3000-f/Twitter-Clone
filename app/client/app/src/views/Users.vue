<template>
  <div class="container">
    <user-card v-for="(userid, usern) in users"
               v-bind:key="userid"
               v-bind:username="usern"
               v-bind:id="userid">
      
    </user-card>
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
  
  import UserCard from '../components/UserCard.vue'
  export default {
  	name: 'Users',
    data () {
  		return {
  			users: {}
      }
    },
    components: {
  		UserCard
    },
    created: function () {
      ax.post('users',{}).then(response=> {
	      this.$data.users = response.data.ans;
	      
      }).catch(e => {console.error(e);})
    }
  }
</script>