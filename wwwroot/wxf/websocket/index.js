const uri = 'ws://' + location.host + ':3000/'
const socket = new WebSocket(uri)

socket.addEventListener('message', (event) => {
  try {
    let data = JSON.parse(event.data)
    console.log(`TA说: “${data.content}”`)
    if (data.detail) console.log('详情: ', data.detail)
  } catch(e) {
    console.log(e)
  }
})

socket.addEventListener('open', (event) => {
  socket.send(JSON.stringify({ 'content': '我来了' }))
})

socket.addEventListener('close', (event) => {
  console.log('被拒绝了。')
})

function say(content, detail) {
  socket.send(JSON.stringify({ 'content': content, 'detail': detail }))
}
