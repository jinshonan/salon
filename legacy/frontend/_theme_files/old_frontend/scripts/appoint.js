document.addEventListener("DOMContentLoaded", () => {
    const appointmentForm = document.getElementById("appointment-form");
    const appointmentStatus = document.getElementById("appointment-status");

    if (appointmentForm) {
        appointmentForm.addEventListener("submit", (event) => {
            event.preventDefault(); // Prevent the form from submitting normally
            
            // Get form values
            const clientName = document.getElementById("client-name").value;
            const appointmentDate = document.getElementById("appointment-date").value;
            
            // Check if inputs are valid
            if (!clientName || !appointmentDate) {
                showStatus("すべてのフィールドを入力してください。", "error");
                return;
            }
            
            // Create appointment data
            const appointmentData = {
                stylist: "静香",
                date: new Date(appointmentDate).toISOString(),
                client: clientName
            };
            
            // Show loading status
            showStatus("予約中...", "loading");
            
            // Send the data to the server
            fetch("/book", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(appointmentData)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error("サーバーエラーが発生しました。");
                }
                return response.json();
            })
            .then(data => {
                // Show success message
                showStatus(`予約が完了しました！\n${appointmentData.client}様、${formatDate(appointmentData.date)}に静香スタイリストがお待ちしております。`, "success");
                
                // Reset the form
                appointmentForm.reset();
            })
            .catch(error => {
                console.error("Error:", error);
                showStatus("予約に失敗しました。もう一度お試しください。", "error");
            });
        });
    }
    
    // Helper function to display status messages
    function showStatus(message, type) {
        appointmentStatus.textContent = message;
        appointmentStatus.className = `status ${type}`;
        
        // For success messages, keep them visible longer
        if (type === "success") {
            setTimeout(() => {
                appointmentStatus.className = "status hidden";
            }, 5000);
        }
    }
    
    // Helper function to format date for display
    function formatDate(dateString) {
        const date = new Date(dateString);
        const options = { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric', 
            hour: '2-digit', 
            minute: '2-digit' 
        };
        return date.toLocaleDateString('ja-JP', options);
    }
});