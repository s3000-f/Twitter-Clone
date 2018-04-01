<template>
  <div class="container  user-card-container">
    <div class="level">
      <div class="level-left">
        <div class="level-item">
          {{username}} @{{id}}
        </div>
      </div>
        <div class="level-right">
          <div class="level-item">
            <button class="button follow-button" @click="follow">Follow</button>
            <button class="button unfollow-button" @click="unfollow">Unfollow</button>
          </div>
        </div>
      
    </div>
    <div class="level">
        <div class="level-item horizontal-line"></div>
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
  	name: 'UserCard',
    data () {
  		return {
  			alreadyFollowedFlag: false,
        UnfolloedFlag: false
      }
    },
    props: {
  		username: {
  			type: String,
        default: "Felani"
      },
      id: {
  			type: Number,
        default: 47
      }
    },
    methods: {
  		follow: function () {
        ax.post('follow',
            qs.stringify({'token': this.$parent.$parent.$data.token}) + '&' + qs.stringify({'followingUsername': this.$props.id})
          )
          .then(response =>{
	          console.log(response.data.ans);
	          if(response.data.ans){
          		alert('User Followed Sucessfuly.');
            }
            else {
	          	alert('You are not Logged in');
	          	this.$router.push('/');
            }
          })
          .catch(e => {
          	console.error(e);
        })
		  },
      unfollow: function () {
        ax.post('unfollow',
            qs.stringify({'token': this.$parent.$parent.$data.token}) + '&' + qs.stringify({'followingUsername': this.$props.id})
          )
          .then(response =>{
	          console.log(response.data.ans);
	          if(response.data.ans){
          		alert('User Unfollowed Sucessfuly.');
            }
            else {
	          	alert('You are not Logged in');
	          	this.$router.push('/');
            }
          })
          .catch(e => {
          	console.error(e);
        })
		  }
    }
  }
</script>


<style>
  .user-card-container {
    background-color: white;
    padding: 25px 5px 0px 5px;
  }
  .horizontal-line {
  border: 0.5px solid #ddd;
  }
  .unfollow-button:hover {
    background-color: dodgerblue;
  }
  .follow-button:hover {
    background-color: dodgerblue;
  }
</style>