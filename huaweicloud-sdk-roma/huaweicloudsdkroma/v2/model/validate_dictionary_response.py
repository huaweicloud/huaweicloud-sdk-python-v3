# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateDictionaryResponse(SdkResponse):

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
        'code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code'
    }

    def __init__(self, name=None, code=None):
        r"""ValidateDictionaryResponse

        The model defined in huaweicloud sdk

        :param name: 字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一
        :type name: str
        :param code: 字典编码 - 字符集：英文字母、数字、下划线和空格 - 约束：实例下唯一
        :type code: str
        """
        
        super(ValidateDictionaryResponse, self).__init__()

        self._name = None
        self._code = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if code is not None:
            self.code = code

    @property
    def name(self):
        r"""Gets the name of this ValidateDictionaryResponse.

        字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一

        :return: The name of this ValidateDictionaryResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ValidateDictionaryResponse.

        字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一

        :param name: The name of this ValidateDictionaryResponse.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        r"""Gets the code of this ValidateDictionaryResponse.

        字典编码 - 字符集：英文字母、数字、下划线和空格 - 约束：实例下唯一

        :return: The code of this ValidateDictionaryResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ValidateDictionaryResponse.

        字典编码 - 字符集：英文字母、数字、下划线和空格 - 约束：实例下唯一

        :param code: The code of this ValidateDictionaryResponse.
        :type code: str
        """
        self._code = code

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
        if not isinstance(other, ValidateDictionaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
