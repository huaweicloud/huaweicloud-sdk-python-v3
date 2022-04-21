# coding: utf-8

import re
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
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, description=None, zone_type=None, email=None, ttl=None, router=None, tags=None, enterprise_project_id=None):
        """CreatePrivateZoneReq

        The model defined in huaweicloud sdk

        :param name: 待创建的域名。
        :type name: str
        :param description: 域名的描述信息。
        :type description: str
        :param zone_type: 域名类型。取值：private。
        :type zone_type: str
        :param email: 管理该zone的管理员邮箱。
        :type email: str
        :param ttl: 用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。
        :type ttl: int
        :param router: 
        :type router: :class:`huaweicloudsdkdns.v2.Router`
        :param tags: 资源标签。
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        :param enterprise_project_id: 域名关联的企业项目ID，长度不超过36个字符。  默认值为0。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._description = None
        self._zone_type = None
        self._email = None
        self._ttl = None
        self._router = None
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
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this CreatePrivateZoneReq.

        待创建的域名。

        :return: The name of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePrivateZoneReq.

        待创建的域名。

        :param name: The name of this CreatePrivateZoneReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreatePrivateZoneReq.

        域名的描述信息。

        :return: The description of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePrivateZoneReq.

        域名的描述信息。

        :param description: The description of this CreatePrivateZoneReq.
        :type description: str
        """
        self._description = description

    @property
    def zone_type(self):
        """Gets the zone_type of this CreatePrivateZoneReq.

        域名类型。取值：private。

        :return: The zone_type of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """Sets the zone_type of this CreatePrivateZoneReq.

        域名类型。取值：private。

        :param zone_type: The zone_type of this CreatePrivateZoneReq.
        :type zone_type: str
        """
        self._zone_type = zone_type

    @property
    def email(self):
        """Gets the email of this CreatePrivateZoneReq.

        管理该zone的管理员邮箱。

        :return: The email of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreatePrivateZoneReq.

        管理该zone的管理员邮箱。

        :param email: The email of this CreatePrivateZoneReq.
        :type email: str
        """
        self._email = email

    @property
    def ttl(self):
        """Gets the ttl of this CreatePrivateZoneReq.

        用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。

        :return: The ttl of this CreatePrivateZoneReq.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CreatePrivateZoneReq.

        用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。

        :param ttl: The ttl of this CreatePrivateZoneReq.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def router(self):
        """Gets the router of this CreatePrivateZoneReq.


        :return: The router of this CreatePrivateZoneReq.
        :rtype: :class:`huaweicloudsdkdns.v2.Router`
        """
        return self._router

    @router.setter
    def router(self, router):
        """Sets the router of this CreatePrivateZoneReq.


        :param router: The router of this CreatePrivateZoneReq.
        :type router: :class:`huaweicloudsdkdns.v2.Router`
        """
        self._router = router

    @property
    def tags(self):
        """Gets the tags of this CreatePrivateZoneReq.

        资源标签。

        :return: The tags of this CreatePrivateZoneReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreatePrivateZoneReq.

        资源标签。

        :param tags: The tags of this CreatePrivateZoneReq.
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreatePrivateZoneReq.

        域名关联的企业项目ID，长度不超过36个字符。  默认值为0。

        :return: The enterprise_project_id of this CreatePrivateZoneReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreatePrivateZoneReq.

        域名关联的企业项目ID，长度不超过36个字符。  默认值为0。

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
