# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointResp:

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
        'direction': 'str',
        'status': 'str',
        'vpc_id': 'str',
        'ipaddress_count': 'int',
        'resolver_rule_count': 'int',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'direction': 'direction',
        'status': 'status',
        'vpc_id': 'vpc_id',
        'ipaddress_count': 'ipaddress_count',
        'resolver_rule_count': 'resolver_rule_count',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, direction=None, status=None, vpc_id=None, ipaddress_count=None, resolver_rule_count=None, create_time=None, update_time=None):
        """EndpointResp

        The model defined in huaweicloud sdk

        :param id: endpoint的ID，uuid形式的一个资源标识。
        :type id: str
        :param name: endpoint的名称。
        :type name: str
        :param direction: endpoint的ID，uuid形式的一个资源标识。
        :type direction: str
        :param status: 资源状态。 取值范围：PENDING_CREATE, ACTIVE, PENDING_DELETE, ERROR。
        :type status: str
        :param vpc_id: endpoint所属的vpc_id。
        :type vpc_id: str
        :param ipaddress_count: 该endpoint下的ip地址数量。
        :type ipaddress_count: int
        :param resolver_rule_count: 该endpoint下的解析规则数量。 仅创建出站终端节点时返回该参数。
        :type resolver_rule_count: int
        :param create_time: 创建时间。
        :type create_time: str
        :param update_time: 更新时间。
        :type update_time: str
        """
        
        

        self._id = None
        self._name = None
        self._direction = None
        self._status = None
        self._vpc_id = None
        self._ipaddress_count = None
        self._resolver_rule_count = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if direction is not None:
            self.direction = direction
        if status is not None:
            self.status = status
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if ipaddress_count is not None:
            self.ipaddress_count = ipaddress_count
        if resolver_rule_count is not None:
            self.resolver_rule_count = resolver_rule_count
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this EndpointResp.

        endpoint的ID，uuid形式的一个资源标识。

        :return: The id of this EndpointResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointResp.

        endpoint的ID，uuid形式的一个资源标识。

        :param id: The id of this EndpointResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EndpointResp.

        endpoint的名称。

        :return: The name of this EndpointResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EndpointResp.

        endpoint的名称。

        :param name: The name of this EndpointResp.
        :type name: str
        """
        self._name = name

    @property
    def direction(self):
        """Gets the direction of this EndpointResp.

        endpoint的ID，uuid形式的一个资源标识。

        :return: The direction of this EndpointResp.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this EndpointResp.

        endpoint的ID，uuid形式的一个资源标识。

        :param direction: The direction of this EndpointResp.
        :type direction: str
        """
        self._direction = direction

    @property
    def status(self):
        """Gets the status of this EndpointResp.

        资源状态。 取值范围：PENDING_CREATE, ACTIVE, PENDING_DELETE, ERROR。

        :return: The status of this EndpointResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EndpointResp.

        资源状态。 取值范围：PENDING_CREATE, ACTIVE, PENDING_DELETE, ERROR。

        :param status: The status of this EndpointResp.
        :type status: str
        """
        self._status = status

    @property
    def vpc_id(self):
        """Gets the vpc_id of this EndpointResp.

        endpoint所属的vpc_id。

        :return: The vpc_id of this EndpointResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this EndpointResp.

        endpoint所属的vpc_id。

        :param vpc_id: The vpc_id of this EndpointResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def ipaddress_count(self):
        """Gets the ipaddress_count of this EndpointResp.

        该endpoint下的ip地址数量。

        :return: The ipaddress_count of this EndpointResp.
        :rtype: int
        """
        return self._ipaddress_count

    @ipaddress_count.setter
    def ipaddress_count(self, ipaddress_count):
        """Sets the ipaddress_count of this EndpointResp.

        该endpoint下的ip地址数量。

        :param ipaddress_count: The ipaddress_count of this EndpointResp.
        :type ipaddress_count: int
        """
        self._ipaddress_count = ipaddress_count

    @property
    def resolver_rule_count(self):
        """Gets the resolver_rule_count of this EndpointResp.

        该endpoint下的解析规则数量。 仅创建出站终端节点时返回该参数。

        :return: The resolver_rule_count of this EndpointResp.
        :rtype: int
        """
        return self._resolver_rule_count

    @resolver_rule_count.setter
    def resolver_rule_count(self, resolver_rule_count):
        """Sets the resolver_rule_count of this EndpointResp.

        该endpoint下的解析规则数量。 仅创建出站终端节点时返回该参数。

        :param resolver_rule_count: The resolver_rule_count of this EndpointResp.
        :type resolver_rule_count: int
        """
        self._resolver_rule_count = resolver_rule_count

    @property
    def create_time(self):
        """Gets the create_time of this EndpointResp.

        创建时间。

        :return: The create_time of this EndpointResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this EndpointResp.

        创建时间。

        :param create_time: The create_time of this EndpointResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this EndpointResp.

        更新时间。

        :return: The update_time of this EndpointResp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this EndpointResp.

        更新时间。

        :param update_time: The update_time of this EndpointResp.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, EndpointResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
