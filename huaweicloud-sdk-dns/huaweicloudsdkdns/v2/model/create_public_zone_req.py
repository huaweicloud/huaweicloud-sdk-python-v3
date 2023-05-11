# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePublicZoneReq:

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
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'zone_type': 'zone_type',
        'email': 'email',
        'ttl': 'ttl',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, zone_type=None, email=None, ttl=None, enterprise_project_id=None, tags=None):
        """CreatePublicZoneReq

        The model defined in huaweicloud sdk

        :param name: Zone名称
        :type name: str
        :param description: 描述
        :type description: str
        :param zone_type: Zone类型,取值public。
        :type zone_type: str
        :param email: 管理该zone的管理员邮箱
        :type email: str
        :param ttl: 用于填写默认生成的SOA记录中有效缓存时间，以秒为单位.
        :type ttl: int
        :param enterprise_project_id: 域名关联的企业项目ID，长度不超过36个字符.
        :type enterprise_project_id: str
        :param tags: 资源标签。
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        
        

        self._name = None
        self._description = None
        self._zone_type = None
        self._email = None
        self._ttl = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if zone_type is not None:
            self.zone_type = zone_type
        if email is not None:
            self.email = email
        if ttl is not None:
            self.ttl = ttl
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreatePublicZoneReq.

        Zone名称

        :return: The name of this CreatePublicZoneReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePublicZoneReq.

        Zone名称

        :param name: The name of this CreatePublicZoneReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreatePublicZoneReq.

        描述

        :return: The description of this CreatePublicZoneReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePublicZoneReq.

        描述

        :param description: The description of this CreatePublicZoneReq.
        :type description: str
        """
        self._description = description

    @property
    def zone_type(self):
        """Gets the zone_type of this CreatePublicZoneReq.

        Zone类型,取值public。

        :return: The zone_type of this CreatePublicZoneReq.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """Sets the zone_type of this CreatePublicZoneReq.

        Zone类型,取值public。

        :param zone_type: The zone_type of this CreatePublicZoneReq.
        :type zone_type: str
        """
        self._zone_type = zone_type

    @property
    def email(self):
        """Gets the email of this CreatePublicZoneReq.

        管理该zone的管理员邮箱

        :return: The email of this CreatePublicZoneReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreatePublicZoneReq.

        管理该zone的管理员邮箱

        :param email: The email of this CreatePublicZoneReq.
        :type email: str
        """
        self._email = email

    @property
    def ttl(self):
        """Gets the ttl of this CreatePublicZoneReq.

        用于填写默认生成的SOA记录中有效缓存时间，以秒为单位.

        :return: The ttl of this CreatePublicZoneReq.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CreatePublicZoneReq.

        用于填写默认生成的SOA记录中有效缓存时间，以秒为单位.

        :param ttl: The ttl of this CreatePublicZoneReq.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreatePublicZoneReq.

        域名关联的企业项目ID，长度不超过36个字符.

        :return: The enterprise_project_id of this CreatePublicZoneReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreatePublicZoneReq.

        域名关联的企业项目ID，长度不超过36个字符.

        :param enterprise_project_id: The enterprise_project_id of this CreatePublicZoneReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreatePublicZoneReq.

        资源标签。

        :return: The tags of this CreatePublicZoneReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreatePublicZoneReq.

        资源标签。

        :param tags: The tags of this CreatePublicZoneReq.
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreatePublicZoneReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
