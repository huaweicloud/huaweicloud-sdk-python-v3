# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalyzerConfigurationUnusedAccess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unused_access_age': 'int'
    }

    attribute_map = {
        'unused_access_age': 'unused_access_age'
    }

    def __init__(self, unused_access_age=None):
        r"""AnalyzerConfigurationUnusedAccess

        The model defined in huaweicloud sdk

        :param unused_access_age: 生成分析结果的预设天数。
        :type unused_access_age: int
        """
        
        

        self._unused_access_age = None
        self.discriminator = None

        if unused_access_age is not None:
            self.unused_access_age = unused_access_age

    @property
    def unused_access_age(self):
        r"""Gets the unused_access_age of this AnalyzerConfigurationUnusedAccess.

        生成分析结果的预设天数。

        :return: The unused_access_age of this AnalyzerConfigurationUnusedAccess.
        :rtype: int
        """
        return self._unused_access_age

    @unused_access_age.setter
    def unused_access_age(self, unused_access_age):
        r"""Sets the unused_access_age of this AnalyzerConfigurationUnusedAccess.

        生成分析结果的预设天数。

        :param unused_access_age: The unused_access_age of this AnalyzerConfigurationUnusedAccess.
        :type unused_access_age: int
        """
        self._unused_access_age = unused_access_age

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
        if not isinstance(other, AnalyzerConfigurationUnusedAccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
