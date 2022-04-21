# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequestParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'parameter_name': 'str',
        'parameter_value': 'str'
    }

    attribute_map = {
        'parameter_name': 'parameter_name',
        'parameter_value': 'parameter_value'
    }

    def __init__(self, parameter_name=None, parameter_value=None):
        """RequestParameter

        The model defined in huaweicloud sdk

        :param parameter_name: 请求参数名
        :type parameter_name: str
        :param parameter_value: 请求参数值
        :type parameter_value: str
        """
        
        

        self._parameter_name = None
        self._parameter_value = None
        self.discriminator = None

        if parameter_name is not None:
            self.parameter_name = parameter_name
        if parameter_value is not None:
            self.parameter_value = parameter_value

    @property
    def parameter_name(self):
        """Gets the parameter_name of this RequestParameter.

        请求参数名

        :return: The parameter_name of this RequestParameter.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this RequestParameter.

        请求参数名

        :param parameter_name: The parameter_name of this RequestParameter.
        :type parameter_name: str
        """
        self._parameter_name = parameter_name

    @property
    def parameter_value(self):
        """Gets the parameter_value of this RequestParameter.

        请求参数值

        :return: The parameter_value of this RequestParameter.
        :rtype: str
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value):
        """Sets the parameter_value of this RequestParameter.

        请求参数值

        :param parameter_value: The parameter_value of this RequestParameter.
        :type parameter_value: str
        """
        self._parameter_value = parameter_value

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
        if not isinstance(other, RequestParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
