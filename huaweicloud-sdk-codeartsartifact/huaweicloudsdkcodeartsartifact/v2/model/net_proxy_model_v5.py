# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetProxyModelV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'domain_id': 'str',
        'region': 'str',
        'created_time': 'str',
        'modified_time': 'str',
        'created_user_id': 'str',
        'created_user_name': 'str',
        'modified_user_id': 'str',
        'modified_user_name': 'str',
        'id': 'int',
        'host_name': 'str',
        'host': 'str',
        'port': 'int',
        'user_name': 'str',
        'password': 'str',
        'is_default': 'int',
        'remark': 'str'
    }

    attribute_map = {
        'status': 'status',
        'domain_id': 'domain_id',
        'region': 'region',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'created_user_id': 'created_user_id',
        'created_user_name': 'created_user_name',
        'modified_user_id': 'modified_user_id',
        'modified_user_name': 'modified_user_name',
        'id': 'id',
        'host_name': 'host_name',
        'host': 'host',
        'port': 'port',
        'user_name': 'user_name',
        'password': 'password',
        'is_default': 'is_default',
        'remark': 'remark'
    }

    def __init__(self, status=None, domain_id=None, region=None, created_time=None, modified_time=None, created_user_id=None, created_user_name=None, modified_user_id=None, modified_user_name=None, id=None, host_name=None, host=None, port=None, user_name=None, password=None, is_default=None, remark=None):
        r"""NetProxyModelV5

        The model defined in huaweicloud sdk

        :param status: **参数解释**: 仓库状态。 **取值范围**: active：正常。 delete：删除。 disabled：无效。 view：私有库浏览者。 trash：废弃。 
        :type status: str
        :param domain_id: **参数解释**: 租户id。 **取值范围**: 不涉及。
        :type domain_id: str
        :param region: **参数解释**: 区域。 **取值范围**: 不涉及。
        :type region: str
        :param created_time: **参数解释**: 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。
        :type created_time: str
        :param modified_time: **参数解释**: 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。
        :type modified_time: str
        :param created_user_id: **参数解释**: 创建人id。 **取值范围**: 不涉及。
        :type created_user_id: str
        :param created_user_name: **参数解释**: 创建人。 **取值范围**: 不涉及。
        :type created_user_name: str
        :param modified_user_id: **参数解释**: 修改人id。 **取值范围**: 不涉及。
        :type modified_user_id: str
        :param modified_user_name: **参数解释**: 修改人。 **取值范围**: 不涉及。
        :type modified_user_name: str
        :param id: **参数解释**: id。 **取值范围**: 不涉及。 
        :type id: int
        :param host_name: **参数解释**: 代理名称。 **取值范围**: 不涉及。 
        :type host_name: str
        :param host: **参数解释**: 域名。 **取值范围**: 不涉及。 
        :type host: str
        :param port: **参数解释**: 端口。 **取值范围**: 不涉及。 
        :type port: int
        :param user_name: **参数解释**: 用户名。 **取值范围**: 不涉及。 
        :type user_name: str
        :param password: **参数解释**: 密码。 **取值范围**: 不涉及。 
        :type password: str
        :param is_default: **参数解释**: 是否默认。 **取值范围**: 不涉及。 
        :type is_default: int
        :param remark: **参数解释**: 备注。 **取值范围**: 不涉及。 
        :type remark: str
        """
        
        

        self._status = None
        self._domain_id = None
        self._region = None
        self._created_time = None
        self._modified_time = None
        self._created_user_id = None
        self._created_user_name = None
        self._modified_user_id = None
        self._modified_user_name = None
        self._id = None
        self._host_name = None
        self._host = None
        self._port = None
        self._user_name = None
        self._password = None
        self._is_default = None
        self._remark = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if domain_id is not None:
            self.domain_id = domain_id
        if region is not None:
            self.region = region
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if created_user_id is not None:
            self.created_user_id = created_user_id
        if created_user_name is not None:
            self.created_user_name = created_user_name
        if modified_user_id is not None:
            self.modified_user_id = modified_user_id
        if modified_user_name is not None:
            self.modified_user_name = modified_user_name
        if id is not None:
            self.id = id
        if host_name is not None:
            self.host_name = host_name
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if is_default is not None:
            self.is_default = is_default
        if remark is not None:
            self.remark = remark

    @property
    def status(self):
        r"""Gets the status of this NetProxyModelV5.

        **参数解释**: 仓库状态。 **取值范围**: active：正常。 delete：删除。 disabled：无效。 view：私有库浏览者。 trash：废弃。 

        :return: The status of this NetProxyModelV5.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NetProxyModelV5.

        **参数解释**: 仓库状态。 **取值范围**: active：正常。 delete：删除。 disabled：无效。 view：私有库浏览者。 trash：废弃。 

        :param status: The status of this NetProxyModelV5.
        :type status: str
        """
        self._status = status

    @property
    def domain_id(self):
        r"""Gets the domain_id of this NetProxyModelV5.

        **参数解释**: 租户id。 **取值范围**: 不涉及。

        :return: The domain_id of this NetProxyModelV5.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this NetProxyModelV5.

        **参数解释**: 租户id。 **取值范围**: 不涉及。

        :param domain_id: The domain_id of this NetProxyModelV5.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region(self):
        r"""Gets the region of this NetProxyModelV5.

        **参数解释**: 区域。 **取值范围**: 不涉及。

        :return: The region of this NetProxyModelV5.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this NetProxyModelV5.

        **参数解释**: 区域。 **取值范围**: 不涉及。

        :param region: The region of this NetProxyModelV5.
        :type region: str
        """
        self._region = region

    @property
    def created_time(self):
        r"""Gets the created_time of this NetProxyModelV5.

        **参数解释**: 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :return: The created_time of this NetProxyModelV5.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this NetProxyModelV5.

        **参数解释**: 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :param created_time: The created_time of this NetProxyModelV5.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this NetProxyModelV5.

        **参数解释**: 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :return: The modified_time of this NetProxyModelV5.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this NetProxyModelV5.

        **参数解释**: 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :param modified_time: The modified_time of this NetProxyModelV5.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def created_user_id(self):
        r"""Gets the created_user_id of this NetProxyModelV5.

        **参数解释**: 创建人id。 **取值范围**: 不涉及。

        :return: The created_user_id of this NetProxyModelV5.
        :rtype: str
        """
        return self._created_user_id

    @created_user_id.setter
    def created_user_id(self, created_user_id):
        r"""Sets the created_user_id of this NetProxyModelV5.

        **参数解释**: 创建人id。 **取值范围**: 不涉及。

        :param created_user_id: The created_user_id of this NetProxyModelV5.
        :type created_user_id: str
        """
        self._created_user_id = created_user_id

    @property
    def created_user_name(self):
        r"""Gets the created_user_name of this NetProxyModelV5.

        **参数解释**: 创建人。 **取值范围**: 不涉及。

        :return: The created_user_name of this NetProxyModelV5.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        r"""Sets the created_user_name of this NetProxyModelV5.

        **参数解释**: 创建人。 **取值范围**: 不涉及。

        :param created_user_name: The created_user_name of this NetProxyModelV5.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def modified_user_id(self):
        r"""Gets the modified_user_id of this NetProxyModelV5.

        **参数解释**: 修改人id。 **取值范围**: 不涉及。

        :return: The modified_user_id of this NetProxyModelV5.
        :rtype: str
        """
        return self._modified_user_id

    @modified_user_id.setter
    def modified_user_id(self, modified_user_id):
        r"""Sets the modified_user_id of this NetProxyModelV5.

        **参数解释**: 修改人id。 **取值范围**: 不涉及。

        :param modified_user_id: The modified_user_id of this NetProxyModelV5.
        :type modified_user_id: str
        """
        self._modified_user_id = modified_user_id

    @property
    def modified_user_name(self):
        r"""Gets the modified_user_name of this NetProxyModelV5.

        **参数解释**: 修改人。 **取值范围**: 不涉及。

        :return: The modified_user_name of this NetProxyModelV5.
        :rtype: str
        """
        return self._modified_user_name

    @modified_user_name.setter
    def modified_user_name(self, modified_user_name):
        r"""Sets the modified_user_name of this NetProxyModelV5.

        **参数解释**: 修改人。 **取值范围**: 不涉及。

        :param modified_user_name: The modified_user_name of this NetProxyModelV5.
        :type modified_user_name: str
        """
        self._modified_user_name = modified_user_name

    @property
    def id(self):
        r"""Gets the id of this NetProxyModelV5.

        **参数解释**: id。 **取值范围**: 不涉及。 

        :return: The id of this NetProxyModelV5.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NetProxyModelV5.

        **参数解释**: id。 **取值范围**: 不涉及。 

        :param id: The id of this NetProxyModelV5.
        :type id: int
        """
        self._id = id

    @property
    def host_name(self):
        r"""Gets the host_name of this NetProxyModelV5.

        **参数解释**: 代理名称。 **取值范围**: 不涉及。 

        :return: The host_name of this NetProxyModelV5.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this NetProxyModelV5.

        **参数解释**: 代理名称。 **取值范围**: 不涉及。 

        :param host_name: The host_name of this NetProxyModelV5.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host(self):
        r"""Gets the host of this NetProxyModelV5.

        **参数解释**: 域名。 **取值范围**: 不涉及。 

        :return: The host of this NetProxyModelV5.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this NetProxyModelV5.

        **参数解释**: 域名。 **取值范围**: 不涉及。 

        :param host: The host of this NetProxyModelV5.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        r"""Gets the port of this NetProxyModelV5.

        **参数解释**: 端口。 **取值范围**: 不涉及。 

        :return: The port of this NetProxyModelV5.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this NetProxyModelV5.

        **参数解释**: 端口。 **取值范围**: 不涉及。 

        :param port: The port of this NetProxyModelV5.
        :type port: int
        """
        self._port = port

    @property
    def user_name(self):
        r"""Gets the user_name of this NetProxyModelV5.

        **参数解释**: 用户名。 **取值范围**: 不涉及。 

        :return: The user_name of this NetProxyModelV5.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this NetProxyModelV5.

        **参数解释**: 用户名。 **取值范围**: 不涉及。 

        :param user_name: The user_name of this NetProxyModelV5.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        r"""Gets the password of this NetProxyModelV5.

        **参数解释**: 密码。 **取值范围**: 不涉及。 

        :return: The password of this NetProxyModelV5.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this NetProxyModelV5.

        **参数解释**: 密码。 **取值范围**: 不涉及。 

        :param password: The password of this NetProxyModelV5.
        :type password: str
        """
        self._password = password

    @property
    def is_default(self):
        r"""Gets the is_default of this NetProxyModelV5.

        **参数解释**: 是否默认。 **取值范围**: 不涉及。 

        :return: The is_default of this NetProxyModelV5.
        :rtype: int
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this NetProxyModelV5.

        **参数解释**: 是否默认。 **取值范围**: 不涉及。 

        :param is_default: The is_default of this NetProxyModelV5.
        :type is_default: int
        """
        self._is_default = is_default

    @property
    def remark(self):
        r"""Gets the remark of this NetProxyModelV5.

        **参数解释**: 备注。 **取值范围**: 不涉及。 

        :return: The remark of this NetProxyModelV5.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this NetProxyModelV5.

        **参数解释**: 备注。 **取值范围**: 不涉及。 

        :param remark: The remark of this NetProxyModelV5.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, NetProxyModelV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
