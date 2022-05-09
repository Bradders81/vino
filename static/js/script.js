document.addEventListener("DOMContentLoaded", () => {

        let = ctaBtn
        
        function callToActionWarning() {
        let ctaBtn = document.getElementById("btn-cta");
        ctaBtn.classList.remove("btn-danger");
        ctaBtn.classList.add("btn-warning");
    };

    function callToActionDanger() {
        let ctaBtn = document.getElementById("btn-cta");
        ctaBtn.classList.remove("btn-warning");
        ctaBtn.classList.add("btn-danger");
    }

    setInterval(callToActionWarning, 1000);

    setInterval(callToActionDanger, 2000);

});