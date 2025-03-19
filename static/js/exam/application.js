function ResizeView() {
    let mainHeaderContainer = document.getElementById('mainHeader');
    let headerBarContainer = document.getElementById('headerBar');
    let taskViewContainer = document.getElementById('taskView');
    let navigationViewContainer = document.getElementById('navigationView');

    console.log(window.innerHeight);
    if (taskViewContainer && window.innerWidth <= 765) {
        taskViewContainer.style.height = '100%';
    }
    else if (taskViewContainer && headerBarContainer && navigationViewContainer && mainHeaderContainer) {
        taskViewContainer.style.height = (window.innerHeight - mainHeaderContainer.offsetHeight - headerBarContainer.offsetHeight - navigationViewContainer.offsetHeight) + "px";
    }
    
}

// Запускаем код после загрузки страницы
$(document).ready(() => {
    $(window).on("resize", ResizeView);
    ResizeView(); // Вызываем при загрузке
});
