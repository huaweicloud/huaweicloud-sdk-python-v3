# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoUserPrivilegeResult:

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
        'list': 'list[RepoUserPrivilegeV5]'
    }

    attribute_map = {
        'total': 'total',
        'list': 'list'
    }

    def __init__(self, total=None, list=None):
        r"""RepoUserPrivilegeResult

        The model defined in huaweicloud sdk

        :param total: **参数解释**: 用户数量。 **取值范围**: 不涉及。 
        :type total: int
        :param list: **参数解释**: 用户列表。 **取值范围**: 不涉及。 
        :type list: list[:class:`huaweicloudsdkcodeartsartifact.v2.RepoUserPrivilegeV5`]
        """
        
        

        self._total = None
        self._list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if list is not None:
            self.list = list

    @property
    def total(self):
        r"""Gets the total of this RepoUserPrivilegeResult.

        **参数解释**: 用户数量。 **取值范围**: 不涉及。 

        :return: The total of this RepoUserPrivilegeResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this RepoUserPrivilegeResult.

        **参数解释**: 用户数量。 **取值范围**: 不涉及。 

        :param total: The total of this RepoUserPrivilegeResult.
        :type total: int
        """
        self._total = total

    @property
    def list(self):
        r"""Gets the list of this RepoUserPrivilegeResult.

        **参数解释**: 用户列表。 **取值范围**: 不涉及。 

        :return: The list of this RepoUserPrivilegeResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsartifact.v2.RepoUserPrivilegeV5`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this RepoUserPrivilegeResult.

        **参数解释**: 用户列表。 **取值范围**: 不涉及。 

        :param list: The list of this RepoUserPrivilegeResult.
        :type list: list[:class:`huaweicloudsdkcodeartsartifact.v2.RepoUserPrivilegeV5`]
        """
        self._list = list

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
        if not isinstance(other, RepoUserPrivilegeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
