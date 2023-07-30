css = '''
<style>
.chat-message{
    padding: 1.5rem; 
    border-radius: 0.8rem; 
    margin-bottom: 1rem; 
    display: flex;
}
.chat-message.user{
    background-color: #2b313e;
}
.chat-message.bot{
    background-color: #475063;
}
.chat-message .avatar{
    width: 15%;
}
.chat-message .avatar img{
    width: 78px;
    height: 78px;
    border-radius: 50%;
    object-fit: cover;
    object-position: center;
    overflow: hidden;
}
.chat-message .message{
    width: 85%;
    padding: 0 1.5rem;
    color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://th.bing.com/th/id/OIP.K1h4mzjWUmIYRsvqlRtecgAAAA?pid=ImgDet&rs=1">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://th.bing.com/th/id/R.0977b8e4d0d4525eafc78a0489480cbe?rik=VzKj1MIDtCur4w&pid=ImgRaw&r=0">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''