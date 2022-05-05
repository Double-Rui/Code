new Vue({
	el:'.Login_panel',
	data:{
		active: 0,
		Loginform:{
			LoginID:'',
			PassWord:'',
		},
		Registerform:{
			NickName:'',
			PassWord:'',
			RePassWord:'',
		}
	},
	methods: {
		Login(){
			var self=this
			if(this.Loginform.LoginID=='' && this.Loginform.PassWord==''){
				self.$message.error('未输入任何参数');
			}
			else if(this.Loginform.LoginID==''){
				self.$message.error('账号不能为空');
			}
			else if(this.Loginform.PassWord==''){
				self.$message.error('密码不能为空');
			}
			else{
				axios.post('/Login','LoginID='+this.Loginform.LoginID+'&PassWord='+this.Loginform.PassWord)
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
		Register(){
			var self=this
			if(this.Registerform.NickName=='' && this.Registerform.PassWord=='' && this.Registerform.RePassWord==''){
				self.$message.error('未输入任何参数');
			}
			else if(this.Registerform.NickName==''){
				self.$message.error('昵称不能为空');
			}
			else if(this.Registerform.PassWord==''||this.Registerform.RePassWord==''){
				self.$message.error('密码不能为空');
			}
			else if(this.Registerform.PassWord!=this.Registerform.RePassWord){
				self.$message.error('两次密码不一样');
			}
			else{
				axios.post('/Register/','NickName='+this.Registerform.NickName+
										'&PassWord='+this.Registerform.PassWord+
										'&RePassWord='+this.Registerform.RePassWord)
				.then(function(response){
					data=response.data
					if(data.status==0){
						self.$message.error(data.result);
					}
					else if(data.status==1){
						$("#Registerid").text(data.ID)
						$("#Spring_frame").animate({ "margin-left": "150px" }, 2000);
					}
				},function(err){
					console.log(err)
				})
			}
		},
		next() {
			if(this.active<2){
				this.active++
			}else{
				
			}
		},
		last() {
			if(this.active>0){
				this.active--
			}else{
				
			}
		}
	}
})