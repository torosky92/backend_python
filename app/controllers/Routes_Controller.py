import string
from app import app, db
from app.models.Routes import Route
from app.utils.response import not_acceptable, success_request, not_found

class Routes_Controller():
    # BUSCAR PATENTE POR EL ID
    def get_patente(self, value):
        find_patente = Route.query.filter(Route.id == int(value)).first()
        if find_patente is not None:
            return success_request(find_patente.placa)
        ret = not_found('No se encontro patente')
        return ret

    # INGRESAR PATENTE
    def add_patente(self, value):
        patente = value.get('placa')
        app.logger.info(patente)
        app.logger.info(len(patente))
        patente_upper = ''
        correct = False
        if len(patente) == 7:
            for index, letter in enumerate(patente):
                app.logger.info(index)
                app.logger.info(str(letter).isalpha())
                app.logger.info(str(letter).isdigit())
                if index < 4:
                    if str(letter).isalpha():
                        app.logger.info('alfabeto')
                        app.logger.info(str(string.ascii_uppercase).find(str(letter).upper()))
                        if str(string.ascii_uppercase).find(str(letter).upper()) >= 0:
                            correct = True
                            patente_upper += str(letter).upper()
                else:
                    if str(letter).isdigit():
                        correct = True
                        patente_upper += str(letter)
        app.logger.info(patente_upper)
        
        if correct:
            find_placa = Route.query.filter(Route.placa.like(patente_upper)).first()
            if find_placa is not None:
                return not_acceptable(f'La Patente ya se ingreso el {find_placa.fecha} con el id {find_placa.id}')
            
            try:
                patentedb = Route(patente_upper)
                db.session.add(patentedb)
                db.session.commit()
                db.session.refresh(patentedb)
                patente_id = patentedb.id
                return success_request(patente_id)
            except Exception as e:
                db.session.rollback()
                app.logger.info(f'Error {e} agregando patente')
        return not_acceptable('No se ingreso patente')
        