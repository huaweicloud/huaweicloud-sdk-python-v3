# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadSlowlogResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_name': 'str',
        'file_name': 'str',
        'status': 'str',
        'file_size': 'str',
        'file_link': 'str',
        'update_at': 'int'
    }

    attribute_map = {
        'node_name': 'node_name',
        'file_name': 'file_name',
        'status': 'status',
        'file_size': 'file_size',
        'file_link': 'file_link',
        'update_at': 'update_at'
    }

    def __init__(self, node_name=None, file_name=None, status=None, file_size=None, file_link=None, update_at=None):
        """DownloadSlowlogResult

        The model defined in huaweicloud sdk

        :param node_name: 节点名称。
        :type node_name: str
        :param file_name: 生成的下载文件名。
        :type file_name: str
        :param status: 当前链接的生成状态。 - SUCCESS，表示下载链接已经生成完成。 - EXPORTING，表示正在生成文件，准备下载链接。 - FAILED，表示存在日志文件准备失败。
        :type status: str
        :param file_size: 文件大小，单位为 KB。
        :type file_size: str
        :param file_link: 下载链接。注意：下载链接在更新时间的 15分钟内有效，超出时间会重新获取。
        :type file_link: str
        :param update_at: 更新时间。
        :type update_at: int
        """
        
        

        self._node_name = None
        self._file_name = None
        self._status = None
        self._file_size = None
        self._file_link = None
        self._update_at = None
        self.discriminator = None

        self.node_name = node_name
        self.file_name = file_name
        self.status = status
        self.file_size = file_size
        self.file_link = file_link
        self.update_at = update_at

    @property
    def node_name(self):
        """Gets the node_name of this DownloadSlowlogResult.

        节点名称。

        :return: The node_name of this DownloadSlowlogResult.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this DownloadSlowlogResult.

        节点名称。

        :param node_name: The node_name of this DownloadSlowlogResult.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def file_name(self):
        """Gets the file_name of this DownloadSlowlogResult.

        生成的下载文件名。

        :return: The file_name of this DownloadSlowlogResult.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DownloadSlowlogResult.

        生成的下载文件名。

        :param file_name: The file_name of this DownloadSlowlogResult.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def status(self):
        """Gets the status of this DownloadSlowlogResult.

        当前链接的生成状态。 - SUCCESS，表示下载链接已经生成完成。 - EXPORTING，表示正在生成文件，准备下载链接。 - FAILED，表示存在日志文件准备失败。

        :return: The status of this DownloadSlowlogResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DownloadSlowlogResult.

        当前链接的生成状态。 - SUCCESS，表示下载链接已经生成完成。 - EXPORTING，表示正在生成文件，准备下载链接。 - FAILED，表示存在日志文件准备失败。

        :param status: The status of this DownloadSlowlogResult.
        :type status: str
        """
        self._status = status

    @property
    def file_size(self):
        """Gets the file_size of this DownloadSlowlogResult.

        文件大小，单位为 KB。

        :return: The file_size of this DownloadSlowlogResult.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this DownloadSlowlogResult.

        文件大小，单位为 KB。

        :param file_size: The file_size of this DownloadSlowlogResult.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def file_link(self):
        """Gets the file_link of this DownloadSlowlogResult.

        下载链接。注意：下载链接在更新时间的 15分钟内有效，超出时间会重新获取。

        :return: The file_link of this DownloadSlowlogResult.
        :rtype: str
        """
        return self._file_link

    @file_link.setter
    def file_link(self, file_link):
        """Sets the file_link of this DownloadSlowlogResult.

        下载链接。注意：下载链接在更新时间的 15分钟内有效，超出时间会重新获取。

        :param file_link: The file_link of this DownloadSlowlogResult.
        :type file_link: str
        """
        self._file_link = file_link

    @property
    def update_at(self):
        """Gets the update_at of this DownloadSlowlogResult.

        更新时间。

        :return: The update_at of this DownloadSlowlogResult.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this DownloadSlowlogResult.

        更新时间。

        :param update_at: The update_at of this DownloadSlowlogResult.
        :type update_at: int
        """
        self._update_at = update_at

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
        if not isinstance(other, DownloadSlowlogResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
