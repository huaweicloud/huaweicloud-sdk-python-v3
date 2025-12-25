# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllRepositoriesResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'repositories': 'list[RepositoryBasicDO]'
    }

    attribute_map = {
        'total': 'total',
        'repositories': 'repositories'
    }

    def __init__(self, total=None, repositories=None):
        r"""ListAllRepositoriesResult

        The model defined in huaweicloud sdk

        :param total: **参数解释**： 总数。 **取值范围**： 不涉及。 
        :type total: int
        :param repositories: **参数解释**： 仓库详情列表。 **取值范围**： 不涉及。 
        :type repositories: list[:class:`huaweicloudsdkcodeartsartifact.v2.RepositoryBasicDO`]
        """
        
        

        self._total = None
        self._repositories = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if repositories is not None:
            self.repositories = repositories

    @property
    def total(self):
        r"""Gets the total of this ListAllRepositoriesResult.

        **参数解释**： 总数。 **取值范围**： 不涉及。 

        :return: The total of this ListAllRepositoriesResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAllRepositoriesResult.

        **参数解释**： 总数。 **取值范围**： 不涉及。 

        :param total: The total of this ListAllRepositoriesResult.
        :type total: int
        """
        self._total = total

    @property
    def repositories(self):
        r"""Gets the repositories of this ListAllRepositoriesResult.

        **参数解释**： 仓库详情列表。 **取值范围**： 不涉及。 

        :return: The repositories of this ListAllRepositoriesResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsartifact.v2.RepositoryBasicDO`]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        r"""Sets the repositories of this ListAllRepositoriesResult.

        **参数解释**： 仓库详情列表。 **取值范围**： 不涉及。 

        :param repositories: The repositories of this ListAllRepositoriesResult.
        :type repositories: list[:class:`huaweicloudsdkcodeartsartifact.v2.RepositoryBasicDO`]
        """
        self._repositories = repositories

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
        if not isinstance(other, ListAllRepositoriesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
