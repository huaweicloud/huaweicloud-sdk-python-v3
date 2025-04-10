# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostClusterRequest:

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
        'slave_cluster_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'slave_cluster_id': 'slave_cluster_id'
    }

    def __init__(self, name=None, description=None, slave_cluster_id=None):
        r"""HostClusterRequest

        The model defined in huaweicloud sdk

        :param name: 主机集群名称
        :type name: str
        :param description: 主机集群描述
        :type description: str
        :param slave_cluster_id: slave集群id，默认为null时使用八爪鱼slave集群，用户自定义slave时为slave集群id
        :type slave_cluster_id: str
        """
        
        

        self._name = None
        self._description = None
        self._slave_cluster_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id

    @property
    def name(self):
        r"""Gets the name of this HostClusterRequest.

        主机集群名称

        :return: The name of this HostClusterRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HostClusterRequest.

        主机集群名称

        :param name: The name of this HostClusterRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this HostClusterRequest.

        主机集群描述

        :return: The description of this HostClusterRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this HostClusterRequest.

        主机集群描述

        :param description: The description of this HostClusterRequest.
        :type description: str
        """
        self._description = description

    @property
    def slave_cluster_id(self):
        r"""Gets the slave_cluster_id of this HostClusterRequest.

        slave集群id，默认为null时使用八爪鱼slave集群，用户自定义slave时为slave集群id

        :return: The slave_cluster_id of this HostClusterRequest.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        r"""Sets the slave_cluster_id of this HostClusterRequest.

        slave集群id，默认为null时使用八爪鱼slave集群，用户自定义slave时为slave集群id

        :param slave_cluster_id: The slave_cluster_id of this HostClusterRequest.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

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
        if not isinstance(other, HostClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
