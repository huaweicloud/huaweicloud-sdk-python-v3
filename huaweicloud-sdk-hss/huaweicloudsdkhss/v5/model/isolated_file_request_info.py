# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsolatedFileRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'file_hash': 'str',
        'file_path': 'str',
        'file_attr': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'file_hash': 'file_hash',
        'file_path': 'file_path',
        'file_attr': 'file_attr'
    }

    def __init__(self, host_id=None, file_hash=None, file_path=None, file_attr=None):
        """IsolatedFileRequestInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机ID
        :type host_id: str
        :param file_hash: 文件哈希
        :type file_hash: str
        :param file_path: 文件路径
        :type file_path: str
        :param file_attr: 文件属性
        :type file_attr: str
        """
        
        

        self._host_id = None
        self._file_hash = None
        self._file_path = None
        self._file_attr = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if file_hash is not None:
            self.file_hash = file_hash
        if file_path is not None:
            self.file_path = file_path
        if file_attr is not None:
            self.file_attr = file_attr

    @property
    def host_id(self):
        """Gets the host_id of this IsolatedFileRequestInfo.

        主机ID

        :return: The host_id of this IsolatedFileRequestInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this IsolatedFileRequestInfo.

        主机ID

        :param host_id: The host_id of this IsolatedFileRequestInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def file_hash(self):
        """Gets the file_hash of this IsolatedFileRequestInfo.

        文件哈希

        :return: The file_hash of this IsolatedFileRequestInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        """Sets the file_hash of this IsolatedFileRequestInfo.

        文件哈希

        :param file_hash: The file_hash of this IsolatedFileRequestInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_path(self):
        """Gets the file_path of this IsolatedFileRequestInfo.

        文件路径

        :return: The file_path of this IsolatedFileRequestInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this IsolatedFileRequestInfo.

        文件路径

        :param file_path: The file_path of this IsolatedFileRequestInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_attr(self):
        """Gets the file_attr of this IsolatedFileRequestInfo.

        文件属性

        :return: The file_attr of this IsolatedFileRequestInfo.
        :rtype: str
        """
        return self._file_attr

    @file_attr.setter
    def file_attr(self, file_attr):
        """Sets the file_attr of this IsolatedFileRequestInfo.

        文件属性

        :param file_attr: The file_attr of this IsolatedFileRequestInfo.
        :type file_attr: str
        """
        self._file_attr = file_attr

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
        if not isinstance(other, IsolatedFileRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
