# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubmoduleReqDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch_name': 'str',
        'file_path': 'str',
        'subrepo_id': 'str',
        'commit_message': 'str',
        'subrepo_branch': 'str'
    }

    attribute_map = {
        'branch_name': 'branch_name',
        'file_path': 'file_path',
        'subrepo_id': 'subrepo_id',
        'commit_message': 'commit_message',
        'subrepo_branch': 'subrepo_branch'
    }

    def __init__(self, branch_name=None, file_path=None, subrepo_id=None, commit_message=None, subrepo_branch=None):
        r"""SubmoduleReqDto

        The model defined in huaweicloud sdk

        :param branch_name: **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节 **约束限制：** 该仓库下的已有分支。
        :type branch_name: str
        :param file_path: 子模块在该仓库下的文件路径
        :type file_path: str
        :param subrepo_id: 子模块所在仓库的仓库ID
        :type subrepo_id: str
        :param commit_message: 提交信息
        :type commit_message: str
        :param subrepo_branch: **参数解释：** 子模块分支名。 **取值范围：** 最小1个字节，最大200字节 **约束限制：** 目标仓库下的已有分支。
        :type subrepo_branch: str
        """
        
        

        self._branch_name = None
        self._file_path = None
        self._subrepo_id = None
        self._commit_message = None
        self._subrepo_branch = None
        self.discriminator = None

        self.branch_name = branch_name
        self.file_path = file_path
        self.subrepo_id = subrepo_id
        self.commit_message = commit_message
        self.subrepo_branch = subrepo_branch

    @property
    def branch_name(self):
        r"""Gets the branch_name of this SubmoduleReqDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节 **约束限制：** 该仓库下的已有分支。

        :return: The branch_name of this SubmoduleReqDto.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this SubmoduleReqDto.

        **参数解释：** 分支名。 **取值范围：** 最小1个字节，最大200字节 **约束限制：** 该仓库下的已有分支。

        :param branch_name: The branch_name of this SubmoduleReqDto.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def file_path(self):
        r"""Gets the file_path of this SubmoduleReqDto.

        子模块在该仓库下的文件路径

        :return: The file_path of this SubmoduleReqDto.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this SubmoduleReqDto.

        子模块在该仓库下的文件路径

        :param file_path: The file_path of this SubmoduleReqDto.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def subrepo_id(self):
        r"""Gets the subrepo_id of this SubmoduleReqDto.

        子模块所在仓库的仓库ID

        :return: The subrepo_id of this SubmoduleReqDto.
        :rtype: str
        """
        return self._subrepo_id

    @subrepo_id.setter
    def subrepo_id(self, subrepo_id):
        r"""Sets the subrepo_id of this SubmoduleReqDto.

        子模块所在仓库的仓库ID

        :param subrepo_id: The subrepo_id of this SubmoduleReqDto.
        :type subrepo_id: str
        """
        self._subrepo_id = subrepo_id

    @property
    def commit_message(self):
        r"""Gets the commit_message of this SubmoduleReqDto.

        提交信息

        :return: The commit_message of this SubmoduleReqDto.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        r"""Sets the commit_message of this SubmoduleReqDto.

        提交信息

        :param commit_message: The commit_message of this SubmoduleReqDto.
        :type commit_message: str
        """
        self._commit_message = commit_message

    @property
    def subrepo_branch(self):
        r"""Gets the subrepo_branch of this SubmoduleReqDto.

        **参数解释：** 子模块分支名。 **取值范围：** 最小1个字节，最大200字节 **约束限制：** 目标仓库下的已有分支。

        :return: The subrepo_branch of this SubmoduleReqDto.
        :rtype: str
        """
        return self._subrepo_branch

    @subrepo_branch.setter
    def subrepo_branch(self, subrepo_branch):
        r"""Sets the subrepo_branch of this SubmoduleReqDto.

        **参数解释：** 子模块分支名。 **取值范围：** 最小1个字节，最大200字节 **约束限制：** 目标仓库下的已有分支。

        :param subrepo_branch: The subrepo_branch of this SubmoduleReqDto.
        :type subrepo_branch: str
        """
        self._subrepo_branch = subrepo_branch

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
        if not isinstance(other, SubmoduleReqDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
