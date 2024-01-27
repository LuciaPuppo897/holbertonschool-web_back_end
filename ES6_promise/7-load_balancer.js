export default function loadBalancer(chinaDownload, USDowload) {
  return Promise.race([chinaDownload, USDowload])
    .then((val) => (val));
}
