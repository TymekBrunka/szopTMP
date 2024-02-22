var updateBtns = document.getElementsByClassName('update-cart')

for (btn of updateBtns){
	btn.onclick = () => {
		var productId = btn.dataset.product //jakbym dał this zamiast btn to this by się nie odnosiło do btn
		var action = btn.dataset.action
		console.log(`product id: ${productId}, action: ${action}`)

		console.log(`USER: ${user}`)
		if (user === 'AnonymousUser'){
			console.log("Niezalogowany")
		} else {
			// console.log("Zalogowany")
			updateUserOrder(productId, action)
		}
	}
}

function updateUserOrder(productId, action){
	console.log("Sending data")	
	var url = '/update_item/'
	fetch(url, {
		method: 'POST',
		headers: {
			'ContentType': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body:JSON.stringify({
			'productId': productId,
			'action': action
		})
	})
	.then((response) => {
		return response.json()
	}).then((data) => {
		console.log("Data: ", data)
		location.reload()
	})
}
