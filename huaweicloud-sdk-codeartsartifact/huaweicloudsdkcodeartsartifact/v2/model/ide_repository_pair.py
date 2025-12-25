# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDERepositoryPair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_name': 'str',
        'includes_pattern': 'str',
        'project_id': 'str',
        'description': 'str',
        'snapshot': 'str',
        'release': 'str'
    }

    attribute_map = {
        'repo_name': 'repo_name',
        'includes_pattern': 'includes_pattern',
        'project_id': 'project_id',
        'description': 'description',
        'snapshot': 'snapshot',
        'release': 'release'
    }

    def __init__(self, repo_name=None, includes_pattern=None, project_id=None, description=None, snapshot=None, release=None):
        r"""IDERepositoryPair

        The model defined in huaweicloud sdk

        :param repo_name: **参数解释**: 仓库名称。 **约束限制**: 长度1-20。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type repo_name: str
        :param includes_pattern: **参数解释**: 路径包含规则。 **约束限制**: 最大长度512。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type includes_pattern: str
        :param project_id: **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type project_id: str
        :param description: **参数解释**: 仓库描述。 **约束限制**: 最大长度200。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type description: str
        :param snapshot: **参数解释**: snapshot仓库名称。 **约束限制**: 长度1-20。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type snapshot: str
        :param release: **参数解释**: release仓库名称。 **约束限制**: 长度1-20。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type release: str
        """
        
        

        self._repo_name = None
        self._includes_pattern = None
        self._project_id = None
        self._description = None
        self._snapshot = None
        self._release = None
        self.discriminator = None

        self.repo_name = repo_name
        self.includes_pattern = includes_pattern
        if project_id is not None:
            self.project_id = project_id
        if description is not None:
            self.description = description
        if snapshot is not None:
            self.snapshot = snapshot
        if release is not None:
            self.release = release

    @property
    def repo_name(self):
        r"""Gets the repo_name of this IDERepositoryPair.

        **参数解释**: 仓库名称。 **约束限制**: 长度1-20。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The repo_name of this IDERepositoryPair.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this IDERepositoryPair.

        **参数解释**: 仓库名称。 **约束限制**: 长度1-20。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param repo_name: The repo_name of this IDERepositoryPair.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def includes_pattern(self):
        r"""Gets the includes_pattern of this IDERepositoryPair.

        **参数解释**: 路径包含规则。 **约束限制**: 最大长度512。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The includes_pattern of this IDERepositoryPair.
        :rtype: str
        """
        return self._includes_pattern

    @includes_pattern.setter
    def includes_pattern(self, includes_pattern):
        r"""Sets the includes_pattern of this IDERepositoryPair.

        **参数解释**: 路径包含规则。 **约束限制**: 最大长度512。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param includes_pattern: The includes_pattern of this IDERepositoryPair.
        :type includes_pattern: str
        """
        self._includes_pattern = includes_pattern

    @property
    def project_id(self):
        r"""Gets the project_id of this IDERepositoryPair.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The project_id of this IDERepositoryPair.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this IDERepositoryPair.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param project_id: The project_id of this IDERepositoryPair.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        r"""Gets the description of this IDERepositoryPair.

        **参数解释**: 仓库描述。 **约束限制**: 最大长度200。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The description of this IDERepositoryPair.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IDERepositoryPair.

        **参数解释**: 仓库描述。 **约束限制**: 最大长度200。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param description: The description of this IDERepositoryPair.
        :type description: str
        """
        self._description = description

    @property
    def snapshot(self):
        r"""Gets the snapshot of this IDERepositoryPair.

        **参数解释**: snapshot仓库名称。 **约束限制**: 长度1-20。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The snapshot of this IDERepositoryPair.
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        r"""Sets the snapshot of this IDERepositoryPair.

        **参数解释**: snapshot仓库名称。 **约束限制**: 长度1-20。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param snapshot: The snapshot of this IDERepositoryPair.
        :type snapshot: str
        """
        self._snapshot = snapshot

    @property
    def release(self):
        r"""Gets the release of this IDERepositoryPair.

        **参数解释**: release仓库名称。 **约束限制**: 长度1-20。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The release of this IDERepositoryPair.
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        r"""Sets the release of this IDERepositoryPair.

        **参数解释**: release仓库名称。 **约束限制**: 长度1-20。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param release: The release of this IDERepositoryPair.
        :type release: str
        """
        self._release = release

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
        if not isinstance(other, IDERepositoryPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
