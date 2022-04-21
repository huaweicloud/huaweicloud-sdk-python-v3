# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProductRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'name': 'str',
        'manufacturer_id': 'str',
        'manufacturer_name': 'str',
        'model': 'str',
        'product_type': 'int',
        'description': 'str',
        'protocol_type': 'int',
        'device_type': 'str',
        'template_id': 'int',
        'version': 'str',
        'data_format': 'int'
    }

    attribute_map = {
        'app_id': 'app_id',
        'name': 'name',
        'manufacturer_id': 'manufacturer_id',
        'manufacturer_name': 'manufacturer_name',
        'model': 'model',
        'product_type': 'product_type',
        'description': 'description',
        'protocol_type': 'protocol_type',
        'device_type': 'device_type',
        'template_id': 'template_id',
        'version': 'version',
        'data_format': 'data_format'
    }

    def __init__(self, app_id=None, name=None, manufacturer_id=None, manufacturer_name=None, model=None, product_type=None, description=None, protocol_type=None, device_type=None, template_id=None, version=None, data_format=None):
        """CreateProductRequestBody

        The model defined in huaweicloud sdk

        :param app_id: 应用ID
        :type app_id: str
        :param name: 产品名称，创建产品时租户内唯一，长度最大64，仅支持中文，英文字母，数字，下划线和中划线
        :type name: str
        :param manufacturer_id: 产品供应商ID
        :type manufacturer_id: str
        :param manufacturer_name: 厂商名称
        :type manufacturer_name: str
        :param model: 产品型号
        :type model: str
        :param product_type: 产品类型，0-普通产品(不支持子设备) 1-网关产品
        :type product_type: int
        :param description: 产品描述，长度0-200
        :type description: str
        :param protocol_type: 产品的协议类型 0-mqtt 2-modbus 4-opcua
        :type protocol_type: int
        :param device_type: 产品的设备类型（默认Default）
        :type device_type: str
        :param template_id: 关联产品模板ID（使用产品模板创建产品时使用，否则为空），自动向下取整
        :type template_id: int
        :param version: 模型版本
        :type version: str
        :param data_format: 产品的数据格式 0-JSON 1-USER_DEFINED
        :type data_format: int
        """
        
        

        self._app_id = None
        self._name = None
        self._manufacturer_id = None
        self._manufacturer_name = None
        self._model = None
        self._product_type = None
        self._description = None
        self._protocol_type = None
        self._device_type = None
        self._template_id = None
        self._version = None
        self._data_format = None
        self.discriminator = None

        self.app_id = app_id
        self.name = name
        self.manufacturer_id = manufacturer_id
        self.manufacturer_name = manufacturer_name
        self.model = model
        self.product_type = product_type
        if description is not None:
            self.description = description
        self.protocol_type = protocol_type
        if device_type is not None:
            self.device_type = device_type
        if template_id is not None:
            self.template_id = template_id
        if version is not None:
            self.version = version
        if data_format is not None:
            self.data_format = data_format

    @property
    def app_id(self):
        """Gets the app_id of this CreateProductRequestBody.

        应用ID

        :return: The app_id of this CreateProductRequestBody.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateProductRequestBody.

        应用ID

        :param app_id: The app_id of this CreateProductRequestBody.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def name(self):
        """Gets the name of this CreateProductRequestBody.

        产品名称，创建产品时租户内唯一，长度最大64，仅支持中文，英文字母，数字，下划线和中划线

        :return: The name of this CreateProductRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateProductRequestBody.

        产品名称，创建产品时租户内唯一，长度最大64，仅支持中文，英文字母，数字，下划线和中划线

        :param name: The name of this CreateProductRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def manufacturer_id(self):
        """Gets the manufacturer_id of this CreateProductRequestBody.

        产品供应商ID

        :return: The manufacturer_id of this CreateProductRequestBody.
        :rtype: str
        """
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        """Sets the manufacturer_id of this CreateProductRequestBody.

        产品供应商ID

        :param manufacturer_id: The manufacturer_id of this CreateProductRequestBody.
        :type manufacturer_id: str
        """
        self._manufacturer_id = manufacturer_id

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this CreateProductRequestBody.

        厂商名称

        :return: The manufacturer_name of this CreateProductRequestBody.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this CreateProductRequestBody.

        厂商名称

        :param manufacturer_name: The manufacturer_name of this CreateProductRequestBody.
        :type manufacturer_name: str
        """
        self._manufacturer_name = manufacturer_name

    @property
    def model(self):
        """Gets the model of this CreateProductRequestBody.

        产品型号

        :return: The model of this CreateProductRequestBody.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this CreateProductRequestBody.

        产品型号

        :param model: The model of this CreateProductRequestBody.
        :type model: str
        """
        self._model = model

    @property
    def product_type(self):
        """Gets the product_type of this CreateProductRequestBody.

        产品类型，0-普通产品(不支持子设备) 1-网关产品

        :return: The product_type of this CreateProductRequestBody.
        :rtype: int
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this CreateProductRequestBody.

        产品类型，0-普通产品(不支持子设备) 1-网关产品

        :param product_type: The product_type of this CreateProductRequestBody.
        :type product_type: int
        """
        self._product_type = product_type

    @property
    def description(self):
        """Gets the description of this CreateProductRequestBody.

        产品描述，长度0-200

        :return: The description of this CreateProductRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateProductRequestBody.

        产品描述，长度0-200

        :param description: The description of this CreateProductRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def protocol_type(self):
        """Gets the protocol_type of this CreateProductRequestBody.

        产品的协议类型 0-mqtt 2-modbus 4-opcua

        :return: The protocol_type of this CreateProductRequestBody.
        :rtype: int
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this CreateProductRequestBody.

        产品的协议类型 0-mqtt 2-modbus 4-opcua

        :param protocol_type: The protocol_type of this CreateProductRequestBody.
        :type protocol_type: int
        """
        self._protocol_type = protocol_type

    @property
    def device_type(self):
        """Gets the device_type of this CreateProductRequestBody.

        产品的设备类型（默认Default）

        :return: The device_type of this CreateProductRequestBody.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this CreateProductRequestBody.

        产品的设备类型（默认Default）

        :param device_type: The device_type of this CreateProductRequestBody.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def template_id(self):
        """Gets the template_id of this CreateProductRequestBody.

        关联产品模板ID（使用产品模板创建产品时使用，否则为空），自动向下取整

        :return: The template_id of this CreateProductRequestBody.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateProductRequestBody.

        关联产品模板ID（使用产品模板创建产品时使用，否则为空），自动向下取整

        :param template_id: The template_id of this CreateProductRequestBody.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def version(self):
        """Gets the version of this CreateProductRequestBody.

        模型版本

        :return: The version of this CreateProductRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateProductRequestBody.

        模型版本

        :param version: The version of this CreateProductRequestBody.
        :type version: str
        """
        self._version = version

    @property
    def data_format(self):
        """Gets the data_format of this CreateProductRequestBody.

        产品的数据格式 0-JSON 1-USER_DEFINED

        :return: The data_format of this CreateProductRequestBody.
        :rtype: int
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this CreateProductRequestBody.

        产品的数据格式 0-JSON 1-USER_DEFINED

        :param data_format: The data_format of this CreateProductRequestBody.
        :type data_format: int
        """
        self._data_format = data_format

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
        if not isinstance(other, CreateProductRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
