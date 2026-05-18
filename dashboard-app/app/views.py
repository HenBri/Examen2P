from flask_appbuilder import BaseView, ModelView, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface

from .extensions import appbuilder, db
from .models import Categoria, Producto, Venta


class CategoriaModelView(ModelView):
    datamodel = SQLAInterface(Categoria)
    base_title = "Categorías"
    list_title = "Lista de Categorías"
    show_title = "Detalle de Categoría"
    add_title = "Nueva Categoría"
    edit_title = "Editar Categoría"

    label_columns = {
        "nombre": "Nombre de Categoría",
        "descripcion": "Descripción",
        "imagen": "Imagen Referencial",
        "estado": "Activo / Disponible",
        "creado_en": "Fecha de Creación",
        "actualizado_en": "Última Actualización",
    }
    formatters_columns = {
        "creado_en": lambda x: x.strftime("%d/%m/%Y %H:%M") if x else "",
        "actualizado_en": lambda x: x.strftime("%d/%m/%Y %H:%M") if x else "",
    }
    list_columns = ["nombre", "descripcion", "estado", "creado_en"]
    add_columns = ["nombre", "descripcion", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "imagen", "estado", "creado_en", "actualizado_en"]


class ProductoModelView(ModelView):
    datamodel = SQLAInterface(Producto)
    base_title = "Productos"
    list_title = "Catálogo de Productos"
    show_title = "Ficha Técnica del Producto"
    add_title = "Registrar Producto"
    edit_title = "Modificar Producto"

    label_columns = {
        "nombre": "Nombre del Producto",
        "descripcion": "Descripción General",
        "precio": "Precio Unitario",
        "categorias": "Categoría Asignada",
        "imagen": "Fotografía / Imagen",
        "estado": "En Stock / Disponible",
        "creado_en": "Fecha de Registro",
        "actualizado_en": "Última Modificación",
    }
    formatters_columns = {
        "creado_en": lambda x: x.strftime("%d/%m/%Y %H:%M") if x else "",
        "actualizado_en": lambda x: x.strftime("%d/%m/%Y %H:%M") if x else "",
        "precio": lambda x: f"{x:,.2f} Bs." if x is not None else "",
    }
    list_columns = ["nombre", "precio", "categorias", "estado"]
    add_columns = ["nombre", "descripcion", "precio", "categorias", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "precio", "categorias", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "precio", "categorias", "imagen", "estado", "creado_en", "actualizado_en"]


class VentaModelView(ModelView):
    datamodel = SQLAInterface(Venta)
    base_title = "Registro de Ventas"
    list_title = "Historial de Transacciones"
    show_title = "Detalle de la Venta"
    add_title = "Registrar Nueva Venta"
    edit_title = "Modificar Registro de Venta"

    label_columns = {
        "producto": "Producto Vendido",
        "cantidad": "Cantidad (Unid.)",
        "precio_unitario": "Precio Unitario",
        "total": "Monto Total",
        "fecha": "Fecha de Venta",
    }
    formatters_columns = {
        "fecha": lambda x: x.strftime("%d/%m/%Y %H:%M") if x else "",
        "precio_unitario": lambda x: f"{x:,.2f} Bs." if x is not None else "",
        "total": lambda x: f"{x:,.2f} Bs." if x is not None else "",
    }
    list_columns = ["producto", "cantidad", "precio_unitario", "total", "fecha"]
    add_columns = ["producto", "cantidad", "precio_unitario", "total"]
    edit_columns = ["producto", "cantidad", "precio_unitario", "total"]


# REPORTES
class ReporteView(BaseView):
    route_base = "/reportes"

    @expose("/")
    def index(self):
        total_ventas = db.session.query(Venta).count()
        total_ingresos = db.session.query(db.func.sum(Venta.total)).scalar() or 0
        venta_por_producto = (
            db.session.query(Venta.producto, db.func.sum(Venta.cantidad))
            .group_by(Venta.producto)
            .all()
        )
        return self.render_template(
            "reportes.html",
            t_ventas=total_ventas,
            t_ingresos=total_ingresos,
            venta_por_producto=venta_por_producto,
        )


appbuilder.add_view(
    CategoriaModelView,
    "Categorías",
    icon="fa-tags",
    category="Gestión de Inventario",
    category_icon="fa-cubes",
)

appbuilder.add_view(
    ProductoModelView,
    "Productos",
    icon="fa-cube",
    category="Gestión de Inventario",
    category_icon="fa-cubes",
)

appbuilder.add_view(
    VentaModelView,
    "Registro de Ventas",
    icon="fa-cart-plus",
    category="Ventas",
    category_icon="fa-shopping-cart",
)

appbuilder.add_view_no_menu(ReporteView())

appbuilder.add_link(
    "Reporte General",
    href="/reportes/",
    icon="fa-pie-chart",
    category="Reportes",
)