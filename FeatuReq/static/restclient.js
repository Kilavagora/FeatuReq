(function (window) {
  class RestClient {
    constructor(endpoint) {
      this.endpoint = endpoint;
      this.headers = new Headers({ 'Content-Type': 'application/json' });
    }
    _request(request) {
      return new Promise((resolve, reject) => {
        fetch(request)
          .then((response) => {
            resolve(response.json());
          })
          .catch(reject);
      });
    }
    getAll(params) {
      let queryString = "";
      if (params) {
        queryString = Object.keys(params).map(k => `${encodeURIComponent(k)}=${encodeURIComponent(params[k])}`).join('&');
      }
      let request = new Request(`/${this.endpoint}/${queryString}`, { method: 'GET', headers: this.headers });
      return this._request(request);
    }
    post(body) {
      let request = new Request(`/${this.endpoint}/`, { method: 'POST', body: body, headers: this.headers });
      return this._request(request);
    }
    get(id) {
      let request = new Request(`/${this.endpoint}/${id}`, { method: 'GET', headers: this.headers });
      return this._request(request);
    }
    put(id, body) {
      let request = new Request(`/${this.endpoint}/${id}`, { method: 'PUT', body: body, headers: this.headers });
      return this._request(request);
    }
    delete(id) {
      let request = new Request(`/${this.endpoint}/${id}`, { method: 'DELETE', headers: this.headers });
      return this._request(request);
    }
  }
  this.RestClient = RestClient;
})(this);