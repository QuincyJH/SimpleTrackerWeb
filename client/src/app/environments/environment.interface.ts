export class EnvironmentVariable {
  api_domain: ApiDomain;

  constructor(init: EnvironmentVariable) {
    Object.assign(this, init);
    this.api_domain = ApiDomain.LOCALHOST;
  }
}

export enum ApiDomain {
  LOCALHOST = 'http://localhost:8000',
  // PRODUCTION = 'https://api.example.com',
  // STAGING = 'https://staging-api.example.com',
  // DEVELOPMENT = 'https://dev-api.example.com'
}
