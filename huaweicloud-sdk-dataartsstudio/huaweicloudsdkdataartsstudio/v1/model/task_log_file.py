# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskLogFile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'file_type': 'str',
        'file_size': 'int',
        'display_name': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_type': 'file_type',
        'file_size': 'file_size',
        'display_name': 'display_name'
    }

    def __init__(self, file_name=None, file_type=None, file_size=None, display_name=None):
        r"""TaskLogFile

        The model defined in huaweicloud sdk

        :param file_name: 文件名称。
        :type file_name: str
        :param file_type: 文件类型: - DIRECTORY：目录 - FILE：文件
        :type file_type: str
        :param file_size: 文件大小，单位字节。
        :type file_size: int
        :param display_name: 文件显示名称。
        :type display_name: str
        """
        
        

        self._file_name = None
        self._file_type = None
        self._file_size = None
        self._display_name = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if file_type is not None:
            self.file_type = file_type
        if file_size is not None:
            self.file_size = file_size
        if display_name is not None:
            self.display_name = display_name

    @property
    def file_name(self):
        r"""Gets the file_name of this TaskLogFile.

        文件名称。

        :return: The file_name of this TaskLogFile.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this TaskLogFile.

        文件名称。

        :param file_name: The file_name of this TaskLogFile.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this TaskLogFile.

        文件类型: - DIRECTORY：目录 - FILE：文件

        :return: The file_type of this TaskLogFile.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this TaskLogFile.

        文件类型: - DIRECTORY：目录 - FILE：文件

        :param file_type: The file_type of this TaskLogFile.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def file_size(self):
        r"""Gets the file_size of this TaskLogFile.

        文件大小，单位字节。

        :return: The file_size of this TaskLogFile.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this TaskLogFile.

        文件大小，单位字节。

        :param file_size: The file_size of this TaskLogFile.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def display_name(self):
        r"""Gets the display_name of this TaskLogFile.

        文件显示名称。

        :return: The display_name of this TaskLogFile.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this TaskLogFile.

        文件显示名称。

        :param display_name: The display_name of this TaskLogFile.
        :type display_name: str
        """
        self._display_name = display_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskLogFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
