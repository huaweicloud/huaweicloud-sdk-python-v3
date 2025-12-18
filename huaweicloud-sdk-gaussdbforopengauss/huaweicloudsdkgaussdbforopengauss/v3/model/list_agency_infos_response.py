# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgencyInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'is_existed': 'bool',
        'roles': 'list[AgencyRoleResult]'
    }

    attribute_map = {
        'name': 'name',
        'is_existed': 'is_existed',
        'roles': 'roles'
    }

    def __init__(self, name=None, is_existed=None, roles=None):
        r"""ListAgencyInfosResponse

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 委托名称。 **取值范围**: 不涉及。
        :type name: str
        :param is_existed: **参数解释**: 委托是否存在。 **取值范围**: true、false
        :type is_existed: bool
        :param roles: **参数解释**: 委托绑定的权限策略信息。
        :type roles: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AgencyRoleResult`]
        """
        
        super().__init__()

        self._name = None
        self._is_existed = None
        self._roles = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if is_existed is not None:
            self.is_existed = is_existed
        if roles is not None:
            self.roles = roles

    @property
    def name(self):
        r"""Gets the name of this ListAgencyInfosResponse.

        **参数解释**: 委托名称。 **取值范围**: 不涉及。

        :return: The name of this ListAgencyInfosResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAgencyInfosResponse.

        **参数解释**: 委托名称。 **取值范围**: 不涉及。

        :param name: The name of this ListAgencyInfosResponse.
        :type name: str
        """
        self._name = name

    @property
    def is_existed(self):
        r"""Gets the is_existed of this ListAgencyInfosResponse.

        **参数解释**: 委托是否存在。 **取值范围**: true、false

        :return: The is_existed of this ListAgencyInfosResponse.
        :rtype: bool
        """
        return self._is_existed

    @is_existed.setter
    def is_existed(self, is_existed):
        r"""Sets the is_existed of this ListAgencyInfosResponse.

        **参数解释**: 委托是否存在。 **取值范围**: true、false

        :param is_existed: The is_existed of this ListAgencyInfosResponse.
        :type is_existed: bool
        """
        self._is_existed = is_existed

    @property
    def roles(self):
        r"""Gets the roles of this ListAgencyInfosResponse.

        **参数解释**: 委托绑定的权限策略信息。

        :return: The roles of this ListAgencyInfosResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AgencyRoleResult`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this ListAgencyInfosResponse.

        **参数解释**: 委托绑定的权限策略信息。

        :param roles: The roles of this ListAgencyInfosResponse.
        :type roles: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AgencyRoleResult`]
        """
        self._roles = roles

    def to_dict(self):
        import warnings
        warnings.warn("ListAgencyInfosResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListAgencyInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
