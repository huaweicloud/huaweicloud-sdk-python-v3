# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'list[str]',
        'computer_name': 'str',
        'desktop_ip': 'str',
        'sids': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'site_id': 'str',
        'pool_id': 'str',
        'enterprise_project_id': 'str',
        'desktop_type': 'str',
        'is_share_desktop': 'bool',
        'subnet_id': 'str',
        'status': 'str',
        'desktop_id': 'list[str]',
        'tag': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'computer_name': 'computer_name',
        'desktop_ip': 'desktop_ip',
        'sids': 'sids',
        'offset': 'offset',
        'limit': 'limit',
        'site_id': 'site_id',
        'pool_id': 'pool_id',
        'enterprise_project_id': 'enterprise_project_id',
        'desktop_type': 'desktop_type',
        'is_share_desktop': 'is_share_desktop',
        'subnet_id': 'subnet_id',
        'status': 'status',
        'desktop_id': 'desktop_id',
        'tag': 'tag'
    }

    def __init__(self, user_name=None, computer_name=None, desktop_ip=None, sids=None, offset=None, limit=None, site_id=None, pool_id=None, enterprise_project_id=None, desktop_type=None, is_share_desktop=None, subnet_id=None, status=None, desktop_id=None, tag=None):
        """ListDesktopsRequest

        The model defined in huaweicloud sdk

        :param user_name: 桌面所属用户。
        :type user_name: list[str]
        :param computer_name: 桌面名。
        :type computer_name: str
        :param desktop_ip: 桌面IP地址。
        :type desktop_ip: str
        :param sids: 桌面的sid列表，一次只能查询20个sid。
        :type sids: list[str]
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，取值范围0-1000，默认值1000。
        :type limit: int
        :param site_id: 用于筛选指定站点下的桌面列表
        :type site_id: str
        :param pool_id: 桌面池ID,多个桌面池ID用逗号隔开。
        :type pool_id: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param desktop_type: 桌面类型，为空时查所有桌面。查询多个类型时用,隔开。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等。 - SHARED: 多用户共享桌面。
        :type desktop_type: str
        :param is_share_desktop: 是否为协同桌面
        :type is_share_desktop: bool
        :param subnet_id: 桌面的子网ID。
        :type subnet_id: str
        :param status: 桌面的运行状态。
        :type status: str
        :param desktop_id: 桌面id，当前最多支持100个桌面id进行查询。
        :type desktop_id: list[str]
        :param tag: 桌面的标签。样例： - key1&#x3D;value1。 - key1&#x3D;value1，key2&#x3D;value2。
        :type tag: str
        """
        
        

        self._user_name = None
        self._computer_name = None
        self._desktop_ip = None
        self._sids = None
        self._offset = None
        self._limit = None
        self._site_id = None
        self._pool_id = None
        self._enterprise_project_id = None
        self._desktop_type = None
        self._is_share_desktop = None
        self._subnet_id = None
        self._status = None
        self._desktop_id = None
        self._tag = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if computer_name is not None:
            self.computer_name = computer_name
        if desktop_ip is not None:
            self.desktop_ip = desktop_ip
        if sids is not None:
            self.sids = sids
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if site_id is not None:
            self.site_id = site_id
        if pool_id is not None:
            self.pool_id = pool_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if desktop_type is not None:
            self.desktop_type = desktop_type
        if is_share_desktop is not None:
            self.is_share_desktop = is_share_desktop
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if status is not None:
            self.status = status
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if tag is not None:
            self.tag = tag

    @property
    def user_name(self):
        """Gets the user_name of this ListDesktopsRequest.

        桌面所属用户。

        :return: The user_name of this ListDesktopsRequest.
        :rtype: list[str]
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListDesktopsRequest.

        桌面所属用户。

        :param user_name: The user_name of this ListDesktopsRequest.
        :type user_name: list[str]
        """
        self._user_name = user_name

    @property
    def computer_name(self):
        """Gets the computer_name of this ListDesktopsRequest.

        桌面名。

        :return: The computer_name of this ListDesktopsRequest.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this ListDesktopsRequest.

        桌面名。

        :param computer_name: The computer_name of this ListDesktopsRequest.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def desktop_ip(self):
        """Gets the desktop_ip of this ListDesktopsRequest.

        桌面IP地址。

        :return: The desktop_ip of this ListDesktopsRequest.
        :rtype: str
        """
        return self._desktop_ip

    @desktop_ip.setter
    def desktop_ip(self, desktop_ip):
        """Sets the desktop_ip of this ListDesktopsRequest.

        桌面IP地址。

        :param desktop_ip: The desktop_ip of this ListDesktopsRequest.
        :type desktop_ip: str
        """
        self._desktop_ip = desktop_ip

    @property
    def sids(self):
        """Gets the sids of this ListDesktopsRequest.

        桌面的sid列表，一次只能查询20个sid。

        :return: The sids of this ListDesktopsRequest.
        :rtype: list[str]
        """
        return self._sids

    @sids.setter
    def sids(self, sids):
        """Sets the sids of this ListDesktopsRequest.

        桌面的sid列表，一次只能查询20个sid。

        :param sids: The sids of this ListDesktopsRequest.
        :type sids: list[str]
        """
        self._sids = sids

    @property
    def offset(self):
        """Gets the offset of this ListDesktopsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListDesktopsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDesktopsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListDesktopsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDesktopsRequest.

        用于分页查询，取值范围0-1000，默认值1000。

        :return: The limit of this ListDesktopsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDesktopsRequest.

        用于分页查询，取值范围0-1000，默认值1000。

        :param limit: The limit of this ListDesktopsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def site_id(self):
        """Gets the site_id of this ListDesktopsRequest.

        用于筛选指定站点下的桌面列表

        :return: The site_id of this ListDesktopsRequest.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ListDesktopsRequest.

        用于筛选指定站点下的桌面列表

        :param site_id: The site_id of this ListDesktopsRequest.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def pool_id(self):
        """Gets the pool_id of this ListDesktopsRequest.

        桌面池ID,多个桌面池ID用逗号隔开。

        :return: The pool_id of this ListDesktopsRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this ListDesktopsRequest.

        桌面池ID,多个桌面池ID用逗号隔开。

        :param pool_id: The pool_id of this ListDesktopsRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListDesktopsRequest.

        企业项目ID

        :return: The enterprise_project_id of this ListDesktopsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListDesktopsRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListDesktopsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def desktop_type(self):
        """Gets the desktop_type of this ListDesktopsRequest.

        桌面类型，为空时查所有桌面。查询多个类型时用,隔开。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等。 - SHARED: 多用户共享桌面。

        :return: The desktop_type of this ListDesktopsRequest.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        """Sets the desktop_type of this ListDesktopsRequest.

        桌面类型，为空时查所有桌面。查询多个类型时用,隔开。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等。 - SHARED: 多用户共享桌面。

        :param desktop_type: The desktop_type of this ListDesktopsRequest.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def is_share_desktop(self):
        """Gets the is_share_desktop of this ListDesktopsRequest.

        是否为协同桌面

        :return: The is_share_desktop of this ListDesktopsRequest.
        :rtype: bool
        """
        return self._is_share_desktop

    @is_share_desktop.setter
    def is_share_desktop(self, is_share_desktop):
        """Sets the is_share_desktop of this ListDesktopsRequest.

        是否为协同桌面

        :param is_share_desktop: The is_share_desktop of this ListDesktopsRequest.
        :type is_share_desktop: bool
        """
        self._is_share_desktop = is_share_desktop

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListDesktopsRequest.

        桌面的子网ID。

        :return: The subnet_id of this ListDesktopsRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListDesktopsRequest.

        桌面的子网ID。

        :param subnet_id: The subnet_id of this ListDesktopsRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def status(self):
        """Gets the status of this ListDesktopsRequest.

        桌面的运行状态。

        :return: The status of this ListDesktopsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDesktopsRequest.

        桌面的运行状态。

        :param status: The status of this ListDesktopsRequest.
        :type status: str
        """
        self._status = status

    @property
    def desktop_id(self):
        """Gets the desktop_id of this ListDesktopsRequest.

        桌面id，当前最多支持100个桌面id进行查询。

        :return: The desktop_id of this ListDesktopsRequest.
        :rtype: list[str]
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this ListDesktopsRequest.

        桌面id，当前最多支持100个桌面id进行查询。

        :param desktop_id: The desktop_id of this ListDesktopsRequest.
        :type desktop_id: list[str]
        """
        self._desktop_id = desktop_id

    @property
    def tag(self):
        """Gets the tag of this ListDesktopsRequest.

        桌面的标签。样例： - key1=value1。 - key1=value1，key2=value2。

        :return: The tag of this ListDesktopsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListDesktopsRequest.

        桌面的标签。样例： - key1=value1。 - key1=value1，key2=value2。

        :param tag: The tag of this ListDesktopsRequest.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ListDesktopsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
