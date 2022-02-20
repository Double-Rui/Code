new Vue({
	el:'.Login_panel',
	data:{
		LoginID:'',
		PassWord:''
	},
	methods: {
		Login(){
			var self=this
			if(this.LoginID=='' && this.PassWord==''){
				self.$message.error('未输入任何参数');
			}
			else if(this.LoginID==''){
				self.$message.error('账号不能为空');
			}
			else if(this.PassWord==''){
				self.$message.error('密码不能为空');
			}
			else{
				axios.post('/Login','LoginID='+this.LoginID+'&PassWord='+this.PassWord)
				.then(function(response){
					data=response.data
					if(data.status==0){
						self.$message.error(data.result);
					}
					else if(data.status==1){
						self.$message.success("登录成功")
						window.location.href=data.url
					}
				},function(err){
					console.log(err)
				})
			}
		},   
	}
})