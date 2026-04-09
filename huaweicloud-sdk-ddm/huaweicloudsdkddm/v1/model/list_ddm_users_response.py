# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDdmUsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'users': 'list[GetUsersListDetailResponsesV3]',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'users': 'users',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, users=None, offset=None, limit=None, total=None):
        r"""ListDdmUsersResponse

        The model defined in huaweicloud sdk

        :param users: **参数解释**：  DDM实例账号相关信息的集合。  **取值范围**：  不涉及
        :type users: list[:class:`huaweicloudsdkddm.v1.GetUsersListDetailResponsesV3`]
        :param offset: **参数解释**：  分页参数: 起始值。  **取值范围**：   大于等于0。
        :type offset: int
        :param limit: **参数解释**：  分页参数: 每页记录数。  **取值范围**：  大于0且小于等于128。
        :type limit: int
        :param total: **参数解释**：  总记录数。  **取值范围**：  不涉及。
        :type total: int
        """
        
        super().__init__()

        self._users = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def users(self):
        r"""Gets the users of this ListDdmUsersResponse.

        **参数解释**：  DDM实例账号相关信息的集合。  **取值范围**：  不涉及

        :return: The users of this ListDdmUsersResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.GetUsersListDetailResponsesV3`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this ListDdmUsersResponse.

        **参数解释**：  DDM实例账号相关信息的集合。  **取值范围**：  不涉及

        :param users: The users of this ListDdmUsersResponse.
        :type users: list[:class:`huaweicloudsdkddm.v1.GetUsersListDetailResponsesV3`]
        """
        self._users = users

    @property
    def offset(self):
        r"""Gets the offset of this ListDdmUsersResponse.

        **参数解释**：  分页参数: 起始值。  **取值范围**：   大于等于0。

        :return: The offset of this ListDdmUsersResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDdmUsersResponse.

        **参数解释**：  分页参数: 起始值。  **取值范围**：   大于等于0。

        :param offset: The offset of this ListDdmUsersResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDdmUsersResponse.

        **参数解释**：  分页参数: 每页记录数。  **取值范围**：  大于0且小于等于128。

        :return: The limit of this ListDdmUsersResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDdmUsersResponse.

        **参数解释**：  分页参数: 每页记录数。  **取值范围**：  大于0且小于等于128。

        :param limit: The limit of this ListDdmUsersResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this ListDdmUsersResponse.

        **参数解释**：  总记录数。  **取值范围**：  不涉及。

        :return: The total of this ListDdmUsersResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDdmUsersResponse.

        **参数解释**：  总记录数。  **取值范围**：  不涉及。

        :param total: The total of this ListDdmUsersResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListDdmUsersResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDdmUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
