# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListChildProxyRepositoriesListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'repo_id': 'repo_id',
        'type': 'type'
    }

    def __init__(self, repo_id=None, type=None):
        r"""ListChildProxyRepositoriesListRequest

        The model defined in huaweicloud sdk

        :param repo_id: **参数解释**: 仓库id，格式为{region}_{domainId}_{format}_{sequence}。可以从私有依赖库首页-&gt;仓库概览-&gt;仓库地址 url 中获取，最后两个\&quot;/\&quot;中间的字符串即为仓库id。 **约束限制**: 不涉及。 **取值范围**: 根据仓库id格式中region, domainId需要为有效值，format有效值为:npm|go|pypi|rpm|composer|maven|debian|conan|nuget|docker2|cocoapods|ohpm|generic|helm|conda, sequence取值根据套餐不同有不同上限值。 **默认取值**: 不涉及。
        :type repo_id: str
        :param type: **参数解释**: type。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type type: str
        """
        
        

        self._repo_id = None
        self._type = None
        self.discriminator = None

        self.repo_id = repo_id
        if type is not None:
            self.type = type

    @property
    def repo_id(self):
        r"""Gets the repo_id of this ListChildProxyRepositoriesListRequest.

        **参数解释**: 仓库id，格式为{region}_{domainId}_{format}_{sequence}。可以从私有依赖库首页->仓库概览->仓库地址 url 中获取，最后两个\"/\"中间的字符串即为仓库id。 **约束限制**: 不涉及。 **取值范围**: 根据仓库id格式中region, domainId需要为有效值，format有效值为:npm|go|pypi|rpm|composer|maven|debian|conan|nuget|docker2|cocoapods|ohpm|generic|helm|conda, sequence取值根据套餐不同有不同上限值。 **默认取值**: 不涉及。

        :return: The repo_id of this ListChildProxyRepositoriesListRequest.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this ListChildProxyRepositoriesListRequest.

        **参数解释**: 仓库id，格式为{region}_{domainId}_{format}_{sequence}。可以从私有依赖库首页->仓库概览->仓库地址 url 中获取，最后两个\"/\"中间的字符串即为仓库id。 **约束限制**: 不涉及。 **取值范围**: 根据仓库id格式中region, domainId需要为有效值，format有效值为:npm|go|pypi|rpm|composer|maven|debian|conan|nuget|docker2|cocoapods|ohpm|generic|helm|conda, sequence取值根据套餐不同有不同上限值。 **默认取值**: 不涉及。

        :param repo_id: The repo_id of this ListChildProxyRepositoriesListRequest.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def type(self):
        r"""Gets the type of this ListChildProxyRepositoriesListRequest.

        **参数解释**: type。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The type of this ListChildProxyRepositoriesListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListChildProxyRepositoriesListRequest.

        **参数解释**: type。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param type: The type of this ListChildProxyRepositoriesListRequest.
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
        if not isinstance(other, ListChildProxyRepositoriesListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
