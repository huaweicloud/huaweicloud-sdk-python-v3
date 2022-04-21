# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobParam:

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
        'value': 'str',
        'param_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'param_type': 'paramType'
    }

    def __init__(self, name=None, value=None, param_type=None):
        """JobParam

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param value: 
        :type value: str
        :param param_type: 
        :type param_type: str
        """
        
        

        self._name = None
        self._value = None
        self._param_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if param_type is not None:
            self.param_type = param_type

    @property
    def name(self):
        """Gets the name of this JobParam.


        :return: The name of this JobParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobParam.


        :param name: The name of this JobParam.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this JobParam.


        :return: The value of this JobParam.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this JobParam.


        :param value: The value of this JobParam.
        :type value: str
        """
        self._value = value

    @property
    def param_type(self):
        """Gets the param_type of this JobParam.


        :return: The param_type of this JobParam.
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        """Sets the param_type of this JobParam.


        :param param_type: The param_type of this JobParam.
        :type param_type: str
        """
        self._param_type = param_type

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
        if not isinstance(other, JobParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
