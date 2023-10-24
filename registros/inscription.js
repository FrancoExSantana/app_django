var careerSelect = document.getElementById('career');
var fields = document.querySelectorAll('.subject-field');

careerSelect.addEventListener('change', function() {
    var selectedOption = this.options[this.selectedIndex];
    var fieldIds = selectedOption.getAttribute('data-fields').split(' ');
    fields.forEach(function(field) {
        if (fieldIds.indexOf(field.id) !== -1) {
            field.style.display = 'block';
        } else {
            field.style.display = 'none';
        }
    });
});