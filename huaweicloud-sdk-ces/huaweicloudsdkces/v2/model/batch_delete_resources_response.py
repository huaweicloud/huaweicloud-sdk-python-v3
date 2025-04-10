# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'succeed_count': 'int'
    }

    attribute_map = {
        'succeed_count': 'succeed_count'
    }

    def __init__(self, succeed_count=None):
        r"""BatchDeleteResourcesResponse

        The model defined in huaweicloud sdk

        :param succeed_count: 成功删除的资源数目
        :type succeed_count: int
        """
        
        super(BatchDeleteResourcesResponse, self).__init__()

        self._succeed_count = None
        self.discriminator = None

        if succeed_count is not None:
            self.succeed_count = succeed_count

    @property
    def succeed_count(self):
        r"""Gets the succeed_count of this BatchDeleteResourcesResponse.

        成功删除的资源数目

        :return: The succeed_count of this BatchDeleteResourcesResponse.
        :rtype: int
        """
        return self._succeed_count

    @succeed_count.setter
    def succeed_count(self, succeed_count):
        r"""Sets the succeed_count of this BatchDeleteResourcesResponse.

        成功删除的资源数目

        :param succeed_count: The succeed_count of this BatchDeleteResourcesResponse.
        :type succeed_count: int
        """
        self._succeed_count = succeed_count

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
        if not isinstance(other, BatchDeleteResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
