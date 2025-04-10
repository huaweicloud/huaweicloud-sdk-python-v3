# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrchestrationMappedParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mapped_param_name': 'str',
        'mapped_param_type': 'str',
        'mapped_param_location': 'str'
    }

    attribute_map = {
        'mapped_param_name': 'mapped_param_name',
        'mapped_param_type': 'mapped_param_type',
        'mapped_param_location': 'mapped_param_location'
    }

    def __init__(self, mapped_param_name=None, mapped_param_type=None, mapped_param_location=None):
        r"""OrchestrationMappedParam

        The model defined in huaweicloud sdk

        :param mapped_param_name: 编排后的请求参数名，只支持英文，数字，中划线，必须以英文开头，1-128个字符，不能与已有的参数重名，默认会透传到后端。
        :type mapped_param_name: str
        :param mapped_param_type: 编排后的参数类型，支持string和number。
        :type mapped_param_type: str
        :param mapped_param_location: 编排后的参数位置，支持query和header。
        :type mapped_param_location: str
        """
        
        

        self._mapped_param_name = None
        self._mapped_param_type = None
        self._mapped_param_location = None
        self.discriminator = None

        self.mapped_param_name = mapped_param_name
        self.mapped_param_type = mapped_param_type
        self.mapped_param_location = mapped_param_location

    @property
    def mapped_param_name(self):
        r"""Gets the mapped_param_name of this OrchestrationMappedParam.

        编排后的请求参数名，只支持英文，数字，中划线，必须以英文开头，1-128个字符，不能与已有的参数重名，默认会透传到后端。

        :return: The mapped_param_name of this OrchestrationMappedParam.
        :rtype: str
        """
        return self._mapped_param_name

    @mapped_param_name.setter
    def mapped_param_name(self, mapped_param_name):
        r"""Sets the mapped_param_name of this OrchestrationMappedParam.

        编排后的请求参数名，只支持英文，数字，中划线，必须以英文开头，1-128个字符，不能与已有的参数重名，默认会透传到后端。

        :param mapped_param_name: The mapped_param_name of this OrchestrationMappedParam.
        :type mapped_param_name: str
        """
        self._mapped_param_name = mapped_param_name

    @property
    def mapped_param_type(self):
        r"""Gets the mapped_param_type of this OrchestrationMappedParam.

        编排后的参数类型，支持string和number。

        :return: The mapped_param_type of this OrchestrationMappedParam.
        :rtype: str
        """
        return self._mapped_param_type

    @mapped_param_type.setter
    def mapped_param_type(self, mapped_param_type):
        r"""Sets the mapped_param_type of this OrchestrationMappedParam.

        编排后的参数类型，支持string和number。

        :param mapped_param_type: The mapped_param_type of this OrchestrationMappedParam.
        :type mapped_param_type: str
        """
        self._mapped_param_type = mapped_param_type

    @property
    def mapped_param_location(self):
        r"""Gets the mapped_param_location of this OrchestrationMappedParam.

        编排后的参数位置，支持query和header。

        :return: The mapped_param_location of this OrchestrationMappedParam.
        :rtype: str
        """
        return self._mapped_param_location

    @mapped_param_location.setter
    def mapped_param_location(self, mapped_param_location):
        r"""Sets the mapped_param_location of this OrchestrationMappedParam.

        编排后的参数位置，支持query和header。

        :param mapped_param_location: The mapped_param_location of this OrchestrationMappedParam.
        :type mapped_param_location: str
        """
        self._mapped_param_location = mapped_param_location

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
        if not isinstance(other, OrchestrationMappedParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
