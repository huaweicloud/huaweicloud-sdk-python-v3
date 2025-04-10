# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TreeNode:

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
        'file_path': 'str',
        'is_leaf': 'bool',
        'checkbox_status': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_path': 'file_path',
        'is_leaf': 'is_leaf',
        'checkbox_status': 'checkbox_status'
    }

    def __init__(self, file_name=None, file_path=None, is_leaf=None, checkbox_status=None):
        r"""TreeNode

        The model defined in huaweicloud sdk

        :param file_name: 目录或文件名
        :type file_name: str
        :param file_path: 目录或文件路径
        :type file_path: str
        :param is_leaf: 是否为叶子节点，true是，false不是
        :type is_leaf: bool
        :param checkbox_status: 屏蔽状态，包括unchecked(不屏蔽)、all(全屏蔽)、half(半屏蔽)
        :type checkbox_status: str
        """
        
        

        self._file_name = None
        self._file_path = None
        self._is_leaf = None
        self._checkbox_status = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if is_leaf is not None:
            self.is_leaf = is_leaf
        if checkbox_status is not None:
            self.checkbox_status = checkbox_status

    @property
    def file_name(self):
        r"""Gets the file_name of this TreeNode.

        目录或文件名

        :return: The file_name of this TreeNode.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this TreeNode.

        目录或文件名

        :param file_name: The file_name of this TreeNode.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this TreeNode.

        目录或文件路径

        :return: The file_path of this TreeNode.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this TreeNode.

        目录或文件路径

        :param file_path: The file_path of this TreeNode.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def is_leaf(self):
        r"""Gets the is_leaf of this TreeNode.

        是否为叶子节点，true是，false不是

        :return: The is_leaf of this TreeNode.
        :rtype: bool
        """
        return self._is_leaf

    @is_leaf.setter
    def is_leaf(self, is_leaf):
        r"""Sets the is_leaf of this TreeNode.

        是否为叶子节点，true是，false不是

        :param is_leaf: The is_leaf of this TreeNode.
        :type is_leaf: bool
        """
        self._is_leaf = is_leaf

    @property
    def checkbox_status(self):
        r"""Gets the checkbox_status of this TreeNode.

        屏蔽状态，包括unchecked(不屏蔽)、all(全屏蔽)、half(半屏蔽)

        :return: The checkbox_status of this TreeNode.
        :rtype: str
        """
        return self._checkbox_status

    @checkbox_status.setter
    def checkbox_status(self, checkbox_status):
        r"""Sets the checkbox_status of this TreeNode.

        屏蔽状态，包括unchecked(不屏蔽)、all(全屏蔽)、half(半屏蔽)

        :param checkbox_status: The checkbox_status of this TreeNode.
        :type checkbox_status: str
        """
        self._checkbox_status = checkbox_status

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
        if not isinstance(other, TreeNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
