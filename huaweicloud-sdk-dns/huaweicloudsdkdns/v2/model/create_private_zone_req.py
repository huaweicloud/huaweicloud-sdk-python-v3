# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivateZoneReq:

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
        'description': 'str',
        'zone_type': 'str',
        'email': 'str',
        'ttl': 'int',
        'router': 'Router',
        'proxy_pattern': 'str',
        'tags': 'list[Tag]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'zone_type': 'zone_type',
        'email': 'email',
        'ttl': 'ttl',
        'router': 'router',
        'proxy_pattern': 'proxy_pattern',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, description=None, zone_type=None, email=None, ttl=None, router=None, proxy_pattern=None, tags=None, enterprise_project_id=None):
        r"""CreatePrivateZoneReq

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 域名。 **约束限制：** 不涉及。 **取值范围：** 由多个以点分隔的字符串组成，可包含字母、数字、汉字、中划线，中划线不能在开头或末尾，单个字符串不超过63个字符，域名总长度不超过254个字符。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** 域名的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。
        :type description: str
        :param zone_type: **参数解释：** 域名类型。 **约束限制：** 不涉及。 **取值范围：** private：内网域名。 **默认取值：** 不涉及。
        :type zone_type: str
        :param email: **参数解释：** 管理该域名的管理员邮箱，用于生成该域名的SOA记录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type email: str
        :param ttl: **参数解释：** 用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300
        :type ttl: int
        :param router: 
        :type router: :class:`huaweicloudsdkdns.v2.Router`
        :param proxy_pattern: **参数解释：** 内网域名的子域名递归解析代理模式。 **约束限制：** 不涉及。 **取值范围：** - AUTHORITY：当前域名未开启递归解析代理 - RECURSIVE：当前域名已开启递归解析代理  **默认取值：** AUTHORITY。
        :type proxy_pattern: str
        :param tags: **参数解释：** 资源标签。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        :param enterprise_project_id: **参数解释：** 域名所属的企业项目ID。可以使用该字段过滤企业项目下的域名。 **约束限制：** 不涉及。 **取值范围：** 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 **默认取值：** 0
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._description = None
        self._zone_type = None
        self._email = None
        self._ttl = None
        self._router = None
        self._proxy_pattern = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.zone_type = zone_type
        if email is not None:
            self.email = email
        if ttl is not None:
            self.ttl = ttl
        self.router = router
        if proxy_pattern is not None:
            self.proxy_pattern = proxy_pattern
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this CreatePrivateZoneReq.

        **参数解释：** 域名。 **约束限制：** 不涉及。 **取值范围：** 由多个以点分隔的字符串组成，可包含字母、数字、汉字、中划线，中划线不能在开头或末尾，单个字符串不超过63个字符，域名总长度不超过254个字符。 **默认取值：** 不涉及。

        :return: The name of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePrivateZoneReq.

        **参数解释：** 域名。 **约束限制：** 不涉及。 **取值范围：** 由多个以点分隔的字符串组成，可包含字母、数字、汉字、中划线，中划线不能在开头或末尾，单个字符串不超过63个字符，域名总长度不超过254个字符。 **默认取值：** 不涉及。

        :param name: The name of this CreatePrivateZoneReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreatePrivateZoneReq.

        **参数解释：** 域名的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。

        :return: The description of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePrivateZoneReq.

        **参数解释：** 域名的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 不涉及。

        :param description: The description of this CreatePrivateZoneReq.
        :type description: str
        """
        self._description = description

    @property
    def zone_type(self):
        r"""Gets the zone_type of this CreatePrivateZoneReq.

        **参数解释：** 域名类型。 **约束限制：** 不涉及。 **取值范围：** private：内网域名。 **默认取值：** 不涉及。

        :return: The zone_type of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        r"""Sets the zone_type of this CreatePrivateZoneReq.

        **参数解释：** 域名类型。 **约束限制：** 不涉及。 **取值范围：** private：内网域名。 **默认取值：** 不涉及。

        :param zone_type: The zone_type of this CreatePrivateZoneReq.
        :type zone_type: str
        """
        self._zone_type = zone_type

    @property
    def email(self):
        r"""Gets the email of this CreatePrivateZoneReq.

        **参数解释：** 管理该域名的管理员邮箱，用于生成该域名的SOA记录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The email of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this CreatePrivateZoneReq.

        **参数解释：** 管理该域名的管理员邮箱，用于生成该域名的SOA记录。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param email: The email of this CreatePrivateZoneReq.
        :type email: str
        """
        self._email = email

    @property
    def ttl(self):
        r"""Gets the ttl of this CreatePrivateZoneReq.

        **参数解释：** 用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300

        :return: The ttl of this CreatePrivateZoneReq.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this CreatePrivateZoneReq.

        **参数解释：** 用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 300

        :param ttl: The ttl of this CreatePrivateZoneReq.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def router(self):
        r"""Gets the router of this CreatePrivateZoneReq.

        :return: The router of this CreatePrivateZoneReq.
        :rtype: :class:`huaweicloudsdkdns.v2.Router`
        """
        return self._router

    @router.setter
    def router(self, router):
        r"""Sets the router of this CreatePrivateZoneReq.

        :param router: The router of this CreatePrivateZoneReq.
        :type router: :class:`huaweicloudsdkdns.v2.Router`
        """
        self._router = router

    @property
    def proxy_pattern(self):
        r"""Gets the proxy_pattern of this CreatePrivateZoneReq.

        **参数解释：** 内网域名的子域名递归解析代理模式。 **约束限制：** 不涉及。 **取值范围：** - AUTHORITY：当前域名未开启递归解析代理 - RECURSIVE：当前域名已开启递归解析代理  **默认取值：** AUTHORITY。

        :return: The proxy_pattern of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._proxy_pattern

    @proxy_pattern.setter
    def proxy_pattern(self, proxy_pattern):
        r"""Sets the proxy_pattern of this CreatePrivateZoneReq.

        **参数解释：** 内网域名的子域名递归解析代理模式。 **约束限制：** 不涉及。 **取值范围：** - AUTHORITY：当前域名未开启递归解析代理 - RECURSIVE：当前域名已开启递归解析代理  **默认取值：** AUTHORITY。

        :param proxy_pattern: The proxy_pattern of this CreatePrivateZoneReq.
        :type proxy_pattern: str
        """
        self._proxy_pattern = proxy_pattern

    @property
    def tags(self):
        r"""Gets the tags of this CreatePrivateZoneReq.

        **参数解释：** 资源标签。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tags of this CreatePrivateZoneReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreatePrivateZoneReq.

        **参数解释：** 资源标签。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tags: The tags of this CreatePrivateZoneReq.
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreatePrivateZoneReq.

        **参数解释：** 域名所属的企业项目ID。可以使用该字段过滤企业项目下的域名。 **约束限制：** 不涉及。 **取值范围：** 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 **默认取值：** 0

        :return: The enterprise_project_id of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreatePrivateZoneReq.

        **参数解释：** 域名所属的企业项目ID。可以使用该字段过滤企业项目下的域名。 **约束限制：** 不涉及。 **取值范围：** 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 **默认取值：** 0

        :param enterprise_project_id: The enterprise_project_id of this CreatePrivateZoneReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreatePrivateZoneReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
