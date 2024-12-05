from db.connection import session
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from modules.materia_prima.controller import registrar_materia_prima, controlar_inventario, gestor_inventario, responsable_compras
from modules.materia_prima.model import MateriaPrima
from modules.produccion.model import Produccion
from modules.produccion.controller import  iniciar_nueva_produccion, obtener_estado_produccion, generar_informe_produccion, finalizar_produccion, gestor_produccion, responsable_produccion
from modules.producto.controller import registrar_producto, controlar_inventario_productos, retirar_producto, actualizar_producto, deshacer_ultima_accion
from modules.pedido.controller import recibir_pedido, monitorear_pedidos, obtener_pedidos
from patterns.creacionales.singleton.singleton import GestorDeInventario
from patterns.creacionales.abstract_factory.fabricas import FabricaConjuntoInvierno, FabricaConjuntoVerano, crear_conjunto


app = Flask(__name__)
app.secret_key = 'fire'
gestor_inventario = GestorDeInventario()
gestor_inventario = GestorDeInventario.get_instance()

@app.route('/')
def index():
    return render_template('index.html')

# Rutas para Materia Prima
@app.route('/materia_prima', methods=['GET', 'POST'])
def materia_prima():
    editar_id = request.args.get('editar_id', None, type=int)

    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        cantidad = request.form['cantidad']
        punto_reorden = request.form['punto_reorden']
        proveedor = request.form['proveedor']
        fecha_adquisicion = request.form['fecha_adquisicion']
        registrar_materia_prima(nombre, descripcion, cantidad, punto_reorden, proveedor, fecha_adquisicion)

    inventario = gestor_inventario.obtener_inventario_materias_primas()
    return render_template('materia_prima.html', inventario=inventario, editar_id=editar_id)

# Rutas para Producción
@app.route('/produccion', methods=['GET', 'POST'])
def produccion():
    if request.method == 'POST':
        tipo_producto = request.form['tipo_producto']
        cantidad_producida = int(request.form['cantidad_producida'])
        mensaje = iniciar_nueva_produccion(tipo_producto, cantidad_producida)
        return render_template('produccion.html', mensaje=mensaje, producciones=obtener_estado_produccion())

    producciones = obtener_estado_produccion()
    informe = generar_informe_produccion()
    return render_template('produccion.html', producciones=producciones, informe=informe)

@app.route('/finalizar_produccion/<int:id_produccion>', methods=['POST'])
def finalizar_produccion_route(id_produccion):
    nombre_producto = request.form['nombre_producto']
    descripcion = request.form['descripcion']
    cantidad = int(request.form['cantidad_final'])
    mensaje = finalizar_produccion(id_produccion, nombre_producto, descripcion, cantidad)
    return redirect(url_for('produccion', mensaje=mensaje))

# Rutas para Productos Terminados
@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        cantidad = request.form['cantidad']
        fecha_produccion = request.form['fecha_produccion']
        id_produccion = request.form['id_produccion']
        mensaje = registrar_producto(nombre, descripcion, cantidad, fecha_produccion, id_produccion)
        flash(mensaje)

    productos_terminados = controlar_inventario_productos()
    return render_template('productos.html', productos=productos_terminados)

@app.route('/retirar_producto/<int:producto_id>', methods=['POST'])
def retirar_producto_route(producto_id):
    mensaje = retirar_producto(producto_id)
    flash(mensaje)
    return redirect(url_for('productos'))

@app.route('/actualizar_producto/<int:producto_id>', methods=['POST'])
def actualizar_producto_route(producto_id):
    nuevos_datos = {
        'nombre': request.form['nombre'],
        'descripcion': request.form['descripcion'],
        'cantidadDisponible': request.form['cantidad'],
        'fechaProduccion': request.form['fecha_produccion']
    }
    mensaje = actualizar_producto(producto_id, nuevos_datos)
    flash(mensaje)
    return redirect(url_for('productos'))

@app.route('/deshacer_accion', methods=['POST'])
def deshacer_accion():
    mensaje = deshacer_ultima_accion()
    flash(mensaje)
    return redirect(url_for('productos'))
# Rutas para Pedidos
@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    if request.method == 'POST':
        cliente_name = request.form['cliente_name']
        fecha_pedido = request.form['fecha_pedido']
        estado = request.form['estado']
        direccion_envio = request.form.get('direccion_envio', '')  # Asumiendo que se agregó este campo
        tipo_distribucion = request.form['tipo_distribucion']
        producto = request.form['producto']
        cantidad = int(request.form['cantidad'])

        mensaje_distribucion = recibir_pedido(cliente_name, fecha_pedido, estado, direccion_envio, tipo_distribucion, producto, cantidad)
        flash(mensaje_distribucion)  # Asumiendo que se usa Flask's flash para mensajes

    pedidos_list = obtener_pedidos()
    return render_template('pedidos.html', pedidos=pedidos_list)

@app.route('/conjunto', methods=['GET', 'POST'])
def conjunto_route():
    conjunto = None
    if request.method == 'POST':
        tipo_conjunto = request.form['tipo_conjunto']
        if tipo_conjunto == 'invierno':
            fabrica = FabricaConjuntoInvierno()
        else:
            fabrica = FabricaConjuntoVerano()
        
        conjunto = crear_conjunto(fabrica)
    
    return render_template('conjunto.html', conjunto=conjunto)

@app.route('/notificaciones')
def obtener_notificaciones():
    notificaciones_compras = responsable_compras.obtener_notificaciones()
    notificaciones_produccion = responsable_produccion.obtener_notificaciones()
    return jsonify({
        'compras': notificaciones_compras,
        'produccion': notificaciones_produccion
    })


@app.route('/editar_materia_prima/<int:id>', methods=['POST'])
def editar_materia_prima(id):
    materia = session.query(MateriaPrima).get(id)
    materia.nombre = request.form['nombre']
    materia.descripcion = request.form['descripcion']
    materia.cantidadDisponible = request.form['cantidad']
    materia.puntoDeReorden = request.form['punto_reorden']
    materia.proveedor = request.form['proveedor']
    materia.fechaAdquisicion = request.form['fecha_adquisicion']
    
    session.commit()
    flash('Materia prima actualizada exitosamente.')
    return redirect(url_for('materia_prima'))


@app.route('/inventario_combinado')
def inventario_combinado():
    inventario_materias_primas = gestor_inventario.obtener_inventario_materias_primas()
    inventario_productos = gestor_inventario.obtener_inventario_productos()
    return render_template('inventario_combinado.html', materias_primas=inventario_materias_primas, productos=inventario_productos)


if __name__ == '__main__':
    app.run(debug=True)