# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductsCalculation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'normal_products_numbers': 'int',
        'gateway_products_numbers': 'int'
    }

    attribute_map = {
        'normal_products_numbers': 'normal_products_numbers',
        'gateway_products_numbers': 'gateway_products_numbers'
    }

    def __init__(self, normal_products_numbers=None, gateway_products_numbers=None):
        """ProductsCalculation

        The model defined in huaweicloud sdk

        :param normal_products_numbers: 普通产品数量
        :type normal_products_numbers: int
        :param gateway_products_numbers: 网关产品数量
        :type gateway_products_numbers: int
        """
        
        

        self._normal_products_numbers = None
        self._gateway_products_numbers = None
        self.discriminator = None

        if normal_products_numbers is not None:
            self.normal_products_numbers = normal_products_numbers
        if gateway_products_numbers is not None:
            self.gateway_products_numbers = gateway_products_numbers

    @property
    def normal_products_numbers(self):
        """Gets the normal_products_numbers of this ProductsCalculation.

        普通产品数量

        :return: The normal_products_numbers of this ProductsCalculation.
        :rtype: int
        """
        return self._normal_products_numbers

    @normal_products_numbers.setter
    def normal_products_numbers(self, normal_products_numbers):
        """Sets the normal_products_numbers of this ProductsCalculation.

        普通产品数量

        :param normal_products_numbers: The normal_products_numbers of this ProductsCalculation.
        :type normal_products_numbers: int
        """
        self._normal_products_numbers = normal_products_numbers

    @property
    def gateway_products_numbers(self):
        """Gets the gateway_products_numbers of this ProductsCalculation.

        网关产品数量

        :return: The gateway_products_numbers of this ProductsCalculation.
        :rtype: int
        """
        return self._gateway_products_numbers

    @gateway_products_numbers.setter
    def gateway_products_numbers(self, gateway_products_numbers):
        """Sets the gateway_products_numbers of this ProductsCalculation.

        网关产品数量

        :param gateway_products_numbers: The gateway_products_numbers of this ProductsCalculation.
        :type gateway_products_numbers: int
        """
        self._gateway_products_numbers = gateway_products_numbers

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
        if not isinstance(other, ProductsCalculation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
