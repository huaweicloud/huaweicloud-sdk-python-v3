# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStructTemplateRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'param': 'str',
        'type': 'str'
    }

    attribute_map = {
        'param': 'param',
        'type': 'type'
    }

    def __init__(self, param=None, type=None):
        """ShowStructTemplateRule

        The model defined in huaweicloud sdk

        :param param: 测试
        :type param: str
        :param type: 结构化类型
        :type type: str
        """
        
        

        self._param = None
        self._type = None
        self.discriminator = None

        if param is not None:
            self.param = param
        if type is not None:
            self.type = type

    @property
    def param(self):
        """Gets the param of this ShowStructTemplateRule.

        测试

        :return: The param of this ShowStructTemplateRule.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this ShowStructTemplateRule.

        测试

        :param param: The param of this ShowStructTemplateRule.
        :type param: str
        """
        self._param = param

    @property
    def type(self):
        """Gets the type of this ShowStructTemplateRule.

        结构化类型

        :return: The type of this ShowStructTemplateRule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowStructTemplateRule.

        结构化类型

        :param type: The type of this ShowStructTemplateRule.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowStructTemplateRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
