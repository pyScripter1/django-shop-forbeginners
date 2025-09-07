// shop/static/shop/js/cart.js
document.addEventListener('DOMContentLoaded', function() {
    // Обновление количества товаров в корзине
    const quantityInputs = document.querySelectorAll('input[name="quantity"]');

    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            const form = this.closest('form');
            if (form) {
                form.submit();
            }
        });
    });

    // Подтверждение удаления из корзины
    const deleteButtons = document.querySelectorAll('form[action*="remove"]');

    deleteButtons.forEach(button => {
        button.addEventListener('submit', function(e) {
            if (!confirm('Вы уверены, что хотите удалить товар из корзины?')) {
                e.preventDefault();
            }
        });
    });

    // Анимация добавления в корзину
    const addToCartButtons = document.querySelectorAll('form[action*="add"]');

    addToCartButtons.forEach(button => {
        button.addEventListener('submit', function() {
            const btn = this.querySelector('button[type="submit"]');
            if (btn) {
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Добавляем...';
                btn.disabled = true;
            }
        });
    });
});