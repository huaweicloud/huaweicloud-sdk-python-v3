# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeChangesTrees:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'level': 'int',
        'file_path': 'str',
        'file_type': 'str'
    }

    attribute_map = {
        'title': 'title',
        'level': 'level',
        'file_path': 'file_path',
        'file_type': 'file_type'
    }

    def __init__(self, title=None, level=None, file_path=None, file_type=None):
        """MergeChangesTrees

        The model defined in huaweicloud sdk

        :param title: 分段路径
        :type title: str
        :param level: 路径级别
        :type level: int
        :param file_path: 当前级别全路径
        :type file_path: str
        :param file_type: 文件类型
        :type file_type: str
        """
        
        

        self._title = None
        self._level = None
        self._file_path = None
        self._file_type = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if level is not None:
            self.level = level
        if file_path is not None:
            self.file_path = file_path
        if file_type is not None:
            self.file_type = file_type

    @property
    def title(self):
        """Gets the title of this MergeChangesTrees.

        分段路径

        :return: The title of this MergeChangesTrees.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MergeChangesTrees.

        分段路径

        :param title: The title of this MergeChangesTrees.
        :type title: str
        """
        self._title = title

    @property
    def level(self):
        """Gets the level of this MergeChangesTrees.

        路径级别

        :return: The level of this MergeChangesTrees.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this MergeChangesTrees.

        路径级别

        :param level: The level of this MergeChangesTrees.
        :type level: int
        """
        self._level = level

    @property
    def file_path(self):
        """Gets the file_path of this MergeChangesTrees.

        当前级别全路径

        :return: The file_path of this MergeChangesTrees.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this MergeChangesTrees.

        当前级别全路径

        :param file_path: The file_path of this MergeChangesTrees.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_type(self):
        """Gets the file_type of this MergeChangesTrees.

        文件类型

        :return: The file_type of this MergeChangesTrees.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this MergeChangesTrees.

        文件类型

        :param file_type: The file_type of this MergeChangesTrees.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, MergeChangesTrees):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
