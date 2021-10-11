# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcMemberInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'weight': 'int',
        'ecs_id': 'str',
        'ecs_name': 'str',
        'id': 'str',
        'status': 'int',
        'vpc_channel_id': 'str',
        'create_time': 'datetime'
    }

    attribute_map = {
        'host': 'host',
        'weight': 'weight',
        'ecs_id': 'ecs_id',
        'ecs_name': 'ecs_name',
        'id': 'id',
        'status': 'status',
        'vpc_channel_id': 'vpc_channel_id',
        'create_time': 'create_time'
    }

    def __init__(self, host=None, weight=None, ecs_id=None, ecs_name=None, id=None, status=None, vpc_channel_id=None, create_time=None):
        """VpcMemberInfo - a model defined in huaweicloud sdk"""
        
        

        self._host = None
        self._weight = None
        self._ecs_id = None
        self._ecs_name = None
        self._id = None
        self._status = None
        self._vpc_channel_id = None
        self._create_time = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if weight is not None:
            self.weight = weight
        if ecs_id is not None:
            self.ecs_id = ecs_id
        if ecs_name is not None:
            self.ecs_name = ecs_name
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if vpc_channel_id is not None:
            self.vpc_channel_id = vpc_channel_id
        if create_time is not None:
            self.create_time = create_time

    @property
    def host(self):
        """Gets the host of this VpcMemberInfo.

        后端服务器地址  后端实例类型为ip时生效

        :return: The host of this VpcMemberInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this VpcMemberInfo.

        后端服务器地址  后端实例类型为ip时生效

        :param host: The host of this VpcMemberInfo.
        :type: str
        """
        self._host = host

    @property
    def weight(self):
        """Gets the weight of this VpcMemberInfo.

        权重值。  允许您对云服务器进行评级，权重值越大，转发到该云服务的请求数量越多。权重只对加权轮询和加权最小连接算法生效  仅VPC通道类型为2时有效。

        :return: The weight of this VpcMemberInfo.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this VpcMemberInfo.

        权重值。  允许您对云服务器进行评级，权重值越大，转发到该云服务的请求数量越多。权重只对加权轮询和加权最小连接算法生效  仅VPC通道类型为2时有效。

        :param weight: The weight of this VpcMemberInfo.
        :type: int
        """
        self._weight = weight

    @property
    def ecs_id(self):
        """Gets the ecs_id of this VpcMemberInfo.

        后端云服务器的编号。  后端实例类型为instance时生效，支持英文，数字，“-”,“_”，1 ~ 64字符。

        :return: The ecs_id of this VpcMemberInfo.
        :rtype: str
        """
        return self._ecs_id

    @ecs_id.setter
    def ecs_id(self, ecs_id):
        """Sets the ecs_id of this VpcMemberInfo.

        后端云服务器的编号。  后端实例类型为instance时生效，支持英文，数字，“-”,“_”，1 ~ 64字符。

        :param ecs_id: The ecs_id of this VpcMemberInfo.
        :type: str
        """
        self._ecs_id = ecs_id

    @property
    def ecs_name(self):
        """Gets the ecs_name of this VpcMemberInfo.

        后端云服务器的名称。  后端实例类型为instance时生效，支持汉字，英文，数字，“-”,“_”,“.”，1 ~ 64字符。

        :return: The ecs_name of this VpcMemberInfo.
        :rtype: str
        """
        return self._ecs_name

    @ecs_name.setter
    def ecs_name(self, ecs_name):
        """Sets the ecs_name of this VpcMemberInfo.

        后端云服务器的名称。  后端实例类型为instance时生效，支持汉字，英文，数字，“-”,“_”,“.”，1 ~ 64字符。

        :param ecs_name: The ecs_name of this VpcMemberInfo.
        :type: str
        """
        self._ecs_name = ecs_name

    @property
    def id(self):
        """Gets the id of this VpcMemberInfo.

        后端实例对象的编号

        :return: The id of this VpcMemberInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VpcMemberInfo.

        后端实例对象的编号

        :param id: The id of this VpcMemberInfo.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this VpcMemberInfo.

        后端实例对象的状态

        :return: The status of this VpcMemberInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VpcMemberInfo.

        后端实例对象的状态

        :param status: The status of this VpcMemberInfo.
        :type: int
        """
        self._status = status

    @property
    def vpc_channel_id(self):
        """Gets the vpc_channel_id of this VpcMemberInfo.

        VPC通道的编号

        :return: The vpc_channel_id of this VpcMemberInfo.
        :rtype: str
        """
        return self._vpc_channel_id

    @vpc_channel_id.setter
    def vpc_channel_id(self, vpc_channel_id):
        """Sets the vpc_channel_id of this VpcMemberInfo.

        VPC通道的编号

        :param vpc_channel_id: The vpc_channel_id of this VpcMemberInfo.
        :type: str
        """
        self._vpc_channel_id = vpc_channel_id

    @property
    def create_time(self):
        """Gets the create_time of this VpcMemberInfo.

        后端实例增加到VPC通道的时间

        :return: The create_time of this VpcMemberInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VpcMemberInfo.

        后端实例增加到VPC通道的时间

        :param create_time: The create_time of this VpcMemberInfo.
        :type: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, VpcMemberInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
