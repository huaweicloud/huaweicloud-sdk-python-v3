# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessClientRequestBody:

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
        'access_mode': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'access_connections': 'list[AccessConnectionRequestBody]'
    }

    attribute_map = {
        'name': 'name',
        'access_mode': 'access_mode',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'access_connections': 'access_connections'
    }

    def __init__(self, name=None, access_mode=None, vpc_id=None, subnet_id=None, access_connections=None):
        """AccessClientRequestBody

        The model defined in huaweicloud sdk

        :param name: 客户端名称
        :type name: str
        :param access_mode: 接入模式， SYSTEM：系统默认模式，由系统自动创建vpcep连接，也是推荐方式。该模式下vpc_id、subnet_id必填。 CUSTOM：定制模式，由外部服务自行创建vpcep连接，适用于跨租户场景等。该模式下access_connection必填。
        :type access_mode: str
        :param vpc_id: VPC ID
        :type vpc_id: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param access_connections: 接入连接列表
        :type access_connections: list[:class:`huaweicloudsdklakeformation.v1.AccessConnectionRequestBody`]
        """
        
        

        self._name = None
        self._access_mode = None
        self._vpc_id = None
        self._subnet_id = None
        self._access_connections = None
        self.discriminator = None

        self.name = name
        if access_mode is not None:
            self.access_mode = access_mode
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if access_connections is not None:
            self.access_connections = access_connections

    @property
    def name(self):
        """Gets the name of this AccessClientRequestBody.

        客户端名称

        :return: The name of this AccessClientRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessClientRequestBody.

        客户端名称

        :param name: The name of this AccessClientRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def access_mode(self):
        """Gets the access_mode of this AccessClientRequestBody.

        接入模式， SYSTEM：系统默认模式，由系统自动创建vpcep连接，也是推荐方式。该模式下vpc_id、subnet_id必填。 CUSTOM：定制模式，由外部服务自行创建vpcep连接，适用于跨租户场景等。该模式下access_connection必填。

        :return: The access_mode of this AccessClientRequestBody.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this AccessClientRequestBody.

        接入模式， SYSTEM：系统默认模式，由系统自动创建vpcep连接，也是推荐方式。该模式下vpc_id、subnet_id必填。 CUSTOM：定制模式，由外部服务自行创建vpcep连接，适用于跨租户场景等。该模式下access_connection必填。

        :param access_mode: The access_mode of this AccessClientRequestBody.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def vpc_id(self):
        """Gets the vpc_id of this AccessClientRequestBody.

        VPC ID

        :return: The vpc_id of this AccessClientRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this AccessClientRequestBody.

        VPC ID

        :param vpc_id: The vpc_id of this AccessClientRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this AccessClientRequestBody.

        子网ID

        :return: The subnet_id of this AccessClientRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this AccessClientRequestBody.

        子网ID

        :param subnet_id: The subnet_id of this AccessClientRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def access_connections(self):
        """Gets the access_connections of this AccessClientRequestBody.

        接入连接列表

        :return: The access_connections of this AccessClientRequestBody.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.AccessConnectionRequestBody`]
        """
        return self._access_connections

    @access_connections.setter
    def access_connections(self, access_connections):
        """Sets the access_connections of this AccessClientRequestBody.

        接入连接列表

        :param access_connections: The access_connections of this AccessClientRequestBody.
        :type access_connections: list[:class:`huaweicloudsdklakeformation.v1.AccessConnectionRequestBody`]
        """
        self._access_connections = access_connections

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
        if not isinstance(other, AccessClientRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
