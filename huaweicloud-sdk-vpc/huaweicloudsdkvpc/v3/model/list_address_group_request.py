# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAddressGroupRequest:

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
        'ip_version': 'int',
        'description': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'ip_version': 'ip_version',
        'description': 'description'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, ip_version=None, description=None):
        """ListAddressGroupRequest

        The model defined in huaweicloud sdk

        :param limit: 功能说明：每页返回的个数 取值范围：0~2000
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: 地址组唯一标识，填写后接口按照id进行过滤，支持多ID同时过滤
        :type id: list[str]
        :param name: 地址组名称，填写后按照名称进行过滤，支持多名称同时过滤
        :type name: list[str]
        :param ip_version: IP地址组ip版本，当前只支持ipv4，填写后按照ip版本进行过滤
        :type ip_version: int
        :param description: 地址组描述信息，填写后按照地址组描述信息过滤，支持多描述同时过滤
        :type description: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._ip_version = None
        self._description = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ip_version is not None:
            self.ip_version = ip_version
        if description is not None:
            self.description = description

    @property
    def limit(self):
        """Gets the limit of this ListAddressGroupRequest.

        功能说明：每页返回的个数 取值范围：0~2000

        :return: The limit of this ListAddressGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAddressGroupRequest.

        功能说明：每页返回的个数 取值范围：0~2000

        :param limit: The limit of this ListAddressGroupRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListAddressGroupRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListAddressGroupRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAddressGroupRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListAddressGroupRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListAddressGroupRequest.

        地址组唯一标识，填写后接口按照id进行过滤，支持多ID同时过滤

        :return: The id of this ListAddressGroupRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAddressGroupRequest.

        地址组唯一标识，填写后接口按照id进行过滤，支持多ID同时过滤

        :param id: The id of this ListAddressGroupRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListAddressGroupRequest.

        地址组名称，填写后按照名称进行过滤，支持多名称同时过滤

        :return: The name of this ListAddressGroupRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAddressGroupRequest.

        地址组名称，填写后按照名称进行过滤，支持多名称同时过滤

        :param name: The name of this ListAddressGroupRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def ip_version(self):
        """Gets the ip_version of this ListAddressGroupRequest.

        IP地址组ip版本，当前只支持ipv4，填写后按照ip版本进行过滤

        :return: The ip_version of this ListAddressGroupRequest.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListAddressGroupRequest.

        IP地址组ip版本，当前只支持ipv4，填写后按照ip版本进行过滤

        :param ip_version: The ip_version of this ListAddressGroupRequest.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def description(self):
        """Gets the description of this ListAddressGroupRequest.

        地址组描述信息，填写后按照地址组描述信息过滤，支持多描述同时过滤

        :return: The description of this ListAddressGroupRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListAddressGroupRequest.

        地址组描述信息，填写后按照地址组描述信息过滤，支持多描述同时过滤

        :param description: The description of this ListAddressGroupRequest.
        :type description: list[str]
        """
        self._description = description

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
        if not isinstance(other, ListAddressGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
