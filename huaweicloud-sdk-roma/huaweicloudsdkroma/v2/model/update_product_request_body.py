# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProductRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'manufacturer_id': 'str',
        'manufacturer_name': 'str',
        'model': 'str',
        'device_type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'manufacturer_id': 'manufacturer_id',
        'manufacturer_name': 'manufacturer_name',
        'model': 'model',
        'device_type': 'device_type',
        'version': 'version'
    }

    def __init__(self, name=None, description=None, manufacturer_id=None, manufacturer_name=None, model=None, device_type=None, version=None):
        r"""UpdateProductRequestBody

        The model defined in huaweicloud sdk

        :param name: 产品名称，创建产品时租户内唯一，长度1-64，仅支持中文，英文字母，数字，下划线和中划线
        :type name: str
        :param description: 产品描述，长度0-200
        :type description: str
        :param manufacturer_id: 产品供应商ID，支持英文大小写，数字，下划线和中划线，长度2-50
        :type manufacturer_id: str
        :param manufacturer_name: 厂商名称，支持长度2-64
        :type manufacturer_name: str
        :param model: 产品型号，支持英文大小写，数字，下划线，中划线和空格(首尾空格会被忽略)，长度2-50
        :type model: str
        :param device_type: 产品的设备类型（默认Default Type）
        :type device_type: str
        :param version: 模型版本
        :type version: str
        """
        
        

        self._name = None
        self._description = None
        self._manufacturer_id = None
        self._manufacturer_name = None
        self._model = None
        self._device_type = None
        self._version = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.manufacturer_id = manufacturer_id
        self.manufacturer_name = manufacturer_name
        self.model = model
        self.device_type = device_type
        if version is not None:
            self.version = version

    @property
    def name(self):
        r"""Gets the name of this UpdateProductRequestBody.

        产品名称，创建产品时租户内唯一，长度1-64，仅支持中文，英文字母，数字，下划线和中划线

        :return: The name of this UpdateProductRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateProductRequestBody.

        产品名称，创建产品时租户内唯一，长度1-64，仅支持中文，英文字母，数字，下划线和中划线

        :param name: The name of this UpdateProductRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateProductRequestBody.

        产品描述，长度0-200

        :return: The description of this UpdateProductRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateProductRequestBody.

        产品描述，长度0-200

        :param description: The description of this UpdateProductRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def manufacturer_id(self):
        r"""Gets the manufacturer_id of this UpdateProductRequestBody.

        产品供应商ID，支持英文大小写，数字，下划线和中划线，长度2-50

        :return: The manufacturer_id of this UpdateProductRequestBody.
        :rtype: str
        """
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        r"""Sets the manufacturer_id of this UpdateProductRequestBody.

        产品供应商ID，支持英文大小写，数字，下划线和中划线，长度2-50

        :param manufacturer_id: The manufacturer_id of this UpdateProductRequestBody.
        :type manufacturer_id: str
        """
        self._manufacturer_id = manufacturer_id

    @property
    def manufacturer_name(self):
        r"""Gets the manufacturer_name of this UpdateProductRequestBody.

        厂商名称，支持长度2-64

        :return: The manufacturer_name of this UpdateProductRequestBody.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        r"""Sets the manufacturer_name of this UpdateProductRequestBody.

        厂商名称，支持长度2-64

        :param manufacturer_name: The manufacturer_name of this UpdateProductRequestBody.
        :type manufacturer_name: str
        """
        self._manufacturer_name = manufacturer_name

    @property
    def model(self):
        r"""Gets the model of this UpdateProductRequestBody.

        产品型号，支持英文大小写，数字，下划线，中划线和空格(首尾空格会被忽略)，长度2-50

        :return: The model of this UpdateProductRequestBody.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this UpdateProductRequestBody.

        产品型号，支持英文大小写，数字，下划线，中划线和空格(首尾空格会被忽略)，长度2-50

        :param model: The model of this UpdateProductRequestBody.
        :type model: str
        """
        self._model = model

    @property
    def device_type(self):
        r"""Gets the device_type of this UpdateProductRequestBody.

        产品的设备类型（默认Default Type）

        :return: The device_type of this UpdateProductRequestBody.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        r"""Sets the device_type of this UpdateProductRequestBody.

        产品的设备类型（默认Default Type）

        :param device_type: The device_type of this UpdateProductRequestBody.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def version(self):
        r"""Gets the version of this UpdateProductRequestBody.

        模型版本

        :return: The version of this UpdateProductRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateProductRequestBody.

        模型版本

        :param version: The version of this UpdateProductRequestBody.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, UpdateProductRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
