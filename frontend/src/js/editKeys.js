const editKeys = JSON.parse(localStorage.getItem("editKeys") || "{}"); // order ID: key
export default editKeys;

export function saveEditKeys() {
    localStorage.setItem("editKeys", JSON.stringify(editKeys));
}
