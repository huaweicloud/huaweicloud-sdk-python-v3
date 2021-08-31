# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlProxyNode:


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
        'available_zones': 'list[MysqlProxyAvailable]'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'status': 'status',
        'name': 'name',
        'weight': 'weight',
        'available_zones': 'available_zones'
    }

    def __init__(self, id=None, instance_id=None, status=None, name=None, weight=None, available_zones=None):
        """MysqlProxyNode - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._instance_id = None
        self._status = None
        self._name = None
        self._weight = None
        self._available_zones = None
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
        if available_zones is not None:
            self.available_zones = available_zones

    @property
    def id(self):
        """Gets the id of this MysqlProxyNode.

        节点id。

        :return: The id of this MysqlProxyNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MysqlProxyNode.

        节点id。

        :param id: The id of this MysqlProxyNode.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this MysqlProxyNode.

        实例id。

        :return: The instance_id of this MysqlProxyNode.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this MysqlProxyNode.

        实例id。

        :param instance_id: The instance_id of this MysqlProxyNode.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        """Gets the status of this MysqlProxyNode.

        节点状态。

        :return: The status of this MysqlProxyNode.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MysqlProxyNode.

        节点状态。

        :param status: The status of this MysqlProxyNode.
        :type: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this MysqlProxyNode.

        节点名称。

        :return: The name of this MysqlProxyNode.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MysqlProxyNode.

        节点名称。

        :param name: The name of this MysqlProxyNode.
        :type: str
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this MysqlProxyNode.

        节点读写分离权重。

        :return: The weight of this MysqlProxyNode.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this MysqlProxyNode.

        节点读写分离权重。

        :param weight: The weight of this MysqlProxyNode.
        :type: int
        """
        self._weight = weight

    @property
    def available_zones(self):
        """Gets the available_zones of this MysqlProxyNode.

        可用区信息。

        :return: The available_zones of this MysqlProxyNode.
        :rtype: list[MysqlProxyAvailable]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this MysqlProxyNode.

        可用区信息。

        :param available_zones: The available_zones of this MysqlProxyNode.
        :type: list[MysqlProxyAvailable]
        """
        self._available_zones = available_zones

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
        if not isinstance(other, MysqlProxyNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
