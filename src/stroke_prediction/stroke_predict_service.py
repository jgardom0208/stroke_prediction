def predict_single(patient, dv, model):
    X = dv.transform([patient])
    y_pred = model.predict_proba(X)[:, 1]
    stroke = y_pred[0] >= 0.5
    return bool(stroke), float(y_pred[0])