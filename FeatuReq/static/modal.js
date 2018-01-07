class Modal {
  constructor(node) {
    let self = this;
    self.modal = node && node.nodeType === 1 ? node : document.getElementById(node + "");
    self.modal.addEventListener("click", e => {
      let el = e.target;
      if (el.dataset.dismiss == "modal") {
        e.preventDefault();        
        self.hide();
      }
    });

    let showModalButtons = document.querySelectorAll(`a[href="#${self.modal.id}"][data-toggle="modal"]`);
    for (let button of showModalButtons) {
      button.addEventListener("click", e => {
        e.preventDefault();
        self.show();
      });      
    }      

  }
  show() {
    this.modal.style.display = "block";
    this.onShow();
  }
  hide() {
    this.modal.style.display = "none";
    this.onHide();
  }
  onShow() {}
  onHide() {}
}

