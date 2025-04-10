# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionSetDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_date': 'int',
        'description': 'str',
        'name': 'str',
        'permission_set_id': 'str',
        'relay_state': 'str',
        'session_duration': 'str',
        'permission_urn': 'str'
    }

    attribute_map = {
        'created_date': 'created_date',
        'description': 'description',
        'name': 'name',
        'permission_set_id': 'permission_set_id',
        'relay_state': 'relay_state',
        'session_duration': 'session_duration',
        'permission_urn': 'permission_urn'
    }

    def __init__(self, created_date=None, description=None, name=None, permission_set_id=None, relay_state=None, session_duration=None, permission_urn=None):
        r"""PermissionSetDto

        The model defined in huaweicloud sdk

        :param created_date: 权限集的创建时间
        :type created_date: int
        :param description: 权限集的描述
        :type description: str
        :param name: 权限集的名称
        :type name: str
        :param permission_set_id: 权限集的唯一标识
        :type permission_set_id: str
        :param relay_state: 用于在联合身份验证过程中重定向应用程序中的用户
        :type relay_state: str
        :param session_duration: 应用程序用户会话在ISO-8601标准中有效的时间长度
        :type session_duration: str
        :param permission_urn: 权限集的统一资源名称（URN）
        :type permission_urn: str
        """
        
        

        self._created_date = None
        self._description = None
        self._name = None
        self._permission_set_id = None
        self._relay_state = None
        self._session_duration = None
        self._permission_urn = None
        self.discriminator = None

        if created_date is not None:
            self.created_date = created_date
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if relay_state is not None:
            self.relay_state = relay_state
        if session_duration is not None:
            self.session_duration = session_duration
        if permission_urn is not None:
            self.permission_urn = permission_urn

    @property
    def created_date(self):
        r"""Gets the created_date of this PermissionSetDto.

        权限集的创建时间

        :return: The created_date of this PermissionSetDto.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this PermissionSetDto.

        权限集的创建时间

        :param created_date: The created_date of this PermissionSetDto.
        :type created_date: int
        """
        self._created_date = created_date

    @property
    def description(self):
        r"""Gets the description of this PermissionSetDto.

        权限集的描述

        :return: The description of this PermissionSetDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PermissionSetDto.

        权限集的描述

        :param description: The description of this PermissionSetDto.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this PermissionSetDto.

        权限集的名称

        :return: The name of this PermissionSetDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PermissionSetDto.

        权限集的名称

        :param name: The name of this PermissionSetDto.
        :type name: str
        """
        self._name = name

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this PermissionSetDto.

        权限集的唯一标识

        :return: The permission_set_id of this PermissionSetDto.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this PermissionSetDto.

        权限集的唯一标识

        :param permission_set_id: The permission_set_id of this PermissionSetDto.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def relay_state(self):
        r"""Gets the relay_state of this PermissionSetDto.

        用于在联合身份验证过程中重定向应用程序中的用户

        :return: The relay_state of this PermissionSetDto.
        :rtype: str
        """
        return self._relay_state

    @relay_state.setter
    def relay_state(self, relay_state):
        r"""Sets the relay_state of this PermissionSetDto.

        用于在联合身份验证过程中重定向应用程序中的用户

        :param relay_state: The relay_state of this PermissionSetDto.
        :type relay_state: str
        """
        self._relay_state = relay_state

    @property
    def session_duration(self):
        r"""Gets the session_duration of this PermissionSetDto.

        应用程序用户会话在ISO-8601标准中有效的时间长度

        :return: The session_duration of this PermissionSetDto.
        :rtype: str
        """
        return self._session_duration

    @session_duration.setter
    def session_duration(self, session_duration):
        r"""Sets the session_duration of this PermissionSetDto.

        应用程序用户会话在ISO-8601标准中有效的时间长度

        :param session_duration: The session_duration of this PermissionSetDto.
        :type session_duration: str
        """
        self._session_duration = session_duration

    @property
    def permission_urn(self):
        r"""Gets the permission_urn of this PermissionSetDto.

        权限集的统一资源名称（URN）

        :return: The permission_urn of this PermissionSetDto.
        :rtype: str
        """
        return self._permission_urn

    @permission_urn.setter
    def permission_urn(self, permission_urn):
        r"""Sets the permission_urn of this PermissionSetDto.

        权限集的统一资源名称（URN）

        :param permission_urn: The permission_urn of this PermissionSetDto.
        :type permission_urn: str
        """
        self._permission_urn = permission_urn

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PermissionSetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
