# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetUsersListDetailResponses:

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
        'password_last_changed': 'int',
        'extend_authority': 'list[str]',
        'description': 'str',
        'created': 'int',
        'databases': 'list[GetUsersListdatabase]'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'base_authority': 'base_authority',
        'password_last_changed': 'password_last_changed',
        'extend_authority': 'extend_authority',
        'description': 'description',
        'created': 'created',
        'databases': 'databases'
    }

    def __init__(self, name=None, status=None, base_authority=None, password_last_changed=None, extend_authority=None, description=None, created=None, databases=None):
        r"""GetUsersListDetailResponses

        The model defined in huaweicloud sdk

        :param name: DDM实例帐号名称。
        :type name: str
        :param status: DDM实例帐号状态。
        :type status: str
        :param base_authority: DDM实例帐号的基础权限。  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT
        :type base_authority: list[str]
        :param password_last_changed: DDM实例账号的密码修改时间，UNIX时间戳格式。
        :type password_last_changed: int
        :param extend_authority: DDM实例帐号的扩展权限。2021年8月开始不支持该字段，9月会去掉该字段。  取值为：fulltableDelete、fulltableSelect、fulltableUpdate
        :type extend_authority: list[str]
        :param description: DDM实例帐号的描述。
        :type description: str
        :param created: DDM实例帐号的创建时间，UNIX时间戳格式。
        :type created: int
        :param databases: 关联的逻辑库的集合。
        :type databases: list[:class:`huaweicloudsdkddm.v1.GetUsersListdatabase`]
        """
        
        

        self._name = None
        self._status = None
        self._base_authority = None
        self._password_last_changed = None
        self._extend_authority = None
        self._description = None
        self._created = None
        self._databases = None
        self.discriminator = None

        self.name = name
        self.status = status
        self.base_authority = base_authority
        if password_last_changed is not None:
            self.password_last_changed = password_last_changed
        if extend_authority is not None:
            self.extend_authority = extend_authority
        self.description = description
        self.created = created
        self.databases = databases

    @property
    def name(self):
        r"""Gets the name of this GetUsersListDetailResponses.

        DDM实例帐号名称。

        :return: The name of this GetUsersListDetailResponses.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetUsersListDetailResponses.

        DDM实例帐号名称。

        :param name: The name of this GetUsersListDetailResponses.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this GetUsersListDetailResponses.

        DDM实例帐号状态。

        :return: The status of this GetUsersListDetailResponses.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetUsersListDetailResponses.

        DDM实例帐号状态。

        :param status: The status of this GetUsersListDetailResponses.
        :type status: str
        """
        self._status = status

    @property
    def base_authority(self):
        r"""Gets the base_authority of this GetUsersListDetailResponses.

        DDM实例帐号的基础权限。  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT

        :return: The base_authority of this GetUsersListDetailResponses.
        :rtype: list[str]
        """
        return self._base_authority

    @base_authority.setter
    def base_authority(self, base_authority):
        r"""Sets the base_authority of this GetUsersListDetailResponses.

        DDM实例帐号的基础权限。  取值为：CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT

        :param base_authority: The base_authority of this GetUsersListDetailResponses.
        :type base_authority: list[str]
        """
        self._base_authority = base_authority

    @property
    def password_last_changed(self):
        r"""Gets the password_last_changed of this GetUsersListDetailResponses.

        DDM实例账号的密码修改时间，UNIX时间戳格式。

        :return: The password_last_changed of this GetUsersListDetailResponses.
        :rtype: int
        """
        return self._password_last_changed

    @password_last_changed.setter
    def password_last_changed(self, password_last_changed):
        r"""Sets the password_last_changed of this GetUsersListDetailResponses.

        DDM实例账号的密码修改时间，UNIX时间戳格式。

        :param password_last_changed: The password_last_changed of this GetUsersListDetailResponses.
        :type password_last_changed: int
        """
        self._password_last_changed = password_last_changed

    @property
    def extend_authority(self):
        r"""Gets the extend_authority of this GetUsersListDetailResponses.

        DDM实例帐号的扩展权限。2021年8月开始不支持该字段，9月会去掉该字段。  取值为：fulltableDelete、fulltableSelect、fulltableUpdate

        :return: The extend_authority of this GetUsersListDetailResponses.
        :rtype: list[str]
        """
        return self._extend_authority

    @extend_authority.setter
    def extend_authority(self, extend_authority):
        r"""Sets the extend_authority of this GetUsersListDetailResponses.

        DDM实例帐号的扩展权限。2021年8月开始不支持该字段，9月会去掉该字段。  取值为：fulltableDelete、fulltableSelect、fulltableUpdate

        :param extend_authority: The extend_authority of this GetUsersListDetailResponses.
        :type extend_authority: list[str]
        """
        self._extend_authority = extend_authority

    @property
    def description(self):
        r"""Gets the description of this GetUsersListDetailResponses.

        DDM实例帐号的描述。

        :return: The description of this GetUsersListDetailResponses.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GetUsersListDetailResponses.

        DDM实例帐号的描述。

        :param description: The description of this GetUsersListDetailResponses.
        :type description: str
        """
        self._description = description

    @property
    def created(self):
        r"""Gets the created of this GetUsersListDetailResponses.

        DDM实例帐号的创建时间，UNIX时间戳格式。

        :return: The created of this GetUsersListDetailResponses.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this GetUsersListDetailResponses.

        DDM实例帐号的创建时间，UNIX时间戳格式。

        :param created: The created of this GetUsersListDetailResponses.
        :type created: int
        """
        self._created = created

    @property
    def databases(self):
        r"""Gets the databases of this GetUsersListDetailResponses.

        关联的逻辑库的集合。

        :return: The databases of this GetUsersListDetailResponses.
        :rtype: list[:class:`huaweicloudsdkddm.v1.GetUsersListdatabase`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this GetUsersListDetailResponses.

        关联的逻辑库的集合。

        :param databases: The databases of this GetUsersListDetailResponses.
        :type databases: list[:class:`huaweicloudsdkddm.v1.GetUsersListdatabase`]
        """
        self._databases = databases

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
        if not isinstance(other, GetUsersListDetailResponses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
