# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceReplicationListInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replication_role': 'str',
        'replication_ip': 'str',
        'is_replication': 'bool',
        'replication_id': 'str',
        'node_id': 'str',
        'status': 'str',
        'az_code': 'str',
        'dimensions': 'list[InstanceReplicationDimensionsInfo]'
    }

    attribute_map = {
        'replication_role': 'replication_role',
        'replication_ip': 'replication_ip',
        'is_replication': 'is_replication',
        'replication_id': 'replication_id',
        'node_id': 'node_id',
        'status': 'status',
        'az_code': 'az_code',
        'dimensions': 'dimensions'
    }

    def __init__(self, replication_role=None, replication_ip=None, is_replication=None, replication_id=None, node_id=None, status=None, az_code=None, dimensions=None):
        """InstanceReplicationListInfo

        The model defined in huaweicloud sdk

        :param replication_role: 副本角色，取值有： - master：表示主节点。 - slave：表示从节点。 
        :type replication_role: str
        :param replication_ip: 副本IP。
        :type replication_ip: str
        :param is_replication: 是否是新加副本。
        :type is_replication: bool
        :param replication_id: 副本id。
        :type replication_id: str
        :param node_id: 节点id。
        :type node_id: str
        :param status: 副本状态。
        :type status: str
        :param az_code: 副本所在的可用区
        :type az_code: str
        :param dimensions: 副本对应的监控指标维度信息。可用于调用云监控服务的查询监控数据指标相关接口 - 副本的监控维度为多维度，返回数组中包含两个维度信息。从云监控查询监控数据时，要按多维度传递指标维度参数，才能查询到监控指标值 - 第一个维度为副本父维度信息，维度名称为dcs_instance_id，维度值对应副本所在的实例ID - 第二个维度，维度名称为dcs_cluster_redis_node,维度值为副本的监控对象ID，与副本ID和节点ID不同。 
        :type dimensions: list[:class:`huaweicloudsdkdcs.v2.InstanceReplicationDimensionsInfo`]
        """
        
        

        self._replication_role = None
        self._replication_ip = None
        self._is_replication = None
        self._replication_id = None
        self._node_id = None
        self._status = None
        self._az_code = None
        self._dimensions = None
        self.discriminator = None

        if replication_role is not None:
            self.replication_role = replication_role
        if replication_ip is not None:
            self.replication_ip = replication_ip
        if is_replication is not None:
            self.is_replication = is_replication
        if replication_id is not None:
            self.replication_id = replication_id
        if node_id is not None:
            self.node_id = node_id
        if status is not None:
            self.status = status
        if az_code is not None:
            self.az_code = az_code
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def replication_role(self):
        """Gets the replication_role of this InstanceReplicationListInfo.

        副本角色，取值有： - master：表示主节点。 - slave：表示从节点。 

        :return: The replication_role of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._replication_role

    @replication_role.setter
    def replication_role(self, replication_role):
        """Sets the replication_role of this InstanceReplicationListInfo.

        副本角色，取值有： - master：表示主节点。 - slave：表示从节点。 

        :param replication_role: The replication_role of this InstanceReplicationListInfo.
        :type replication_role: str
        """
        self._replication_role = replication_role

    @property
    def replication_ip(self):
        """Gets the replication_ip of this InstanceReplicationListInfo.

        副本IP。

        :return: The replication_ip of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._replication_ip

    @replication_ip.setter
    def replication_ip(self, replication_ip):
        """Sets the replication_ip of this InstanceReplicationListInfo.

        副本IP。

        :param replication_ip: The replication_ip of this InstanceReplicationListInfo.
        :type replication_ip: str
        """
        self._replication_ip = replication_ip

    @property
    def is_replication(self):
        """Gets the is_replication of this InstanceReplicationListInfo.

        是否是新加副本。

        :return: The is_replication of this InstanceReplicationListInfo.
        :rtype: bool
        """
        return self._is_replication

    @is_replication.setter
    def is_replication(self, is_replication):
        """Sets the is_replication of this InstanceReplicationListInfo.

        是否是新加副本。

        :param is_replication: The is_replication of this InstanceReplicationListInfo.
        :type is_replication: bool
        """
        self._is_replication = is_replication

    @property
    def replication_id(self):
        """Gets the replication_id of this InstanceReplicationListInfo.

        副本id。

        :return: The replication_id of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._replication_id

    @replication_id.setter
    def replication_id(self, replication_id):
        """Sets the replication_id of this InstanceReplicationListInfo.

        副本id。

        :param replication_id: The replication_id of this InstanceReplicationListInfo.
        :type replication_id: str
        """
        self._replication_id = replication_id

    @property
    def node_id(self):
        """Gets the node_id of this InstanceReplicationListInfo.

        节点id。

        :return: The node_id of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this InstanceReplicationListInfo.

        节点id。

        :param node_id: The node_id of this InstanceReplicationListInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def status(self):
        """Gets the status of this InstanceReplicationListInfo.

        副本状态。

        :return: The status of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceReplicationListInfo.

        副本状态。

        :param status: The status of this InstanceReplicationListInfo.
        :type status: str
        """
        self._status = status

    @property
    def az_code(self):
        """Gets the az_code of this InstanceReplicationListInfo.

        副本所在的可用区

        :return: The az_code of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this InstanceReplicationListInfo.

        副本所在的可用区

        :param az_code: The az_code of this InstanceReplicationListInfo.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def dimensions(self):
        """Gets the dimensions of this InstanceReplicationListInfo.

        副本对应的监控指标维度信息。可用于调用云监控服务的查询监控数据指标相关接口 - 副本的监控维度为多维度，返回数组中包含两个维度信息。从云监控查询监控数据时，要按多维度传递指标维度参数，才能查询到监控指标值 - 第一个维度为副本父维度信息，维度名称为dcs_instance_id，维度值对应副本所在的实例ID - 第二个维度，维度名称为dcs_cluster_redis_node,维度值为副本的监控对象ID，与副本ID和节点ID不同。 

        :return: The dimensions of this InstanceReplicationListInfo.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.InstanceReplicationDimensionsInfo`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this InstanceReplicationListInfo.

        副本对应的监控指标维度信息。可用于调用云监控服务的查询监控数据指标相关接口 - 副本的监控维度为多维度，返回数组中包含两个维度信息。从云监控查询监控数据时，要按多维度传递指标维度参数，才能查询到监控指标值 - 第一个维度为副本父维度信息，维度名称为dcs_instance_id，维度值对应副本所在的实例ID - 第二个维度，维度名称为dcs_cluster_redis_node,维度值为副本的监控对象ID，与副本ID和节点ID不同。 

        :param dimensions: The dimensions of this InstanceReplicationListInfo.
        :type dimensions: list[:class:`huaweicloudsdkdcs.v2.InstanceReplicationDimensionsInfo`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, InstanceReplicationListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
