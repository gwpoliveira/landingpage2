// Ver Mais - Expandir os cursos escondidos
document.getElementById('show-more').addEventListener('click', function() {
    var items = document.querySelectorAll('.course-item.d-none');
    items.forEach(function(item) {
        item.classList.remove('d-none');
    });
    this.style.display = 'none'; // Esconder o botão "Ver Mais"
});

// Filtros por categoria
document.querySelectorAll('.filter-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
        var filter = this.getAttribute('data-filter');
        var items = document.querySelectorAll('.course-item');

        items.forEach(function(item) {
            if (filter === 'all' || item.getAttribute('data-category') === filter) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });
});

// Campo de busca para filtrar cursos por nome
document.getElementById('search').addEventListener('input', function() {
    var searchQuery = this.value.toLowerCase();
    var items = document.querySelectorAll('.course-item');

    items.forEach(function(item) {
        var title = item.querySelector('.card-title').textContent.toLowerCase();
        if (title.includes(searchQuery)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
});
