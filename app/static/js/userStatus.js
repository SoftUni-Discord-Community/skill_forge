document.addEventListener('DOMContentLoaded', () => {
    const userId = "{{ user.user_id }}";  // Get the user ID dynamically
    const socket = io('http://192.168.0.169:5000/', {
        query: {
            user_id: userId
        }
    });

    socket.on('connect', () => {
        // When the Socket.IO connection is established, request the user's current status
        socket.emit('request_user_status', { user_id: userId });
    });

    socket.on('disconnect', () => {
        updateOnlineStatus('Offline');
    });

    socket.on('status_update', (data) => {
        // Update the user's status when the status is received from the server
        updateOnlineStatus(data.status);
    });

    socket.on('current_user_status', (data) => {
        // Update the user's status when the current status is received from the server
        updateOnlineStatus(data.status);
    });

    socket.on('current_user_status', (data) => {
        // Update the user's status when the current status is received from the server
        updateOnlineStatus(data.status);
    });

    function updateOnlineStatus(status) {
        const onlineStatusDiv = document.getElementById('onlineStatusDiv');
        if (onlineStatusDiv) {
            if (status === 'Online') {
                onlineStatusDiv.innerHTML = `<p class="online_status title online">${status}</p>`;
            } else {
                // Make AJAX request to fetch last logged date
                fetch('/get_last_logged_date')
                    .then(response => response.json())
                    .then(data => {
                        const lastLoggedDate = data.last_logged_date;
                        onlineStatusDiv.innerHTML = `<p class="online_status title offline">Last seen</p>
                            <p class="online_status title offline">${lastLoggedDate}</p>`;
                    })
                    .catch(error => {
                        onlineStatusDiv.innerHTML = `<p class="online_status title offline">${status}</p>`;
                    });
            }
        }
    }
});