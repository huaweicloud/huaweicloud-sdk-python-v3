# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryDirDto:

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
        'branch_name': 'str',
        'commit_message': 'str'
    }

    attribute_map = {
        'file_path': 'file_path',
        'branch_name': 'branch_name',
        'commit_message': 'commit_message'
    }

    def __init__(self, file_path=None, branch_name=None, commit_message=None):
        r"""RepositoryDirDto

        The model defined in huaweicloud sdk

        :param file_path: **参数解释：** 目录路径。 **约束限制：** 目录路径层级最大不能超过29。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type file_path: str
        :param branch_name: **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节 **约束限制：** 该仓库下的已有分支。
        :type branch_name: str
        :param commit_message: **参数解释：** 提交信息。 **取值范围：** 不涉及。
        :type commit_message: str
        """
        
        

        self._file_path = None
        self._branch_name = None
        self._commit_message = None
        self.discriminator = None

        self.file_path = file_path
        self.branch_name = branch_name
        self.commit_message = commit_message

    @property
    def file_path(self):
        r"""Gets the file_path of this RepositoryDirDto.

        **参数解释：** 目录路径。 **约束限制：** 目录路径层级最大不能超过29。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The file_path of this RepositoryDirDto.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this RepositoryDirDto.

        **参数解释：** 目录路径。 **约束限制：** 目录路径层级最大不能超过29。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param file_path: The file_path of this RepositoryDirDto.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def branch_name(self):
        r"""Gets the branch_name of this RepositoryDirDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节 **约束限制：** 该仓库下的已有分支。

        :return: The branch_name of this RepositoryDirDto.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this RepositoryDirDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节 **约束限制：** 该仓库下的已有分支。

        :param branch_name: The branch_name of this RepositoryDirDto.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def commit_message(self):
        r"""Gets the commit_message of this RepositoryDirDto.

        **参数解释：** 提交信息。 **取值范围：** 不涉及。

        :return: The commit_message of this RepositoryDirDto.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        r"""Sets the commit_message of this RepositoryDirDto.

        **参数解释：** 提交信息。 **取值范围：** 不涉及。

        :param commit_message: The commit_message of this RepositoryDirDto.
        :type commit_message: str
        """
        self._commit_message = commit_message

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
        if not isinstance(other, RepositoryDirDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
