# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpDetectRequestBodyExtension:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'header': 'dict(str, str)'
    }

    attribute_map = {
        'header': 'header'
    }

    def __init__(self, header=None):
        r"""HttpDetectRequestBodyExtension

        The model defined in huaweicloud sdk

        :param header: header应满足如下要求： 1. key值限定为：包含英文字母([A-Za-z])、数字([0-9])、中划线(-)hyphens，中划线不得作为结尾，不得连续出现。 2. K/V不得超过10个 3. key需要以\&quot;x-\&quot;开头，不能以\&quot;x-smn\&quot;开头，正确示例：x-abc-cba,  x-abc 4. 所有K/V长度总和不得超过1024个字符 5. key不区分大小写 6. key值不可重复 7. value值限定为ASCII码，不支持中文或其他Unicode，支持空格
        :type header: dict(str, str)
        """
        
        

        self._header = None
        self.discriminator = None

        if header is not None:
            self.header = header

    @property
    def header(self):
        r"""Gets the header of this HttpDetectRequestBodyExtension.

        header应满足如下要求： 1. key值限定为：包含英文字母([A-Za-z])、数字([0-9])、中划线(-)hyphens，中划线不得作为结尾，不得连续出现。 2. K/V不得超过10个 3. key需要以\"x-\"开头，不能以\"x-smn\"开头，正确示例：x-abc-cba,  x-abc 4. 所有K/V长度总和不得超过1024个字符 5. key不区分大小写 6. key值不可重复 7. value值限定为ASCII码，不支持中文或其他Unicode，支持空格

        :return: The header of this HttpDetectRequestBodyExtension.
        :rtype: dict(str, str)
        """
        return self._header

    @header.setter
    def header(self, header):
        r"""Sets the header of this HttpDetectRequestBodyExtension.

        header应满足如下要求： 1. key值限定为：包含英文字母([A-Za-z])、数字([0-9])、中划线(-)hyphens，中划线不得作为结尾，不得连续出现。 2. K/V不得超过10个 3. key需要以\"x-\"开头，不能以\"x-smn\"开头，正确示例：x-abc-cba,  x-abc 4. 所有K/V长度总和不得超过1024个字符 5. key不区分大小写 6. key值不可重复 7. value值限定为ASCII码，不支持中文或其他Unicode，支持空格

        :param header: The header of this HttpDetectRequestBodyExtension.
        :type header: dict(str, str)
        """
        self._header = header

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
        if not isinstance(other, HttpDetectRequestBodyExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
