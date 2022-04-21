# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadSlowlogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'list': 'list[DownloadSlowlogResult]',
        'status': 'str',
        'count': 'int'
    }

    attribute_map = {
        'list': 'list',
        'status': 'status',
        'count': 'count'
    }

    def __init__(self, list=None, status=None, count=None):
        """DownloadSlowlogResponse

        The model defined in huaweicloud sdk

        :param list: 具体信息。
        :type list: list[:class:`huaweicloudsdkdds.v3.DownloadSlowlogResult`]
        :param status: 慢日志下载链接生成状态。 - FINISH，表示下载链接已经生成完成。 - CREATING，表示正在生成文件，准备下载链接。 - FAILED，表示存在日志文件准备失败。
        :type status: str
        :param count: 慢日志链接数量。
        :type count: int
        """
        
        super(DownloadSlowlogResponse, self).__init__()

        self._list = None
        self._status = None
        self._count = None
        self.discriminator = None

        if list is not None:
            self.list = list
        if status is not None:
            self.status = status
        if count is not None:
            self.count = count

    @property
    def list(self):
        """Gets the list of this DownloadSlowlogResponse.

        具体信息。

        :return: The list of this DownloadSlowlogResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.DownloadSlowlogResult`]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this DownloadSlowlogResponse.

        具体信息。

        :param list: The list of this DownloadSlowlogResponse.
        :type list: list[:class:`huaweicloudsdkdds.v3.DownloadSlowlogResult`]
        """
        self._list = list

    @property
    def status(self):
        """Gets the status of this DownloadSlowlogResponse.

        慢日志下载链接生成状态。 - FINISH，表示下载链接已经生成完成。 - CREATING，表示正在生成文件，准备下载链接。 - FAILED，表示存在日志文件准备失败。

        :return: The status of this DownloadSlowlogResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DownloadSlowlogResponse.

        慢日志下载链接生成状态。 - FINISH，表示下载链接已经生成完成。 - CREATING，表示正在生成文件，准备下载链接。 - FAILED，表示存在日志文件准备失败。

        :param status: The status of this DownloadSlowlogResponse.
        :type status: str
        """
        self._status = status

    @property
    def count(self):
        """Gets the count of this DownloadSlowlogResponse.

        慢日志链接数量。

        :return: The count of this DownloadSlowlogResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DownloadSlowlogResponse.

        慢日志链接数量。

        :param count: The count of this DownloadSlowlogResponse.
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
        if not isinstance(other, DownloadSlowlogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
