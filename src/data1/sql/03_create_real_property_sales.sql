
DROP TABLE IF EXISTS real_property_sales;

-- Create a table real_proerty_sales data table\n",

CREATE TABLE real_property_sales
(ExciseTaxNbr INTEGER 
    ,Major CHAR (6)
    ,Minor CHAR (4)
    ,DocumentDate DATE
    ,SalePrice NUMERIC
    ,RecordingNumber CHAR (14)
    ,RecordingVolume CHAR (3)
    ,RecordingPage CHAR (3)
    ,PlatNbr CHAR (6)
    ,PlatType CHAR (1)
    ,PlatLot CHAR (14)
    ,PlatBlock CHAR (7)
    ,SellerName CHAR(300)
    ,BuyerName CHAR (300)
    ,PropertyType INTEGER
    ,PrincipalUse INTEGER
    ,SaleInstrument INTEGER
    ,ForestLand CHAR (1)
    ,CurrentUseLand CHAR (1)
    ,NonProfitUse CHAR (1)
    ,HistoricProperty CHAR (1)
    ,SaleReason INTEGER
    ,PropertyClass INTEGER
    ,SaleWarning CHAR (100)
    );