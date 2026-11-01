/* 904 외주작업 — 공용 로직 (홈페이지 데모 + Apps Script 서버가 같이 씀)
   역할별로 보이는 데이터는 여기서 서버 쪽에서 걸러서 내려보냄. */
var Core = (function () {
  var A = 'abcdefghjkmnpqrstuvwxyz23456789';
  function uid(n) { var s = ''; for (var i = 0; i < n; i++) s += A.charAt(Math.floor(Math.random() * A.length)); return s; }
  function now() { return new Date().toISOString(); }
  function find(arr, k, v) { for (var i = 0; i < arr.length; i++) if (arr[i][k] === v) return arr[i]; return null; }
  function err(m) { var e = new Error(m); e.user = true; throw e; }
  function pick(o, keys) { var r = {}; keys.forEach(function (k) { if (o[k] !== undefined) r[k] = o[k]; }); return r; }
  function tok(S) { var t; do { t = uid(7); } while (find(S.sites, 'cTok', t) || find(S.jobs, 'wTok', t)); return t; }
  function str(v, n) { return String(v == null ? '' : v).slice(0, n || 2000); }

  var SITE_F = ['name', 'addr', 'unit', 'pw', 'cname', 'cphone', 'memo'];
  var JOB_F = ['siteId', 'proc', 'loc', 'date', 'time', 'content', 'vendor', 'vphone', 'est', 'final', 'showC', 'status', 'memo', 'days'];
  var STATUSES = ['예정', '완료보고', '결제요청', '정산완료'];
  /* 공정별 기본 일수 (완성도 계산용). 작업마다 따로 고칠 수 있음 */
  var DAYS = { '철거': 1, '액방': 1, '액체방수': 1, '도막': 1, '도막 1차': 1, '도막 2차': 1, '타일': 4, '도기': 1, '도기 세팅': 1, '돔': 1, '돔천장': 1 };
  function jobDays(j) { var d = parseFloat(j.days); if (d > 0) return d; return DAYS[String(j.proc || '').trim()] || 1; }
  /* 완성도: 완료 공정은 일수 전부, 여러 날 공정은 지난 날만큼 (보고 전까지 마지막 날은 안 셈) */
  function progress(jobs, today) {
    var total = 0, done = 0;
    jobs.forEach(function (j) {
      var d = jobDays(j); total += d;
      if (j.done || (j.status && j.status !== '예정')) { done += d; return; }
      if (d > 1 && j.date && today) {
        var el = Math.floor((Date.parse(today) - Date.parse(j.date)) / 864e5);
        done += Math.max(0, Math.min(d - 1, el));
      }
    });
    return { total: total, done: done, pct: total ? Math.round(done / total * 100) : 0 };
  }

  function files(list) {
    return (Array.isArray(list) ? list : []).slice(0, 40).filter(function (f) { return f && f.id; })
      .map(function (f) { return { id: String(f.id), type: f.type === 'v' ? 'v' : 'i' }; });
  }
  function addPost(S, p) {
    var post = { id: uid(9), siteId: p.siteId, jobId: p.jobId || '', from: p.from, to: p.to || '', kind: p.kind,
      text: str(p.text), files: files(p.files), amount: p.amount || '', at: now(), read: p.from === 'admin' };
    S.posts.push(post); return post;
  }
  var KIND = { done: '작업 완료', ask: '문의', issue: '문제', pay: '결제요청', reply: '답변', note: '메시지' };

  /* ---------- 작업자 ---------- */
  function wJob(S, t) { var j = t && find(S.jobs, 'wTok', String(t)); if (!j) err('링크가 맞지 않거나 삭제된 작업이에요'); return j; }
  function workerView(S, t) {
    var j = wJob(S, t), s = find(S.sites, 'id', j.siteId) || {};
    return {
      job: pick(j, ['proc', 'loc', 'date', 'time', 'content', 'vendor', 'est', 'final', 'status']),
      site: pick(s, ['name', 'addr', 'unit', 'pw']),
      posts: S.posts.filter(function (p) { return p.jobId === j.id && (p.from === 'worker' || (p.from === 'admin' && p.to === 'worker')); })
        .map(function (p) { return pick(p, ['id', 'from', 'kind', 'text', 'files', 'amount', 'at']); })
    };
  }
  function workerPost(S, t, q) {
    var j = wJob(S, t), s = find(S.sites, 'id', j.siteId) || {};
    var kind = ({ done: 1, ask: 1, issue: 1, pay: 1 })[q.kind] ? q.kind : 'ask';
    if (kind === 'done' && !files(q.files).length) err('완료 사진을 1장 이상 올려 주세요');
    if ((kind === 'ask' || kind === 'issue') && !str(q.text).trim() && !files(q.files).length) err('내용을 적어 주세요');
    var amount = '';
    if (kind === 'pay') { amount = String(q.amount || '').replace(/[^0-9]/g, ''); if (!amount) err('최종 금액을 적어 주세요'); j.final = amount; j.status = '결제요청'; }
    if (kind === 'done' && j.status === '예정') j.status = '완료보고';
    var p = addPost(S, { siteId: j.siteId, jobId: j.id, from: 'worker', kind: kind, text: q.text, files: q.files, amount: amount });
    return { write: true, data: workerView(S, t),
      notify: { subject: '[904 외주] ' + KIND[kind] + ' · ' + (s.name || '') + ' · ' + (j.proc || ''),
        body: (j.vendor || '작업자') + ' → ' + KIND[kind] + '\n현장: ' + (s.name || '') + '\n공정: ' + (j.proc || '') + ' ' + (j.loc || '') +
          (amount ? '\n최종 금액: ' + Number(amount).toLocaleString() + '원' : '') + '\n사진/영상: ' + p.files.length + '개\n\n' + (p.text || '') } };
  }

  /* ---------- 소비자 ---------- */
  function cSite(S, t) { var s = t && find(S.sites, 'cTok', String(t)); if (!s) err('링크가 맞지 않거나 삭제된 현장이에요'); return s; }
  function customerView(S, t) {
    var s = cSite(S, t);
    var jobs = S.jobs.filter(function (j) { return j.siteId === s.id; })
      .sort(function (a, b) { return String(a.date).localeCompare(String(b.date)); })
      .map(function (j) {
        var ph = [];
        if (j.showC) S.posts.forEach(function (p) { if (p.jobId === j.id && p.from === 'worker' && p.kind === 'done') ph = ph.concat(p.files); });
        return { proc: j.proc, loc: j.loc, date: j.date, days: jobDays(j), done: j.status !== '예정', files: ph };
      });
    return {
      site: { name: s.name, cname: s.cname }, jobs: jobs,
      posts: S.posts.filter(function (p) { return p.siteId === s.id && !p.jobId && (p.from === 'customer' || (p.from === 'admin' && p.to === 'customer')); })
        .map(function (p) { return pick(p, ['id', 'from', 'kind', 'text', 'files', 'at']); })
    };
  }
  function customerPost(S, t, q) {
    var s = cSite(S, t);
    if (!str(q.text).trim() && !files(q.files).length) err('내용을 적어 주세요');
    var p = addPost(S, { siteId: s.id, from: 'customer', kind: q.kind === 'issue' ? 'issue' : 'ask', text: q.text, files: q.files });
    return { write: true, data: customerView(S, t),
      notify: { subject: '[904 소비자] ' + KIND[p.kind] + ' · ' + (s.name || ''), body: (s.cname || '소비자') + '님 ' + KIND[p.kind] + '\n현장: ' + (s.name || '') + '\n\n' + p.text } };
  }

  /* ---------- 관리자 ---------- */
  function saveSite(S, d) {
    var s = d.id ? find(S.sites, 'id', d.id) : null;
    if (!s) { s = { id: uid(8), cTok: tok(S), at: now() }; S.sites.push(s); }
    SITE_F.forEach(function (k) { if (d[k] !== undefined) s[k] = str(d[k], 500); });
    if (!s.name) err('현장 이름을 적어 주세요');
    return s;
  }
  function saveJob(S, d) {
    var j = d.id ? find(S.jobs, 'id', d.id) : null;
    if (!j) { if (!find(S.sites, 'id', d.siteId)) err('현장을 찾을 수 없어요'); j = { id: uid(8), wTok: tok(S), status: '예정', at: now() }; S.jobs.push(j); }
    JOB_F.forEach(function (k) { if (d[k] !== undefined) j[k] = k === 'showC' ? !!d[k] : str(d[k], 2000); });
    if (STATUSES.indexOf(j.status) < 0) j.status = '예정';
    if (!j.proc) err('공정을 적어 주세요');
    return j;
  }
  function admin(S, q) {
    switch (q.a) {
      case 'all': return { data: S };
      case 'saveSite': saveSite(S, q.site || {}); return { write: true, data: S };
      case 'saveJob': saveJob(S, q.job || {}); return { write: true, data: S };
      case 'newTok': {
        if (q.siteId) { var s = find(S.sites, 'id', q.siteId); if (s) s.cTok = tok(S); }
        if (q.jobId) { var j = find(S.jobs, 'id', q.jobId); if (j) j.wTok = tok(S); }
        return { write: true, data: S };
      }
      case 'delSite':
        S.sites = S.sites.filter(function (s) { return s.id !== q.id; });
        S.jobs = S.jobs.filter(function (j) { return j.siteId !== q.id; });
        S.posts = S.posts.filter(function (p) { return p.siteId !== q.id; });
        return { write: true, data: S };
      case 'delJob':
        S.jobs = S.jobs.filter(function (j) { return j.id !== q.id; });
        S.posts = S.posts.filter(function (p) { return p.jobId !== q.id; });
        return { write: true, data: S };
      case 'reply': {
        var site = find(S.sites, 'id', q.siteId); if (!site) err('현장을 찾을 수 없어요');
        if (!str(q.text).trim() && !files(q.files).length) err('내용을 적어 주세요');
        addPost(S, { siteId: site.id, jobId: q.to === 'worker' ? q.jobId : '', from: 'admin', to: q.to === 'worker' ? 'worker' : 'customer', kind: 'reply', text: q.text, files: q.files });
        S.posts.forEach(function (p) { if (p.siteId === site.id && (q.to === 'worker' ? p.jobId === q.jobId : !p.jobId)) p.read = true; });
        return { write: true, data: S };
      }
      case 'read': {
        var ids = q.ids || []; S.posts.forEach(function (p) { if (ids.indexOf(p.id) >= 0) p.read = true; });
        return { write: true, data: S };
      }
    }
    err('알 수 없는 요청');
  }

  /* ---------- 진입점 ---------- */
  function handle(S, q, env) {
    S.sites = S.sites || []; S.jobs = S.jobs || []; S.posts = S.posts || [];
    switch (q.a) {
      case 'w': return { data: workerView(S, q.t) };
      case 'wPost': return workerPost(S, q.t, q);
      case 'c': return { data: customerView(S, q.t) };
      case 'cPost': return customerPost(S, q.t, q);
      case 'up': {
        var sid;
        if (q.t) { var j = find(S.jobs, 'wTok', String(q.t)), s = find(S.sites, 'cTok', String(q.t)); sid = j ? j.siteId : s ? s.id : null; }
        else if (env.adminPw && q.pw === env.adminPw) sid = q.siteId;
        if (!sid) err('올릴 권한이 없어요');
        var f = q.file || {}; if (!f.b64) err('파일이 비어 있어요');
        return { data: env.saveFile(sid, f) };
      }
    }
    if (!env.adminPw || q.pw !== env.adminPw) err('관리자 비밀번호가 맞지 않아요');
    return admin(S, q);
  }

  return { handle: handle, STATUSES: STATUSES, KIND: KIND, DAYS: DAYS, jobDays: jobDays, progress: progress };
})();
if (typeof module !== 'undefined') module.exports = Core;
