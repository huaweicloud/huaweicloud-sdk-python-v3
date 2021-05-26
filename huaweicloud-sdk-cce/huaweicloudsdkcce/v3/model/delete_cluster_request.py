# coding: utf-8

import pprint
import re

import six





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
        'error_status': 'str',
        'delete_efs': 'str',
        'delete_eni': 'str',
        'delete_evs': 'str',
        'delete_net': 'str',
        'delete_obs': 'str',
        'delete_sfs': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'error_status': 'errorStatus',
        'delete_efs': 'delete_efs',
        'delete_eni': 'delete_eni',
        'delete_evs': 'delete_evs',
        'delete_net': 'delete_net',
        'delete_obs': 'delete_obs',
        'delete_sfs': 'delete_sfs'
    }

    def __init__(self, cluster_id=None, error_status=None, delete_efs=None, delete_eni=None, delete_evs=None, delete_net=None, delete_obs=None, delete_sfs=None):
        """DeleteClusterRequest - a model defined in huaweicloud sdk"""
        
        

        self._cluster_id = None
        self._error_status = None
        self._delete_efs = None
        self._delete_eni = None
        self._delete_evs = None
        self._delete_net = None
        self._delete_obs = None
        self._delete_sfs = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if error_status is not None:
            self.error_status = error_status
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

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DeleteClusterRequest.

        集群 ID，获取方式请参见[[如何获取接口URI中参数](https://support.huaweicloud.com/api-cce/cce_02_0271.html)](tag:hws)[[如何获取接口URI中参数](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0271.html)](tag:hws_hk)

        :return: The cluster_id of this DeleteClusterRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DeleteClusterRequest.

        集群 ID，获取方式请参见[[如何获取接口URI中参数](https://support.huaweicloud.com/api-cce/cce_02_0271.html)](tag:hws)[[如何获取接口URI中参数](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0271.html)](tag:hws_hk)

        :param cluster_id: The cluster_id of this DeleteClusterRequest.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def error_status(self):
        """Gets the error_status of this DeleteClusterRequest.

        集群状态兼容Error参数，用于API平滑切换。 兼容场景下，errorStatus为空则屏蔽Error状态为Deleting状态。

        :return: The error_status of this DeleteClusterRequest.
        :rtype: str
        """
        return self._error_status

    @error_status.setter
    def error_status(self, error_status):
        """Sets the error_status of this DeleteClusterRequest.

        集群状态兼容Error参数，用于API平滑切换。 兼容场景下，errorStatus为空则屏蔽Error状态为Deleting状态。

        :param error_status: The error_status of this DeleteClusterRequest.
        :type: str
        """
        self._error_status = error_status

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
        :type: str
        """
        self._delete_efs = delete_efs

    @property
    def delete_eni(self):
        """Gets the delete_eni of this DeleteClusterRequest.

        是否删除eni ports（原生弹性网卡）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The delete_eni of this DeleteClusterRequest.
        :rtype: str
        """
        return self._delete_eni

    @delete_eni.setter
    def delete_eni(self, delete_eni):
        """Sets the delete_eni of this DeleteClusterRequest.

        是否删除eni ports（原生弹性网卡）， 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param delete_eni: The delete_eni of this DeleteClusterRequest.
        :type: str
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
        :type: str
        """
        self._delete_evs = delete_evs

    @property
    def delete_net(self):
        """Gets the delete_net of this DeleteClusterRequest.

        是否删除elb（弹性负载均衡）等集群Service/Ingress相关资源。 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :return: The delete_net of this DeleteClusterRequest.
        :rtype: str
        """
        return self._delete_net

    @delete_net.setter
    def delete_net(self, delete_net):
        """Sets the delete_net of this DeleteClusterRequest.

        是否删除elb（弹性负载均衡）等集群Service/Ingress相关资源。 枚举取值： - true或block (执行删除流程，失败则阻塞后续流程) - try (执行删除流程，失败则忽略，并继续执行后续流程) - false或skip (跳过删除流程，默认选项)

        :param delete_net: The delete_net of this DeleteClusterRequest.
        :type: str
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
        :type: str
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
        :type: str
        """
        self._delete_sfs = delete_sfs

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
