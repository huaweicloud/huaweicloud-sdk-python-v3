# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceDiskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'used': 'str',
        'total': 'str'
    }

    attribute_map = {
        'used': 'used',
        'total': 'total'
    }

    def __init__(self, used=None, total=None):
        """ShowInstanceDiskResponse

        The model defined in huaweicloud sdk

        :param used: 已使用量。表示当前实例已使用的存储空间大小。单位：GB
        :type used: str
        :param total: 总量。表示当前实例最大存储空间大小。单位：GB
        :type total: str
        """
        
        super(ShowInstanceDiskResponse, self).__init__()

        self._used = None
        self._total = None
        self.discriminator = None

        if used is not None:
            self.used = used
        if total is not None:
            self.total = total

    @property
    def used(self):
        """Gets the used of this ShowInstanceDiskResponse.

        已使用量。表示当前实例已使用的存储空间大小。单位：GB

        :return: The used of this ShowInstanceDiskResponse.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ShowInstanceDiskResponse.

        已使用量。表示当前实例已使用的存储空间大小。单位：GB

        :param used: The used of this ShowInstanceDiskResponse.
        :type used: str
        """
        self._used = used

    @property
    def total(self):
        """Gets the total of this ShowInstanceDiskResponse.

        总量。表示当前实例最大存储空间大小。单位：GB

        :return: The total of this ShowInstanceDiskResponse.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowInstanceDiskResponse.

        总量。表示当前实例最大存储空间大小。单位：GB

        :param total: The total of this ShowInstanceDiskResponse.
        :type total: str
        """
        self._total = total

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
        if not isinstance(other, ShowInstanceDiskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
