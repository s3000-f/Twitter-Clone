<template>
  <tr>
    <td>{{hid}}</td>
    <td>{{hashtagName}}</td>
    <td>{{numOfRepetition}}</td>
  </tr>
</template>


<script>
  export default {
  	name: 'HashtagCard',
    props: {
  		hid: {
  			type: Number,
        default: 0
      },
      hashtagName: {
  			type: String,
        default: 'foo'
      },
      numOfRepetition: {
  			type: Number,
        default: 99
      }
    }
  }
</script>