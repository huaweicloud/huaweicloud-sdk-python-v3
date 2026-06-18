# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebHookBranchCfgDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch_type': 'int',
        'branch': 'str',
        'project_type': 'int',
        'project': 'str'
    }

    attribute_map = {
        'branch_type': 'branch_type',
        'branch': 'branch',
        'project_type': 'project_type',
        'project': 'project'
    }

    def __init__(self, branch_type=None, branch=None, project_type=None, project=None):
        r"""WebHookBranchCfgDto

        The model defined in huaweicloud sdk

        :param branch_type: **参数解释：** 分支类型。 **取值范围：** - 0，文本。 - 1，通配符。 - 2，正则。
        :type branch_type: int
        :param branch: **参数解释：** 分支名配置。 **取值范围：** 最小1个字节，最大255字节
        :type branch: str
        :param project_type: **参数解释：** 仓库名类型。 **取值范围：** - 0，文本。 - 1，通配符。 - 2，正则。
        :type project_type: int
        :param project: **参数解释：** 仓库名配置。 **取值范围：** 最小1个字节，最大255字节
        :type project: str
        """
        
        

        self._branch_type = None
        self._branch = None
        self._project_type = None
        self._project = None
        self.discriminator = None

        if branch_type is not None:
            self.branch_type = branch_type
        if branch is not None:
            self.branch = branch
        if project_type is not None:
            self.project_type = project_type
        if project is not None:
            self.project = project

    @property
    def branch_type(self):
        r"""Gets the branch_type of this WebHookBranchCfgDto.

        **参数解释：** 分支类型。 **取值范围：** - 0，文本。 - 1，通配符。 - 2，正则。

        :return: The branch_type of this WebHookBranchCfgDto.
        :rtype: int
        """
        return self._branch_type

    @branch_type.setter
    def branch_type(self, branch_type):
        r"""Sets the branch_type of this WebHookBranchCfgDto.

        **参数解释：** 分支类型。 **取值范围：** - 0，文本。 - 1，通配符。 - 2，正则。

        :param branch_type: The branch_type of this WebHookBranchCfgDto.
        :type branch_type: int
        """
        self._branch_type = branch_type

    @property
    def branch(self):
        r"""Gets the branch of this WebHookBranchCfgDto.

        **参数解释：** 分支名配置。 **取值范围：** 最小1个字节，最大255字节

        :return: The branch of this WebHookBranchCfgDto.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this WebHookBranchCfgDto.

        **参数解释：** 分支名配置。 **取值范围：** 最小1个字节，最大255字节

        :param branch: The branch of this WebHookBranchCfgDto.
        :type branch: str
        """
        self._branch = branch

    @property
    def project_type(self):
        r"""Gets the project_type of this WebHookBranchCfgDto.

        **参数解释：** 仓库名类型。 **取值范围：** - 0，文本。 - 1，通配符。 - 2，正则。

        :return: The project_type of this WebHookBranchCfgDto.
        :rtype: int
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        r"""Sets the project_type of this WebHookBranchCfgDto.

        **参数解释：** 仓库名类型。 **取值范围：** - 0，文本。 - 1，通配符。 - 2，正则。

        :param project_type: The project_type of this WebHookBranchCfgDto.
        :type project_type: int
        """
        self._project_type = project_type

    @property
    def project(self):
        r"""Gets the project of this WebHookBranchCfgDto.

        **参数解释：** 仓库名配置。 **取值范围：** 最小1个字节，最大255字节

        :return: The project of this WebHookBranchCfgDto.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this WebHookBranchCfgDto.

        **参数解释：** 仓库名配置。 **取值范围：** 最小1个字节，最大255字节

        :param project: The project of this WebHookBranchCfgDto.
        :type project: str
        """
        self._project = project

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
        if not isinstance(other, WebHookBranchCfgDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
