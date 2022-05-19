# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskNodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'node_size': 'str',
        'data_volume_type': 'str',
        'data_volume_count': 'int',
        'data_volume_size': 'int'
    }

    attribute_map = {
        'node_size': 'node_size',
        'data_volume_type': 'data_volume_type',
        'data_volume_count': 'data_volume_count',
        'data_volume_size': 'data_volume_size'
    }

    def __init__(self, node_size=None, data_volume_type=None, data_volume_count=None, data_volume_size=None):
        """TaskNodeInfo

        The model defined in huaweicloud sdk

        :param node_size: Task节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。
        :type node_size: str
        :param data_volume_type: Task节点数据磁盘存储类别，目前支持SATA、SAS和SSD。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD
        :type data_volume_type: str
        :param data_volume_count: Task节点数据磁盘存储数目，取值范围：0～10。
        :type data_volume_count: int
        :param data_volume_size: Task节点数据磁盘存储大小。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。
        :type data_volume_size: int
        """
        
        

        self._node_size = None
        self._data_volume_type = None
        self._data_volume_count = None
        self._data_volume_size = None
        self.discriminator = None

        self.node_size = node_size
        self.data_volume_type = data_volume_type
        self.data_volume_count = data_volume_count
        self.data_volume_size = data_volume_size

    @property
    def node_size(self):
        """Gets the node_size of this TaskNodeInfo.

        Task节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。

        :return: The node_size of this TaskNodeInfo.
        :rtype: str
        """
        return self._node_size

    @node_size.setter
    def node_size(self, node_size):
        """Sets the node_size of this TaskNodeInfo.

        Task节点的实例规格，例如：c3.4xlarge.2.linux.bigdata。实例规格详细说明请参见[MRS所使用的弹性云服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9006.html)和[MRS所使用的裸金属服务器规格](https://support.huaweicloud.com/api-mrs/mrs_01_9001.html)。 该参数建议从MRS控制台的集群创建页面获取对应区域对应版本所支持的规格。

        :param node_size: The node_size of this TaskNodeInfo.
        :type node_size: str
        """
        self._node_size = node_size

    @property
    def data_volume_type(self):
        """Gets the data_volume_type of this TaskNodeInfo.

        Task节点数据磁盘存储类别，目前支持SATA、SAS和SSD。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD

        :return: The data_volume_type of this TaskNodeInfo.
        :rtype: str
        """
        return self._data_volume_type

    @data_volume_type.setter
    def data_volume_type(self, data_volume_type):
        """Sets the data_volume_type of this TaskNodeInfo.

        Task节点数据磁盘存储类别，目前支持SATA、SAS和SSD。 - SATA：普通IO - SAS：高IO - SSD：超高IO - GPSSD：通用型SSD

        :param data_volume_type: The data_volume_type of this TaskNodeInfo.
        :type data_volume_type: str
        """
        self._data_volume_type = data_volume_type

    @property
    def data_volume_count(self):
        """Gets the data_volume_count of this TaskNodeInfo.

        Task节点数据磁盘存储数目，取值范围：0～10。

        :return: The data_volume_count of this TaskNodeInfo.
        :rtype: int
        """
        return self._data_volume_count

    @data_volume_count.setter
    def data_volume_count(self, data_volume_count):
        """Sets the data_volume_count of this TaskNodeInfo.

        Task节点数据磁盘存储数目，取值范围：0～10。

        :param data_volume_count: The data_volume_count of this TaskNodeInfo.
        :type data_volume_count: int
        """
        self._data_volume_count = data_volume_count

    @property
    def data_volume_size(self):
        """Gets the data_volume_size of this TaskNodeInfo.

        Task节点数据磁盘存储大小。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。

        :return: The data_volume_size of this TaskNodeInfo.
        :rtype: int
        """
        return self._data_volume_size

    @data_volume_size.setter
    def data_volume_size(self, data_volume_size):
        """Sets the data_volume_size of this TaskNodeInfo.

        Task节点数据磁盘存储大小。  取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。

        :param data_volume_size: The data_volume_size of this TaskNodeInfo.
        :type data_volume_size: int
        """
        self._data_volume_size = data_volume_size

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
        if not isinstance(other, TaskNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
