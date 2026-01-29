# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Product:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'resource_size': 'int'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'resource_size': 'resource_size'
    }

    def __init__(self, resource_type=None, resource_spec_code=None, resource_size=None):
        r"""Product

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param resource_size: 订购数量
        :type resource_size: int
        """
        
        

        self._resource_type = None
        self._resource_spec_code = None
        self._resource_size = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_spec_code = resource_spec_code
        self.resource_size = resource_size

    @property
    def resource_type(self):
        r"""Gets the resource_type of this Product.

        资源类型

        :return: The resource_type of this Product.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this Product.

        资源类型

        :param resource_type: The resource_type of this Product.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this Product.

        资源规格编码

        :return: The resource_spec_code of this Product.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this Product.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this Product.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_size(self):
        r"""Gets the resource_size of this Product.

        订购数量

        :return: The resource_size of this Product.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this Product.

        订购数量

        :param resource_size: The resource_size of this Product.
        :type resource_size: int
        """
        self._resource_size = resource_size

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
