# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointResponse(SdkResponse):

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
        'endpoints': 'list[EndpointConnection]'
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
        'endpoints': 'endpoints'
    }

    def __init__(self, id=None, name=None, vpc_id=None, subnet_id=None, domain=None, description=None, status=None, error_info=None, type=None, scalable=None, created_time=None, updated_time=None, endpoints=None):
        r"""UpdateEndpointResponse

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
        """
        
        super(UpdateEndpointResponse, self).__init__()

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

    @property
    def id(self):
        r"""Gets the id of this UpdateEndpointResponse.

        访问端点ID

        :return: The id of this UpdateEndpointResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateEndpointResponse.

        访问端点ID

        :param id: The id of this UpdateEndpointResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateEndpointResponse.

        用户指定的访问端点名称

        :return: The name of this UpdateEndpointResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateEndpointResponse.

        用户指定的访问端点名称

        :param name: The name of this UpdateEndpointResponse.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this UpdateEndpointResponse.

        访问端点所在的VPC的ID

        :return: The vpc_id of this UpdateEndpointResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this UpdateEndpointResponse.

        访问端点所在的VPC的ID

        :param vpc_id: The vpc_id of this UpdateEndpointResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this UpdateEndpointResponse.

        访问端点所在的子网的ID

        :return: The subnet_id of this UpdateEndpointResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this UpdateEndpointResponse.

        访问端点所在的子网的ID

        :param subnet_id: The subnet_id of this UpdateEndpointResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def domain(self):
        r"""Gets the domain of this UpdateEndpointResponse.

        访问域名

        :return: The domain of this UpdateEndpointResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this UpdateEndpointResponse.

        访问域名

        :param domain: The domain of this UpdateEndpointResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def description(self):
        r"""Gets the description of this UpdateEndpointResponse.

        描述

        :return: The description of this UpdateEndpointResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateEndpointResponse.

        描述

        :param description: The description of this UpdateEndpointResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this UpdateEndpointResponse.

        访问端点状态

        :return: The status of this UpdateEndpointResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateEndpointResponse.

        访问端点状态

        :param status: The status of this UpdateEndpointResponse.
        :type status: str
        """
        self._status = status

    @property
    def error_info(self):
        r"""Gets the error_info of this UpdateEndpointResponse.

        :return: The error_info of this UpdateEndpointResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this UpdateEndpointResponse.

        :param error_info: The error_info of this UpdateEndpointResponse.
        :type error_info: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        """
        self._error_info = error_info

    @property
    def type(self):
        r"""Gets the type of this UpdateEndpointResponse.

        访问端点类型

        :return: The type of this UpdateEndpointResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateEndpointResponse.

        访问端点类型

        :param type: The type of this UpdateEndpointResponse.
        :type type: str
        """
        self._type = type

    @property
    def scalable(self):
        r"""Gets the scalable of this UpdateEndpointResponse.

        是否可更新

        :return: The scalable of this UpdateEndpointResponse.
        :rtype: bool
        """
        return self._scalable

    @scalable.setter
    def scalable(self, scalable):
        r"""Sets the scalable of this UpdateEndpointResponse.

        是否可更新

        :param scalable: The scalable of this UpdateEndpointResponse.
        :type scalable: bool
        """
        self._scalable = scalable

    @property
    def created_time(self):
        r"""Gets the created_time of this UpdateEndpointResponse.

        创建UTC时间

        :return: The created_time of this UpdateEndpointResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this UpdateEndpointResponse.

        创建UTC时间

        :param created_time: The created_time of this UpdateEndpointResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this UpdateEndpointResponse.

        更新UTC时间

        :return: The updated_time of this UpdateEndpointResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this UpdateEndpointResponse.

        更新UTC时间

        :param updated_time: The updated_time of this UpdateEndpointResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def endpoints(self):
        r"""Gets the endpoints of this UpdateEndpointResponse.

        访问端点终端节点列表

        :return: The endpoints of this UpdateEndpointResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.EndpointConnection`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this UpdateEndpointResponse.

        访问端点终端节点列表

        :param endpoints: The endpoints of this UpdateEndpointResponse.
        :type endpoints: list[:class:`huaweicloudsdkeg.v1.EndpointConnection`]
        """
        self._endpoints = endpoints

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
        if not isinstance(other, UpdateEndpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
