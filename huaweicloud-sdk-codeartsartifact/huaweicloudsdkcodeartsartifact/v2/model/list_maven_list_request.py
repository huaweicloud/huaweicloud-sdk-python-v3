# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMavenListRequest:

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
        'default': 'bool',
        'policy': 'str',
        'repo_ids': 'str',
        'access': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'default': 'default',
        'policy': 'policy',
        'repo_ids': 'repo_ids',
        'access': 'access'
    }

    def __init__(self, project_id=None, default=None, policy=None, repo_ids=None, access=None):
        r"""ListMavenListRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type project_id: str
        :param default: **参数解释**: 是否返回默认仓库。 **约束限制**: 不涉及。 **取值范围**: true or false。 **默认取值**: false。
        :type default: bool
        :param policy: **参数解释**: 仓库类型：snapshot 或 release。 **约束限制**: 不涉及。 **取值范围**: snapshot or releases。 **默认取值**: 不涉及。
        :type policy: str
        :param repo_ids: **参数解释**: 仓库id，多个仓库id用英文逗号间隔。仓库id格式为{region}_{domainId}_{format}_{sequence}。可以从私有依赖库首页-&gt;仓库概览-&gt;仓库地址 url 中获取，最后两个\&quot;/\&quot;中间的字符串即为仓库id。 **约束限制**: 不涉及。 **取值范围**: 最大长度512。 **默认取值**: 不涉及。
        :type repo_ids: str
        :param access: **参数解释**: 权限过滤设置，允许过滤读(r)和读写(rw)权限。 **约束限制**: 不涉及。 **取值范围**: r or rw。 **默认取值**: r。
        :type access: str
        """
        
        

        self._project_id = None
        self._default = None
        self._policy = None
        self._repo_ids = None
        self._access = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if default is not None:
            self.default = default
        if policy is not None:
            self.policy = policy
        if repo_ids is not None:
            self.repo_ids = repo_ids
        if access is not None:
            self.access = access

    @property
    def project_id(self):
        r"""Gets the project_id of this ListMavenListRequest.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The project_id of this ListMavenListRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListMavenListRequest.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param project_id: The project_id of this ListMavenListRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def default(self):
        r"""Gets the default of this ListMavenListRequest.

        **参数解释**: 是否返回默认仓库。 **约束限制**: 不涉及。 **取值范围**: true or false。 **默认取值**: false。

        :return: The default of this ListMavenListRequest.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this ListMavenListRequest.

        **参数解释**: 是否返回默认仓库。 **约束限制**: 不涉及。 **取值范围**: true or false。 **默认取值**: false。

        :param default: The default of this ListMavenListRequest.
        :type default: bool
        """
        self._default = default

    @property
    def policy(self):
        r"""Gets the policy of this ListMavenListRequest.

        **参数解释**: 仓库类型：snapshot 或 release。 **约束限制**: 不涉及。 **取值范围**: snapshot or releases。 **默认取值**: 不涉及。

        :return: The policy of this ListMavenListRequest.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ListMavenListRequest.

        **参数解释**: 仓库类型：snapshot 或 release。 **约束限制**: 不涉及。 **取值范围**: snapshot or releases。 **默认取值**: 不涉及。

        :param policy: The policy of this ListMavenListRequest.
        :type policy: str
        """
        self._policy = policy

    @property
    def repo_ids(self):
        r"""Gets the repo_ids of this ListMavenListRequest.

        **参数解释**: 仓库id，多个仓库id用英文逗号间隔。仓库id格式为{region}_{domainId}_{format}_{sequence}。可以从私有依赖库首页->仓库概览->仓库地址 url 中获取，最后两个\"/\"中间的字符串即为仓库id。 **约束限制**: 不涉及。 **取值范围**: 最大长度512。 **默认取值**: 不涉及。

        :return: The repo_ids of this ListMavenListRequest.
        :rtype: str
        """
        return self._repo_ids

    @repo_ids.setter
    def repo_ids(self, repo_ids):
        r"""Sets the repo_ids of this ListMavenListRequest.

        **参数解释**: 仓库id，多个仓库id用英文逗号间隔。仓库id格式为{region}_{domainId}_{format}_{sequence}。可以从私有依赖库首页->仓库概览->仓库地址 url 中获取，最后两个\"/\"中间的字符串即为仓库id。 **约束限制**: 不涉及。 **取值范围**: 最大长度512。 **默认取值**: 不涉及。

        :param repo_ids: The repo_ids of this ListMavenListRequest.
        :type repo_ids: str
        """
        self._repo_ids = repo_ids

    @property
    def access(self):
        r"""Gets the access of this ListMavenListRequest.

        **参数解释**: 权限过滤设置，允许过滤读(r)和读写(rw)权限。 **约束限制**: 不涉及。 **取值范围**: r or rw。 **默认取值**: r。

        :return: The access of this ListMavenListRequest.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        r"""Sets the access of this ListMavenListRequest.

        **参数解释**: 权限过滤设置，允许过滤读(r)和读写(rw)权限。 **约束限制**: 不涉及。 **取值范围**: r or rw。 **默认取值**: r。

        :param access: The access of this ListMavenListRequest.
        :type access: str
        """
        self._access = access

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
        if not isinstance(other, ListMavenListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
