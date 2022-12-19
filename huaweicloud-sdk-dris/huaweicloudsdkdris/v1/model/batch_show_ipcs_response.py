# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowIpcsResponse(SdkResponse):

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
        'ipcs': 'list[IpcResponseDTO]'
    }

    attribute_map = {
        'count': 'count',
        'ipcs': 'ipcs'
    }

    def __init__(self, count=None, ipcs=None):
        """BatchShowIpcsResponse

        The model defined in huaweicloud sdk

        :param count: **参数说明**：总数
        :type count: int
        :param ipcs: **参数说明**：IPC列表
        :type ipcs: list[:class:`huaweicloudsdkdris.v1.IpcResponseDTO`]
        """
        
        super(BatchShowIpcsResponse, self).__init__()

        self._count = None
        self._ipcs = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if ipcs is not None:
            self.ipcs = ipcs

    @property
    def count(self):
        """Gets the count of this BatchShowIpcsResponse.

        **参数说明**：总数

        :return: The count of this BatchShowIpcsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchShowIpcsResponse.

        **参数说明**：总数

        :param count: The count of this BatchShowIpcsResponse.
        :type count: int
        """
        self._count = count

    @property
    def ipcs(self):
        """Gets the ipcs of this BatchShowIpcsResponse.

        **参数说明**：IPC列表

        :return: The ipcs of this BatchShowIpcsResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.IpcResponseDTO`]
        """
        return self._ipcs

    @ipcs.setter
    def ipcs(self, ipcs):
        """Sets the ipcs of this BatchShowIpcsResponse.

        **参数说明**：IPC列表

        :param ipcs: The ipcs of this BatchShowIpcsResponse.
        :type ipcs: list[:class:`huaweicloudsdkdris.v1.IpcResponseDTO`]
        """
        self._ipcs = ipcs

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
        if not isinstance(other, BatchShowIpcsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
