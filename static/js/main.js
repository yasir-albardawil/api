// let tbody = document.querySelector('tbody');
// let id = document.createElement('td');
// let first_name = document.createElement('td');
// let last_name = document.createElement('td');
// let a = document.createElement('a');
//
// let gitgub = document.createElement('td');
// let tr = document.createElement('tr');
//
// let xhr = new XMLHttpRequest(); // the constructor has no arguments
// xhr.onload = function () {
//     if (this.status === 200) {
//         try {
//
//             const responseObject = JSON.parse(this.responseText);
//             let resObj = null;
//
//             for (resObj in responseObject.data) {
//                 id.textContent = responseObject.data[resObj].id;
//                 first_name.textContent = responseObject.data[resObj].first_name;
//                 last_name.textContent = responseObject.data[resObj].last_name;
//                 a.textContent = responseObject.data[resObj].github_link;
//                 a.href = responseObject.data[resObj].github_link;
//                 tbody.appendChild(tr);
//                 console.log(a);
//                 tr.appendChild(id);
//                 tr.appendChild(first_name);
//                 tr.appendChild(last_name);
//                 tr.appendChild(gitgub);
//                 gitgub.appendChild(a);
//
//                 tbody.innerHTML += '';
//             }
//         } catch (e) {
//             console.warn('There was an error in the JSON. Could not parse!');
//         }
//     } else {
//         console.warn('Did not receive 200 Ok from response');
//     }
// };
//
// // Secured api
// // xhr.open('GET', 'http://127.0.0.1:5000/data.json?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoieWFzaXIifQ.SlMcGE7m4Xy-IkrYbHXa3J3hpuQrEQz_sb0lBrLRJIE');
// xhr.open('GET', 'https://yasir-api.herokuapp.com/data.json?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoieWFzaXIifQ.SlMcGE7m4Xy-IkrYbHXa3J3hpuQrEQz_sb0lBrLRJIE');
// xhr.send();
