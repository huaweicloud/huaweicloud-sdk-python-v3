# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceInfo:

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
        'status': 'str',
        'name': 'str',
        'weight': 'int',
        'available_zones': 'list[MysqlAvailableZoneInfo]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'weight': 'weight',
        'available_zones': 'available_zones'
    }

    def __init__(self, id=None, status=None, name=None, weight=None, available_zones=None):
        r"""InstanceInfo

        The model defined in huaweicloud sdk

        :param id: 数据库主实例或只读实例ID。
        :type id: str
        :param status: 节点状态。
        :type status: str
        :param name: 数据库实例名称。
        :type name: str
        :param weight: 数据库实例读权重。
        :type weight: int
        :param available_zones: 可用区信息。
        :type available_zones: list[:class:`huaweicloudsdkrds.v3.MysqlAvailableZoneInfo`]
        """
        
        

        self._id = None
        self._status = None
        self._name = None
        self._weight = None
        self._available_zones = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        r"""Gets the id of this InstanceInfo.

        数据库主实例或只读实例ID。

        :return: The id of this InstanceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstanceInfo.

        数据库主实例或只读实例ID。

        :param id: The id of this InstanceInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this InstanceInfo.

        节点状态。

        :return: The status of this InstanceInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceInfo.

        节点状态。

        :param status: The status of this InstanceInfo.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this InstanceInfo.

        数据库实例名称。

        :return: The name of this InstanceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceInfo.

        数据库实例名称。

        :param name: The name of this InstanceInfo.
        :type name: str
        """
        self._name = name

    @property
    def weight(self):
        r"""Gets the weight of this InstanceInfo.

        数据库实例读权重。

        :return: The weight of this InstanceInfo.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this InstanceInfo.

        数据库实例读权重。

        :param weight: The weight of this InstanceInfo.
        :type weight: int
        """
        self._weight = weight

    @property
    def available_zones(self):
        r"""Gets the available_zones of this InstanceInfo.

        可用区信息。

        :return: The available_zones of this InstanceInfo.
        :rtype: list[:class:`huaweicloudsdkrds.v3.MysqlAvailableZoneInfo`]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this InstanceInfo.

        可用区信息。

        :param available_zones: The available_zones of this InstanceInfo.
        :type available_zones: list[:class:`huaweicloudsdkrds.v3.MysqlAvailableZoneInfo`]
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
        if not isinstance(other, InstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
