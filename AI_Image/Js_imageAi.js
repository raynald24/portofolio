let defaultText = 'hello';
let p=document.querySelector ("p")
let body = document.body;
btn1.textContent = defaultText;
let newText = null; // Inisialisasi newText dengan null
let kerenAdded = false; // Flag untuk memeriksa apakah kata 'Keren' sudah ditambahkan atau belum
let input = document.querySelector('input')

function clickbutton() {
    btn1.style.background = 'red';
    let isi =input.value;
    p.innerHTML = isi;
}

function ubahText() {
    if (!kerenAdded) { // Periksa apakah kata 'Keren' sudah ditambahkan sebelumnya
        newText = document.createElement('p');
        newText.textContent = 'Keren';
        newText.style.color = 'red'; // Mengatur warna teks menjadi merah
        body.append(newText);
        kerenAdded = true; // Setel flag menjadi true karena kata 'Keren' telah ditambahkan
    }
}

function oriText() {
    btn1.style.color = 'blue';
    if (newText) { // Periksa apakah kata 'Keren' sudah ditambahkan sebelumnya
        newText.remove(); // Hapus newText jika sudah ditambahkan sebelumnya
        newText = null; // Set newText kembali ke null
        kerenAdded = false; // Setel flag kembali ke false karena kata 'Keren' telah dihapus
        btn1.textContent = defaultText;
    }
}

btn1.addEventListener('click', clickbutton);
btn1.addEventListener('mouseover', ubahText);
btn1.addEventListener('mouseout', oriText);
