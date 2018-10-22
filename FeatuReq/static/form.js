class Form {
  constructor(node) {
    let self = this;
    self.form = node && node.nodeType === 1 ? node : document.getElementById(node + "");
    if (self.form.nodeName != "FORM") {
      throw ("Object is not a form element!");
    }
    self.headers = new Headers({ 'Content-Type': 'application/json' });
    self.onsubmit();
  }
  reset() {
    this.form.reset();
    this.form.action = this.form.dataset.defaultAction;
    this.form.method = this.form.dataset.defaultMethod;
  }
  onsubmit() {
    let self = this;
    self.form.addEventListener("submit", e => {
      e.preventDefault();
      let callback;      
      let method = self.form.getAttribute('method');
      switch (method) {
        case "PUT":
          callback = self.onPut;
          break;
        default:
          callback = self.onPost;
      }
      self.submit()
        .then(callback)
        .catch(error => {
          alert(`Unable to submit the form:\n ${error}`);
        });
    });
  }
  submit() {
    let self = this;
    return new Promise((resolve, reject) => {
      if (self.form.checkValidity()) {
        let request = new Request(`${self.form.action}`,
          {
            method: self.form.getAttribute('method'),
            headers: self.headers,
            body: self.JSON()
          });
        fetch(request)
          .then((response) => {
            if (!response.ok) {
              throw new Error(`Server responded with ${response.status}`)
            }
            let contentType = response.headers.get("content-type");
            if (contentType && contentType.includes("application/json")) {
              self.reset();
              resolve(response.json());
            } else {
              throw new TypeError("Oops, we haven't got JSON!");
            }
          })
          .catch(reject);
        return;
      }
      reject("One or more field values are invalid!");
    });
  }
  setter(name, value) {
    let element = this.form.querySelector(`[name="${name}"]`);
    if (element.type == 'checkbox' || element.type == 'radio') {
      element.checked = value;
    } else {
      this.form.querySelector(`[name="${name}"]`).value = value;
    }
  }
  getter(name) {
    let element = this.form.querySelector(`[name="${name}"]`);
    return (element.type == 'checkbox' || element.type == 'radio') ? element.checked : element.value;
  }
  fromObj(obj) {
    for (let element of this.form.elements) {
      let name = element.getAttribute("name");
      if (!name) {
        continue;
      }
      if (!(name in obj)) {
        continue;
      }
      let value = obj[name];
      if (element.type == 'checkbox' || element.type == 'radio') {
        element.checked = value;
      } else {
        this.form.querySelector(`[name="${name}"]`).value = value;
      }
    }
  }
  fromJSON(json){
    this.fromObj(JSON.parse(json));
  }
  obj() {
    let out = {};
    for (let element of this.form.elements) {
      let name = element.getAttribute("name");
      if (name) {
        out[name] = (element.type == 'checkbox' || element.type == 'radio') ? element.checked : element.value;
      }
    }
    return out;
  }
  JSON() {
    return JSON.stringify(this.obj());
  }
}



