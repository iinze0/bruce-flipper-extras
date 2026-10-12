document.addEventListener('DOMContentLoaded', () => {
  const toggles = document.querySelectorAll('.category-toggle');
  toggles.forEach(toggle => {
    toggle.addEventListener('change', () => {
      const group = toggle.closest('.group');
      group.querySelectorAll('.file-checkbox').forEach(cb => cb.checked = toggle.checked);
    });
  });
});
