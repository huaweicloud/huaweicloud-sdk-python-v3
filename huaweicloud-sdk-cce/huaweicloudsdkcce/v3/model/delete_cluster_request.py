# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteClusterRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'delete_efs': 'str',
        'delete_eni': 'str',
        'delete_evs': 'str',
        'delete_net': 'str',
        'delete_obs': 'str',
        'delete_sfs': 'str',
        'delete_sfs30': 'str',
        'lts_reclaim_policy': 'str',
        'tobedeleted': 'str',
        'ondemand_node_policy': 'str',
        'periodic_node_policy': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'delete_efs': 'delete_efs',
        'delete_eni': 'delete_eni',
        'delete_evs': 'delete_evs',
        'delete_net': 'delete_net',
        'delete_obs': 'delete_obs',
        'delete_sfs': 'delete_sfs',
        'delete_sfs30': 'delete_sfs30',
        'lts_reclaim_policy': 'lts_reclaim_policy',
        'tobedeleted': 'tobedeleted',
        'ondemand_node_policy': 'ondemand_node_policy',
        'periodic_node_policy': 'periodic_node_policy'
    }

    def __init__(self, cluster_id=None, delete_efs=None, delete_eni=None, delete_evs=None, delete_net=None, delete_obs=None, delete_sfs=None, delete_sfs30=None, lts_reclaim_policy=None, tobedeleted=None, ondemand_node_policy=None, periodic_node_policy=None):
        """DeleteClusterRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param delete_efs: 是否删除SFS Turbo（极速文件存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)
        :type delete_efs: str
        :param delete_eni: 是否删除eni ports（原生弹性网卡）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)
        :type delete_eni: str
        :param delete_evs: 是否删除evs（云硬盘）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)
        :type delete_evs: str
        :param delete_net: 是否删除elb（弹性负载均衡）等集群Service/Ingress相关资源。 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)
        :type delete_net: str
        :param delete_obs: 是否删除obs（对象存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)
        :type delete_obs: str
        :param delete_sfs: 是否删除sfs（文件存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)
        :type delete_sfs: str
        :param delete_sfs30: 是否删除sfs3.0（文件存储卷3.0）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)
        :type delete_sfs30: str
        :param lts_reclaim_policy: 是否删除LTS LogStream（日志流）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)
        :type lts_reclaim_policy: str
        :param tobedeleted: 是否使用包周期集群删除参数预置模式（仅对包周期集群生效）。  需要和其他删除选项参数一起使用，未指定的参数，则使用默认值。  使用该参数，集群不执行真正的删除，仅将本次请求的全部query参数都预置到集群数据库中，用于包周期集群退订时识别用户要删除的资源。  允许重复执行，覆盖预置的删除参数。  枚举取值： - true  (预置模式，仅预置query参数，不执行删除)
        :type tobedeleted: str
        :param ondemand_node_policy: 集群下所有按需节点处理策略， 枚举取值： - delete (删除服务器) - reset (保留服务器并重置服务器，数据不保留) - retain （保留服务器不重置服务器，数据保留）
        :type ondemand_node_policy: str
        :param periodic_node_policy: 集群下所有包周期节点处理策略， 枚举取值： - reset (保留服务器并重置服务器，数据不保留) - retain （保留服务器不重置服务器，数据保留）
        :type periodic_node_policy: str
        """
        
        

        self._cluster_id = None
        self._delete_efs = None
        self._delete_eni = None
        self._delete_evs = None
        self._delete_net = None
        self._delete_obs = None
        self._delete_sfs = None
        self._delete_sfs30 = None
        self._lts_reclaim_policy = None
        self._tobedeleted = None
        self._ondemand_node_policy = None
        self._periodic_node_policy = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if delete_efs is not None:
            self.delete_efs = delete_efs
        if delete_eni is not None:
            self.delete_eni = delete_eni
        if delete_evs is not None:
            self.delete_evs = delete_evs
        if delete_net is not None:
            self.delete_net = delete_net
        if delete_obs is not None:
            self.delete_obs = delete_obs
        if delete_sfs is not None:
            self.delete_sfs = delete_sfs
        if delete_sfs30 is not None:
            self.delete_sfs30 = delete_sfs30
        if lts_reclaim_policy is not None:
            self.lts_reclaim_policy = lts_reclaim_policy
        if tobedeleted is not None:
            self.tobedeleted = tobedeleted
        if ondemand_node_policy is not None:
            self.ondemand_node_policy = ondemand_node_policy
        if periodic_node_policy is not None:
            self.periodic_node_policy = periodic_node_policy

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DeleteClusterRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this DeleteClusterRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DeleteClusterRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this DeleteClusterRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def delete_efs(self):
        """Gets the delete_efs of this DeleteClusterRequest.

        是否删除SFS Turbo（极速文件存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The delete_efs of this DeleteClusterRequest.
        :rtype: str
        """
        return self._delete_efs

    @delete_efs.setter
    def delete_efs(self, delete_efs):
        """Sets the delete_efs of this DeleteClusterRequest.

        是否删除SFS Turbo（极速文件存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param delete_efs: The delete_efs of this DeleteClusterRequest.
        :type delete_efs: str
        """
        self._delete_efs = delete_efs

    @property
    def delete_eni(self):
        """Gets the delete_eni of this DeleteClusterRequest.

        是否删除eni ports（原生弹性网卡）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)

        :return: The delete_eni of this DeleteClusterRequest.
        :rtype: str
        """
        return self._delete_eni

    @delete_eni.setter
    def delete_eni(self, delete_eni):
        """Sets the delete_eni of this DeleteClusterRequest.

        是否删除eni ports（原生弹性网卡）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)

        :param delete_eni: The delete_eni of this DeleteClusterRequest.
        :type delete_eni: str
        """
        self._delete_eni = delete_eni

    @property
    def delete_evs(self):
        """Gets the delete_evs of this DeleteClusterRequest.

        是否删除evs（云硬盘）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The delete_evs of this DeleteClusterRequest.
        :rtype: str
        """
        return self._delete_evs

    @delete_evs.setter
    def delete_evs(self, delete_evs):
        """Sets the delete_evs of this DeleteClusterRequest.

        是否删除evs（云硬盘）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param delete_evs: The delete_evs of this DeleteClusterRequest.
        :type delete_evs: str
        """
        self._delete_evs = delete_evs

    @property
    def delete_net(self):
        """Gets the delete_net of this DeleteClusterRequest.

        是否删除elb（弹性负载均衡）等集群Service/Ingress相关资源。 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)

        :return: The delete_net of this DeleteClusterRequest.
        :rtype: str
        """
        return self._delete_net

    @delete_net.setter
    def delete_net(self, delete_net):
        """Sets the delete_net of this DeleteClusterRequest.

        是否删除elb（弹性负载均衡）等集群Service/Ingress相关资源。 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)

        :param delete_net: The delete_net of this DeleteClusterRequest.
        :type delete_net: str
        """
        self._delete_net = delete_net

    @property
    def delete_obs(self):
        """Gets the delete_obs of this DeleteClusterRequest.

        是否删除obs（对象存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The delete_obs of this DeleteClusterRequest.
        :rtype: str
        """
        return self._delete_obs

    @delete_obs.setter
    def delete_obs(self, delete_obs):
        """Sets the delete_obs of this DeleteClusterRequest.

        是否删除obs（对象存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param delete_obs: The delete_obs of this DeleteClusterRequest.
        :type delete_obs: str
        """
        self._delete_obs = delete_obs

    @property
    def delete_sfs(self):
        """Gets the delete_sfs of this DeleteClusterRequest.

        是否删除sfs（文件存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The delete_sfs of this DeleteClusterRequest.
        :rtype: str
        """
        return self._delete_sfs

    @delete_sfs.setter
    def delete_sfs(self, delete_sfs):
        """Sets the delete_sfs of this DeleteClusterRequest.

        是否删除sfs（文件存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param delete_sfs: The delete_sfs of this DeleteClusterRequest.
        :type delete_sfs: str
        """
        self._delete_sfs = delete_sfs

    @property
    def delete_sfs30(self):
        """Gets the delete_sfs30 of this DeleteClusterRequest.

        是否删除sfs3.0（文件存储卷3.0）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The delete_sfs30 of this DeleteClusterRequest.
        :rtype: str
        """
        return self._delete_sfs30

    @delete_sfs30.setter
    def delete_sfs30(self, delete_sfs30):
        """Sets the delete_sfs30 of this DeleteClusterRequest.

        是否删除sfs3.0（文件存储卷3.0）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param delete_sfs30: The delete_sfs30 of this DeleteClusterRequest.
        :type delete_sfs30: str
        """
        self._delete_sfs30 = delete_sfs30

    @property
    def lts_reclaim_policy(self):
        """Gets the lts_reclaim_policy of this DeleteClusterRequest.

        是否删除LTS LogStream（日志流）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The lts_reclaim_policy of this DeleteClusterRequest.
        :rtype: str
        """
        return self._lts_reclaim_policy

    @lts_reclaim_policy.setter
    def lts_reclaim_policy(self, lts_reclaim_policy):
        """Sets the lts_reclaim_policy of this DeleteClusterRequest.

        是否删除LTS LogStream（日志流）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param lts_reclaim_policy: The lts_reclaim_policy of this DeleteClusterRequest.
        :type lts_reclaim_policy: str
        """
        self._lts_reclaim_policy = lts_reclaim_policy

    @property
    def tobedeleted(self):
        """Gets the tobedeleted of this DeleteClusterRequest.

        是否使用包周期集群删除参数预置模式（仅对包周期集群生效）。  需要和其他删除选项参数一起使用，未指定的参数，则使用默认值。  使用该参数，集群不执行真正的删除，仅将本次请求的全部query参数都预置到集群数据库中，用于包周期集群退订时识别用户要删除的资源。  允许重复执行，覆盖预置的删除参数。  枚举取值： - true  (预置模式，仅预置query参数，不执行删除)

        :return: The tobedeleted of this DeleteClusterRequest.
        :rtype: str
        """
        return self._tobedeleted

    @tobedeleted.setter
    def tobedeleted(self, tobedeleted):
        """Sets the tobedeleted of this DeleteClusterRequest.

        是否使用包周期集群删除参数预置模式（仅对包周期集群生效）。  需要和其他删除选项参数一起使用，未指定的参数，则使用默认值。  使用该参数，集群不执行真正的删除，仅将本次请求的全部query参数都预置到集群数据库中，用于包周期集群退订时识别用户要删除的资源。  允许重复执行，覆盖预置的删除参数。  枚举取值： - true  (预置模式，仅预置query参数，不执行删除)

        :param tobedeleted: The tobedeleted of this DeleteClusterRequest.
        :type tobedeleted: str
        """
        self._tobedeleted = tobedeleted

    @property
    def ondemand_node_policy(self):
        """Gets the ondemand_node_policy of this DeleteClusterRequest.

        集群下所有按需节点处理策略， 枚举取值： - delete (删除服务器) - reset (保留服务器并重置服务器，数据不保留) - retain （保留服务器不重置服务器，数据保留）

        :return: The ondemand_node_policy of this DeleteClusterRequest.
        :rtype: str
        """
        return self._ondemand_node_policy

    @ondemand_node_policy.setter
    def ondemand_node_policy(self, ondemand_node_policy):
        """Sets the ondemand_node_policy of this DeleteClusterRequest.

        集群下所有按需节点处理策略， 枚举取值： - delete (删除服务器) - reset (保留服务器并重置服务器，数据不保留) - retain （保留服务器不重置服务器，数据保留）

        :param ondemand_node_policy: The ondemand_node_policy of this DeleteClusterRequest.
        :type ondemand_node_policy: str
        """
        self._ondemand_node_policy = ondemand_node_policy

    @property
    def periodic_node_policy(self):
        """Gets the periodic_node_policy of this DeleteClusterRequest.

        集群下所有包周期节点处理策略， 枚举取值： - reset (保留服务器并重置服务器，数据不保留) - retain （保留服务器不重置服务器，数据保留）

        :return: The periodic_node_policy of this DeleteClusterRequest.
        :rtype: str
        """
        return self._periodic_node_policy

    @periodic_node_policy.setter
    def periodic_node_policy(self, periodic_node_policy):
        """Sets the periodic_node_policy of this DeleteClusterRequest.

        集群下所有包周期节点处理策略， 枚举取值： - reset (保留服务器并重置服务器，数据不保留) - retain （保留服务器不重置服务器，数据保留）

        :param periodic_node_policy: The periodic_node_policy of this DeleteClusterRequest.
        :type periodic_node_policy: str
        """
        self._periodic_node_policy = periodic_node_policy

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
        if not isinstance(other, DeleteClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
