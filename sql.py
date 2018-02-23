import pyodbc


def sr(sqlreq):
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=10.120.52.101;'
                          'DATABASE=Patio;'
                          'UID=it;'
                          'PWD=it').cursor().execute(sqlreq)


ord_sql = 'SELECT LV_Order.ord_CustomerOrderCode,' \
          'LV_Order.ord_StatusID,' \
          'CAST(dbo.F_P_PickedQtyPC(LV_Order.ord_ID) / dbo.F_P_OrderQTY(LV_Order.ord_ID) * 100 AS int),' \
          'LV_Shipment.shp_Code ' \
          'FROM LV_Order INNER JOIN ' \
          'LV_OrderShipment ON LV_Order.ord_ID = LV_OrderShipment.ost_OrderID INNER JOIN ' \
          'LV_Shipment ON LV_OrderShipment.ost_ShipmentID = LV_Shipment.shp_ID ' \
          'WHERE  LV_Shipment.shp_ID = (' \
          'SELECT TOP 1 LV_OrderShipment.ost_ShipmentID ' \
          'FROM   LV_Order INNER JOIN ' \
          'LV_OrderShipment ON LV_Order.ord_ID = LV_OrderShipment.ost_OrderID ' \
          'WHERE LV_Order.ord_CustomerOrderCode = \'%s\' AND LV_Order.ord_DepositorID = %d)'
