css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img alt="imgbot" src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/dfc47f68-5935-483b-8f5d-ff478c7c9c5d/dg10htp-89e6b0ef-ad41-4928-a282-32773e7c0881.png/v1/fill/w_1280,h_1280,q_80,strp/cyborg_6_by_deathhtaed_dg10htp-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2RmYzQ3ZjY4LTU5MzUtNDgzYi04ZjVkLWZmNDc4YzdjOWM1ZFwvZGcxMGh0cC04OWU2YjBlZi1hZDQxLTQ5MjgtYTI4Mi0zMjc3M2U3YzA4ODEucG5nIiwiaGVpZ2h0IjoiPD0xMjgwIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uud2F0ZXJtYXJrIl0sIndtayI6eyJwYXRoIjoiXC93bVwvZGZjNDdmNjgtNTkzNS00ODNiLThmNWQtZmY0NzhjN2M5YzVkXC9kZWF0aGh0YWVkLTQucG5nIiwib3BhY2l0eSI6OTUsInByb3BvcnRpb25zIjowLjQ1LCJncmF2aXR5IjoiY2VudGVyIn19.ZTPD8hO3797IlQnr1yXI7KebJUAvd8T7yJdmqMfUF0A" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;"></img>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://th.bing.com/th/id/OIP.nqValcTDqLOyqJYSTYf_ZQHaHa?pid=ImgDet&rs=1">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''