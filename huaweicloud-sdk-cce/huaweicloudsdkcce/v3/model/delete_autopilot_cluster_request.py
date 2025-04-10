# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAutopilotClusterRequest:

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
        'delete_net': 'str',
        'delete_obs': 'str',
        'delete_sfs30': 'str',
        'lts_reclaim_policy': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'delete_efs': 'delete_efs',
        'delete_eni': 'delete_eni',
        'delete_net': 'delete_net',
        'delete_obs': 'delete_obs',
        'delete_sfs30': 'delete_sfs30',
        'lts_reclaim_policy': 'lts_reclaim_policy'
    }

    def __init__(self, cluster_id=None, delete_efs=None, delete_eni=None, delete_net=None, delete_obs=None, delete_sfs30=None, lts_reclaim_policy=None):
        r"""DeleteAutopilotClusterRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param delete_efs: 是否删除SFS Turbo（极速文件存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)
        :type delete_efs: str
        :param delete_eni: 是否删除eni ports（原生弹性网卡）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)
        :type delete_eni: str
        :param delete_net: 是否删除elb（弹性负载均衡）等集群Service/Ingress相关资源。 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)
        :type delete_net: str
        :param delete_obs: 是否删除obs（对象存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)
        :type delete_obs: str
        :param delete_sfs30: 是否删除sfs3.0（文件存储卷3.0）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)
        :type delete_sfs30: str
        :param lts_reclaim_policy: 是否删除LTS资源（日志组/日志流）。 枚举取值： - Delete_Log_Group：删除日志组，失败则忽略，并继续执行后续流程。 - Delete_Master_Log_Stream：删除Master接入日志流，失败则忽略，并继续执行后续流程，默认选项。 - Retain：跳过删除流程。
        :type lts_reclaim_policy: str
        """
        
        

        self._cluster_id = None
        self._delete_efs = None
        self._delete_eni = None
        self._delete_net = None
        self._delete_obs = None
        self._delete_sfs30 = None
        self._lts_reclaim_policy = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if delete_efs is not None:
            self.delete_efs = delete_efs
        if delete_eni is not None:
            self.delete_eni = delete_eni
        if delete_net is not None:
            self.delete_net = delete_net
        if delete_obs is not None:
            self.delete_obs = delete_obs
        if delete_sfs30 is not None:
            self.delete_sfs30 = delete_sfs30
        if lts_reclaim_policy is not None:
            self.lts_reclaim_policy = lts_reclaim_policy

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this DeleteAutopilotClusterRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this DeleteAutopilotClusterRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this DeleteAutopilotClusterRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this DeleteAutopilotClusterRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def delete_efs(self):
        r"""Gets the delete_efs of this DeleteAutopilotClusterRequest.

        是否删除SFS Turbo（极速文件存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The delete_efs of this DeleteAutopilotClusterRequest.
        :rtype: str
        """
        return self._delete_efs

    @delete_efs.setter
    def delete_efs(self, delete_efs):
        r"""Sets the delete_efs of this DeleteAutopilotClusterRequest.

        是否删除SFS Turbo（极速文件存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param delete_efs: The delete_efs of this DeleteAutopilotClusterRequest.
        :type delete_efs: str
        """
        self._delete_efs = delete_efs

    @property
    def delete_eni(self):
        r"""Gets the delete_eni of this DeleteAutopilotClusterRequest.

        是否删除eni ports（原生弹性网卡）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)

        :return: The delete_eni of this DeleteAutopilotClusterRequest.
        :rtype: str
        """
        return self._delete_eni

    @delete_eni.setter
    def delete_eni(self, delete_eni):
        r"""Sets the delete_eni of this DeleteAutopilotClusterRequest.

        是否删除eni ports（原生弹性网卡）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)

        :param delete_eni: The delete_eni of this DeleteAutopilotClusterRequest.
        :type delete_eni: str
        """
        self._delete_eni = delete_eni

    @property
    def delete_net(self):
        r"""Gets the delete_net of this DeleteAutopilotClusterRequest.

        是否删除elb（弹性负载均衡）等集群Service/Ingress相关资源。 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)

        :return: The delete_net of this DeleteAutopilotClusterRequest.
        :rtype: str
        """
        return self._delete_net

    @delete_net.setter
    def delete_net(self, delete_net):
        r"""Sets the delete_net of this DeleteAutopilotClusterRequest.

        是否删除elb（弹性负载均衡）等集群Service/Ingress相关资源。 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程，默认选项) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程)

        :param delete_net: The delete_net of this DeleteAutopilotClusterRequest.
        :type delete_net: str
        """
        self._delete_net = delete_net

    @property
    def delete_obs(self):
        r"""Gets the delete_obs of this DeleteAutopilotClusterRequest.

        是否删除obs（对象存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The delete_obs of this DeleteAutopilotClusterRequest.
        :rtype: str
        """
        return self._delete_obs

    @delete_obs.setter
    def delete_obs(self, delete_obs):
        r"""Sets the delete_obs of this DeleteAutopilotClusterRequest.

        是否删除obs（对象存储卷）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param delete_obs: The delete_obs of this DeleteAutopilotClusterRequest.
        :type delete_obs: str
        """
        self._delete_obs = delete_obs

    @property
    def delete_sfs30(self):
        r"""Gets the delete_sfs30 of this DeleteAutopilotClusterRequest.

        是否删除sfs3.0（文件存储卷3.0）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The delete_sfs30 of this DeleteAutopilotClusterRequest.
        :rtype: str
        """
        return self._delete_sfs30

    @delete_sfs30.setter
    def delete_sfs30(self, delete_sfs30):
        r"""Sets the delete_sfs30 of this DeleteAutopilotClusterRequest.

        是否删除sfs3.0（文件存储卷3.0）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param delete_sfs30: The delete_sfs30 of this DeleteAutopilotClusterRequest.
        :type delete_sfs30: str
        """
        self._delete_sfs30 = delete_sfs30

    @property
    def lts_reclaim_policy(self):
        r"""Gets the lts_reclaim_policy of this DeleteAutopilotClusterRequest.

        是否删除LTS资源（日志组/日志流）。 枚举取值： - Delete_Log_Group：删除日志组，失败则忽略，并继续执行后续流程。 - Delete_Master_Log_Stream：删除Master接入日志流，失败则忽略，并继续执行后续流程，默认选项。 - Retain：跳过删除流程。

        :return: The lts_reclaim_policy of this DeleteAutopilotClusterRequest.
        :rtype: str
        """
        return self._lts_reclaim_policy

    @lts_reclaim_policy.setter
    def lts_reclaim_policy(self, lts_reclaim_policy):
        r"""Sets the lts_reclaim_policy of this DeleteAutopilotClusterRequest.

        是否删除LTS资源（日志组/日志流）。 枚举取值： - Delete_Log_Group：删除日志组，失败则忽略，并继续执行后续流程。 - Delete_Master_Log_Stream：删除Master接入日志流，失败则忽略，并继续执行后续流程，默认选项。 - Retain：跳过删除流程。

        :param lts_reclaim_policy: The lts_reclaim_policy of this DeleteAutopilotClusterRequest.
        :type lts_reclaim_policy: str
        """
        self._lts_reclaim_policy = lts_reclaim_policy

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
        if not isinstance(other, DeleteAutopilotClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
