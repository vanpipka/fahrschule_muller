function ResizeView() {
    let mainHeaderContainer = document.getElementById('mainHeader');
    let headerBarContainer = document.getElementById('headerBar');
    let taskViewContainer = document.getElementById('taskView');
    let navigationViewContainer = document.getElementById('navigationView');
    
    let height = 0;
    
    if (taskViewContainer && headerBarContainer && navigationViewContainer && mainHeaderContainer) {
        height = (window.innerHeight - mainHeaderContainer.offsetHeight - headerBarContainer.offsetHeight - navigationViewContainer.offsetHeight);
    }
    
    if (height === 0) { return }
    
    taskViewContainer.style.minHeight = height + "px";
    
}

// Запускаем код после загрузки страницы
$(document).ready(() => {
    $(window).on("resize", ResizeView);
    ResizeView(); // Вызываем при загрузке
});
