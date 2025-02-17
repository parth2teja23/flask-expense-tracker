// function deleteExpense(expenseId) {
//   fetch("/delete-expense", {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({ expenseId: expenseId }),
//   })
//     .then((response) => {
//       if (!response.ok) throw new Error("Failed to delete expense");
//       return response.json();
//     })
//     .then(() => location.reload())
//     .catch((error) => console.error("Error:", error));
// }

// function openEditModal(id, description, amount, category) {
//   document.getElementById("editExpenseId").value = id;
//   document.getElementById("editDescription").value = description;
//   document.getElementById("editAmount").value = amount;
//   document.getElementById("editCategory").value = category;
//   $("#editModal").modal("show");  // Bootstrap modal
// }

// document.getElementById("editExpenseForm").onsubmit = function (event) {
//   event.preventDefault();
  
//   const expenseId = document.getElementById("editExpenseId").value;
//   const formData = new FormData(this);
  
//   fetch(`/edit-expense/${expenseId}`, {
//     method: "POST",
//     body: formData,
//   })
//     .then((response) => {
//       if (!response.ok) throw new Error("Failed to update expense");
//       location.reload();
//     })
//     .catch((error) => console.error("Error:", error));
// };
