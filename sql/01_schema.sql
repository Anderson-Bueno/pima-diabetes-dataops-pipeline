DROP TABLE IF EXISTS diabetes;

CREATE TABLE diabetes (
  Pregnancies INTEGER,
  Glucose INTEGER,
  BloodPressure INTEGER,
  SkinThickness INTEGER,
  Insulin INTEGER,
  BMI REAL,
  DiabetesPedigreeFunction REAL,
  Age INTEGER,
  Outcome INTEGER
);

DROP TABLE IF EXISTS pacientes;

CREATE TABLE pacientes AS
SELECT *
FROM diabetes
WHERE 1 = 0;
