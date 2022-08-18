# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PushShareFilesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'object_path': 'str',
        'server_ids': 'list[str]',
        'file_paths': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'object_path': 'object_path',
        'server_ids': 'server_ids',
        'file_paths': 'file_paths'
    }

    def __init__(self, bucket_name=None, object_path=None, server_ids=None, file_paths=None):
        """PushShareFilesRequestBody

        The model defined in huaweicloud sdk

        :param bucket_name: 合法的OBS桶名，3-63个字符，只能由小写字母、数字、中划线（-）和小数点组成。仅推送共享存储接口使用。
        :type bucket_name: str
        :param object_path: 合法的OBS对象key，最大长度1024字符。 推送的文件只支持tar文件类型。推送时，按tar文件解压后的文件目录结构推送到手机。当前只支持/data和/cache目录推送。仅推送共享存储接口使用。
        :type object_path: str
        :param server_ids: 云手机服务器ID列表。
        :type server_ids: list[str]
        :param file_paths: 所需删除的共享存储文件绝对路径。以/开头，最大长度4096字节，目前只支持大小写字母、数字、点（.）、斜线（/）、中划线（-）、空格、下划线（_）、等号（&#x3D;），不支持中文。路径中不能包含.. 上层目录路径，防止跨目录攻击。仅删除共享存储接口使用。
        :type file_paths: str
        """
        
        

        self._bucket_name = None
        self._object_path = None
        self._server_ids = None
        self._file_paths = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if object_path is not None:
            self.object_path = object_path
        self.server_ids = server_ids
        if file_paths is not None:
            self.file_paths = file_paths

    @property
    def bucket_name(self):
        """Gets the bucket_name of this PushShareFilesRequestBody.

        合法的OBS桶名，3-63个字符，只能由小写字母、数字、中划线（-）和小数点组成。仅推送共享存储接口使用。

        :return: The bucket_name of this PushShareFilesRequestBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this PushShareFilesRequestBody.

        合法的OBS桶名，3-63个字符，只能由小写字母、数字、中划线（-）和小数点组成。仅推送共享存储接口使用。

        :param bucket_name: The bucket_name of this PushShareFilesRequestBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_path(self):
        """Gets the object_path of this PushShareFilesRequestBody.

        合法的OBS对象key，最大长度1024字符。 推送的文件只支持tar文件类型。推送时，按tar文件解压后的文件目录结构推送到手机。当前只支持/data和/cache目录推送。仅推送共享存储接口使用。

        :return: The object_path of this PushShareFilesRequestBody.
        :rtype: str
        """
        return self._object_path

    @object_path.setter
    def object_path(self, object_path):
        """Sets the object_path of this PushShareFilesRequestBody.

        合法的OBS对象key，最大长度1024字符。 推送的文件只支持tar文件类型。推送时，按tar文件解压后的文件目录结构推送到手机。当前只支持/data和/cache目录推送。仅推送共享存储接口使用。

        :param object_path: The object_path of this PushShareFilesRequestBody.
        :type object_path: str
        """
        self._object_path = object_path

    @property
    def server_ids(self):
        """Gets the server_ids of this PushShareFilesRequestBody.

        云手机服务器ID列表。

        :return: The server_ids of this PushShareFilesRequestBody.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        """Sets the server_ids of this PushShareFilesRequestBody.

        云手机服务器ID列表。

        :param server_ids: The server_ids of this PushShareFilesRequestBody.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

    @property
    def file_paths(self):
        """Gets the file_paths of this PushShareFilesRequestBody.

        所需删除的共享存储文件绝对路径。以/开头，最大长度4096字节，目前只支持大小写字母、数字、点（.）、斜线（/）、中划线（-）、空格、下划线（_）、等号（=），不支持中文。路径中不能包含.. 上层目录路径，防止跨目录攻击。仅删除共享存储接口使用。

        :return: The file_paths of this PushShareFilesRequestBody.
        :rtype: str
        """
        return self._file_paths

    @file_paths.setter
    def file_paths(self, file_paths):
        """Sets the file_paths of this PushShareFilesRequestBody.

        所需删除的共享存储文件绝对路径。以/开头，最大长度4096字节，目前只支持大小写字母、数字、点（.）、斜线（/）、中划线（-）、空格、下划线（_）、等号（=），不支持中文。路径中不能包含.. 上层目录路径，防止跨目录攻击。仅删除共享存储接口使用。

        :param file_paths: The file_paths of this PushShareFilesRequestBody.
        :type file_paths: str
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
        if not isinstance(other, PushShareFilesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
