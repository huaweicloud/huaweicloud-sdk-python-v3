# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointResponse(SdkResponse):

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
        'name': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'domain': 'str',
        'description': 'str',
        'status': 'str',
        'error_info': 'ErrorInfo',
        'type': 'str',
        'scalable': 'bool',
        'created_time': 'str',
        'updated_time': 'str',
        'endpoints': 'list[EndpointConnection]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'domain': 'domain',
        'description': 'description',
        'status': 'status',
        'error_info': 'error_info',
        'type': 'type',
        'scalable': 'scalable',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'endpoints': 'endpoints',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, id=None, name=None, vpc_id=None, subnet_id=None, domain=None, description=None, status=None, error_info=None, type=None, scalable=None, created_time=None, updated_time=None, endpoints=None, x_request_id=None):
        """CreateEndpointResponse

        The model defined in huaweicloud sdk

        :param id: 访问端点ID
        :type id: str
        :param name: 用户指定的访问端点名称
        :type name: str
        :param vpc_id: 访问端点所在的VPC的ID
        :type vpc_id: str
        :param subnet_id: 访问端点所在的子网的ID
        :type subnet_id: str
        :param domain: 访问域名
        :type domain: str
        :param description: 描述
        :type description: str
        :param status: 访问端点状态
        :type status: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        :param type: 访问端点类型
        :type type: str
        :param scalable: 是否可更新
        :type scalable: bool
        :param created_time: 创建UTC时间
        :type created_time: str
        :param updated_time: 更新UTC时间
        :type updated_time: str
        :param endpoints: 访问端点终端节点列表
        :type endpoints: list[:class:`huaweicloudsdkeg.v1.EndpointConnection`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateEndpointResponse, self).__init__()

        self._id = None
        self._name = None
        self._vpc_id = None
        self._subnet_id = None
        self._domain = None
        self._description = None
        self._status = None
        self._error_info = None
        self._type = None
        self._scalable = None
        self._created_time = None
        self._updated_time = None
        self._endpoints = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if domain is not None:
            self.domain = domain
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if error_info is not None:
            self.error_info = error_info
        if type is not None:
            self.type = type
        if scalable is not None:
            self.scalable = scalable
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if endpoints is not None:
            self.endpoints = endpoints
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        """Gets the id of this CreateEndpointResponse.

        访问端点ID

        :return: The id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateEndpointResponse.

        访问端点ID

        :param id: The id of this CreateEndpointResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateEndpointResponse.

        用户指定的访问端点名称

        :return: The name of this CreateEndpointResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEndpointResponse.

        用户指定的访问端点名称

        :param name: The name of this CreateEndpointResponse.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateEndpointResponse.

        访问端点所在的VPC的ID

        :return: The vpc_id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateEndpointResponse.

        访问端点所在的VPC的ID

        :param vpc_id: The vpc_id of this CreateEndpointResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateEndpointResponse.

        访问端点所在的子网的ID

        :return: The subnet_id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateEndpointResponse.

        访问端点所在的子网的ID

        :param subnet_id: The subnet_id of this CreateEndpointResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def domain(self):
        """Gets the domain of this CreateEndpointResponse.

        访问域名

        :return: The domain of this CreateEndpointResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateEndpointResponse.

        访问域名

        :param domain: The domain of this CreateEndpointResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def description(self):
        """Gets the description of this CreateEndpointResponse.

        描述

        :return: The description of this CreateEndpointResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEndpointResponse.

        描述

        :param description: The description of this CreateEndpointResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this CreateEndpointResponse.

        访问端点状态

        :return: The status of this CreateEndpointResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateEndpointResponse.

        访问端点状态

        :param status: The status of this CreateEndpointResponse.
        :type status: str
        """
        self._status = status

    @property
    def error_info(self):
        """Gets the error_info of this CreateEndpointResponse.

        :return: The error_info of this CreateEndpointResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """Sets the error_info of this CreateEndpointResponse.

        :param error_info: The error_info of this CreateEndpointResponse.
        :type error_info: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        """
        self._error_info = error_info

    @property
    def type(self):
        """Gets the type of this CreateEndpointResponse.

        访问端点类型

        :return: The type of this CreateEndpointResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateEndpointResponse.

        访问端点类型

        :param type: The type of this CreateEndpointResponse.
        :type type: str
        """
        self._type = type

    @property
    def scalable(self):
        """Gets the scalable of this CreateEndpointResponse.

        是否可更新

        :return: The scalable of this CreateEndpointResponse.
        :rtype: bool
        """
        return self._scalable

    @scalable.setter
    def scalable(self, scalable):
        """Sets the scalable of this CreateEndpointResponse.

        是否可更新

        :param scalable: The scalable of this CreateEndpointResponse.
        :type scalable: bool
        """
        self._scalable = scalable

    @property
    def created_time(self):
        """Gets the created_time of this CreateEndpointResponse.

        创建UTC时间

        :return: The created_time of this CreateEndpointResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this CreateEndpointResponse.

        创建UTC时间

        :param created_time: The created_time of this CreateEndpointResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this CreateEndpointResponse.

        更新UTC时间

        :return: The updated_time of this CreateEndpointResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this CreateEndpointResponse.

        更新UTC时间

        :param updated_time: The updated_time of this CreateEndpointResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def endpoints(self):
        """Gets the endpoints of this CreateEndpointResponse.

        访问端点终端节点列表

        :return: The endpoints of this CreateEndpointResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.EndpointConnection`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this CreateEndpointResponse.

        访问端点终端节点列表

        :param endpoints: The endpoints of this CreateEndpointResponse.
        :type endpoints: list[:class:`huaweicloudsdkeg.v1.EndpointConnection`]
        """
        self._endpoints = endpoints

    @property
    def x_request_id(self):
        """Gets the x_request_id of this CreateEndpointResponse.

        :return: The x_request_id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this CreateEndpointResponse.

        :param x_request_id: The x_request_id of this CreateEndpointResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CreateEndpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
