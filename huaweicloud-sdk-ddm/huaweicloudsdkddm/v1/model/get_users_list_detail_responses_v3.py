# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetUsersListDetailResponsesV3:

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
        'status': 'str',
        'base_authority': 'list[str]',
        'password_lifetime': 'int',
        'password_last_changed': 'str',
        'description': 'str',
        'created': 'str',
        'databases': 'list[GetUsersListdatabaseV3]'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'base_authority': 'base_authority',
        'password_lifetime': 'password_lifetime',
        'password_last_changed': 'password_last_changed',
        'description': 'description',
        'created': 'created',
        'databases': 'databases'
    }

    def __init__(self, name=None, status=None, base_authority=None, password_lifetime=None, password_last_changed=None, description=None, created=None, databases=None):
        r"""GetUsersListDetailResponsesV3

        The model defined in huaweicloud sdk

        :param name: **参数解释**：  DDM实例账号的名称。  **取值范围**：  不涉及。
        :type name: str
        :param status: **参数解释**：  DDM实例账号的状态。  **取值范围**：  不涉及。
        :type status: str
        :param base_authority: **参数解释**：  DDM实例账号的基础权限。  **取值范围**：  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT
        :type base_authority: list[str]
        :param password_lifetime: **参数解释**：  DDM实例账号密码的有效期。  **取值范围**：  取值范围为0-65535的整数，单位为天。  0与空表示密码永不过期。
        :type password_lifetime: int
        :param password_last_changed: **参数解释**：  DDM实例账号密码最近一次的修改时间。  格式为yyyy-mm-ddThh:mm:ssZ。其中，T指定某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。  **取值范围**：  不涉及。
        :type password_last_changed: str
        :param description: **参数解释**：  账号的描述信息。  **取值范围**：  不涉及。
        :type description: str
        :param created: **参数解释**：  DDM实例账号的创建时间。  格式为yyyy-mm-ddThh:mm:ssZ。其中，T指定某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。  **取值范围**：  不涉及。
        :type created: str
        :param databases: **参数解释**：  关联的逻辑库集合。账号只对已关联的逻辑库有访问权限。  **取值范围**：  不涉及。
        :type databases: list[:class:`huaweicloudsdkddm.v1.GetUsersListdatabaseV3`]
        """
        
        

        self._name = None
        self._status = None
        self._base_authority = None
        self._password_lifetime = None
        self._password_last_changed = None
        self._description = None
        self._created = None
        self._databases = None
        self.discriminator = None

        self.name = name
        self.status = status
        self.base_authority = base_authority
        if password_lifetime is not None:
            self.password_lifetime = password_lifetime
        if password_last_changed is not None:
            self.password_last_changed = password_last_changed
        self.description = description
        self.created = created
        self.databases = databases

    @property
    def name(self):
        r"""Gets the name of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号的名称。  **取值范围**：  不涉及。

        :return: The name of this GetUsersListDetailResponsesV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号的名称。  **取值范围**：  不涉及。

        :param name: The name of this GetUsersListDetailResponsesV3.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号的状态。  **取值范围**：  不涉及。

        :return: The status of this GetUsersListDetailResponsesV3.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号的状态。  **取值范围**：  不涉及。

        :param status: The status of this GetUsersListDetailResponsesV3.
        :type status: str
        """
        self._status = status

    @property
    def base_authority(self):
        r"""Gets the base_authority of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号的基础权限。  **取值范围**：  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT

        :return: The base_authority of this GetUsersListDetailResponsesV3.
        :rtype: list[str]
        """
        return self._base_authority

    @base_authority.setter
    def base_authority(self, base_authority):
        r"""Sets the base_authority of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号的基础权限。  **取值范围**：  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT

        :param base_authority: The base_authority of this GetUsersListDetailResponsesV3.
        :type base_authority: list[str]
        """
        self._base_authority = base_authority

    @property
    def password_lifetime(self):
        r"""Gets the password_lifetime of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号密码的有效期。  **取值范围**：  取值范围为0-65535的整数，单位为天。  0与空表示密码永不过期。

        :return: The password_lifetime of this GetUsersListDetailResponsesV3.
        :rtype: int
        """
        return self._password_lifetime

    @password_lifetime.setter
    def password_lifetime(self, password_lifetime):
        r"""Sets the password_lifetime of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号密码的有效期。  **取值范围**：  取值范围为0-65535的整数，单位为天。  0与空表示密码永不过期。

        :param password_lifetime: The password_lifetime of this GetUsersListDetailResponsesV3.
        :type password_lifetime: int
        """
        self._password_lifetime = password_lifetime

    @property
    def password_last_changed(self):
        r"""Gets the password_last_changed of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号密码最近一次的修改时间。  格式为yyyy-mm-ddThh:mm:ssZ。其中，T指定某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。  **取值范围**：  不涉及。

        :return: The password_last_changed of this GetUsersListDetailResponsesV3.
        :rtype: str
        """
        return self._password_last_changed

    @password_last_changed.setter
    def password_last_changed(self, password_last_changed):
        r"""Sets the password_last_changed of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号密码最近一次的修改时间。  格式为yyyy-mm-ddThh:mm:ssZ。其中，T指定某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。  **取值范围**：  不涉及。

        :param password_last_changed: The password_last_changed of this GetUsersListDetailResponsesV3.
        :type password_last_changed: str
        """
        self._password_last_changed = password_last_changed

    @property
    def description(self):
        r"""Gets the description of this GetUsersListDetailResponsesV3.

        **参数解释**：  账号的描述信息。  **取值范围**：  不涉及。

        :return: The description of this GetUsersListDetailResponsesV3.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GetUsersListDetailResponsesV3.

        **参数解释**：  账号的描述信息。  **取值范围**：  不涉及。

        :param description: The description of this GetUsersListDetailResponsesV3.
        :type description: str
        """
        self._description = description

    @property
    def created(self):
        r"""Gets the created of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号的创建时间。  格式为yyyy-mm-ddThh:mm:ssZ。其中，T指定某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。  **取值范围**：  不涉及。

        :return: The created of this GetUsersListDetailResponsesV3.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this GetUsersListDetailResponsesV3.

        **参数解释**：  DDM实例账号的创建时间。  格式为yyyy-mm-ddThh:mm:ssZ。其中，T指定某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。  **取值范围**：  不涉及。

        :param created: The created of this GetUsersListDetailResponsesV3.
        :type created: str
        """
        self._created = created

    @property
    def databases(self):
        r"""Gets the databases of this GetUsersListDetailResponsesV3.

        **参数解释**：  关联的逻辑库集合。账号只对已关联的逻辑库有访问权限。  **取值范围**：  不涉及。

        :return: The databases of this GetUsersListDetailResponsesV3.
        :rtype: list[:class:`huaweicloudsdkddm.v1.GetUsersListdatabaseV3`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this GetUsersListDetailResponsesV3.

        **参数解释**：  关联的逻辑库集合。账号只对已关联的逻辑库有访问权限。  **取值范围**：  不涉及。

        :param databases: The databases of this GetUsersListDetailResponsesV3.
        :type databases: list[:class:`huaweicloudsdkddm.v1.GetUsersListdatabaseV3`]
        """
        self._databases = databases

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
        if not isinstance(other, GetUsersListDetailResponsesV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
