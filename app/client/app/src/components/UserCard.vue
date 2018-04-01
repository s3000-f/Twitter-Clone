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
            <button class="button follow-button">Follow</button>
            <button class="button unfollow-button">Unfollow</button>
          </div>
        </div>
      
    </div>
    <div class="level">
        <div class="level-item horizontal-line"></div>
      </div>
    
  </div>
</template>


<script>
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
</style>