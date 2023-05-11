# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'cidr': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'cidr': 'cidr'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, description=None, cidr=None):
        """ListVpcsRequest

        The model defined in huaweicloud sdk

        :param limit: 功能说明：每页返回的个数 取值范围：0-2000
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: VPC资源ID。可以使用该字段过滤VPC
        :type id: list[str]
        :param name: VPC的name信息，可以使用该字段过滤VPC
        :type name: list[str]
        :param description: VPC的描述信息。可以使用该字段过滤VPC
        :type description: list[str]
        :param cidr: VPC的CIDR。可以使用该字段过滤VPC
        :type cidr: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._description = None
        self._cidr = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cidr is not None:
            self.cidr = cidr

    @property
    def limit(self):
        """Gets the limit of this ListVpcsRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :return: The limit of this ListVpcsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVpcsRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :param limit: The limit of this ListVpcsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListVpcsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListVpcsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListVpcsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListVpcsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListVpcsRequest.

        VPC资源ID。可以使用该字段过滤VPC

        :return: The id of this ListVpcsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListVpcsRequest.

        VPC资源ID。可以使用该字段过滤VPC

        :param id: The id of this ListVpcsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListVpcsRequest.

        VPC的name信息，可以使用该字段过滤VPC

        :return: The name of this ListVpcsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListVpcsRequest.

        VPC的name信息，可以使用该字段过滤VPC

        :param name: The name of this ListVpcsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListVpcsRequest.

        VPC的描述信息。可以使用该字段过滤VPC

        :return: The description of this ListVpcsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListVpcsRequest.

        VPC的描述信息。可以使用该字段过滤VPC

        :param description: The description of this ListVpcsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def cidr(self):
        """Gets the cidr of this ListVpcsRequest.

        VPC的CIDR。可以使用该字段过滤VPC

        :return: The cidr of this ListVpcsRequest.
        :rtype: list[str]
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this ListVpcsRequest.

        VPC的CIDR。可以使用该字段过滤VPC

        :param cidr: The cidr of this ListVpcsRequest.
        :type cidr: list[str]
        """
        self._cidr = cidr

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
        if not isinstance(other, ListVpcsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
