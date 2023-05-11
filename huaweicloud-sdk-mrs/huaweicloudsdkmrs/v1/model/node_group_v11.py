# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeGroupV11:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'node_num': 'int',
        'node_size': 'str',
        'root_volume_size': 'str',
        'root_volume_type': 'str',
        'data_volume_type': 'str',
        'data_volume_count': 'int',
        'data_volume_size': 'int',
        'auto_scaling_policy': 'AutoScalingPolicy'
    }

    attribute_map = {
        'group_name': 'group_name',
        'node_num': 'node_num',
        'node_size': 'node_size',
        'root_volume_size': 'root_volume_size',
        'root_volume_type': 'root_volume_type',
        'data_volume_type': 'data_volume_type',
        'data_volume_count': 'data_volume_count',
        'data_volume_size': 'data_volume_size',
        'auto_scaling_policy': 'auto_scaling_policy'
    }

    def __init__(self, group_name=None, node_num=None, node_size=None, root_volume_size=None, root_volume_type=None, data_volume_type=None, data_volume_count=None, data_volume_size=None, auto_scaling_policy=None):
        """NodeGroupV11

        The model defined in huaweicloud sdk

        :param group_name: 节点组名。 - master_node_default_group - core_node_analysis_group - core_node_streaming_group - task_node_analysis_group - task_node_streaming_group
        :type group_name: str
        :param node_num: 节点数量，取值范围0～500，Core与Task节点总数最大为500个。
        :type node_num: int
        :param node_size: 节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。MRS当前支持主机规格的配型由CPU+内存+Disk共同决定。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。
        :type node_size: str
        :param root_volume_size: 节点系统磁盘存储大小。
        :type root_volume_size: str
        :param root_volume_type: 节点系统磁盘存储类别，目前支持SATA、SAS和SSD。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD
        :type root_volume_type: str
        :param data_volume_type: 节点数据磁盘存储类别，目前支持SATA、SAS和SSD。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD
        :type data_volume_type: str
        :param data_volume_count: 节点数据磁盘存储数目 取值范围：0～10。
        :type data_volume_count: int
        :param data_volume_size: 节点数据磁盘存储大小 取值范围：100GB～32000GB。
        :type data_volume_size: int
        :param auto_scaling_policy: 
        :type auto_scaling_policy: :class:`huaweicloudsdkmrs.v1.AutoScalingPolicy`
        """
        
        

        self._group_name = None
        self._node_num = None
        self._node_size = None
        self._root_volume_size = None
        self._root_volume_type = None
        self._data_volume_type = None
        self._data_volume_count = None
        self._data_volume_size = None
        self._auto_scaling_policy = None
        self.discriminator = None

        self.group_name = group_name
        self.node_num = node_num
        self.node_size = node_size
        if root_volume_size is not None:
            self.root_volume_size = root_volume_size
        if root_volume_type is not None:
            self.root_volume_type = root_volume_type
        if data_volume_type is not None:
            self.data_volume_type = data_volume_type
        if data_volume_count is not None:
            self.data_volume_count = data_volume_count
        if data_volume_size is not None:
            self.data_volume_size = data_volume_size
        if auto_scaling_policy is not None:
            self.auto_scaling_policy = auto_scaling_policy

    @property
    def group_name(self):
        """Gets the group_name of this NodeGroupV11.

        节点组名。 - master_node_default_group - core_node_analysis_group - core_node_streaming_group - task_node_analysis_group - task_node_streaming_group

        :return: The group_name of this NodeGroupV11.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this NodeGroupV11.

        节点组名。 - master_node_default_group - core_node_analysis_group - core_node_streaming_group - task_node_analysis_group - task_node_streaming_group

        :param group_name: The group_name of this NodeGroupV11.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def node_num(self):
        """Gets the node_num of this NodeGroupV11.

        节点数量，取值范围0～500，Core与Task节点总数最大为500个。

        :return: The node_num of this NodeGroupV11.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this NodeGroupV11.

        节点数量，取值范围0～500，Core与Task节点总数最大为500个。

        :param node_num: The node_num of this NodeGroupV11.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def node_size(self):
        """Gets the node_size of this NodeGroupV11.

        节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。MRS当前支持主机规格的配型由CPU+内存+Disk共同决定。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。

        :return: The node_size of this NodeGroupV11.
        :rtype: str
        """
        return self._node_size

    @node_size.setter
    def node_size(self, node_size):
        """Sets the node_size of this NodeGroupV11.

        节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。MRS当前支持主机规格的配型由CPU+内存+Disk共同决定。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。

        :param node_size: The node_size of this NodeGroupV11.
        :type node_size: str
        """
        self._node_size = node_size

    @property
    def root_volume_size(self):
        """Gets the root_volume_size of this NodeGroupV11.

        节点系统磁盘存储大小。

        :return: The root_volume_size of this NodeGroupV11.
        :rtype: str
        """
        return self._root_volume_size

    @root_volume_size.setter
    def root_volume_size(self, root_volume_size):
        """Sets the root_volume_size of this NodeGroupV11.

        节点系统磁盘存储大小。

        :param root_volume_size: The root_volume_size of this NodeGroupV11.
        :type root_volume_size: str
        """
        self._root_volume_size = root_volume_size

    @property
    def root_volume_type(self):
        """Gets the root_volume_type of this NodeGroupV11.

        节点系统磁盘存储类别，目前支持SATA、SAS和SSD。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD

        :return: The root_volume_type of this NodeGroupV11.
        :rtype: str
        """
        return self._root_volume_type

    @root_volume_type.setter
    def root_volume_type(self, root_volume_type):
        """Sets the root_volume_type of this NodeGroupV11.

        节点系统磁盘存储类别，目前支持SATA、SAS和SSD。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD

        :param root_volume_type: The root_volume_type of this NodeGroupV11.
        :type root_volume_type: str
        """
        self._root_volume_type = root_volume_type

    @property
    def data_volume_type(self):
        """Gets the data_volume_type of this NodeGroupV11.

        节点数据磁盘存储类别，目前支持SATA、SAS和SSD。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD

        :return: The data_volume_type of this NodeGroupV11.
        :rtype: str
        """
        return self._data_volume_type

    @data_volume_type.setter
    def data_volume_type(self, data_volume_type):
        """Sets the data_volume_type of this NodeGroupV11.

        节点数据磁盘存储类别，目前支持SATA、SAS和SSD。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD

        :param data_volume_type: The data_volume_type of this NodeGroupV11.
        :type data_volume_type: str
        """
        self._data_volume_type = data_volume_type

    @property
    def data_volume_count(self):
        """Gets the data_volume_count of this NodeGroupV11.

        节点数据磁盘存储数目 取值范围：0～10。

        :return: The data_volume_count of this NodeGroupV11.
        :rtype: int
        """
        return self._data_volume_count

    @data_volume_count.setter
    def data_volume_count(self, data_volume_count):
        """Sets the data_volume_count of this NodeGroupV11.

        节点数据磁盘存储数目 取值范围：0～10。

        :param data_volume_count: The data_volume_count of this NodeGroupV11.
        :type data_volume_count: int
        """
        self._data_volume_count = data_volume_count

    @property
    def data_volume_size(self):
        """Gets the data_volume_size of this NodeGroupV11.

        节点数据磁盘存储大小 取值范围：100GB～32000GB。

        :return: The data_volume_size of this NodeGroupV11.
        :rtype: int
        """
        return self._data_volume_size

    @data_volume_size.setter
    def data_volume_size(self, data_volume_size):
        """Sets the data_volume_size of this NodeGroupV11.

        节点数据磁盘存储大小 取值范围：100GB～32000GB。

        :param data_volume_size: The data_volume_size of this NodeGroupV11.
        :type data_volume_size: int
        """
        self._data_volume_size = data_volume_size

    @property
    def auto_scaling_policy(self):
        """Gets the auto_scaling_policy of this NodeGroupV11.

        :return: The auto_scaling_policy of this NodeGroupV11.
        :rtype: :class:`huaweicloudsdkmrs.v1.AutoScalingPolicy`
        """
        return self._auto_scaling_policy

    @auto_scaling_policy.setter
    def auto_scaling_policy(self, auto_scaling_policy):
        """Sets the auto_scaling_policy of this NodeGroupV11.

        :param auto_scaling_policy: The auto_scaling_policy of this NodeGroupV11.
        :type auto_scaling_policy: :class:`huaweicloudsdkmrs.v1.AutoScalingPolicy`
        """
        self._auto_scaling_policy = auto_scaling_policy

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
        if not isinstance(other, NodeGroupV11):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
