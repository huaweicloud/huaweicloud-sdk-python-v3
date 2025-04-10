# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'differences': 'list[DiffDetails]'
    }

    attribute_map = {
        'differences': 'differences'
    }

    def __init__(self, differences=None):
        r"""CompareConfigurationResponse

        The model defined in huaweicloud sdk

        :param differences: 参数模板之间的区别集合。
        :type differences: list[:class:`huaweicloudsdkdds.v3.DiffDetails`]
        """
        
        super(CompareConfigurationResponse, self).__init__()

        self._differences = None
        self.discriminator = None

        if differences is not None:
            self.differences = differences

    @property
    def differences(self):
        r"""Gets the differences of this CompareConfigurationResponse.

        参数模板之间的区别集合。

        :return: The differences of this CompareConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.DiffDetails`]
        """
        return self._differences

    @differences.setter
    def differences(self, differences):
        r"""Sets the differences of this CompareConfigurationResponse.

        参数模板之间的区别集合。

        :param differences: The differences of this CompareConfigurationResponse.
        :type differences: list[:class:`huaweicloudsdkdds.v3.DiffDetails`]
        """
        self._differences = differences

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
        if not isinstance(other, CompareConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
