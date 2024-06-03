const LOAD_PURCHASES = "purchases/loadPurchases";
const ADD_PURCHASE = "purchases/addPurchase";
const DELETE_PURCHASE = "purchase/deletePurchase";

const loadPurchases = (purchases) => ({
  type: LOAD_PURCHASES,
  purchases,
});
const addPurchase = (purchase) => ({
  type: ADD_PURCHASE,
  purchase,
});
const deletePurchase = (purchaseId) => ({
  type: DELETE_PURCHASE,
  purchaseId,
});

export const thunkLoadUserPurchases = () => async (dispatch) => {
  const response = await fetch(`/api/user_purchases`);

  if (response.ok) {
    const data = await response.json();
    return dispatch(loadPurchases(data));
  } else {
    const errors = await response.json();
    console.log({ errors });
    return;
  }
};
export const thunkEditPurchase = (purchase) => async (dispatch) => {
  const response = await fetch(`/api/user_purchases/${purchase.id}/edit`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: purchase.userId,
      vehicle_id: purchase.vehicleId,
      first_name: purchase.firstName,
      last_name: purchase.lastName,
      delivery_address: purchase.deliveryAddress,
      finalized: purchase.finalized,
    }),
  });

  console.log({ response, purchase });

  if (response.ok) {
    const data = await response.json();
    return dispatch(addPurchase(data));
  } else {
    const errors = await response.json();
    console.log({ errors });
    return;
  }
};

const initialState = {};

const userPurchasesReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD_PURCHASES: {
      const newState = { ...state };
      action.purchases.forEach((purchase) => {
        newState[purchase.id] = purchase;
      });
      return newState;
    }
    case ADD_PURCHASE: {
      const newState = { ...state };
      newState[action.purchase.id] = action.purchase;
      return newState;
    }
    default: {
      return state;
    }
  }
};

export default userPurchasesReducer;
