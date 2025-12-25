# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDERepositoryDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_name': 'str',
        'format': 'str',
        'description': 'str',
        'release': 'str',
        'snapshot': 'str',
        'includes_pattern': 'str',
        'share_right': 'str',
        'project_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'repository_name': 'repository_name',
        'format': 'format',
        'description': 'description',
        'release': 'release',
        'snapshot': 'snapshot',
        'includes_pattern': 'includes_pattern',
        'share_right': 'share_right',
        'project_id': 'project_id',
        'type': 'type'
    }

    def __init__(self, repository_name=None, format=None, description=None, release=None, snapshot=None, includes_pattern=None, share_right=None, project_id=None, type=None):
        r"""IDERepositoryDO

        The model defined in huaweicloud sdk

        :param repository_name: **参数解释**: 仓库名称。 **约束限制**: 长度1-50。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type repository_name: str
        :param format: **参数解释**: 制品类型。 **约束限制**: 不涉及。 **取值范围**: maven2。 **默认取值**: 无。 
        :type format: str
        :param description: **参数解释**: 仓库描述。 **约束限制**: 最大长度200。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type description: str
        :param release: **参数解释**: release仓库名称。 **约束限制**: 长度1-50。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type release: str
        :param snapshot: **参数解释**: snapshot仓库名称。 **约束限制**: 长度1-50。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type snapshot: str
        :param includes_pattern: **参数解释**: 路径包含规则。 **约束限制**: 最大长度512。 **取值范围**: 不涉及。 **默认取值**: 无。 
        :type includes_pattern: str
        :param share_right: **参数解释**: 共享权限级别。 **约束限制**: 不涉及。 **取值范围**: PROJECT。 **默认取值**: 无。 
        :type share_right: str
        :param project_id: **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type project_id: str
        :param type: **参数解释**: 仓库类型。 **约束限制**: 不涉及。 **取值范围**: hosted：本地仓库。 **默认取值**: 无。 
        :type type: str
        """
        
        

        self._repository_name = None
        self._format = None
        self._description = None
        self._release = None
        self._snapshot = None
        self._includes_pattern = None
        self._share_right = None
        self._project_id = None
        self._type = None
        self.discriminator = None

        self.repository_name = repository_name
        self.format = format
        if description is not None:
            self.description = description
        if release is not None:
            self.release = release
        if snapshot is not None:
            self.snapshot = snapshot
        if includes_pattern is not None:
            self.includes_pattern = includes_pattern
        if share_right is not None:
            self.share_right = share_right
        if project_id is not None:
            self.project_id = project_id
        self.type = type

    @property
    def repository_name(self):
        r"""Gets the repository_name of this IDERepositoryDO.

        **参数解释**: 仓库名称。 **约束限制**: 长度1-50。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The repository_name of this IDERepositoryDO.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this IDERepositoryDO.

        **参数解释**: 仓库名称。 **约束限制**: 长度1-50。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param repository_name: The repository_name of this IDERepositoryDO.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def format(self):
        r"""Gets the format of this IDERepositoryDO.

        **参数解释**: 制品类型。 **约束限制**: 不涉及。 **取值范围**: maven2。 **默认取值**: 无。 

        :return: The format of this IDERepositoryDO.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this IDERepositoryDO.

        **参数解释**: 制品类型。 **约束限制**: 不涉及。 **取值范围**: maven2。 **默认取值**: 无。 

        :param format: The format of this IDERepositoryDO.
        :type format: str
        """
        self._format = format

    @property
    def description(self):
        r"""Gets the description of this IDERepositoryDO.

        **参数解释**: 仓库描述。 **约束限制**: 最大长度200。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The description of this IDERepositoryDO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IDERepositoryDO.

        **参数解释**: 仓库描述。 **约束限制**: 最大长度200。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param description: The description of this IDERepositoryDO.
        :type description: str
        """
        self._description = description

    @property
    def release(self):
        r"""Gets the release of this IDERepositoryDO.

        **参数解释**: release仓库名称。 **约束限制**: 长度1-50。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The release of this IDERepositoryDO.
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        r"""Sets the release of this IDERepositoryDO.

        **参数解释**: release仓库名称。 **约束限制**: 长度1-50。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param release: The release of this IDERepositoryDO.
        :type release: str
        """
        self._release = release

    @property
    def snapshot(self):
        r"""Gets the snapshot of this IDERepositoryDO.

        **参数解释**: snapshot仓库名称。 **约束限制**: 长度1-50。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The snapshot of this IDERepositoryDO.
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        r"""Sets the snapshot of this IDERepositoryDO.

        **参数解释**: snapshot仓库名称。 **约束限制**: 长度1-50。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param snapshot: The snapshot of this IDERepositoryDO.
        :type snapshot: str
        """
        self._snapshot = snapshot

    @property
    def includes_pattern(self):
        r"""Gets the includes_pattern of this IDERepositoryDO.

        **参数解释**: 路径包含规则。 **约束限制**: 最大长度512。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :return: The includes_pattern of this IDERepositoryDO.
        :rtype: str
        """
        return self._includes_pattern

    @includes_pattern.setter
    def includes_pattern(self, includes_pattern):
        r"""Sets the includes_pattern of this IDERepositoryDO.

        **参数解释**: 路径包含规则。 **约束限制**: 最大长度512。 **取值范围**: 不涉及。 **默认取值**: 无。 

        :param includes_pattern: The includes_pattern of this IDERepositoryDO.
        :type includes_pattern: str
        """
        self._includes_pattern = includes_pattern

    @property
    def share_right(self):
        r"""Gets the share_right of this IDERepositoryDO.

        **参数解释**: 共享权限级别。 **约束限制**: 不涉及。 **取值范围**: PROJECT。 **默认取值**: 无。 

        :return: The share_right of this IDERepositoryDO.
        :rtype: str
        """
        return self._share_right

    @share_right.setter
    def share_right(self, share_right):
        r"""Sets the share_right of this IDERepositoryDO.

        **参数解释**: 共享权限级别。 **约束限制**: 不涉及。 **取值范围**: PROJECT。 **默认取值**: 无。 

        :param share_right: The share_right of this IDERepositoryDO.
        :type share_right: str
        """
        self._share_right = share_right

    @property
    def project_id(self):
        r"""Gets the project_id of this IDERepositoryDO.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The project_id of this IDERepositoryDO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this IDERepositoryDO.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param project_id: The project_id of this IDERepositoryDO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        r"""Gets the type of this IDERepositoryDO.

        **参数解释**: 仓库类型。 **约束限制**: 不涉及。 **取值范围**: hosted：本地仓库。 **默认取值**: 无。 

        :return: The type of this IDERepositoryDO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IDERepositoryDO.

        **参数解释**: 仓库类型。 **约束限制**: 不涉及。 **取值范围**: hosted：本地仓库。 **默认取值**: 无。 

        :param type: The type of this IDERepositoryDO.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, IDERepositoryDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
