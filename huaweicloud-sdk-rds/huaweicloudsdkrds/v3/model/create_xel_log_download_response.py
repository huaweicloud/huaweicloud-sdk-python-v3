# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateXelLogDownloadResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'list': 'list[CreateXelLogDownloadResult]',
        'count': 'int'
    }

    attribute_map = {
        'list': 'list',
        'count': 'count'
    }

    def __init__(self, list=None, count=None):
        r"""CreateXelLogDownloadResponse

        The model defined in huaweicloud sdk

        :param list: 扩展日志文件返回实体
        :type list: list[:class:`huaweicloudsdkrds.v3.CreateXelLogDownloadResult`]
        :param count: 扩展日志文件信息数量。
        :type count: int
        """
        
        super(CreateXelLogDownloadResponse, self).__init__()

        self._list = None
        self._count = None
        self.discriminator = None

        if list is not None:
            self.list = list
        if count is not None:
            self.count = count

    @property
    def list(self):
        r"""Gets the list of this CreateXelLogDownloadResponse.

        扩展日志文件返回实体

        :return: The list of this CreateXelLogDownloadResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.CreateXelLogDownloadResult`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this CreateXelLogDownloadResponse.

        扩展日志文件返回实体

        :param list: The list of this CreateXelLogDownloadResponse.
        :type list: list[:class:`huaweicloudsdkrds.v3.CreateXelLogDownloadResult`]
        """
        self._list = list

    @property
    def count(self):
        r"""Gets the count of this CreateXelLogDownloadResponse.

        扩展日志文件信息数量。

        :return: The count of this CreateXelLogDownloadResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this CreateXelLogDownloadResponse.

        扩展日志文件信息数量。

        :param count: The count of this CreateXelLogDownloadResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, CreateXelLogDownloadResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
