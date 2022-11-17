# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileTreeNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_path': 'str',
        'file_name': 'str',
        'file_type': 'str'
    }

    attribute_map = {
        'file_path': 'file_path',
        'file_name': 'file_name',
        'file_type': 'file_type'
    }

    def __init__(self, file_path=None, file_name=None, file_type=None):
        """FileTreeNode

        The model defined in huaweicloud sdk

        :param file_path: 文件路径
        :type file_path: str
        :param file_name: 文件名称
        :type file_name: str
        :param file_type: 是否文件夹
        :type file_type: str
        """
        
        

        self._file_path = None
        self._file_name = None
        self._file_type = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if file_name is not None:
            self.file_name = file_name
        if file_type is not None:
            self.file_type = file_type

    @property
    def file_path(self):
        """Gets the file_path of this FileTreeNode.

        文件路径

        :return: The file_path of this FileTreeNode.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this FileTreeNode.

        文件路径

        :param file_path: The file_path of this FileTreeNode.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_name(self):
        """Gets the file_name of this FileTreeNode.

        文件名称

        :return: The file_name of this FileTreeNode.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileTreeNode.

        文件名称

        :param file_name: The file_name of this FileTreeNode.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        """Gets the file_type of this FileTreeNode.

        是否文件夹

        :return: The file_type of this FileTreeNode.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this FileTreeNode.

        是否文件夹

        :param file_type: The file_type of this FileTreeNode.
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
        if not isinstance(other, FileTreeNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
