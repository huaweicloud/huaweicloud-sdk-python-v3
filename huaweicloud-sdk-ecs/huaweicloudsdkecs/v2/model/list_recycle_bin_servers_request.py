# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecycleBinServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_tenants': 'str',
        'availability_zone': 'str',
        'expect_fields': 'str',
        'ip_address': 'str',
        'limit': 'int',
        'marker': 'str',
        'name': 'str',
        'offset': 'str',
        'tags': 'list[str]',
        'tags_key': 'list[str]'
    }

    attribute_map = {
        'all_tenants': 'all_tenants',
        'availability_zone': 'availability_zone',
        'expect_fields': 'expect-fields',
        'ip_address': 'ip_address',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'offset': 'offset',
        'tags': 'tags',
        'tags_key': 'tags_key'
    }

    def __init__(self, all_tenants=None, availability_zone=None, expect_fields=None, ip_address=None, limit=None, marker=None, name=None, offset=None, tags=None, tags_key=None):
        r"""ListRecycleBinServersRequest

        The model defined in huaweicloud sdk

        :param all_tenants: 所有租户 管理员字段 1: 返回所有租户的VM 0: 返回当前租户的VM，如果为0，与不设置该查询字段的效果一致
        :type all_tenants: str
        :param availability_zone: 
        :type availability_zone: str
        :param expect_fields: 
        :type expect_fields: str
        :param ip_address: 
        :type ip_address: str
        :param limit: 
        :type limit: int
        :param marker: 
        :type marker: str
        :param name: 
        :type name: str
        :param offset: 
        :type offset: str
        :param tags: 
        :type tags: list[str]
        :param tags_key: 
        :type tags_key: list[str]
        """
        
        

        self._all_tenants = None
        self._availability_zone = None
        self._expect_fields = None
        self._ip_address = None
        self._limit = None
        self._marker = None
        self._name = None
        self._offset = None
        self._tags = None
        self._tags_key = None
        self.discriminator = None

        if all_tenants is not None:
            self.all_tenants = all_tenants
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if expect_fields is not None:
            self.expect_fields = expect_fields
        if ip_address is not None:
            self.ip_address = ip_address
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if tags_key is not None:
            self.tags_key = tags_key

    @property
    def all_tenants(self):
        r"""Gets the all_tenants of this ListRecycleBinServersRequest.

        所有租户 管理员字段 1: 返回所有租户的VM 0: 返回当前租户的VM，如果为0，与不设置该查询字段的效果一致

        :return: The all_tenants of this ListRecycleBinServersRequest.
        :rtype: str
        """
        return self._all_tenants

    @all_tenants.setter
    def all_tenants(self, all_tenants):
        r"""Sets the all_tenants of this ListRecycleBinServersRequest.

        所有租户 管理员字段 1: 返回所有租户的VM 0: 返回当前租户的VM，如果为0，与不设置该查询字段的效果一致

        :param all_tenants: The all_tenants of this ListRecycleBinServersRequest.
        :type all_tenants: str
        """
        self._all_tenants = all_tenants

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListRecycleBinServersRequest.

        :return: The availability_zone of this ListRecycleBinServersRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListRecycleBinServersRequest.

        :param availability_zone: The availability_zone of this ListRecycleBinServersRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def expect_fields(self):
        r"""Gets the expect_fields of this ListRecycleBinServersRequest.

        :return: The expect_fields of this ListRecycleBinServersRequest.
        :rtype: str
        """
        return self._expect_fields

    @expect_fields.setter
    def expect_fields(self, expect_fields):
        r"""Sets the expect_fields of this ListRecycleBinServersRequest.

        :param expect_fields: The expect_fields of this ListRecycleBinServersRequest.
        :type expect_fields: str
        """
        self._expect_fields = expect_fields

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ListRecycleBinServersRequest.

        :return: The ip_address of this ListRecycleBinServersRequest.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ListRecycleBinServersRequest.

        :param ip_address: The ip_address of this ListRecycleBinServersRequest.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def limit(self):
        r"""Gets the limit of this ListRecycleBinServersRequest.

        :return: The limit of this ListRecycleBinServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRecycleBinServersRequest.

        :param limit: The limit of this ListRecycleBinServersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListRecycleBinServersRequest.

        :return: The marker of this ListRecycleBinServersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRecycleBinServersRequest.

        :param marker: The marker of this ListRecycleBinServersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def name(self):
        r"""Gets the name of this ListRecycleBinServersRequest.

        :return: The name of this ListRecycleBinServersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListRecycleBinServersRequest.

        :param name: The name of this ListRecycleBinServersRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListRecycleBinServersRequest.

        :return: The offset of this ListRecycleBinServersRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRecycleBinServersRequest.

        :param offset: The offset of this ListRecycleBinServersRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def tags(self):
        r"""Gets the tags of this ListRecycleBinServersRequest.

        :return: The tags of this ListRecycleBinServersRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListRecycleBinServersRequest.

        :param tags: The tags of this ListRecycleBinServersRequest.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def tags_key(self):
        r"""Gets the tags_key of this ListRecycleBinServersRequest.

        :return: The tags_key of this ListRecycleBinServersRequest.
        :rtype: list[str]
        """
        return self._tags_key

    @tags_key.setter
    def tags_key(self, tags_key):
        r"""Sets the tags_key of this ListRecycleBinServersRequest.

        :param tags_key: The tags_key of this ListRecycleBinServersRequest.
        :type tags_key: list[str]
        """
        self._tags_key = tags_key

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
        if not isinstance(other, ListRecycleBinServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
