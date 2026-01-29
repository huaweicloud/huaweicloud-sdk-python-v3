# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryRolesPrivilegeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'repo_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'repo_id': 'repo_id',
        'x_language': 'x-language'
    }

    def __init__(self, project_id=None, repo_id=None, x_language=None):
        r"""ShowRepositoryRolesPrivilegeRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type project_id: str
        :param repo_id: **参数解释**: 仓库id。可在私有库仓库**概览**界面查看。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type repo_id: str
        :param x_language: **参数解释**: 语言类型。 **约束限制**: 不涉及。 **取值范围**: 可选值：zh-cn,en-us。 **默认取值**: zh-cn。
        :type x_language: str
        """
        
        

        self._project_id = None
        self._repo_id = None
        self._x_language = None
        self.discriminator = None

        self.project_id = project_id
        self.repo_id = repo_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowRepositoryRolesPrivilegeRequest.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The project_id of this ShowRepositoryRolesPrivilegeRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowRepositoryRolesPrivilegeRequest.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param project_id: The project_id of this ShowRepositoryRolesPrivilegeRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def repo_id(self):
        r"""Gets the repo_id of this ShowRepositoryRolesPrivilegeRequest.

        **参数解释**: 仓库id。可在私有库仓库**概览**界面查看。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The repo_id of this ShowRepositoryRolesPrivilegeRequest.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this ShowRepositoryRolesPrivilegeRequest.

        **参数解释**: 仓库id。可在私有库仓库**概览**界面查看。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param repo_id: The repo_id of this ShowRepositoryRolesPrivilegeRequest.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowRepositoryRolesPrivilegeRequest.

        **参数解释**: 语言类型。 **约束限制**: 不涉及。 **取值范围**: 可选值：zh-cn,en-us。 **默认取值**: zh-cn。

        :return: The x_language of this ShowRepositoryRolesPrivilegeRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowRepositoryRolesPrivilegeRequest.

        **参数解释**: 语言类型。 **约束限制**: 不涉及。 **取值范围**: 可选值：zh-cn,en-us。 **默认取值**: zh-cn。

        :param x_language: The x_language of this ShowRepositoryRolesPrivilegeRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowRepositoryRolesPrivilegeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
