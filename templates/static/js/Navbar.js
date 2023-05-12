const nav = document.createElement('header')
nav.classList.add("top-bar")
nav.innerHTML = `
<div class="top-bar__content-wrapper">

    <a href="/" class="top-bar__logo-link"><img class="top-bar__logo" src="/static/img/logo.png" alt="Foresight Diagnostics Logo"></a>
    <nav class="main-nav">
    <nav class="main-menu">
    <ul class="main-menu__list">
    <li class="main-menu___list-item ">
    <a class="main-menu__list-item-link" href="/about">About</a>
    </li></ul></nav>

    <button class="hamburger hamburger--slider" type="button">
    <span class="hamburger-box">
        <span class="hamburger-inner"></span>
    </span>
    </button>



</nav>
</div>
`

document.body.prepend(nav)