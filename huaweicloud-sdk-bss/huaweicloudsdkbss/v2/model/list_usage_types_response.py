# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsageTypesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'usage_types': 'list[UsageType]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'usage_types': 'usage_types'
    }

    def __init__(self, total_count=None, usage_types=None):
        """ListUsageTypesResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数。
        :type total_count: int
        :param usage_types: 使用量类型列表，具体请参见表3。
        :type usage_types: list[:class:`huaweicloudsdkbss.v2.UsageType`]
        """
        
        super(ListUsageTypesResponse, self).__init__()

        self._total_count = None
        self._usage_types = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if usage_types is not None:
            self.usage_types = usage_types

    @property
    def total_count(self):
        """Gets the total_count of this ListUsageTypesResponse.

        总数。

        :return: The total_count of this ListUsageTypesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListUsageTypesResponse.

        总数。

        :param total_count: The total_count of this ListUsageTypesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def usage_types(self):
        """Gets the usage_types of this ListUsageTypesResponse.

        使用量类型列表，具体请参见表3。

        :return: The usage_types of this ListUsageTypesResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.UsageType`]
        """
        return self._usage_types

    @usage_types.setter
    def usage_types(self, usage_types):
        """Sets the usage_types of this ListUsageTypesResponse.

        使用量类型列表，具体请参见表3。

        :param usage_types: The usage_types of this ListUsageTypesResponse.
        :type usage_types: list[:class:`huaweicloudsdkbss.v2.UsageType`]
        """
        self._usage_types = usage_types

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
        if not isinstance(other, ListUsageTypesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
