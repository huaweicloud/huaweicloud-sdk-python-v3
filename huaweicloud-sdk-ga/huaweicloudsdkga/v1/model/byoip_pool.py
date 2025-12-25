# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ByoipPool:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'cidr': 'str',
        'ip_type': 'str',
        'created_at': 'datetime',
        'updated_at': 'str',
        'area': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cidr': 'cidr',
        'ip_type': 'ip_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'area': 'area',
        'domain_id': 'domain_id'
    }

    def __init__(self, id=None, cidr=None, ip_type=None, created_at=None, updated_at=None, area=None, domain_id=None):
        r"""ByoipPool

        The model defined in huaweicloud sdk

        :param id: 自带IP地址池ID。
        :type id: str
        :param cidr: 自带IP地址池的IP网段。
        :type cidr: str
        :param ip_type: IP地址类型。 取值范围：IPV4、IPV6
        :type ip_type: str
        :param created_at: 创建时间。
        :type created_at: datetime
        :param updated_at: 更新时间。
        :type updated_at: str
        :param area: 地区，取值： - OUTOFCM：中国大陆以外 - CM：中国大陆
        :type area: str
        :param domain_id: 租户ID。
        :type domain_id: str
        """
        
        

        self._id = None
        self._cidr = None
        self._ip_type = None
        self._created_at = None
        self._updated_at = None
        self._area = None
        self._domain_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cidr is not None:
            self.cidr = cidr
        if ip_type is not None:
            self.ip_type = ip_type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if area is not None:
            self.area = area
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def id(self):
        r"""Gets the id of this ByoipPool.

        自带IP地址池ID。

        :return: The id of this ByoipPool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ByoipPool.

        自带IP地址池ID。

        :param id: The id of this ByoipPool.
        :type id: str
        """
        self._id = id

    @property
    def cidr(self):
        r"""Gets the cidr of this ByoipPool.

        自带IP地址池的IP网段。

        :return: The cidr of this ByoipPool.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this ByoipPool.

        自带IP地址池的IP网段。

        :param cidr: The cidr of this ByoipPool.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def ip_type(self):
        r"""Gets the ip_type of this ByoipPool.

        IP地址类型。 取值范围：IPV4、IPV6

        :return: The ip_type of this ByoipPool.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        r"""Sets the ip_type of this ByoipPool.

        IP地址类型。 取值范围：IPV4、IPV6

        :param ip_type: The ip_type of this ByoipPool.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def created_at(self):
        r"""Gets the created_at of this ByoipPool.

        创建时间。

        :return: The created_at of this ByoipPool.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ByoipPool.

        创建时间。

        :param created_at: The created_at of this ByoipPool.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ByoipPool.

        更新时间。

        :return: The updated_at of this ByoipPool.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ByoipPool.

        更新时间。

        :param updated_at: The updated_at of this ByoipPool.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def area(self):
        r"""Gets the area of this ByoipPool.

        地区，取值： - OUTOFCM：中国大陆以外 - CM：中国大陆

        :return: The area of this ByoipPool.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        r"""Sets the area of this ByoipPool.

        地区，取值： - OUTOFCM：中国大陆以外 - CM：中国大陆

        :param area: The area of this ByoipPool.
        :type area: str
        """
        self._area = area

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ByoipPool.

        租户ID。

        :return: The domain_id of this ByoipPool.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ByoipPool.

        租户ID。

        :param domain_id: The domain_id of this ByoipPool.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, ByoipPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
