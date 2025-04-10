# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowRsusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'rsus': 'list[RsuDTO]'
    }

    attribute_map = {
        'count': 'count',
        'rsus': 'rsus'
    }

    def __init__(self, count=None, rsus=None):
        r"""BatchShowRsusResponse

        The model defined in huaweicloud sdk

        :param count: **参数说明**：返回RSU的总体数量。
        :type count: int
        :param rsus: **参数说明**：RSU数据列表。
        :type rsus: list[:class:`huaweicloudsdkdris.v1.RsuDTO`]
        """
        
        super(BatchShowRsusResponse, self).__init__()

        self._count = None
        self._rsus = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if rsus is not None:
            self.rsus = rsus

    @property
    def count(self):
        r"""Gets the count of this BatchShowRsusResponse.

        **参数说明**：返回RSU的总体数量。

        :return: The count of this BatchShowRsusResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this BatchShowRsusResponse.

        **参数说明**：返回RSU的总体数量。

        :param count: The count of this BatchShowRsusResponse.
        :type count: int
        """
        self._count = count

    @property
    def rsus(self):
        r"""Gets the rsus of this BatchShowRsusResponse.

        **参数说明**：RSU数据列表。

        :return: The rsus of this BatchShowRsusResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.RsuDTO`]
        """
        return self._rsus

    @rsus.setter
    def rsus(self, rsus):
        r"""Sets the rsus of this BatchShowRsusResponse.

        **参数说明**：RSU数据列表。

        :param rsus: The rsus of this BatchShowRsusResponse.
        :type rsus: list[:class:`huaweicloudsdkdris.v1.RsuDTO`]
        """
        self._rsus = rsus

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
        if not isinstance(other, BatchShowRsusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
