<template>
  <div class="main" id="app">
    <div v-if="!this.showCode">
      <div class="loginPage">
        <h3>LOGIN</h3><input id="user" v-model="user" type="text">
        <h3>PASSWORD</h3><input id="pwd" v-model="pwd" type="text">
        <br>
        <button class="loginBtn" @click="loginFunc()">LOGIN</button>
      </div>
    </div>
    <div v-if="this.showCode">
      <div class="textBox">
        <!-- <prism-editor ref="code" :code="this.code" language="js" lineNumbers="True" emitEvents="True" class="prismEditor">
        </prism-editor> -->
        <textarea v-model="code"></textarea>
      </div>
      <div class="buttons">
        <button @click="saveFunc()">Save</button> <button @click="commitFunc()">Commit</button>
      </div>
    </div>
  </div>
</template>

<script>

import * as sha1 from 'js-sha1'

export default {
  name: 'app',
  data () {
    return {
      code : "",
      showCode: false,
      user: '',
      pwd: '',
      savedCode: ''
    }
  },
  mounted: function () {
  },
  methods: {
    submitFunc(){
      alert('submit function is working')
    },
    commitFunc(){
      alert('commit function is working')
    },
    loginFunc(){
      var vm = this
      if(this.user && this.pwd) {
        var usrSha1 = sha1(vm.user)
        var usrB64 = window.btoa(usrSha1)
        alert(usrB64)
        vm.$http.post('http://localhost:5000/', {'username': vm.user, 'password': vm.pwd}).then(
          resp => {
            console.log(resp)
            vm.showCode = true
            vm.code = resp.body[0]
          }
        )  
      }    
    },
    saveFunc(){
      console.log(this.code)
       this.$http.post('http://localhost:5000/saveCode',{'savedCode' : this.code}).then(
         resp => {
           console.log(resp)
         }
       )
    },
    commitFunc(){
       this.$http.post('http://localhost:5000/commitCode',{'commitedCode' : this.code, 'username': this.user }).then(
         resp => {
           console.log(resp)
         }
       )
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.loginBtn{
  margin-top: 2vh;
}
.main{

}
.textBox{
position: absolute;
height: 80vh;
width: 85vw;
left: 13vw;
}
.buttons{
position: absolute;
top: 90vh;
left: 45vw;
font-size: 
}
.prismEditor{
  width: 50vw;
  height: 100vh;
}
</style>
