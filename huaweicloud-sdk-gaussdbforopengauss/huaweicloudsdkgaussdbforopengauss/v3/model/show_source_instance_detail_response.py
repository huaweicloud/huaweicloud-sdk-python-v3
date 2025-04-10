# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSourceInstanceDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_mode': 'str',
        'instance_mode': 'str',
        'data_volume_size': 'str',
        'solution': 'str',
        'node_num': 'int',
        'coordinator_num': 'int',
        'sharding_num': 'int',
        'replica_num': 'int',
        'engine_version': 'str'
    }

    attribute_map = {
        'cluster_mode': 'cluster_mode',
        'instance_mode': 'instance_mode',
        'data_volume_size': 'data_volume_size',
        'solution': 'solution',
        'node_num': 'node_num',
        'coordinator_num': 'coordinator_num',
        'sharding_num': 'sharding_num',
        'replica_num': 'replica_num',
        'engine_version': 'engine_version'
    }

    def __init__(self, cluster_mode=None, instance_mode=None, data_volume_size=None, solution=None, node_num=None, coordinator_num=None, sharding_num=None, replica_num=None, engine_version=None):
        r"""ShowSourceInstanceDetailResponse

        The model defined in huaweicloud sdk

        :param cluster_mode: 实例部署形态。集中式Ha(主备)、分布式Independent(独立部署)。
        :type cluster_mode: str
        :param instance_mode: 实例模型，企业版enterprise，标准版standard，基础版basic。
        :type instance_mode: str
        :param data_volume_size: 磁盘大小，单位：GB。
        :type data_volume_size: str
        :param solution: 解决方案模板类型。集中式Ha一般用triset，分布式Independent一般为空或者默认hws。  描述如下：  triset：高可用(1主2备)  hws：默认。
        :type solution: str
        :param node_num: 节点数量。
        :type node_num: int
        :param coordinator_num: 协调节点数量。
        :type coordinator_num: int
        :param sharding_num: 分片数量。
        :type sharding_num: int
        :param replica_num: 副本数量。
        :type replica_num: int
        :param engine_version: 引擎版本。
        :type engine_version: str
        """
        
        super(ShowSourceInstanceDetailResponse, self).__init__()

        self._cluster_mode = None
        self._instance_mode = None
        self._data_volume_size = None
        self._solution = None
        self._node_num = None
        self._coordinator_num = None
        self._sharding_num = None
        self._replica_num = None
        self._engine_version = None
        self.discriminator = None

        if cluster_mode is not None:
            self.cluster_mode = cluster_mode
        if instance_mode is not None:
            self.instance_mode = instance_mode
        if data_volume_size is not None:
            self.data_volume_size = data_volume_size
        if solution is not None:
            self.solution = solution
        if node_num is not None:
            self.node_num = node_num
        if coordinator_num is not None:
            self.coordinator_num = coordinator_num
        if sharding_num is not None:
            self.sharding_num = sharding_num
        if replica_num is not None:
            self.replica_num = replica_num
        if engine_version is not None:
            self.engine_version = engine_version

    @property
    def cluster_mode(self):
        r"""Gets the cluster_mode of this ShowSourceInstanceDetailResponse.

        实例部署形态。集中式Ha(主备)、分布式Independent(独立部署)。

        :return: The cluster_mode of this ShowSourceInstanceDetailResponse.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        r"""Sets the cluster_mode of this ShowSourceInstanceDetailResponse.

        实例部署形态。集中式Ha(主备)、分布式Independent(独立部署)。

        :param cluster_mode: The cluster_mode of this ShowSourceInstanceDetailResponse.
        :type cluster_mode: str
        """
        self._cluster_mode = cluster_mode

    @property
    def instance_mode(self):
        r"""Gets the instance_mode of this ShowSourceInstanceDetailResponse.

        实例模型，企业版enterprise，标准版standard，基础版basic。

        :return: The instance_mode of this ShowSourceInstanceDetailResponse.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        r"""Sets the instance_mode of this ShowSourceInstanceDetailResponse.

        实例模型，企业版enterprise，标准版standard，基础版basic。

        :param instance_mode: The instance_mode of this ShowSourceInstanceDetailResponse.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def data_volume_size(self):
        r"""Gets the data_volume_size of this ShowSourceInstanceDetailResponse.

        磁盘大小，单位：GB。

        :return: The data_volume_size of this ShowSourceInstanceDetailResponse.
        :rtype: str
        """
        return self._data_volume_size

    @data_volume_size.setter
    def data_volume_size(self, data_volume_size):
        r"""Sets the data_volume_size of this ShowSourceInstanceDetailResponse.

        磁盘大小，单位：GB。

        :param data_volume_size: The data_volume_size of this ShowSourceInstanceDetailResponse.
        :type data_volume_size: str
        """
        self._data_volume_size = data_volume_size

    @property
    def solution(self):
        r"""Gets the solution of this ShowSourceInstanceDetailResponse.

        解决方案模板类型。集中式Ha一般用triset，分布式Independent一般为空或者默认hws。  描述如下：  triset：高可用(1主2备)  hws：默认。

        :return: The solution of this ShowSourceInstanceDetailResponse.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this ShowSourceInstanceDetailResponse.

        解决方案模板类型。集中式Ha一般用triset，分布式Independent一般为空或者默认hws。  描述如下：  triset：高可用(1主2备)  hws：默认。

        :param solution: The solution of this ShowSourceInstanceDetailResponse.
        :type solution: str
        """
        self._solution = solution

    @property
    def node_num(self):
        r"""Gets the node_num of this ShowSourceInstanceDetailResponse.

        节点数量。

        :return: The node_num of this ShowSourceInstanceDetailResponse.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this ShowSourceInstanceDetailResponse.

        节点数量。

        :param node_num: The node_num of this ShowSourceInstanceDetailResponse.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def coordinator_num(self):
        r"""Gets the coordinator_num of this ShowSourceInstanceDetailResponse.

        协调节点数量。

        :return: The coordinator_num of this ShowSourceInstanceDetailResponse.
        :rtype: int
        """
        return self._coordinator_num

    @coordinator_num.setter
    def coordinator_num(self, coordinator_num):
        r"""Sets the coordinator_num of this ShowSourceInstanceDetailResponse.

        协调节点数量。

        :param coordinator_num: The coordinator_num of this ShowSourceInstanceDetailResponse.
        :type coordinator_num: int
        """
        self._coordinator_num = coordinator_num

    @property
    def sharding_num(self):
        r"""Gets the sharding_num of this ShowSourceInstanceDetailResponse.

        分片数量。

        :return: The sharding_num of this ShowSourceInstanceDetailResponse.
        :rtype: int
        """
        return self._sharding_num

    @sharding_num.setter
    def sharding_num(self, sharding_num):
        r"""Sets the sharding_num of this ShowSourceInstanceDetailResponse.

        分片数量。

        :param sharding_num: The sharding_num of this ShowSourceInstanceDetailResponse.
        :type sharding_num: int
        """
        self._sharding_num = sharding_num

    @property
    def replica_num(self):
        r"""Gets the replica_num of this ShowSourceInstanceDetailResponse.

        副本数量。

        :return: The replica_num of this ShowSourceInstanceDetailResponse.
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        r"""Sets the replica_num of this ShowSourceInstanceDetailResponse.

        副本数量。

        :param replica_num: The replica_num of this ShowSourceInstanceDetailResponse.
        :type replica_num: int
        """
        self._replica_num = replica_num

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ShowSourceInstanceDetailResponse.

        引擎版本。

        :return: The engine_version of this ShowSourceInstanceDetailResponse.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ShowSourceInstanceDetailResponse.

        引擎版本。

        :param engine_version: The engine_version of this ShowSourceInstanceDetailResponse.
        :type engine_version: str
        """
        self._engine_version = engine_version

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
        if not isinstance(other, ShowSourceInstanceDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
