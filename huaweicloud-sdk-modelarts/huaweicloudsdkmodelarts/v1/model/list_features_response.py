# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFeaturesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_at': 'int',
        'enabled': 'bool',
        'id': 'str',
        'name': 'str',
        'quota': 'int',
        'used': 'int',
        'update_at': 'int',
        'user_id': 'str'
    }

    attribute_map = {
        'create_at': 'create_at',
        'enabled': 'enabled',
        'id': 'id',
        'name': 'name',
        'quota': 'quota',
        'used': 'used',
        'update_at': 'update_at',
        'user_id': 'user_id'
    }

    def __init__(self, create_at=None, enabled=None, id=None, name=None, quota=None, used=None, update_at=None, user_id=None):
        r"""ListFeaturesResponse

        The model defined in huaweicloud sdk

        :param create_at: **参数解释**：实例创建的时间，UTC毫秒。 **取值范围**：不涉及。
        :type create_at: int
        :param enabled: **参数解释**：特性开关。 **取值范围**：布尔类型： - true：开启。 - false：未开启。
        :type enabled: bool
        :param id: **参数解释**：特性ID。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：特性名称。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：用户显式创建的Notebook实例。
        :type name: str
        :param quota: **参数解释**：特性配额。 **取值范围**：不涉及。
        :type quota: int
        :param used: **参数解释**：特性已使用额度。 **取值范围**：不涉及。
        :type used: int
        :param update_at: **参数解释**：实例最后更新的时间，UTC毫秒。 **取值范围**：不涉及。
        :type update_at: int
        :param user_id: **参数解释**：用户ID。 **取值范围**：不涉及。
        :type user_id: str
        """
        
        super().__init__()

        self._create_at = None
        self._enabled = None
        self._id = None
        self._name = None
        self._quota = None
        self._used = None
        self._update_at = None
        self._user_id = None
        self.discriminator = None

        if create_at is not None:
            self.create_at = create_at
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used
        if update_at is not None:
            self.update_at = update_at
        if user_id is not None:
            self.user_id = user_id

    @property
    def create_at(self):
        r"""Gets the create_at of this ListFeaturesResponse.

        **参数解释**：实例创建的时间，UTC毫秒。 **取值范围**：不涉及。

        :return: The create_at of this ListFeaturesResponse.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ListFeaturesResponse.

        **参数解释**：实例创建的时间，UTC毫秒。 **取值范围**：不涉及。

        :param create_at: The create_at of this ListFeaturesResponse.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def enabled(self):
        r"""Gets the enabled of this ListFeaturesResponse.

        **参数解释**：特性开关。 **取值范围**：布尔类型： - true：开启。 - false：未开启。

        :return: The enabled of this ListFeaturesResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListFeaturesResponse.

        **参数解释**：特性开关。 **取值范围**：布尔类型： - true：开启。 - false：未开启。

        :param enabled: The enabled of this ListFeaturesResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        r"""Gets the id of this ListFeaturesResponse.

        **参数解释**：特性ID。 **取值范围**：不涉及。

        :return: The id of this ListFeaturesResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListFeaturesResponse.

        **参数解释**：特性ID。 **取值范围**：不涉及。

        :param id: The id of this ListFeaturesResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListFeaturesResponse.

        **参数解释**：特性名称。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：用户显式创建的Notebook实例。

        :return: The name of this ListFeaturesResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFeaturesResponse.

        **参数解释**：特性名称。 **取值范围**：枚举类型，取值如下： - NOTEBOOK：用户显式创建的Notebook实例。

        :param name: The name of this ListFeaturesResponse.
        :type name: str
        """
        self._name = name

    @property
    def quota(self):
        r"""Gets the quota of this ListFeaturesResponse.

        **参数解释**：特性配额。 **取值范围**：不涉及。

        :return: The quota of this ListFeaturesResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ListFeaturesResponse.

        **参数解释**：特性配额。 **取值范围**：不涉及。

        :param quota: The quota of this ListFeaturesResponse.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this ListFeaturesResponse.

        **参数解释**：特性已使用额度。 **取值范围**：不涉及。

        :return: The used of this ListFeaturesResponse.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this ListFeaturesResponse.

        **参数解释**：特性已使用额度。 **取值范围**：不涉及。

        :param used: The used of this ListFeaturesResponse.
        :type used: int
        """
        self._used = used

    @property
    def update_at(self):
        r"""Gets the update_at of this ListFeaturesResponse.

        **参数解释**：实例最后更新的时间，UTC毫秒。 **取值范围**：不涉及。

        :return: The update_at of this ListFeaturesResponse.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ListFeaturesResponse.

        **参数解释**：实例最后更新的时间，UTC毫秒。 **取值范围**：不涉及。

        :param update_at: The update_at of this ListFeaturesResponse.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def user_id(self):
        r"""Gets the user_id of this ListFeaturesResponse.

        **参数解释**：用户ID。 **取值范围**：不涉及。

        :return: The user_id of this ListFeaturesResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListFeaturesResponse.

        **参数解释**：用户ID。 **取值范围**：不涉及。

        :param user_id: The user_id of this ListFeaturesResponse.
        :type user_id: str
        """
        self._user_id = user_id

    def to_dict(self):
        import warnings
        warnings.warn("ListFeaturesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListFeaturesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
