# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'password': 'str',
        'list': 'list[UserAccountVO]',
        'user_roles': 'list[UserRoleVO]',
        'is_set_password': 'bool',
        'is_migrate_user': 'bool',
        'is_sync_object_privilege': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'password': 'password',
        'list': 'list',
        'user_roles': 'user_roles',
        'is_set_password': 'is_set_password',
        'is_migrate_user': 'is_migrate_user',
        'is_sync_object_privilege': 'is_sync_object_privilege'
    }

    def __init__(self, job_id=None, password=None, list=None, user_roles=None, is_set_password=None, is_migrate_user=None, is_sync_object_privilege=None):
        """UpdateUserReq

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param password: 全局密码。
        :type password: str
        :param list: 用户迁移信息，迁移用户时必填
        :type list: list[:class:`huaweicloudsdkdrs.v3.UserAccountVO`]
        :param user_roles: 角色迁移信息，迁移用户时必填
        :type user_roles: list[:class:`huaweicloudsdkdrs.v3.UserRoleVO`]
        :param is_set_password: 是否设置密码
        :type is_set_password: bool
        :param is_migrate_user: 是否迁移用户
        :type is_migrate_user: bool
        :param is_sync_object_privilege: 是否同步权限，不填默认为false，PG同步使用。
        :type is_sync_object_privilege: bool
        """
        
        

        self._job_id = None
        self._password = None
        self._list = None
        self._user_roles = None
        self._is_set_password = None
        self._is_migrate_user = None
        self._is_sync_object_privilege = None
        self.discriminator = None

        self.job_id = job_id
        if password is not None:
            self.password = password
        if list is not None:
            self.list = list
        if user_roles is not None:
            self.user_roles = user_roles
        self.is_set_password = is_set_password
        self.is_migrate_user = is_migrate_user
        if is_sync_object_privilege is not None:
            self.is_sync_object_privilege = is_sync_object_privilege

    @property
    def job_id(self):
        """Gets the job_id of this UpdateUserReq.

        任务ID

        :return: The job_id of this UpdateUserReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateUserReq.

        任务ID

        :param job_id: The job_id of this UpdateUserReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def password(self):
        """Gets the password of this UpdateUserReq.

        全局密码。

        :return: The password of this UpdateUserReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateUserReq.

        全局密码。

        :param password: The password of this UpdateUserReq.
        :type password: str
        """
        self._password = password

    @property
    def list(self):
        """Gets the list of this UpdateUserReq.

        用户迁移信息，迁移用户时必填

        :return: The list of this UpdateUserReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.UserAccountVO`]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this UpdateUserReq.

        用户迁移信息，迁移用户时必填

        :param list: The list of this UpdateUserReq.
        :type list: list[:class:`huaweicloudsdkdrs.v3.UserAccountVO`]
        """
        self._list = list

    @property
    def user_roles(self):
        """Gets the user_roles of this UpdateUserReq.

        角色迁移信息，迁移用户时必填

        :return: The user_roles of this UpdateUserReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.UserRoleVO`]
        """
        return self._user_roles

    @user_roles.setter
    def user_roles(self, user_roles):
        """Sets the user_roles of this UpdateUserReq.

        角色迁移信息，迁移用户时必填

        :param user_roles: The user_roles of this UpdateUserReq.
        :type user_roles: list[:class:`huaweicloudsdkdrs.v3.UserRoleVO`]
        """
        self._user_roles = user_roles

    @property
    def is_set_password(self):
        """Gets the is_set_password of this UpdateUserReq.

        是否设置密码

        :return: The is_set_password of this UpdateUserReq.
        :rtype: bool
        """
        return self._is_set_password

    @is_set_password.setter
    def is_set_password(self, is_set_password):
        """Sets the is_set_password of this UpdateUserReq.

        是否设置密码

        :param is_set_password: The is_set_password of this UpdateUserReq.
        :type is_set_password: bool
        """
        self._is_set_password = is_set_password

    @property
    def is_migrate_user(self):
        """Gets the is_migrate_user of this UpdateUserReq.

        是否迁移用户

        :return: The is_migrate_user of this UpdateUserReq.
        :rtype: bool
        """
        return self._is_migrate_user

    @is_migrate_user.setter
    def is_migrate_user(self, is_migrate_user):
        """Sets the is_migrate_user of this UpdateUserReq.

        是否迁移用户

        :param is_migrate_user: The is_migrate_user of this UpdateUserReq.
        :type is_migrate_user: bool
        """
        self._is_migrate_user = is_migrate_user

    @property
    def is_sync_object_privilege(self):
        """Gets the is_sync_object_privilege of this UpdateUserReq.

        是否同步权限，不填默认为false，PG同步使用。

        :return: The is_sync_object_privilege of this UpdateUserReq.
        :rtype: bool
        """
        return self._is_sync_object_privilege

    @is_sync_object_privilege.setter
    def is_sync_object_privilege(self, is_sync_object_privilege):
        """Sets the is_sync_object_privilege of this UpdateUserReq.

        是否同步权限，不填默认为false，PG同步使用。

        :param is_sync_object_privilege: The is_sync_object_privilege of this UpdateUserReq.
        :type is_sync_object_privilege: bool
        """
        self._is_sync_object_privilege = is_sync_object_privilege

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
        if not isinstance(other, UpdateUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
