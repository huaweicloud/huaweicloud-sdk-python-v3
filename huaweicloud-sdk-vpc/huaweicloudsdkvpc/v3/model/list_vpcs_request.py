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
        'enterprise_project_id': 'str',
        'name': 'list[str]',
        'description': 'list[str]',
        'cidr': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'description': 'description',
        'cidr': 'cidr'
    }

    def __init__(self, limit=None, marker=None, id=None, enterprise_project_id=None, name=None, description=None, cidr=None):
        r"""ListVpcsRequest

        The model defined in huaweicloud sdk

        :param limit: 功能说明：每页返回的个数 取值范围：0-2000
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: VPC资源ID。可以使用该字段过滤VPC
        :type id: list[str]
        :param enterprise_project_id: 功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的VPC。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的VPC，请传参all_granted_eps。
        :type enterprise_project_id: str
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
        self._enterprise_project_id = None
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
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cidr is not None:
            self.cidr = cidr

    @property
    def limit(self):
        r"""Gets the limit of this ListVpcsRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :return: The limit of this ListVpcsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVpcsRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :param limit: The limit of this ListVpcsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListVpcsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListVpcsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListVpcsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListVpcsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        r"""Gets the id of this ListVpcsRequest.

        VPC资源ID。可以使用该字段过滤VPC

        :return: The id of this ListVpcsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListVpcsRequest.

        VPC资源ID。可以使用该字段过滤VPC

        :param id: The id of this ListVpcsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVpcsRequest.

        功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的VPC。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的VPC，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListVpcsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVpcsRequest.

        功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的VPC。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的VPC，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListVpcsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this ListVpcsRequest.

        VPC的name信息，可以使用该字段过滤VPC

        :return: The name of this ListVpcsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListVpcsRequest.

        VPC的name信息，可以使用该字段过滤VPC

        :param name: The name of this ListVpcsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListVpcsRequest.

        VPC的描述信息。可以使用该字段过滤VPC

        :return: The description of this ListVpcsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListVpcsRequest.

        VPC的描述信息。可以使用该字段过滤VPC

        :param description: The description of this ListVpcsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def cidr(self):
        r"""Gets the cidr of this ListVpcsRequest.

        VPC的CIDR。可以使用该字段过滤VPC

        :return: The cidr of this ListVpcsRequest.
        :rtype: list[str]
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this ListVpcsRequest.

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
