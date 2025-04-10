# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudStorageLogPathInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dir_path': 'str',
        'file_name_pattern': 'str'
    }

    attribute_map = {
        'dir_path': 'dir_path',
        'file_name_pattern': 'file_name_pattern'
    }

    def __init__(self, dir_path=None, file_name_pattern=None):
        r"""CloudStorageLogPathInfo

        The model defined in huaweicloud sdk

        :param dir_path: 容器挂载路径。
        :type dir_path: str
        :param file_name_pattern: 日志文件名匹配模式。
        :type file_name_pattern: str
        """
        
        

        self._dir_path = None
        self._file_name_pattern = None
        self.discriminator = None

        if dir_path is not None:
            self.dir_path = dir_path
        if file_name_pattern is not None:
            self.file_name_pattern = file_name_pattern

    @property
    def dir_path(self):
        r"""Gets the dir_path of this CloudStorageLogPathInfo.

        容器挂载路径。

        :return: The dir_path of this CloudStorageLogPathInfo.
        :rtype: str
        """
        return self._dir_path

    @dir_path.setter
    def dir_path(self, dir_path):
        r"""Sets the dir_path of this CloudStorageLogPathInfo.

        容器挂载路径。

        :param dir_path: The dir_path of this CloudStorageLogPathInfo.
        :type dir_path: str
        """
        self._dir_path = dir_path

    @property
    def file_name_pattern(self):
        r"""Gets the file_name_pattern of this CloudStorageLogPathInfo.

        日志文件名匹配模式。

        :return: The file_name_pattern of this CloudStorageLogPathInfo.
        :rtype: str
        """
        return self._file_name_pattern

    @file_name_pattern.setter
    def file_name_pattern(self, file_name_pattern):
        r"""Sets the file_name_pattern of this CloudStorageLogPathInfo.

        日志文件名匹配模式。

        :param file_name_pattern: The file_name_pattern of this CloudStorageLogPathInfo.
        :type file_name_pattern: str
        """
        self._file_name_pattern = file_name_pattern

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
        if not isinstance(other, CloudStorageLogPathInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
