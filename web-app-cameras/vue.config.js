module.exports = {
  devServer: {
    proxy: {
      '^/api': {
        target: process.env.DEVSERVER_PROXY_TARGET,
        changeOrigin: true,
      },
    },
  },
};
