# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StaticParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'para_name': 'str',
        'para_value': 'str'
    }

    attribute_map = {
        'para_name': 'para_name',
        'para_value': 'para_value'
    }

    def __init__(self, para_name=None, para_value=None):
        """StaticParam

        The model defined in huaweicloud sdk

        :param para_name: 静态参数名
        :type para_name: str
        :param para_value: 静态参数值
        :type para_value: str
        """
        
        

        self._para_name = None
        self._para_value = None
        self.discriminator = None

        if para_name is not None:
            self.para_name = para_name
        if para_value is not None:
            self.para_value = para_value

    @property
    def para_name(self):
        """Gets the para_name of this StaticParam.

        静态参数名

        :return: The para_name of this StaticParam.
        :rtype: str
        """
        return self._para_name

    @para_name.setter
    def para_name(self, para_name):
        """Sets the para_name of this StaticParam.

        静态参数名

        :param para_name: The para_name of this StaticParam.
        :type para_name: str
        """
        self._para_name = para_name

    @property
    def para_value(self):
        """Gets the para_value of this StaticParam.

        静态参数值

        :return: The para_value of this StaticParam.
        :rtype: str
        """
        return self._para_value

    @para_value.setter
    def para_value(self, para_value):
        """Sets the para_value of this StaticParam.

        静态参数值

        :param para_value: The para_value of this StaticParam.
        :type para_value: str
        """
        self._para_value = para_value

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
        if not isinstance(other, StaticParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
