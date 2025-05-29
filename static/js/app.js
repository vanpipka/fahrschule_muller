// 'use strict';

document.addEventListener("DOMContentLoaded", function () {
  // ===================================
  // Полифил для метода forEach для NodeList (IE не читает forEach!)
  if (window.NodeList && !NodeList.prototype.forEach) {
    NodeList.prototype.forEach = function (callback, thisArg) {
      thisArg = thisArg || window;
      for (var i = 0; i < this.length; i++) {
        callback.call(thisArg, this[i], i, this);
      }
    };
  }

  // Как вычислить горизонтальную прокрутку
  const gorizontScroll = () => {

    if (window.innerWidth >= 320) {

      let docWidth = document.documentElement.offsetWidth;
      [].forEach.call(
        document.querySelectorAll('*'),
        function (el) {
          if (el.offsetWidth > docWidth) {
            console.log("выходит за пределы: " + el);
          }
        }
      );

    }

  };

  window.addEventListener('resize', gorizontScroll);
  // вычислить горизонтальную прокрутку



  const body = document.querySelector('.body');
  const header = body.querySelector('[data-js-header]');
  const burger = header.querySelector('[data-js-burger]');
  const burgerIcon = burger.querySelector('[data-js-icon-burger]');
  const headerNavigation = header.querySelector('[data-js-navigation]');
  const wtsBtn = header.querySelector('[data-js-wts]');
  const hoverBlocks = header.querySelectorAll('[data-js-header-hover]');


  const mobileWrapper = body.querySelector('[data-js-mobile-wrapper]');
  const mobileNav = mobileWrapper.querySelector('[data-js-mobile-nav]');
  const mobileNavFooter = mobileWrapper.querySelector('[data-js-mobile-footer]');

  const toggleMobileNav = () => {
    mobileWrapper.classList.toggle('active');
    burgerIcon.classList.toggle('active');
    body.classList.toggle('no-scroll');
  }
  const closeMobileNav = () => {
    mobileWrapper.classList.remove('active');
    burgerIcon.classList.remove('active');
    body.classList.remove('no-scroll');
  }

  // ======== Закрытие меню при изменении размера окна ===========
  const handleResize = () => {
    if (window.innerWidth >= 720) {
      closeMobileNav();
    }
  };
  window.addEventListener('resize', handleResize);
  // ======== Закрытие меню при изменении размера окна ===========

  // if (header) {
  // Мобильное меню
  if (burger) {
    // Открытие или закрытие меню
    burger.addEventListener('click', () => {
      toggleMobileNav();
    });
  }


  if (mobileWrapper) {
    // Копирование меню в мобильное
    mobileNav.innerHTML = headerNavigation.innerHTML;
    mobileNavFooter.innerHTML = wtsBtn.innerHTML;

    // Сбор mobileNavList после копирования!
    const mobileNavList = mobileWrapper.querySelectorAll('[data-js-menu-list]');

    if (mobileWrapper.querySelector('[data-js-menu-list]')) {
      // Открытие вложенного меню в мобильной версии
      mobileNavList.forEach(function (btn) {
        btn.addEventListener('click', function () {
          const content = btn.nextElementSibling;
          const isOpen = btn.classList.toggle('active');

          if (isOpen) {
            content.style.maxHeight = content.scrollHeight + 'px';
          } else {
            content.style.maxHeight = '0px';
          }

        })
      })
    }
  }

  // ===========Большое меню при наведении==============
  if (header.querySelector('[data-js-header-hover]')) {
    // Обходим каждый блок
    hoverBlocks.forEach(hoverBlock => {
      // Получаем кнопку в текущем блоке
      const btn = hoverBlock.querySelector('[data-js-header-btn]');

      // Получаем скрытый блок с информацией в текущем блоке
      const infoBlock = hoverBlock.querySelector('[data-js-header-info]');

      const showInfo = () => {
        infoBlock.classList.add('active');
        btn.classList.add('active');
      };

      const hideInfo = () => {
        infoBlock.classList.remove('active');
        btn.classList.remove('active');
      };

      // Показываем скрытый блок при наведении на блок
      hoverBlock.addEventListener('mouseenter', showInfo);
      // Скрываем скрытый блок при уходе мыши с блока
      hoverBlock.addEventListener('mouseleave', hideInfo);


      btn.addEventListener('click', () => {
        showInfo();
        closeMobileNav();
      });

      // Скрываем скрытый блок при клике вне блока
      document.addEventListener('click', (event) => {
        // Проверяем, является ли цель клика сам блок или его потомок
        if (!hoverBlock.contains(event.target)) {
          // Если нет, то скрываем скрытый блок
          hideInfo();
        }
      });

    });
  }

  // }

  // Закрытие выпадающего большого меню
  const hoverBlockClose = () => {
    hoverBlocks.forEach(hoverBlock => {
      const btn = hoverBlock.querySelector('[data-js-header-btn]');
      const infoBlock = hoverBlock.querySelector('[data-js-header-info]');
      infoBlock.classList.remove('active');
      btn.classList.remove('active');
    });
  }
  // ===========Большое меню при наведении==============

  // Фиксация меню при скролле =====================

  // const header = document.querySelector('.header');

  $(window).scroll(function () {
    if ($(this).scrollTop() > 1800) {
      $(header).addClass('fixed');
    } else {
      $(header).removeClass('fixed');
    }
  });


  // ===============// Модалки //=============
  if (body.querySelector('[data-js-modal-target]')) {

    const openModalTriggers = body.querySelectorAll('[data-js-modal-target]');

    openModalTriggers.forEach(function (modalTrigger) {
      modalTrigger.addEventListener('click', function (event) {
        event.preventDefault();

        const modalId = this.getAttribute('data-js-modal-target');
        const btnDesc = this.getAttribute('data-js-desc');
        const btnTitle = this.getAttribute('data-js-title');

        // Модальное окно
        const modal = document.getElementById(modalId);
        const modalClose = modal.querySelector('[data-js-modal-close]');
        const modalSubTitle = modal.querySelector('[data-js-modal-subtitle]');
        const modalTitle = modal.querySelector('[data-js-modal-title]');

        // Форма
        const form = modal.querySelector('[data-js-form]');
        const inputFormName = form.querySelector('input[name="formName"]');

        // Проверяем, существует ли модальное окно
        if (modal) {
          // if (navMobileFix.classList.contains("active")) {
          // 	navMobileFix.classList.remove("active");
          // }
          if (header.querySelector('[data-js-header-hover]')) {
            hoverBlockClose();
          }

          modal.classList.add('active');
          body.classList.add('no-scroll');

          if (modalTitle) {
            modalTitle.innerHTML = btnTitle;
          }
          if (modalSubTitle) {
            modalSubTitle.innerHTML = btnDesc;
          }
          if (inputFormName) {
            inputFormName.value = btnTitle;
          }
        }

        function closeModal() {
          modal.classList.remove('active');
          body.classList.remove('no-scroll');
        }
        // Закрытие модального окна при клике на кнопку
        modalClose.addEventListener('click', function () {
          closeModal();
        });

        // Закрытие модального окна при клике вне его области
        window.addEventListener('click', function (event) {
          if (event.target === modal) {
            closeModal();
          }
        });

      })
    })

  }
  // ===============// Модалки //=============


  // ===============// Формы //=============
  // ================= Маска телефона и имени =================
  const mask = (dataValue, options) => {
    const elements = document.querySelectorAll(`[data-mask="${dataValue}"]`);
    if (!elements) return;

    elements.forEach(el => {
      IMask(el, options);
    });
  };

  // Маска для имени
  mask('name', {
    mask: /^[А-Яа-яA-Za-z\s'-]{1,25}$/,
    lazy: false
  });
  // Маска для номера телефона
  mask('phone', {
    mask: [
      '+{49} (000) 000-00-00',
      '+{49} (000) 000-0000',
      '+{49} (000) 0000000',
      '+{49} (000) 000000',
      '+{49} (000) 00000',
      '+{49} (000) 0000'  
    ],
    definitions: {
      '#': /[49]/
    },
    lazy: true,
    autoclear: false
  });
  
  // Маска для номера телефона Колеса Фортуны
  mask('wheel-phone', {
    mask: '+{7}(#00) 000-00-00',
    definitions: {
      '#': /[49]/
    },
    lazy: true,
    autoclear: false
  });
  
  // Отправка формы в телеграмм
  if (document.querySelector('[data-js-form]')) {

    // Функция отображения ошибок
    function displayError(inputElement, errorMessage) {
      const errorElement = document.createElement('div');
      errorElement.className = 'error';
      errorElement.textContent = errorMessage;
      errorElement.style.position = 'absolute';
      errorElement.style.bottom = '-24px';
      errorElement.style.color = 'red';
      errorElement.style.fontSize = '12px';
      errorElement.style.padding = '5px';
      inputElement.parentNode.style.position = 'relative';
      inputElement.parentNode.appendChild(errorElement);

      // Удаление ошибки при исправлении
      inputElement.addEventListener('input', function () {
        if (inputElement.value.trim() !== '') {
          errorElement.remove();
        }
      });
    }

    // Функция удаления ошибки при заполнении инпута
    function removeError(inputElement) {
      if (inputElement && inputElement.parentNode) { // Проверка на наличие inputElement и его родителя
        const error = inputElement.parentNode.querySelector('.error');
        if (error) {
          error.remove();
        }
      }
    }

    // Функция очистки ошибок
    function removeAllErrors(form) {
      const errors = form.querySelectorAll('.error');
      errors.forEach(error => {
        error.remove();
      });
    }


    const forms = document.querySelectorAll('[data-js-form]');
    for (let i = 0; i < forms.length; i++) {
      let form = forms[i];


      // Поднимаем LABEL в блоке с input
      const inputsForm = form.querySelectorAll('[data-js-input]');
      inputsForm.forEach(function (input) {
        console.log(input);
        const input_elmnt = input.closest('.input-container.input-container--inner')
           
        if (input_elmnt) {
          const label = input_elmnt.querySelector('.label');

          input.addEventListener('focus', function () {
            label.classList.add('label--active');
          });

          input.addEventListener('blur', function () {
            if (input.value.length === 0) {
              label.classList.remove('label--active');
            }
          });
        };
      })


      // ================= Выпадающий список =================
      const inputSelect = form.querySelectorAll('[data-js-select-block]');

      inputSelect.forEach(function (selectWrapper) {

        const selectInput = selectWrapper.querySelector('[data-js-input-select]');
        const selectList = selectWrapper.querySelector('[data-js-select-list]');
        const selectListItem = selectList.querySelectorAll('[data-js-select]');
        const selectHidden = selectWrapper.querySelector('[data-js-select-hidden]');

        selectInput.addEventListener('click', function () {
          selectList.classList.toggle('active');
        });

        selectListItem.forEach(function (listItem) {
          listItem.addEventListener('click', function (e) {
            e.stopPropagation();
            const selectedValue = this.getAttribute('data-js-select'); // Получаем значение атрибута data-js-select
            selectInput.innerText = this.innerText;
            selectInput.classList.add('active');
            selectHidden.value = selectedValue; // Присвоение значения скрытому инпуту
            removeError(selectHidden); // Убираем ошибку при выборе значения
            console.log('Выбран элемент:', this.innerText, 'Значение:', selectedValue); // Лог для проверки
            selectList.classList.remove('active');
          });
        });

        // Кликая снаружи - закрыть список
        document.addEventListener('click', function (e) {
          if (e.target !== selectInput) {
            selectList.classList.remove('active');
          }
        });

        // Нажатие на 'Tab' или 'Escape' - закрыть список
        document.addEventListener('keydown', function (e) {
          if (e.key === 'Tab' || e.key === 'Escape') {
            selectList.classList.remove('active');
          }
        });

      });
      // ================= Выпадающий список =================

      // ================= Валидация и отправка формы =================
      
      form.addEventListener('submit', function (event) {
        event.preventDefault();

        const submitButton = form.querySelector('button[type="submit"]');
        const inputName = form.querySelector('input[name="name"]');
        const inputPhone = form.querySelector('input[name="phone"]');
        const inputNameForm = form.querySelector('input[name="formName"]');
        const inputSocial = form.querySelector('input[name="social"]');
        const inputFill = form.querySelector('input[name="fill"]');
        const inputUrl = form.querySelector('input[name="url"]');
        const formMessage = form.querySelector('textarea[name="formMessage"]');

        // Значения value
        const inputNameValue = inputName.value.trim();
        const inputPhoneValue = inputPhone.value.trim();
        const inputNameFormValue = inputNameForm.value.trim();
        const inputFillValue = inputFill ? inputFill.value.trim() : ''; // Проверяем, есть ли поле
        const inputSocialValue = inputSocial ? inputSocial.value.trim() : ''; // Проверяем, есть ли поле
        const formMessageValue = formMessage ? formMessage.value.trim() : ''; // Проверяем, есть ли поле
        const inputUrlValue = inputUrl.value.trim();
        const connectionType = inputSocialValue ? inputSocialValue : 'Телефон'; // Значение по умолчанию
        // Очистить все ошибки
        removeAllErrors(form);

        // Проверка имени
        if (inputNameValue.length === 0) {
          displayError(inputName, 'Das Feld darf nicht leer sein');
        } else if (!/^[\sА-Яа-яA-Za-z'-]{2,20}$/.test(inputNameValue)) {
          displayError(inputName, 'Ungültiges Format');
        } else {
          removeError(inputName);
        }

        // Проверка телефона
        if (inputPhoneValue.length === 0) {
          displayError(inputPhone, 'Das Feld darf nicht leer sein');
        //} else if (!/^\+7\(\d{3}\)\s\d{3}-\d{2}-\d{2}$/.test(inputPhoneValue)) {
        //  displayError(inputPhone, 'Ungültiges Format');
        } else {
          removeError(inputPhone);
        }

        // Проверка поля "Способ связи", если оно существует
        if (inputSocial && inputSocialValue.length === 0) {
          displayError(inputSocial, 'Wählen Sie eine Verbindungsmethode aus');
        } else if (inputSocial) {
          removeError(inputSocial);
        }

        // Проверка наличия ошибок перед отправкой формы
        const errors = form.querySelectorAll('.error');

        if (errors.length === 0) {
          // Блокировка кнопки отправки
          submitButton.disabled = true;

          // Формируем сообщение для отправки в Telegram
          let message = `ФОРМА «<b>${inputNameFormValue}</b>»\n\n<b>Имя:</b> ${inputNameValue}\n<b>Телефон:</b> ${inputPhoneValue}\n`;
          
          // Добавляем поле филиала, если оно есть и заполнено
          if (inputFill && inputFillValue) {
            message += `<b>Филиал:</b> ${inputFillValue}\n`;
          }
          
          message += `<b>Страница сайта:</b> ${window.location.href}\n`;

          // Добавляем поле способа связи, если оно есть и заполнено
          
        if (inputSocial && inputSocialValue) {

            let cleanedPhone = inputPhoneValue.replace(/[\s()-]/g, '');        
            if (inputSocialValue === 'WhatsApp') {
              // Remove spaces, parentheses, and dashes from the phone number
              message += `\n<b>Способ связи:</b> по WhatsApp wa.me/${cleanedPhone}`;
            } else {
              message += `\n<b>Способ связи:</b> по телефону ${cleanedPhone}`;
            }
          }
          
          // Отправка данных в Telegram
          sendTelegramMessage(message);
        }

        // Функция отправки сообщения в Telegram
        function sendTelegramMessage(message) {

          console.log('Отправка сообщения в Telegram:', message);

          fetch("/anfrage/", {
            method: "POST",
            body: JSON.stringify(
                      {
                        url: window.location.href, 
                        name: inputNameValue, 
                        form: inputNameFormValue, 
                        phone: inputPhoneValue,
                        message: formMessageValue,
                        connection_type: connectionType
                      }
                    ),
            headers: {
              "Content-type": "application/json; charset=UTF-8",
              "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
          })
              .then(response => response.json())
              .then(data => {
                console.log(data.redirect_url);
                window.location.href = data.redirect_url; // Выполняем редирект
              })
              .catch(error => {
                console.error(error);
              })
              .finally(() => {
                  submitButton.disabled = false;
              });
          
          return;

        }


      });

    }
  }

  // ===============// Формы //=============


  // =====================
  // Табы
  if (document.querySelector("[data-tabs-section]")) {


    const tabSections = document.querySelectorAll("[data-tabs-section]");

    tabSections.forEach((section) => {
      const tabs = section.querySelectorAll("[data-tab]");
      const tabContents = section.querySelectorAll("[data-tab-content]");

      // Показываем первый контент при загрузке
      const firstContent = section.querySelector(".tabs-content.active");
      firstContent.style.display = "block";

      tabs.forEach((tab) => {
        tab.addEventListener("click", function () {
          const targetContent = tab.getAttribute("data-tab");

          // Удаляем класс 'active' у всех табов и содержимого
          tabs.forEach(t => t.classList.remove("active"));
          tabContents.forEach(content => {
            content.classList.remove("active");
            content.style.display = "none"; // Скрываем все содержимое
          });

          // Добавляем класс 'active' к выбранному табу и его содержимому
          tab.classList.add("active");
          const activeContent = section.querySelector(`[data-tab-content="${targetContent}"]`);
          activeContent.classList.add("active");
          activeContent.style.display = "block"; // Показываем выбранное содержимое
        });
      });
    });

  }
  // =====================


  // =======================================
  // Ищем все элементы с атрибутом data-js-accordion-btn
  const accordionBtns = document.querySelectorAll('[data-js-accordion-btn]');

  // Проходим по каждой кнопке
  accordionBtns.forEach(button => {
    button.addEventListener('click', () => {
      // Получаем значение атрибута data-js-accordion-btn
      const target = button.getAttribute('data-js-accordion-btn');

      // Ищем элемент с атрибутом data-js-accordion-content, соответствующим значению target
      const content = document.querySelector(`[data-js-accordion-content="${target}"]`);

      if (content) {
        // Если контент скрыт
        if (!content.classList.contains('active')) {
          // Устанавливаем высоту на auto, чтобы элемент занял свою полную высоту
          content.style.maxHeight = content.scrollHeight + "px";
          content.classList.add('active'); // Добавляем класс 'active'
        } else {
          // При повторном клике возвращаем высоту в 0 для плавного скрытия
          content.style.maxHeight = null;
          content.classList.remove('active'); // Убираем класс 'active'
        }
      }
    });
  });


  // ===========// АККОРДЕОН //===============
  if (document.querySelector('[data-js-faqs]')) {

    const accordions = document.querySelectorAll('[data-js-faqs]');

    // accordion.forEach
    accordions.forEach(accordion => {
      const headers = accordion.querySelectorAll('[data-js-faqs-header]');

      // headers.forEach
      headers.forEach(header => {

        // header.addEventListener
        header.addEventListener('click', () => {
          const currentActive = accordion.querySelector('[data-js-faqs-item][data-active="true"]');
          const clickedItem = header.parentElement;
          const content = clickedItem.querySelector('[data-js-faqs-content]');
          const isActive = clickedItem.getAttribute('data-active') === 'true';

          // Закрытие текущего активного элемента
          if (currentActive && currentActive !== clickedItem) {
            const currentContent = currentActive.querySelector('[data-js-faqs-content]');
            currentActive.setAttribute('data-active', 'false');
            currentContent.style.maxHeight = null;
          }

          // Открытие/закрытие нового элемента
          if (!isActive) {
            clickedItem.setAttribute('data-active', 'true');
            content.style.maxHeight = content.scrollHeight + 'px';

            // Добавляем задержку, чтобы контент успел раскрыться перед прокруткой
            setTimeout(() => {
              const newOffsetTop = clickedItem.getBoundingClientRect().top + window.scrollY;
              window.scrollTo({
                top: newOffsetTop - 120,
                behavior: 'smooth'
              });
            }, 200); // Задержка для корректной анимации
          } else {
            clickedItem.setAttribute('data-active', 'false');
            content.style.maxHeight = null;
          }
        });
        // header.addEventListener

      });
      // headers.forEach

    });
    // accordions.forEach
  }
  // ===========// АККОРДЕОН //===============



  // =============== Галерея ===============

  lightbox.option({
    'showImageNumberLabel': true,
    'imageFadeDuration': 100,
    'wrapAround': false, // остановка на последнем
    'disableScrolling': true
  })
  
  // =============// Форматирование цены //============
   
  if (document.querySelector("[data-js-num]")) {

    const priceNum = document.querySelectorAll('[data-js-num]');

    const formatPrice = price => {
      return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " ₽";
    };

    priceNum.forEach(function (element) {
      const price = parseInt(element.textContent, 10);
      if (!isNaN(price)) {
        element.textContent = formatPrice(price);
      }
    });
  }
  // =============// Форматирование цены //============

  // ===========// SWIPER //===============
  if (document.querySelector('[data-js-slider-hero-index]')) {
    let swiperIndex = new Swiper('[data-js-slider-hero-index]', {
      spaceBetween: 0,
      loop: true,
      centeredSlides: true,

      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      breakpoints: {
        1600: {
          slidesPerView: 1.4,
        },
        1024: {
          slidesPerView: 1.2,
        },
        320: {
          slidesPerView: 1,
          // spaceBetween: 0,
        }
      },
      keyboard: {
        enabled: false,
        onlyInViewport: true,
        pageUpDown: true,
      }
    });
  };

  // ===========// SWIPER //===============
  if (document.querySelector('[data-js-reviews]')) {
    let swiperIndex = new Swiper('[data-js-reviews]', {
      loop: true,
      grabCursor: true,
      centeredSlides: true,
      speed: 800,
      slidesPerView: 'auto',

      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      keyboard: {
        enabled: false,
        onlyInViewport: true,
        pageUpDown: true,
      },
    });
  };

  
  // ===========// SWIPER //===============



  // ==================// Видео галерея //=============
  if (document.querySelector('.video-section')) {
    const videoSection = document.querySelector('.video-section');
    const videoImg = videoSection.querySelectorAll('.video-img');

    for (const item of videoImg) {
      item.addEventListener('click', function () {
        console.log('клик');
        let videoLink = this.getAttribute('data-link');
        document.getElementById('video-slider').src = videoLink;

        videoSection.querySelectorAll('.video-img--open').forEach(tab => tab.classList.remove('video-img--open'));
        this.classList.add('video-img--open');
      });

    }
  }


  // Находим все элементы с data-js-review
  const reviews = document.querySelectorAll('[data-js-review]');

  reviews.forEach(function (review) {
    // Находим кнопку с data-js-modal-target="modal-review" внутри каждого отзыва
    // const button = review.querySelector('[data-js-rev-modal-target="modal-review"]');
    const button = review.querySelector('[data-js-rev-modal-target]');

    if (button) {
      button.addEventListener('click', function (event) {
        event.preventDefault();
        // Модальное окно
        const modalId = this.getAttribute('data-js-rev-modal-target');
        const modal = document.getElementById(modalId);
        const modalClose = modal.querySelector('[data-js-modal-close]');

        // Проверяем, существует ли модальное окно
        if (modal) {
          const body = document.querySelector('body');

          if (header.querySelector('[data-js-header-hover]')) {
            hoverBlockClose();
          }

          modal.classList.add('active');
          body.classList.add('no-scroll');

          // Находим элементы внутри текущего отзыва
          const name = review.querySelector('[data-js-review-name]').textContent;
          const date = review.querySelector('[data-js-review-date]').textContent;
          const text = review.querySelector('[data-js-review-text]').textContent;
          const agregator = review.querySelector('[data-js-review-agregator]');
          const agregatorHref = agregator.getAttribute('href');
          const agregatorText = agregator.getAttribute('data-js-review-agregator');

          // Находим элементы в модальном окне
          // const modal = document.getElementById('modal-review');
          const modalName = modal.querySelector('[data-js-review-name-modal]');
          const modalDate = modal.querySelector('[data-js-review-date-modal]');
          const modalText = modal.querySelector('[data-js-review-text-modal]');
          const modalAgregator = modal.querySelector('[data-js-review-agregator-modal]');

          // Копируем данные в модальное окно
          modalName.textContent = name;
          modalDate.textContent = date;
          modalText.textContent = text;
          modalAgregator.setAttribute('href', agregatorHref);
          modalAgregator.setAttribute('data-js-review-agregator-modal', agregatorText);
          // modalAgregator.textContent = agregatorText;

          modalClose.addEventListener('click', function () {
            closeModal();
          });

          // Закрытие модального окна при клике вне его области
          window.addEventListener('click', function (event) {
            if (event.target === modal) {
              closeModal();
            }
          });

          function closeModal() {
            modal.classList.remove('active');
            body.classList.remove('no-scroll');
          }
        }

      });
    }

  });


// =================== Последний день месяца ===================
if (document.querySelector(".lastday")) {

    // Получаем последний день месяца и форматируем дату
    const getLastDayOfMonth = (locale = 'ru') => {
      const date = new Date();
      const lastDayDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
      const lastDay = lastDayDate.toLocaleString(locale, { day: 'numeric' });

      const months = [
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
      ];

      const monthName = months[date.getMonth()];
      const year = date.getFullYear();

      return {
        dayAndMonth: `${lastDay} ${monthName}`,
        fullDate: `${lastDay} ${monthName} ${year}`
      };
    };

    // Обновляем текст в элементах с классом "lastday"
    const updateLastDayElements = () => {
      const { dayAndMonth } = getLastDayOfMonth();
      const elements = document.querySelectorAll(".lastday");

      elements.forEach(element => {
        element.innerText = dayAndMonth;
      });
    };

      // Вызываем функцию обновления элементов
  updateLastDayElements();
  }

  // ===================================
});
