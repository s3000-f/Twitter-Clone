<template>
  <div>
    <div class="content">
      <h1 class="title">Logs</h1>
      <h4 class="subtitle">This is where the logs of the user can be found.</h4>
      <section class="section">
       <div v-if="showList === 1" class="log-section">
         <ol>
           <li v-for="log in logs">{{log}}</li>
         </ol>
       </div>
        <div v-else-if="showList === -1">
          No Logs was found ... :(
        </div>
        <div v-else-if="showList === 0">
         <i class="fas fa-spinner fa-spin"></i> Loading Data from server
        </div>
      </section>
    </div>
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
  	name: 'Logs',
    data () {
      return {
        logs: ["!@#Loading#@!"]
      }
    },
    computed: {
  		showList: function () {
  			
        if (this.$data.logs.length > 0)
        	if (this.$data.logs[0].indexOf('!@#Loading#@!') !== -1){
            return 0;
          }
          else {
        		return 1;
          }
        else
        	return -1;
        
      }
    },
    created: function () {
	    console.log('created Logs');
      ax.post('showlog',
        qs.stringify({'token': this.$parent.$data.token})
      ).then( response => {
	      if (response.data.ans.indexOf('Invalid Token') !== -1){
	      	alert('User is Not Logged in')
          this.$router.push('/');
        }
	      this.$data.logs = response.data.ans
        console.log('log Section ',this.$data.logs.length);
      }).catch( (error) =>{
      	console.error(error)
      })
    }
  }
</script>

<style>
  .log-section {
    background-color: white;
    white-space: pre-wrap;
    word-wrap: break-word;
  }
</style>