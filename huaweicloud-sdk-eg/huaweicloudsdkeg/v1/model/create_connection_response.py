# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConnectionResponse(SdkResponse):

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
        'description': 'str',
        'status': 'str',
        'error_info': 'ErrorInfo',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'agency': 'str',
        'flavor': 'ConnectionInfoFlavor',
        'type': 'ConnectionType',
        'kafka_detail': 'KafkaConnectionDetail',
        'created_time': 'str',
        'updated_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'error_info': 'error_info',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'agency': 'agency',
        'flavor': 'flavor',
        'type': 'type',
        'kafka_detail': 'kafka_detail',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, id=None, name=None, description=None, status=None, error_info=None, vpc_id=None, subnet_id=None, agency=None, flavor=None, type=None, kafka_detail=None, created_time=None, updated_time=None, x_request_id=None):
        r"""CreateConnectionResponse

        The model defined in huaweicloud sdk

        :param id: 事件源ID
        :type id: str
        :param name: 目标连接名称，租户下唯一，由小写字母、数字、点、下划线和中划线组成，必须以字母或数字开头，不能为default
        :type name: str
        :param description: 目标连接描述
        :type description: str
        :param status: 目标连接状态
        :type status: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        :param vpc_id: 待连接的VPC ID
        :type vpc_id: str
        :param subnet_id: 待连接的子网ID
        :type subnet_id: str
        :param agency: 私网目标连接使用的用户委托名称
        :type agency: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkeg.v1.ConnectionInfoFlavor`
        :param type: 
        :type type: :class:`huaweicloudsdkeg.v1.ConnectionType`
        :param kafka_detail: 
        :type kafka_detail: :class:`huaweicloudsdkeg.v1.KafkaConnectionDetail`
        :param created_time: 创建UTC时间
        :type created_time: str
        :param updated_time: 更新UTC时间
        :type updated_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateConnectionResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._error_info = None
        self._vpc_id = None
        self._subnet_id = None
        self._agency = None
        self._flavor = None
        self._type = None
        self._kafka_detail = None
        self._created_time = None
        self._updated_time = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if error_info is not None:
            self.error_info = error_info
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if agency is not None:
            self.agency = agency
        if flavor is not None:
            self.flavor = flavor
        if type is not None:
            self.type = type
        if kafka_detail is not None:
            self.kafka_detail = kafka_detail
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this CreateConnectionResponse.

        事件源ID

        :return: The id of this CreateConnectionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateConnectionResponse.

        事件源ID

        :param id: The id of this CreateConnectionResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateConnectionResponse.

        目标连接名称，租户下唯一，由小写字母、数字、点、下划线和中划线组成，必须以字母或数字开头，不能为default

        :return: The name of this CreateConnectionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateConnectionResponse.

        目标连接名称，租户下唯一，由小写字母、数字、点、下划线和中划线组成，必须以字母或数字开头，不能为default

        :param name: The name of this CreateConnectionResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateConnectionResponse.

        目标连接描述

        :return: The description of this CreateConnectionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateConnectionResponse.

        目标连接描述

        :param description: The description of this CreateConnectionResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateConnectionResponse.

        目标连接状态

        :return: The status of this CreateConnectionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateConnectionResponse.

        目标连接状态

        :param status: The status of this CreateConnectionResponse.
        :type status: str
        """
        self._status = status

    @property
    def error_info(self):
        r"""Gets the error_info of this CreateConnectionResponse.

        :return: The error_info of this CreateConnectionResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this CreateConnectionResponse.

        :param error_info: The error_info of this CreateConnectionResponse.
        :type error_info: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        """
        self._error_info = error_info

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateConnectionResponse.

        待连接的VPC ID

        :return: The vpc_id of this CreateConnectionResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateConnectionResponse.

        待连接的VPC ID

        :param vpc_id: The vpc_id of this CreateConnectionResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateConnectionResponse.

        待连接的子网ID

        :return: The subnet_id of this CreateConnectionResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateConnectionResponse.

        待连接的子网ID

        :param subnet_id: The subnet_id of this CreateConnectionResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def agency(self):
        r"""Gets the agency of this CreateConnectionResponse.

        私网目标连接使用的用户委托名称

        :return: The agency of this CreateConnectionResponse.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this CreateConnectionResponse.

        私网目标连接使用的用户委托名称

        :param agency: The agency of this CreateConnectionResponse.
        :type agency: str
        """
        self._agency = agency

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateConnectionResponse.

        :return: The flavor of this CreateConnectionResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.ConnectionInfoFlavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateConnectionResponse.

        :param flavor: The flavor of this CreateConnectionResponse.
        :type flavor: :class:`huaweicloudsdkeg.v1.ConnectionInfoFlavor`
        """
        self._flavor = flavor

    @property
    def type(self):
        r"""Gets the type of this CreateConnectionResponse.

        :return: The type of this CreateConnectionResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.ConnectionType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateConnectionResponse.

        :param type: The type of this CreateConnectionResponse.
        :type type: :class:`huaweicloudsdkeg.v1.ConnectionType`
        """
        self._type = type

    @property
    def kafka_detail(self):
        r"""Gets the kafka_detail of this CreateConnectionResponse.

        :return: The kafka_detail of this CreateConnectionResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.KafkaConnectionDetail`
        """
        return self._kafka_detail

    @kafka_detail.setter
    def kafka_detail(self, kafka_detail):
        r"""Sets the kafka_detail of this CreateConnectionResponse.

        :param kafka_detail: The kafka_detail of this CreateConnectionResponse.
        :type kafka_detail: :class:`huaweicloudsdkeg.v1.KafkaConnectionDetail`
        """
        self._kafka_detail = kafka_detail

    @property
    def created_time(self):
        r"""Gets the created_time of this CreateConnectionResponse.

        创建UTC时间

        :return: The created_time of this CreateConnectionResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this CreateConnectionResponse.

        创建UTC时间

        :param created_time: The created_time of this CreateConnectionResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this CreateConnectionResponse.

        更新UTC时间

        :return: The updated_time of this CreateConnectionResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this CreateConnectionResponse.

        更新UTC时间

        :param updated_time: The updated_time of this CreateConnectionResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateConnectionResponse.

        :return: The x_request_id of this CreateConnectionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateConnectionResponse.

        :param x_request_id: The x_request_id of this CreateConnectionResponse.
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
        if not isinstance(other, CreateConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
