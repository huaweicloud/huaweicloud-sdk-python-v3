# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionCreateReq:

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
        'vpc_id': 'str',
        'subnet_id': 'str',
        'type': 'ConnectionType',
        'kafka_detail': 'KafkaConnectionDetail'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'type': 'type',
        'kafka_detail': 'kafka_detail'
    }

    def __init__(self, name=None, description=None, vpc_id=None, subnet_id=None, type=None, kafka_detail=None):
        """ConnectionCreateReq

        The model defined in huaweicloud sdk

        :param name: 目标连接名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须以字母或数字开头，不能为default
        :type name: str
        :param description: 目标连接描述
        :type description: str
        :param vpc_id: 待连接的VPC ID
        :type vpc_id: str
        :param subnet_id: 待连接的子网ID
        :type subnet_id: str
        :param type: 
        :type type: :class:`huaweicloudsdkeg.v1.ConnectionType`
        :param kafka_detail: 
        :type kafka_detail: :class:`huaweicloudsdkeg.v1.KafkaConnectionDetail`
        """
        
        

        self._name = None
        self._description = None
        self._vpc_id = None
        self._subnet_id = None
        self._type = None
        self._kafka_detail = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if type is not None:
            self.type = type
        if kafka_detail is not None:
            self.kafka_detail = kafka_detail

    @property
    def name(self):
        """Gets the name of this ConnectionCreateReq.

        目标连接名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须以字母或数字开头，不能为default

        :return: The name of this ConnectionCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectionCreateReq.

        目标连接名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须以字母或数字开头，不能为default

        :param name: The name of this ConnectionCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ConnectionCreateReq.

        目标连接描述

        :return: The description of this ConnectionCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConnectionCreateReq.

        目标连接描述

        :param description: The description of this ConnectionCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ConnectionCreateReq.

        待连接的VPC ID

        :return: The vpc_id of this ConnectionCreateReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ConnectionCreateReq.

        待连接的VPC ID

        :param vpc_id: The vpc_id of this ConnectionCreateReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ConnectionCreateReq.

        待连接的子网ID

        :return: The subnet_id of this ConnectionCreateReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ConnectionCreateReq.

        待连接的子网ID

        :param subnet_id: The subnet_id of this ConnectionCreateReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def type(self):
        """Gets the type of this ConnectionCreateReq.

        :return: The type of this ConnectionCreateReq.
        :rtype: :class:`huaweicloudsdkeg.v1.ConnectionType`
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConnectionCreateReq.

        :param type: The type of this ConnectionCreateReq.
        :type type: :class:`huaweicloudsdkeg.v1.ConnectionType`
        """
        self._type = type

    @property
    def kafka_detail(self):
        """Gets the kafka_detail of this ConnectionCreateReq.

        :return: The kafka_detail of this ConnectionCreateReq.
        :rtype: :class:`huaweicloudsdkeg.v1.KafkaConnectionDetail`
        """
        return self._kafka_detail

    @kafka_detail.setter
    def kafka_detail(self, kafka_detail):
        """Sets the kafka_detail of this ConnectionCreateReq.

        :param kafka_detail: The kafka_detail of this ConnectionCreateReq.
        :type kafka_detail: :class:`huaweicloudsdkeg.v1.KafkaConnectionDetail`
        """
        self._kafka_detail = kafka_detail

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
        if not isinstance(other, ConnectionCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
