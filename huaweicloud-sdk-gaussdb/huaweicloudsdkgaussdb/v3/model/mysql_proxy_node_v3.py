# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlProxyNodeV3:

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
        'instance_id': 'str',
        'status': 'str',
        'name': 'str',
        'weight': 'int',
        'availability_zone': 'list[MysqlProxyAvailable]'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'status': 'status',
        'name': 'name',
        'weight': 'weight',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, id=None, instance_id=None, status=None, name=None, weight=None, availability_zone=None):
        """MysqlProxyNodeV3

        The model defined in huaweicloud sdk

        :param id: 节点ID。
        :type id: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param status: 节点状态。
        :type status: str
        :param name: 节点名称。
        :type name: str
        :param weight: 节点读写分离读权重。
        :type weight: int
        :param availability_zone: 主实例所有节点的可用区信息。
        :type availability_zone: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyAvailable`]
        """
        
        

        self._id = None
        self._instance_id = None
        self._status = None
        self._name = None
        self._weight = None
        self._availability_zone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def id(self):
        """Gets the id of this MysqlProxyNodeV3.

        节点ID。

        :return: The id of this MysqlProxyNodeV3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MysqlProxyNodeV3.

        节点ID。

        :param id: The id of this MysqlProxyNodeV3.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this MysqlProxyNodeV3.

        实例ID。

        :return: The instance_id of this MysqlProxyNodeV3.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this MysqlProxyNodeV3.

        实例ID。

        :param instance_id: The instance_id of this MysqlProxyNodeV3.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        """Gets the status of this MysqlProxyNodeV3.

        节点状态。

        :return: The status of this MysqlProxyNodeV3.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MysqlProxyNodeV3.

        节点状态。

        :param status: The status of this MysqlProxyNodeV3.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this MysqlProxyNodeV3.

        节点名称。

        :return: The name of this MysqlProxyNodeV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MysqlProxyNodeV3.

        节点名称。

        :param name: The name of this MysqlProxyNodeV3.
        :type name: str
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this MysqlProxyNodeV3.

        节点读写分离读权重。

        :return: The weight of this MysqlProxyNodeV3.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this MysqlProxyNodeV3.

        节点读写分离读权重。

        :param weight: The weight of this MysqlProxyNodeV3.
        :type weight: int
        """
        self._weight = weight

    @property
    def availability_zone(self):
        """Gets the availability_zone of this MysqlProxyNodeV3.

        主实例所有节点的可用区信息。

        :return: The availability_zone of this MysqlProxyNodeV3.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyAvailable`]
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this MysqlProxyNodeV3.

        主实例所有节点的可用区信息。

        :param availability_zone: The availability_zone of this MysqlProxyNodeV3.
        :type availability_zone: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyAvailable`]
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, MysqlProxyNodeV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
