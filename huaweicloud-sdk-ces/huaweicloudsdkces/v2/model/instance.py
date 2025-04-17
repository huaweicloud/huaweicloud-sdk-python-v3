# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Instance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_name': 'str',
        'logical_operator': 'str',
        'instance_names': 'list[ResourceNameItem]'
    }

    attribute_map = {
        'product_name': 'product_name',
        'logical_operator': 'logical_operator',
        'instance_names': 'instance_names'
    }

    def __init__(self, product_name=None, logical_operator=None, instance_names=None):
        r"""Instance

        The model defined in huaweicloud sdk

        :param product_name: 云产品名称
        :type product_name: str
        :param logical_operator: 逻辑运算符  ALL 所有条件匹配成功  ANY 任意条件匹配成功 
        :type logical_operator: str
        :param instance_names: 资源名称匹配参数数组
        :type instance_names: list[:class:`huaweicloudsdkces.v2.ResourceNameItem`]
        """
        
        

        self._product_name = None
        self._logical_operator = None
        self._instance_names = None
        self.discriminator = None

        self.product_name = product_name
        self.logical_operator = logical_operator
        self.instance_names = instance_names

    @property
    def product_name(self):
        r"""Gets the product_name of this Instance.

        云产品名称

        :return: The product_name of this Instance.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this Instance.

        云产品名称

        :param product_name: The product_name of this Instance.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def logical_operator(self):
        r"""Gets the logical_operator of this Instance.

        逻辑运算符  ALL 所有条件匹配成功  ANY 任意条件匹配成功 

        :return: The logical_operator of this Instance.
        :rtype: str
        """
        return self._logical_operator

    @logical_operator.setter
    def logical_operator(self, logical_operator):
        r"""Sets the logical_operator of this Instance.

        逻辑运算符  ALL 所有条件匹配成功  ANY 任意条件匹配成功 

        :param logical_operator: The logical_operator of this Instance.
        :type logical_operator: str
        """
        self._logical_operator = logical_operator

    @property
    def instance_names(self):
        r"""Gets the instance_names of this Instance.

        资源名称匹配参数数组

        :return: The instance_names of this Instance.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceNameItem`]
        """
        return self._instance_names

    @instance_names.setter
    def instance_names(self, instance_names):
        r"""Sets the instance_names of this Instance.

        资源名称匹配参数数组

        :param instance_names: The instance_names of this Instance.
        :type instance_names: list[:class:`huaweicloudsdkces.v2.ResourceNameItem`]
        """
        self._instance_names = instance_names

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
        if not isinstance(other, Instance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
