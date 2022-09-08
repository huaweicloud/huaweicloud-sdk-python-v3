# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGlobalValueReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'var_value': 'str'
    }

    attribute_map = {
        'var_value': 'var_value'
    }

    def __init__(self, var_value=None):
        """UpdateGlobalValueReq

        The model defined in huaweicloud sdk

        :param var_value: 变量值
        :type var_value: str
        """
        
        

        self._var_value = None
        self.discriminator = None

        self.var_value = var_value

    @property
    def var_value(self):
        """Gets the var_value of this UpdateGlobalValueReq.

        变量值

        :return: The var_value of this UpdateGlobalValueReq.
        :rtype: str
        """
        return self._var_value

    @var_value.setter
    def var_value(self, var_value):
        """Sets the var_value of this UpdateGlobalValueReq.

        变量值

        :param var_value: The var_value of this UpdateGlobalValueReq.
        :type var_value: str
        """
        self._var_value = var_value

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
        if not isinstance(other, UpdateGlobalValueReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
