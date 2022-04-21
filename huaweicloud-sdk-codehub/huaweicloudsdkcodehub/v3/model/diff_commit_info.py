# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiffCommitInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'old_path': 'str',
        'new_path': 'str',
        'a_mode': 'str',
        'b_mode': 'str',
        'new_file': 'bool',
        'renamed_file': 'bool',
        'deleted_file': 'bool',
        'diff': 'bool'
    }

    attribute_map = {
        'old_path': 'old_path',
        'new_path': 'new_path',
        'a_mode': 'a_mode',
        'b_mode': 'b_mode',
        'new_file': 'new_file',
        'renamed_file': 'renamed_file',
        'deleted_file': 'deleted_file',
        'diff': 'diff'
    }

    def __init__(self, old_path=None, new_path=None, a_mode=None, b_mode=None, new_file=None, renamed_file=None, deleted_file=None, diff=None):
        """DiffCommitInfo

        The model defined in huaweicloud sdk

        :param old_path: 变更前文件路径
        :type old_path: str
        :param new_path: 变更后文件路径
        :type new_path: str
        :param a_mode: 变更前文件模式
        :type a_mode: str
        :param b_mode: 变更后文件模式
        :type b_mode: str
        :param new_file: 此次变更是否新增文件
        :type new_file: bool
        :param renamed_file: 此次变更是否重命名文件
        :type renamed_file: bool
        :param deleted_file: 此次变更是否删除文件
        :type deleted_file: bool
        :param diff: 差异信息
        :type diff: bool
        """
        
        

        self._old_path = None
        self._new_path = None
        self._a_mode = None
        self._b_mode = None
        self._new_file = None
        self._renamed_file = None
        self._deleted_file = None
        self._diff = None
        self.discriminator = None

        if old_path is not None:
            self.old_path = old_path
        if new_path is not None:
            self.new_path = new_path
        if a_mode is not None:
            self.a_mode = a_mode
        if b_mode is not None:
            self.b_mode = b_mode
        if new_file is not None:
            self.new_file = new_file
        if renamed_file is not None:
            self.renamed_file = renamed_file
        if deleted_file is not None:
            self.deleted_file = deleted_file
        if diff is not None:
            self.diff = diff

    @property
    def old_path(self):
        """Gets the old_path of this DiffCommitInfo.

        变更前文件路径

        :return: The old_path of this DiffCommitInfo.
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        """Sets the old_path of this DiffCommitInfo.

        变更前文件路径

        :param old_path: The old_path of this DiffCommitInfo.
        :type old_path: str
        """
        self._old_path = old_path

    @property
    def new_path(self):
        """Gets the new_path of this DiffCommitInfo.

        变更后文件路径

        :return: The new_path of this DiffCommitInfo.
        :rtype: str
        """
        return self._new_path

    @new_path.setter
    def new_path(self, new_path):
        """Sets the new_path of this DiffCommitInfo.

        变更后文件路径

        :param new_path: The new_path of this DiffCommitInfo.
        :type new_path: str
        """
        self._new_path = new_path

    @property
    def a_mode(self):
        """Gets the a_mode of this DiffCommitInfo.

        变更前文件模式

        :return: The a_mode of this DiffCommitInfo.
        :rtype: str
        """
        return self._a_mode

    @a_mode.setter
    def a_mode(self, a_mode):
        """Sets the a_mode of this DiffCommitInfo.

        变更前文件模式

        :param a_mode: The a_mode of this DiffCommitInfo.
        :type a_mode: str
        """
        self._a_mode = a_mode

    @property
    def b_mode(self):
        """Gets the b_mode of this DiffCommitInfo.

        变更后文件模式

        :return: The b_mode of this DiffCommitInfo.
        :rtype: str
        """
        return self._b_mode

    @b_mode.setter
    def b_mode(self, b_mode):
        """Sets the b_mode of this DiffCommitInfo.

        变更后文件模式

        :param b_mode: The b_mode of this DiffCommitInfo.
        :type b_mode: str
        """
        self._b_mode = b_mode

    @property
    def new_file(self):
        """Gets the new_file of this DiffCommitInfo.

        此次变更是否新增文件

        :return: The new_file of this DiffCommitInfo.
        :rtype: bool
        """
        return self._new_file

    @new_file.setter
    def new_file(self, new_file):
        """Sets the new_file of this DiffCommitInfo.

        此次变更是否新增文件

        :param new_file: The new_file of this DiffCommitInfo.
        :type new_file: bool
        """
        self._new_file = new_file

    @property
    def renamed_file(self):
        """Gets the renamed_file of this DiffCommitInfo.

        此次变更是否重命名文件

        :return: The renamed_file of this DiffCommitInfo.
        :rtype: bool
        """
        return self._renamed_file

    @renamed_file.setter
    def renamed_file(self, renamed_file):
        """Sets the renamed_file of this DiffCommitInfo.

        此次变更是否重命名文件

        :param renamed_file: The renamed_file of this DiffCommitInfo.
        :type renamed_file: bool
        """
        self._renamed_file = renamed_file

    @property
    def deleted_file(self):
        """Gets the deleted_file of this DiffCommitInfo.

        此次变更是否删除文件

        :return: The deleted_file of this DiffCommitInfo.
        :rtype: bool
        """
        return self._deleted_file

    @deleted_file.setter
    def deleted_file(self, deleted_file):
        """Sets the deleted_file of this DiffCommitInfo.

        此次变更是否删除文件

        :param deleted_file: The deleted_file of this DiffCommitInfo.
        :type deleted_file: bool
        """
        self._deleted_file = deleted_file

    @property
    def diff(self):
        """Gets the diff of this DiffCommitInfo.

        差异信息

        :return: The diff of this DiffCommitInfo.
        :rtype: bool
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        """Sets the diff of this DiffCommitInfo.

        差异信息

        :param diff: The diff of this DiffCommitInfo.
        :type diff: bool
        """
        self._diff = diff

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
        if not isinstance(other, DiffCommitInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
