# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepoTagConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'repository': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'tag': 'tag'
    }

    def __init__(self, namespace=None, repository=None, tag=None):
        r"""ShowRepoTagConfigRequest

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**： 组织名称。用于唯一标识一个组织，组织下的所有镜像仓库都属于该组织。  **约束限制**： 不涉及。  **取值范围**： 小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，不同类型分隔符不能直接相连），小写字母或数字结尾，长度1~64个字符。  **默认取值**： 不涉及。
        :type namespace: str
        :param repository: **参数解释**： 镜像仓库名称过滤关键字，用于模糊匹配镜像仓库列表。  **约束限制**： 不涉及。  **取值范围**： 小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，不同类型分隔符不能直接相连），小写字母或数字结尾，长度1~128个字符。  **默认取值**： 不涉及。
        :type repository: str
        :param tag: **参数解释**： 镜像版本名称。用于唯一标识镜像仓库下的一个镜像版本。  **约束限制**： 不涉及。  **取值范围**： 小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，不同类型分隔符不能直接相连），小写字母或数字结尾，长度1~128个字符。  **默认取值**： 不涉及。
        :type tag: str
        """
        
        

        self._namespace = None
        self._repository = None
        self._tag = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.tag = tag

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowRepoTagConfigRequest.

        **参数解释**： 组织名称。用于唯一标识一个组织，组织下的所有镜像仓库都属于该组织。  **约束限制**： 不涉及。  **取值范围**： 小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，不同类型分隔符不能直接相连），小写字母或数字结尾，长度1~64个字符。  **默认取值**： 不涉及。

        :return: The namespace of this ShowRepoTagConfigRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowRepoTagConfigRequest.

        **参数解释**： 组织名称。用于唯一标识一个组织，组织下的所有镜像仓库都属于该组织。  **约束限制**： 不涉及。  **取值范围**： 小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，不同类型分隔符不能直接相连），小写字母或数字结尾，长度1~64个字符。  **默认取值**： 不涉及。

        :param namespace: The namespace of this ShowRepoTagConfigRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this ShowRepoTagConfigRequest.

        **参数解释**： 镜像仓库名称过滤关键字，用于模糊匹配镜像仓库列表。  **约束限制**： 不涉及。  **取值范围**： 小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，不同类型分隔符不能直接相连），小写字母或数字结尾，长度1~128个字符。  **默认取值**： 不涉及。

        :return: The repository of this ShowRepoTagConfigRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this ShowRepoTagConfigRequest.

        **参数解释**： 镜像仓库名称过滤关键字，用于模糊匹配镜像仓库列表。  **约束限制**： 不涉及。  **取值范围**： 小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，不同类型分隔符不能直接相连），小写字母或数字结尾，长度1~128个字符。  **默认取值**： 不涉及。

        :param repository: The repository of this ShowRepoTagConfigRequest.
        :type repository: str
        """
        self._repository = repository

    @property
    def tag(self):
        r"""Gets the tag of this ShowRepoTagConfigRequest.

        **参数解释**： 镜像版本名称。用于唯一标识镜像仓库下的一个镜像版本。  **约束限制**： 不涉及。  **取值范围**： 小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，不同类型分隔符不能直接相连），小写字母或数字结尾，长度1~128个字符。  **默认取值**： 不涉及。

        :return: The tag of this ShowRepoTagConfigRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ShowRepoTagConfigRequest.

        **参数解释**： 镜像版本名称。用于唯一标识镜像仓库下的一个镜像版本。  **约束限制**： 不涉及。  **取值范围**： 小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，不同类型分隔符不能直接相连），小写字母或数字结尾，长度1~128个字符。  **默认取值**： 不涉及。

        :param tag: The tag of this ShowRepoTagConfigRequest.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ShowRepoTagConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
