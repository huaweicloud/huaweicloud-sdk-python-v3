# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectRelatedRepositoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'repo_id': 'str'
    }

    attribute_map = {
        'search_name': 'search_name',
        'offset': 'offset',
        'limit': 'limit',
        'repo_id': 'repo_id'
    }

    def __init__(self, search_name=None, offset=None, limit=None, repo_id=None):
        r"""ShowProjectRelatedRepositoryRequest

        The model defined in huaweicloud sdk

        :param search_name: **参数解释**： 项目名称，支持模糊查询。 **约束限制**： 不涉及。 **取值范围**： 最大200个字符。 **默认取值**： 不涉及。
        :type search_name: str
        :param offset: **参数解释**： 分页查询的起始位置。 **约束限制**： 不涉及。 **取值范围**： 0-2147483647 **默认取值**： 0
        :type offset: int
        :param limit: **参数解释**： 分页查询每页的数据量。 **约束限制**： 不涉及。 **取值范围**： 1-2147483647 **默认取值**： 10
        :type limit: int
        :param repo_id: **参数解释**： 仓库ID，格式为{region}\\_{domainId}\\_{format}_{sequence}。可以从“私有依赖库首页 &gt; 仓库概览 &gt; 仓库地址url”中获取，最后两个“/”中间的字符串即为仓库ID。如仓库地址：https://devrepo.devcloud.abcde.abc.xyz.com/artgalaxy/abcde_09d2ca2f5080d5b60f51c00ae5bad0a0_maven_2_50/，其中abcde_09d2ca2f5080d5b60f51c00ae5bad0a0_maven_2_50即为仓库ID。 **约束限制**： 不涉及。 **取值范围**： 仓库ID格式中的format支持以下值： - npm - go - pypi - rpm - composer - maven - debian - conan - nuget - docker2 - cocoapods **默认取值**： 不涉及。
        :type repo_id: str
        """
        
        

        self._search_name = None
        self._offset = None
        self._limit = None
        self._repo_id = None
        self.discriminator = None

        if search_name is not None:
            self.search_name = search_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if repo_id is not None:
            self.repo_id = repo_id

    @property
    def search_name(self):
        r"""Gets the search_name of this ShowProjectRelatedRepositoryRequest.

        **参数解释**： 项目名称，支持模糊查询。 **约束限制**： 不涉及。 **取值范围**： 最大200个字符。 **默认取值**： 不涉及。

        :return: The search_name of this ShowProjectRelatedRepositoryRequest.
        :rtype: str
        """
        return self._search_name

    @search_name.setter
    def search_name(self, search_name):
        r"""Sets the search_name of this ShowProjectRelatedRepositoryRequest.

        **参数解释**： 项目名称，支持模糊查询。 **约束限制**： 不涉及。 **取值范围**： 最大200个字符。 **默认取值**： 不涉及。

        :param search_name: The search_name of this ShowProjectRelatedRepositoryRequest.
        :type search_name: str
        """
        self._search_name = search_name

    @property
    def offset(self):
        r"""Gets the offset of this ShowProjectRelatedRepositoryRequest.

        **参数解释**： 分页查询的起始位置。 **约束限制**： 不涉及。 **取值范围**： 0-2147483647 **默认取值**： 0

        :return: The offset of this ShowProjectRelatedRepositoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowProjectRelatedRepositoryRequest.

        **参数解释**： 分页查询的起始位置。 **约束限制**： 不涉及。 **取值范围**： 0-2147483647 **默认取值**： 0

        :param offset: The offset of this ShowProjectRelatedRepositoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowProjectRelatedRepositoryRequest.

        **参数解释**： 分页查询每页的数据量。 **约束限制**： 不涉及。 **取值范围**： 1-2147483647 **默认取值**： 10

        :return: The limit of this ShowProjectRelatedRepositoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowProjectRelatedRepositoryRequest.

        **参数解释**： 分页查询每页的数据量。 **约束限制**： 不涉及。 **取值范围**： 1-2147483647 **默认取值**： 10

        :param limit: The limit of this ShowProjectRelatedRepositoryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def repo_id(self):
        r"""Gets the repo_id of this ShowProjectRelatedRepositoryRequest.

        **参数解释**： 仓库ID，格式为{region}\\_{domainId}\\_{format}_{sequence}。可以从“私有依赖库首页 > 仓库概览 > 仓库地址url”中获取，最后两个“/”中间的字符串即为仓库ID。如仓库地址：https://devrepo.devcloud.abcde.abc.xyz.com/artgalaxy/abcde_09d2ca2f5080d5b60f51c00ae5bad0a0_maven_2_50/，其中abcde_09d2ca2f5080d5b60f51c00ae5bad0a0_maven_2_50即为仓库ID。 **约束限制**： 不涉及。 **取值范围**： 仓库ID格式中的format支持以下值： - npm - go - pypi - rpm - composer - maven - debian - conan - nuget - docker2 - cocoapods **默认取值**： 不涉及。

        :return: The repo_id of this ShowProjectRelatedRepositoryRequest.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this ShowProjectRelatedRepositoryRequest.

        **参数解释**： 仓库ID，格式为{region}\\_{domainId}\\_{format}_{sequence}。可以从“私有依赖库首页 > 仓库概览 > 仓库地址url”中获取，最后两个“/”中间的字符串即为仓库ID。如仓库地址：https://devrepo.devcloud.abcde.abc.xyz.com/artgalaxy/abcde_09d2ca2f5080d5b60f51c00ae5bad0a0_maven_2_50/，其中abcde_09d2ca2f5080d5b60f51c00ae5bad0a0_maven_2_50即为仓库ID。 **约束限制**： 不涉及。 **取值范围**： 仓库ID格式中的format支持以下值： - npm - go - pypi - rpm - composer - maven - debian - conan - nuget - docker2 - cocoapods **默认取值**： 不涉及。

        :param repo_id: The repo_id of this ShowProjectRelatedRepositoryRequest.
        :type repo_id: str
        """
        self._repo_id = repo_id

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
        if not isinstance(other, ShowProjectRelatedRepositoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
