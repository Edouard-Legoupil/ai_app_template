import axios from 'axios';

axios.defaults.baseURL = '/api/v1/';
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = 'Bearer ' + token;
  return config;
});

export async function login(username, password) {
  const {data} = await axios.post('login', {username, password});
  localStorage.setItem('token', data.token);
}
export async function signup(username, password) {
  const {data} = await axios.post('signup', {username, password});
  localStorage.setItem('token', data.token);
}

export async function fetchCollectiveContext() {
  const {data} = await axios.get('collective_context');
  return data;
}

export async function fetchPendingDecisions() {
  const {data} = await axios.get('decisions/pending');
  return data.decisions;
}

export async function submitDecision(decisionId, choice, rationale) {
  await axios.post(`decisions/${decisionId}/submit`, {choice, rationale});
}

export async function fetchRippleForecast(decisionId) {
  const {data} = await axios.get(`decisions/${decisionId}/ripple`);
  return data;
}

export async function fetchProcessStoryThread() {
  const {data} = await axios.get('process/thread');
  return data.events;
}
