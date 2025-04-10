# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PositionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_sha': 'str',
        'start_sha': 'str',
        'head_sha': 'str',
        'old_path': 'str',
        'new_path': 'str',
        'position_type': 'str',
        'old_line': 'int',
        'new_line': 'int'
    }

    attribute_map = {
        'base_sha': 'base_sha',
        'start_sha': 'start_sha',
        'head_sha': 'head_sha',
        'old_path': 'old_path',
        'new_path': 'new_path',
        'position_type': 'position_type',
        'old_line': 'old_line',
        'new_line': 'new_line'
    }

    def __init__(self, base_sha=None, start_sha=None, head_sha=None, old_path=None, new_path=None, position_type=None, old_line=None, new_line=None):
        r"""PositionDto

        The model defined in huaweicloud sdk

        :param base_sha: 源分支base提交节点
        :type base_sha: str
        :param start_sha: 目标分支最新提交节点
        :type start_sha: str
        :param head_sha: 源分支最新提交节点
        :type head_sha: str
        :param old_path: 修改前文件路径
        :type old_path: str
        :param new_path: 修改后文件路径
        :type new_path: str
        :param position_type: 变更类型
        :type position_type: str
        :param old_line: 修改前行号
        :type old_line: int
        :param new_line: 修改后行号
        :type new_line: int
        """
        
        

        self._base_sha = None
        self._start_sha = None
        self._head_sha = None
        self._old_path = None
        self._new_path = None
        self._position_type = None
        self._old_line = None
        self._new_line = None
        self.discriminator = None

        if base_sha is not None:
            self.base_sha = base_sha
        if start_sha is not None:
            self.start_sha = start_sha
        if head_sha is not None:
            self.head_sha = head_sha
        if old_path is not None:
            self.old_path = old_path
        if new_path is not None:
            self.new_path = new_path
        if position_type is not None:
            self.position_type = position_type
        if old_line is not None:
            self.old_line = old_line
        if new_line is not None:
            self.new_line = new_line

    @property
    def base_sha(self):
        r"""Gets the base_sha of this PositionDto.

        源分支base提交节点

        :return: The base_sha of this PositionDto.
        :rtype: str
        """
        return self._base_sha

    @base_sha.setter
    def base_sha(self, base_sha):
        r"""Sets the base_sha of this PositionDto.

        源分支base提交节点

        :param base_sha: The base_sha of this PositionDto.
        :type base_sha: str
        """
        self._base_sha = base_sha

    @property
    def start_sha(self):
        r"""Gets the start_sha of this PositionDto.

        目标分支最新提交节点

        :return: The start_sha of this PositionDto.
        :rtype: str
        """
        return self._start_sha

    @start_sha.setter
    def start_sha(self, start_sha):
        r"""Sets the start_sha of this PositionDto.

        目标分支最新提交节点

        :param start_sha: The start_sha of this PositionDto.
        :type start_sha: str
        """
        self._start_sha = start_sha

    @property
    def head_sha(self):
        r"""Gets the head_sha of this PositionDto.

        源分支最新提交节点

        :return: The head_sha of this PositionDto.
        :rtype: str
        """
        return self._head_sha

    @head_sha.setter
    def head_sha(self, head_sha):
        r"""Sets the head_sha of this PositionDto.

        源分支最新提交节点

        :param head_sha: The head_sha of this PositionDto.
        :type head_sha: str
        """
        self._head_sha = head_sha

    @property
    def old_path(self):
        r"""Gets the old_path of this PositionDto.

        修改前文件路径

        :return: The old_path of this PositionDto.
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        r"""Sets the old_path of this PositionDto.

        修改前文件路径

        :param old_path: The old_path of this PositionDto.
        :type old_path: str
        """
        self._old_path = old_path

    @property
    def new_path(self):
        r"""Gets the new_path of this PositionDto.

        修改后文件路径

        :return: The new_path of this PositionDto.
        :rtype: str
        """
        return self._new_path

    @new_path.setter
    def new_path(self, new_path):
        r"""Sets the new_path of this PositionDto.

        修改后文件路径

        :param new_path: The new_path of this PositionDto.
        :type new_path: str
        """
        self._new_path = new_path

    @property
    def position_type(self):
        r"""Gets the position_type of this PositionDto.

        变更类型

        :return: The position_type of this PositionDto.
        :rtype: str
        """
        return self._position_type

    @position_type.setter
    def position_type(self, position_type):
        r"""Sets the position_type of this PositionDto.

        变更类型

        :param position_type: The position_type of this PositionDto.
        :type position_type: str
        """
        self._position_type = position_type

    @property
    def old_line(self):
        r"""Gets the old_line of this PositionDto.

        修改前行号

        :return: The old_line of this PositionDto.
        :rtype: int
        """
        return self._old_line

    @old_line.setter
    def old_line(self, old_line):
        r"""Sets the old_line of this PositionDto.

        修改前行号

        :param old_line: The old_line of this PositionDto.
        :type old_line: int
        """
        self._old_line = old_line

    @property
    def new_line(self):
        r"""Gets the new_line of this PositionDto.

        修改后行号

        :return: The new_line of this PositionDto.
        :rtype: int
        """
        return self._new_line

    @new_line.setter
    def new_line(self, new_line):
        r"""Sets the new_line of this PositionDto.

        修改后行号

        :param new_line: The new_line of this PositionDto.
        :type new_line: int
        """
        self._new_line = new_line

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
        if not isinstance(other, PositionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
