DELETE FROM pacientes;

INSERT INTO pacientes
SELECT *
FROM diabetes
WHERE Age > 50;

ALTER TABLE pacientes ADD COLUMN Perfil TEXT;

UPDATE pacientes
SET Perfil = CASE
  WHEN BMI >= 30 THEN 'Obeso'
  ELSE 'Normal'
END;
