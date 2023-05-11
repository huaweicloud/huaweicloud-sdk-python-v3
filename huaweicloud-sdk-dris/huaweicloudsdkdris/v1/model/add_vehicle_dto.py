# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddVehicleDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vehicle_id': 'str',
        'plate_no': 'str',
        'vin': 'str',
        'obu_id': 'str',
        'imei': 'str',
        'brand': 'str',
        'model': 'str',
        'style': 'str',
        'fuel_type': 'str',
        'color': 'str',
        'plate_color': 'str',
        'access_type': 'str',
        'secret': 'str',
        'description': 'str'
    }

    attribute_map = {
        'vehicle_id': 'vehicle_id',
        'plate_no': 'plate_no',
        'vin': 'vin',
        'obu_id': 'obu_id',
        'imei': 'imei',
        'brand': 'brand',
        'model': 'model',
        'style': 'style',
        'fuel_type': 'fuel_type',
        'color': 'color',
        'plate_color': 'plate_color',
        'access_type': 'access_type',
        'secret': 'secret',
        'description': 'description'
    }

    def __init__(self, vehicle_id=None, plate_no=None, vin=None, obu_id=None, imei=None, brand=None, model=None, style=None, fuel_type=None, color=None, plate_color=None, access_type=None, secret=None, description=None):
        """AddVehicleDTO

        The model defined in huaweicloud sdk

        :param vehicle_id: **参数说明**：车辆唯一标识符。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 
        :type vehicle_id: str
        :param plate_no: **参数说明**：车牌号。  **取值范围**：长度最小1最大64，支持中文、字母、数字、下划线（_）、横杠（-）的组合。 
        :type plate_no: str
        :param vin: **参数说明**：VIN码，车辆的17位VIN码。  **取值范围**：长度不超过17，只允许字母、数字字符的组合。 
        :type vin: str
        :param obu_id: **参数说明**：车载OBU的唯一标识。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 
        :type obu_id: str
        :param imei: **参数说明**：IMEI，OBU上电子序列号。  **取值范围**：长度最小1最大255，支持纯数字的组合。 
        :type imei: str
        :param brand: **参数说明**：车俩品牌。  **取值范围**：长度最小1最大64，支持中文、字母、数字、下划线（_）、横杠（-）的组合。 
        :type brand: str
        :param model: **参数说明**：车牌型号。  **取值范围**：长度最小1最大64，支持字母、数字、下划线（_）、横杠（-）的组合。 
        :type model: str
        :param style: **参数说明**：车辆年款。  **取值范围**：长度最小1最大64，支持纯数字的组合。 
        :type style: str
        :param fuel_type: **参数说明**：定义车辆的燃料动力类。  **取值范围**： - unknownFuel：未知 - gasoline：汽油 - ethanol：乙醇 - diesel：柴油 - electric：电动 - hybrid：混合燃料类型 - hydrogen：氢气 - natGasLiquid：液化天然气 - natGasComp：压缩天然气 - propane：丙烷 
        :type fuel_type: str
        :param color: **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - gray：灰色 - red：红色 - blue：蓝色 - yellow：黄色 - orange：橙色 - brown：棕色 - green：绿色 - purple：紫色 - cyan：青色 - pink：粉红色 - transparent：透明色 - other：其他 
        :type color: str
        :param plate_color: **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - blue：蓝色 - yellow：黄色 - green：绿色\&quot; 
        :type plate_color: str
        :param access_type: **参数说明**：车辆接入网络的方式。  **取值范围**： - 5g - 4g - 3g - 2g - pc5Only - pc5And5g - pc5And4g - pc5And3g - pc5And2g 
        :type access_type: str
        :param secret: **参数说明**：第三方车辆密钥，输入车辆型号ID后方可填写该字段以设置方车辆密码。
        :type secret: str
        :param description: **参数说明**：描述。  **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合 
        :type description: str
        """
        
        

        self._vehicle_id = None
        self._plate_no = None
        self._vin = None
        self._obu_id = None
        self._imei = None
        self._brand = None
        self._model = None
        self._style = None
        self._fuel_type = None
        self._color = None
        self._plate_color = None
        self._access_type = None
        self._secret = None
        self._description = None
        self.discriminator = None

        self.vehicle_id = vehicle_id
        if plate_no is not None:
            self.plate_no = plate_no
        if vin is not None:
            self.vin = vin
        if obu_id is not None:
            self.obu_id = obu_id
        if imei is not None:
            self.imei = imei
        if brand is not None:
            self.brand = brand
        if model is not None:
            self.model = model
        if style is not None:
            self.style = style
        if fuel_type is not None:
            self.fuel_type = fuel_type
        if color is not None:
            self.color = color
        if plate_color is not None:
            self.plate_color = plate_color
        if access_type is not None:
            self.access_type = access_type
        self.secret = secret
        if description is not None:
            self.description = description

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this AddVehicleDTO.

        **参数说明**：车辆唯一标识符。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 

        :return: The vehicle_id of this AddVehicleDTO.
        :rtype: str
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this AddVehicleDTO.

        **参数说明**：车辆唯一标识符。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 

        :param vehicle_id: The vehicle_id of this AddVehicleDTO.
        :type vehicle_id: str
        """
        self._vehicle_id = vehicle_id

    @property
    def plate_no(self):
        """Gets the plate_no of this AddVehicleDTO.

        **参数说明**：车牌号。  **取值范围**：长度最小1最大64，支持中文、字母、数字、下划线（_）、横杠（-）的组合。 

        :return: The plate_no of this AddVehicleDTO.
        :rtype: str
        """
        return self._plate_no

    @plate_no.setter
    def plate_no(self, plate_no):
        """Sets the plate_no of this AddVehicleDTO.

        **参数说明**：车牌号。  **取值范围**：长度最小1最大64，支持中文、字母、数字、下划线（_）、横杠（-）的组合。 

        :param plate_no: The plate_no of this AddVehicleDTO.
        :type plate_no: str
        """
        self._plate_no = plate_no

    @property
    def vin(self):
        """Gets the vin of this AddVehicleDTO.

        **参数说明**：VIN码，车辆的17位VIN码。  **取值范围**：长度不超过17，只允许字母、数字字符的组合。 

        :return: The vin of this AddVehicleDTO.
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this AddVehicleDTO.

        **参数说明**：VIN码，车辆的17位VIN码。  **取值范围**：长度不超过17，只允许字母、数字字符的组合。 

        :param vin: The vin of this AddVehicleDTO.
        :type vin: str
        """
        self._vin = vin

    @property
    def obu_id(self):
        """Gets the obu_id of this AddVehicleDTO.

        **参数说明**：车载OBU的唯一标识。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 

        :return: The obu_id of this AddVehicleDTO.
        :rtype: str
        """
        return self._obu_id

    @obu_id.setter
    def obu_id(self, obu_id):
        """Sets the obu_id of this AddVehicleDTO.

        **参数说明**：车载OBU的唯一标识。  **取值范围**：长度不超过128，只允许字母、数字、以及_-等字符的组合。 

        :param obu_id: The obu_id of this AddVehicleDTO.
        :type obu_id: str
        """
        self._obu_id = obu_id

    @property
    def imei(self):
        """Gets the imei of this AddVehicleDTO.

        **参数说明**：IMEI，OBU上电子序列号。  **取值范围**：长度最小1最大255，支持纯数字的组合。 

        :return: The imei of this AddVehicleDTO.
        :rtype: str
        """
        return self._imei

    @imei.setter
    def imei(self, imei):
        """Sets the imei of this AddVehicleDTO.

        **参数说明**：IMEI，OBU上电子序列号。  **取值范围**：长度最小1最大255，支持纯数字的组合。 

        :param imei: The imei of this AddVehicleDTO.
        :type imei: str
        """
        self._imei = imei

    @property
    def brand(self):
        """Gets the brand of this AddVehicleDTO.

        **参数说明**：车俩品牌。  **取值范围**：长度最小1最大64，支持中文、字母、数字、下划线（_）、横杠（-）的组合。 

        :return: The brand of this AddVehicleDTO.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this AddVehicleDTO.

        **参数说明**：车俩品牌。  **取值范围**：长度最小1最大64，支持中文、字母、数字、下划线（_）、横杠（-）的组合。 

        :param brand: The brand of this AddVehicleDTO.
        :type brand: str
        """
        self._brand = brand

    @property
    def model(self):
        """Gets the model of this AddVehicleDTO.

        **参数说明**：车牌型号。  **取值范围**：长度最小1最大64，支持字母、数字、下划线（_）、横杠（-）的组合。 

        :return: The model of this AddVehicleDTO.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this AddVehicleDTO.

        **参数说明**：车牌型号。  **取值范围**：长度最小1最大64，支持字母、数字、下划线（_）、横杠（-）的组合。 

        :param model: The model of this AddVehicleDTO.
        :type model: str
        """
        self._model = model

    @property
    def style(self):
        """Gets the style of this AddVehicleDTO.

        **参数说明**：车辆年款。  **取值范围**：长度最小1最大64，支持纯数字的组合。 

        :return: The style of this AddVehicleDTO.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this AddVehicleDTO.

        **参数说明**：车辆年款。  **取值范围**：长度最小1最大64，支持纯数字的组合。 

        :param style: The style of this AddVehicleDTO.
        :type style: str
        """
        self._style = style

    @property
    def fuel_type(self):
        """Gets the fuel_type of this AddVehicleDTO.

        **参数说明**：定义车辆的燃料动力类。  **取值范围**： - unknownFuel：未知 - gasoline：汽油 - ethanol：乙醇 - diesel：柴油 - electric：电动 - hybrid：混合燃料类型 - hydrogen：氢气 - natGasLiquid：液化天然气 - natGasComp：压缩天然气 - propane：丙烷 

        :return: The fuel_type of this AddVehicleDTO.
        :rtype: str
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        """Sets the fuel_type of this AddVehicleDTO.

        **参数说明**：定义车辆的燃料动力类。  **取值范围**： - unknownFuel：未知 - gasoline：汽油 - ethanol：乙醇 - diesel：柴油 - electric：电动 - hybrid：混合燃料类型 - hydrogen：氢气 - natGasLiquid：液化天然气 - natGasComp：压缩天然气 - propane：丙烷 

        :param fuel_type: The fuel_type of this AddVehicleDTO.
        :type fuel_type: str
        """
        self._fuel_type = fuel_type

    @property
    def color(self):
        """Gets the color of this AddVehicleDTO.

        **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - gray：灰色 - red：红色 - blue：蓝色 - yellow：黄色 - orange：橙色 - brown：棕色 - green：绿色 - purple：紫色 - cyan：青色 - pink：粉红色 - transparent：透明色 - other：其他 

        :return: The color of this AddVehicleDTO.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this AddVehicleDTO.

        **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - gray：灰色 - red：红色 - blue：蓝色 - yellow：黄色 - orange：橙色 - brown：棕色 - green：绿色 - purple：紫色 - cyan：青色 - pink：粉红色 - transparent：透明色 - other：其他 

        :param color: The color of this AddVehicleDTO.
        :type color: str
        """
        self._color = color

    @property
    def plate_color(self):
        """Gets the plate_color of this AddVehicleDTO.

        **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - blue：蓝色 - yellow：黄色 - green：绿色\" 

        :return: The plate_color of this AddVehicleDTO.
        :rtype: str
        """
        return self._plate_color

    @plate_color.setter
    def plate_color(self, plate_color):
        """Sets the plate_color of this AddVehicleDTO.

        **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - blue：蓝色 - yellow：黄色 - green：绿色\" 

        :param plate_color: The plate_color of this AddVehicleDTO.
        :type plate_color: str
        """
        self._plate_color = plate_color

    @property
    def access_type(self):
        """Gets the access_type of this AddVehicleDTO.

        **参数说明**：车辆接入网络的方式。  **取值范围**： - 5g - 4g - 3g - 2g - pc5Only - pc5And5g - pc5And4g - pc5And3g - pc5And2g 

        :return: The access_type of this AddVehicleDTO.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this AddVehicleDTO.

        **参数说明**：车辆接入网络的方式。  **取值范围**： - 5g - 4g - 3g - 2g - pc5Only - pc5And5g - pc5And4g - pc5And3g - pc5And2g 

        :param access_type: The access_type of this AddVehicleDTO.
        :type access_type: str
        """
        self._access_type = access_type

    @property
    def secret(self):
        """Gets the secret of this AddVehicleDTO.

        **参数说明**：第三方车辆密钥，输入车辆型号ID后方可填写该字段以设置方车辆密码。

        :return: The secret of this AddVehicleDTO.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this AddVehicleDTO.

        **参数说明**：第三方车辆密钥，输入车辆型号ID后方可填写该字段以设置方车辆密码。

        :param secret: The secret of this AddVehicleDTO.
        :type secret: str
        """
        self._secret = secret

    @property
    def description(self):
        """Gets the description of this AddVehicleDTO.

        **参数说明**：描述。  **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合 

        :return: The description of this AddVehicleDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddVehicleDTO.

        **参数说明**：描述。  **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合 

        :param description: The description of this AddVehicleDTO.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddVehicleDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
