// Filtros por categoria
document.querySelectorAll('.filter-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
        var filter = this.getAttribute('data-filter');
        var items = document.querySelectorAll('.course-item');

        items.forEach(function(item) {
            var category = item.getAttribute('data-category');
            if (filter === 'all' || category === filter) {
                item.style.display = 'block'; // Mostra o item se ele corresponder à categoria
            } else {
                item.style.display = 'none';  // Esconde o item se ele não corresponder à categoria
            }
        });
    });
});

// Simula o clique no botão da categoria 'Humanas' quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.filter-btn[data-filter="humanas"]').click();
});
