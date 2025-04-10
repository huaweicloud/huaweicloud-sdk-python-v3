# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyVehicleRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'imei': 'str',
        'brand': 'str',
        'model': 'str',
        'style': 'str',
        'fuel_type': 'str',
        'color': 'str',
        'plate_color': 'str',
        'access_type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'imei': 'imei',
        'brand': 'brand',
        'model': 'model',
        'style': 'style',
        'fuel_type': 'fuel_type',
        'color': 'color',
        'plate_color': 'plate_color',
        'access_type': 'access_type',
        'description': 'description'
    }

    def __init__(self, imei=None, brand=None, model=None, style=None, fuel_type=None, color=None, plate_color=None, access_type=None, description=None):
        r"""ModifyVehicleRequestDTO

        The model defined in huaweicloud sdk

        :param imei: **参数说明**：IMEI，OBU上电子序列号。  **取值范围**：长度最小1最大255，支持纯数字的组合。 
        :type imei: str
        :param brand: **参数说明**：车俩品牌。  **取值范围**：长度最小1最大64，支持中文、字母、数字、下划线（_）、横杠（-）的组合。 
        :type brand: str
        :param model: **参数说明**：车牌型号。  **取值范围**：长度最小1最大64，支持字母、数字、下划线（_）、横杠（-）的组合。 
        :type model: str
        :param style: **参数说明**：车辆年款。  **取值范围**：长度最小1最大64，支持纯数字的组合。 
        :type style: str
        :param fuel_type: **参数说明**：定义车辆的燃料动力类。  **取值范围**： - unknownFuel：未知 - gasoline：汽油 - ethanol：乙醇 - diesel：柴油 - electric：电动 - hybrid：混合燃料类型 - hydrogen：氢气 - natGasLiquid：液化天然气 - natGasComp：压缩天然气 - propane：丙烷\&quot; 
        :type fuel_type: str
        :param color: **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - gray：灰色 - red：红色 - blue：蓝色 - yellow：黄色 - orange：橙色 - brown：棕色 - green：绿色 - purple：紫色 - cyan：青色 - pink：粉红色 - transparent：透明色 - other：其他 
        :type color: str
        :param plate_color: **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - blue：蓝色 - yellow：黄色 - green：绿色 
        :type plate_color: str
        :param access_type: **参数说明**：车辆接入网络的方式。  **取值范围**： - 5g - 4g - 3g - 2g - pc5Only - pc5And5g - pc5And4g - pc5And3g - pc5And2g 
        :type access_type: str
        :param description: **参数说明**：描述  **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合 
        :type description: str
        """
        
        

        self._imei = None
        self._brand = None
        self._model = None
        self._style = None
        self._fuel_type = None
        self._color = None
        self._plate_color = None
        self._access_type = None
        self._description = None
        self.discriminator = None

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
        if description is not None:
            self.description = description

    @property
    def imei(self):
        r"""Gets the imei of this ModifyVehicleRequestDTO.

        **参数说明**：IMEI，OBU上电子序列号。  **取值范围**：长度最小1最大255，支持纯数字的组合。 

        :return: The imei of this ModifyVehicleRequestDTO.
        :rtype: str
        """
        return self._imei

    @imei.setter
    def imei(self, imei):
        r"""Sets the imei of this ModifyVehicleRequestDTO.

        **参数说明**：IMEI，OBU上电子序列号。  **取值范围**：长度最小1最大255，支持纯数字的组合。 

        :param imei: The imei of this ModifyVehicleRequestDTO.
        :type imei: str
        """
        self._imei = imei

    @property
    def brand(self):
        r"""Gets the brand of this ModifyVehicleRequestDTO.

        **参数说明**：车俩品牌。  **取值范围**：长度最小1最大64，支持中文、字母、数字、下划线（_）、横杠（-）的组合。 

        :return: The brand of this ModifyVehicleRequestDTO.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        r"""Sets the brand of this ModifyVehicleRequestDTO.

        **参数说明**：车俩品牌。  **取值范围**：长度最小1最大64，支持中文、字母、数字、下划线（_）、横杠（-）的组合。 

        :param brand: The brand of this ModifyVehicleRequestDTO.
        :type brand: str
        """
        self._brand = brand

    @property
    def model(self):
        r"""Gets the model of this ModifyVehicleRequestDTO.

        **参数说明**：车牌型号。  **取值范围**：长度最小1最大64，支持字母、数字、下划线（_）、横杠（-）的组合。 

        :return: The model of this ModifyVehicleRequestDTO.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this ModifyVehicleRequestDTO.

        **参数说明**：车牌型号。  **取值范围**：长度最小1最大64，支持字母、数字、下划线（_）、横杠（-）的组合。 

        :param model: The model of this ModifyVehicleRequestDTO.
        :type model: str
        """
        self._model = model

    @property
    def style(self):
        r"""Gets the style of this ModifyVehicleRequestDTO.

        **参数说明**：车辆年款。  **取值范围**：长度最小1最大64，支持纯数字的组合。 

        :return: The style of this ModifyVehicleRequestDTO.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        r"""Sets the style of this ModifyVehicleRequestDTO.

        **参数说明**：车辆年款。  **取值范围**：长度最小1最大64，支持纯数字的组合。 

        :param style: The style of this ModifyVehicleRequestDTO.
        :type style: str
        """
        self._style = style

    @property
    def fuel_type(self):
        r"""Gets the fuel_type of this ModifyVehicleRequestDTO.

        **参数说明**：定义车辆的燃料动力类。  **取值范围**： - unknownFuel：未知 - gasoline：汽油 - ethanol：乙醇 - diesel：柴油 - electric：电动 - hybrid：混合燃料类型 - hydrogen：氢气 - natGasLiquid：液化天然气 - natGasComp：压缩天然气 - propane：丙烷\" 

        :return: The fuel_type of this ModifyVehicleRequestDTO.
        :rtype: str
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        r"""Sets the fuel_type of this ModifyVehicleRequestDTO.

        **参数说明**：定义车辆的燃料动力类。  **取值范围**： - unknownFuel：未知 - gasoline：汽油 - ethanol：乙醇 - diesel：柴油 - electric：电动 - hybrid：混合燃料类型 - hydrogen：氢气 - natGasLiquid：液化天然气 - natGasComp：压缩天然气 - propane：丙烷\" 

        :param fuel_type: The fuel_type of this ModifyVehicleRequestDTO.
        :type fuel_type: str
        """
        self._fuel_type = fuel_type

    @property
    def color(self):
        r"""Gets the color of this ModifyVehicleRequestDTO.

        **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - gray：灰色 - red：红色 - blue：蓝色 - yellow：黄色 - orange：橙色 - brown：棕色 - green：绿色 - purple：紫色 - cyan：青色 - pink：粉红色 - transparent：透明色 - other：其他 

        :return: The color of this ModifyVehicleRequestDTO.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this ModifyVehicleRequestDTO.

        **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - gray：灰色 - red：红色 - blue：蓝色 - yellow：黄色 - orange：橙色 - brown：棕色 - green：绿色 - purple：紫色 - cyan：青色 - pink：粉红色 - transparent：透明色 - other：其他 

        :param color: The color of this ModifyVehicleRequestDTO.
        :type color: str
        """
        self._color = color

    @property
    def plate_color(self):
        r"""Gets the plate_color of this ModifyVehicleRequestDTO.

        **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - blue：蓝色 - yellow：黄色 - green：绿色 

        :return: The plate_color of this ModifyVehicleRequestDTO.
        :rtype: str
        """
        return self._plate_color

    @plate_color.setter
    def plate_color(self, plate_color):
        r"""Sets the plate_color of this ModifyVehicleRequestDTO.

        **参数说明**：车辆颜色。  **取值范围**： - black：黑色 - white：白色 - blue：蓝色 - yellow：黄色 - green：绿色 

        :param plate_color: The plate_color of this ModifyVehicleRequestDTO.
        :type plate_color: str
        """
        self._plate_color = plate_color

    @property
    def access_type(self):
        r"""Gets the access_type of this ModifyVehicleRequestDTO.

        **参数说明**：车辆接入网络的方式。  **取值范围**： - 5g - 4g - 3g - 2g - pc5Only - pc5And5g - pc5And4g - pc5And3g - pc5And2g 

        :return: The access_type of this ModifyVehicleRequestDTO.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        r"""Sets the access_type of this ModifyVehicleRequestDTO.

        **参数说明**：车辆接入网络的方式。  **取值范围**： - 5g - 4g - 3g - 2g - pc5Only - pc5And5g - pc5And4g - pc5And3g - pc5And2g 

        :param access_type: The access_type of this ModifyVehicleRequestDTO.
        :type access_type: str
        """
        self._access_type = access_type

    @property
    def description(self):
        r"""Gets the description of this ModifyVehicleRequestDTO.

        **参数说明**：描述  **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合 

        :return: The description of this ModifyVehicleRequestDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModifyVehicleRequestDTO.

        **参数说明**：描述  **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合 

        :param description: The description of this ModifyVehicleRequestDTO.
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
        if not isinstance(other, ModifyVehicleRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
