module.exports = {
  async redirects() {
    return [
      {
        source: "/",
        destination: "/gloves",
        permanent: true,
      },
    ];
  },
};
