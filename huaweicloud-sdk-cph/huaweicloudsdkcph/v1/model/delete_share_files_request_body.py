# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteShareFilesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_ids': 'list[str]',
        'file_paths': 'list[str]'
    }

    attribute_map = {
        'server_ids': 'server_ids',
        'file_paths': 'file_paths'
    }

    def __init__(self, server_ids=None, file_paths=None):
        r"""DeleteShareFilesRequestBody

        The model defined in huaweicloud sdk

        :param server_ids: 云手机服务器ID列表。
        :type server_ids: list[str]
        :param file_paths: 所需删除的共享存储文件绝对路径。以/开头，最大长度4096字节，目前只支持大小写字母、数字、点（.）、斜线（/）、中划线（-）、空格、下划线（_）、等号（&#x3D;），不支持中文。路径中不能包含.. 上层目录路径，防止跨目录攻击。
        :type file_paths: list[str]
        """
        
        

        self._server_ids = None
        self._file_paths = None
        self.discriminator = None

        self.server_ids = server_ids
        self.file_paths = file_paths

    @property
    def server_ids(self):
        r"""Gets the server_ids of this DeleteShareFilesRequestBody.

        云手机服务器ID列表。

        :return: The server_ids of this DeleteShareFilesRequestBody.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        r"""Sets the server_ids of this DeleteShareFilesRequestBody.

        云手机服务器ID列表。

        :param server_ids: The server_ids of this DeleteShareFilesRequestBody.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

    @property
    def file_paths(self):
        r"""Gets the file_paths of this DeleteShareFilesRequestBody.

        所需删除的共享存储文件绝对路径。以/开头，最大长度4096字节，目前只支持大小写字母、数字、点（.）、斜线（/）、中划线（-）、空格、下划线（_）、等号（=），不支持中文。路径中不能包含.. 上层目录路径，防止跨目录攻击。

        :return: The file_paths of this DeleteShareFilesRequestBody.
        :rtype: list[str]
        """
        return self._file_paths

    @file_paths.setter
    def file_paths(self, file_paths):
        r"""Sets the file_paths of this DeleteShareFilesRequestBody.

        所需删除的共享存储文件绝对路径。以/开头，最大长度4096字节，目前只支持大小写字母、数字、点（.）、斜线（/）、中划线（-）、空格、下划线（_）、等号（=），不支持中文。路径中不能包含.. 上层目录路径，防止跨目录攻击。

        :param file_paths: The file_paths of this DeleteShareFilesRequestBody.
        :type file_paths: list[str]
        """
        self._file_paths = file_paths

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
        if not isinstance(other, DeleteShareFilesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
