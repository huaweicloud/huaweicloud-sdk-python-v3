# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterNode:

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
        'az': 'str',
        'ip': 'str',
        'label': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'az': 'az',
        'ip': 'ip',
        'label': 'label',
        'status': 'status'
    }

    def __init__(self, id=None, az=None, ip=None, label=None, status=None):
        """ClusterNode

        The model defined in huaweicloud sdk

        :param id: 微服务引擎专享版CCE节点ID
        :type id: str
        :param az: 微服务引擎专享版CCE节点所属可用区
        :type az: str
        :param ip: 微服务引擎专享版CCE节点IP
        :type ip: str
        :param label: 微服务引擎专享版CCE节点标签
        :type label: str
        :param status: 微服务引擎专享版CCE节点状态
        :type status: str
        """
        
        

        self._id = None
        self._az = None
        self._ip = None
        self._label = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if az is not None:
            self.az = az
        if ip is not None:
            self.ip = ip
        if label is not None:
            self.label = label
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this ClusterNode.

        微服务引擎专享版CCE节点ID

        :return: The id of this ClusterNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterNode.

        微服务引擎专享版CCE节点ID

        :param id: The id of this ClusterNode.
        :type id: str
        """
        self._id = id

    @property
    def az(self):
        """Gets the az of this ClusterNode.

        微服务引擎专享版CCE节点所属可用区

        :return: The az of this ClusterNode.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this ClusterNode.

        微服务引擎专享版CCE节点所属可用区

        :param az: The az of this ClusterNode.
        :type az: str
        """
        self._az = az

    @property
    def ip(self):
        """Gets the ip of this ClusterNode.

        微服务引擎专享版CCE节点IP

        :return: The ip of this ClusterNode.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ClusterNode.

        微服务引擎专享版CCE节点IP

        :param ip: The ip of this ClusterNode.
        :type ip: str
        """
        self._ip = ip

    @property
    def label(self):
        """Gets the label of this ClusterNode.

        微服务引擎专享版CCE节点标签

        :return: The label of this ClusterNode.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ClusterNode.

        微服务引擎专享版CCE节点标签

        :param label: The label of this ClusterNode.
        :type label: str
        """
        self._label = label

    @property
    def status(self):
        """Gets the status of this ClusterNode.

        微服务引擎专享版CCE节点状态

        :return: The status of this ClusterNode.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterNode.

        微服务引擎专享版CCE节点状态

        :param status: The status of this ClusterNode.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ClusterNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
