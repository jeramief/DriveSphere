const priceFormatter = (price) => {
  Intl.NumberFormat("en-us", {
    style: "currency",
    currency: "USD",
  }).format(price);
};

export { priceFormatter };
