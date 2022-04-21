# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductReferer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'product_id': 'int',
        'product_name': 'str',
        'manufacturer_id': 'str',
        'model': 'str',
        'protocol_type': 'int',
        'product_type': 'int'
    }

    attribute_map = {
        'product_id': 'product_id',
        'product_name': 'product_name',
        'manufacturer_id': 'manufacturer_id',
        'model': 'model',
        'protocol_type': 'protocol_type',
        'product_type': 'product_type'
    }

    def __init__(self, product_id=None, product_name=None, manufacturer_id=None, model=None, protocol_type=None, product_type=None):
        """ProductReferer

        The model defined in huaweicloud sdk

        :param product_id: 产品ID，未填写厂商ID+型号时产品ID必填
        :type product_id: int
        :param product_name: 产品名称
        :type product_name: str
        :param manufacturer_id: 厂商ID，未填写产品ID时厂商ID和型号必填
        :type manufacturer_id: str
        :param model: 型号，未填写产品ID时厂商ID和型号必填
        :type model: str
        :param protocol_type: 产品的协议类型：0-mqtt，1-coap，2-modbus，3-http, 4-opcua
        :type protocol_type: int
        :param product_type: 产品类型：0-普通产品 1-网关产品
        :type product_type: int
        """
        
        

        self._product_id = None
        self._product_name = None
        self._manufacturer_id = None
        self._model = None
        self._protocol_type = None
        self._product_type = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if manufacturer_id is not None:
            self.manufacturer_id = manufacturer_id
        if model is not None:
            self.model = model
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if product_type is not None:
            self.product_type = product_type

    @property
    def product_id(self):
        """Gets the product_id of this ProductReferer.

        产品ID，未填写厂商ID+型号时产品ID必填

        :return: The product_id of this ProductReferer.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductReferer.

        产品ID，未填写厂商ID+型号时产品ID必填

        :param product_id: The product_id of this ProductReferer.
        :type product_id: int
        """
        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this ProductReferer.

        产品名称

        :return: The product_name of this ProductReferer.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ProductReferer.

        产品名称

        :param product_name: The product_name of this ProductReferer.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def manufacturer_id(self):
        """Gets the manufacturer_id of this ProductReferer.

        厂商ID，未填写产品ID时厂商ID和型号必填

        :return: The manufacturer_id of this ProductReferer.
        :rtype: str
        """
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        """Sets the manufacturer_id of this ProductReferer.

        厂商ID，未填写产品ID时厂商ID和型号必填

        :param manufacturer_id: The manufacturer_id of this ProductReferer.
        :type manufacturer_id: str
        """
        self._manufacturer_id = manufacturer_id

    @property
    def model(self):
        """Gets the model of this ProductReferer.

        型号，未填写产品ID时厂商ID和型号必填

        :return: The model of this ProductReferer.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ProductReferer.

        型号，未填写产品ID时厂商ID和型号必填

        :param model: The model of this ProductReferer.
        :type model: str
        """
        self._model = model

    @property
    def protocol_type(self):
        """Gets the protocol_type of this ProductReferer.

        产品的协议类型：0-mqtt，1-coap，2-modbus，3-http, 4-opcua

        :return: The protocol_type of this ProductReferer.
        :rtype: int
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this ProductReferer.

        产品的协议类型：0-mqtt，1-coap，2-modbus，3-http, 4-opcua

        :param protocol_type: The protocol_type of this ProductReferer.
        :type protocol_type: int
        """
        self._protocol_type = protocol_type

    @property
    def product_type(self):
        """Gets the product_type of this ProductReferer.

        产品类型：0-普通产品 1-网关产品

        :return: The product_type of this ProductReferer.
        :rtype: int
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ProductReferer.

        产品类型：0-普通产品 1-网关产品

        :param product_type: The product_type of this ProductReferer.
        :type product_type: int
        """
        self._product_type = product_type

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
        if not isinstance(other, ProductReferer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
