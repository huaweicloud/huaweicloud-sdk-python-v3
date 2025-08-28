# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgentDaemonsetDetailInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'yaml_content': 'str',
        'node_num': 'int',
        'runtime_info': 'list[RuntimeRequestBody]',
        'cluster_status': 'str',
        'ds_info': 'ClusterInfoResponseDsInfo',
        'installed_status': 'str',
        'schedule_info': 'CreateDaemonsetRequestBodyScheduleInfo'
    }

    attribute_map = {
        'yaml_content': 'yaml_content',
        'node_num': 'node_num',
        'runtime_info': 'runtime_info',
        'cluster_status': 'cluster_status',
        'ds_info': 'ds_info',
        'installed_status': 'installed_status',
        'schedule_info': 'schedule_info'
    }

    def __init__(self, yaml_content=None, node_num=None, runtime_info=None, cluster_status=None, ds_info=None, installed_status=None, schedule_info=None):
        r"""ShowAgentDaemonsetDetailInfoResponse

        The model defined in huaweicloud sdk

        :param yaml_content: 原始yaml
        :type yaml_content: str
        :param node_num: 节点总数
        :type node_num: int
        :param runtime_info: 容器运行时配置
        :type runtime_info: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        :param cluster_status: **参数解释**: 集群状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。  - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。  - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。  - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常，需联系管理员进行回滚重试。  - Empty：集群无任何资源。  **默认取值**: 不涉及 
        :type cluster_status: str
        :param ds_info: 
        :type ds_info: :class:`huaweicloudsdkhss.v5.ClusterInfoResponseDsInfo`
        :param installed_status: **参数解释**: 集群ds安装状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - installing：安装中。 - install_success：安装成功。 - install_failed：安装失败。 - partially_success：部分安装成功。 - upgrade_success：升级成功。  - upgrade_failed：升级失败。 - upgrading：升级中。 - none：未安装。  **默认取值**: 不涉及 
        :type installed_status: str
        :param schedule_info: 
        :type schedule_info: :class:`huaweicloudsdkhss.v5.CreateDaemonsetRequestBodyScheduleInfo`
        """
        
        super(ShowAgentDaemonsetDetailInfoResponse, self).__init__()

        self._yaml_content = None
        self._node_num = None
        self._runtime_info = None
        self._cluster_status = None
        self._ds_info = None
        self._installed_status = None
        self._schedule_info = None
        self.discriminator = None

        if yaml_content is not None:
            self.yaml_content = yaml_content
        if node_num is not None:
            self.node_num = node_num
        if runtime_info is not None:
            self.runtime_info = runtime_info
        if cluster_status is not None:
            self.cluster_status = cluster_status
        if ds_info is not None:
            self.ds_info = ds_info
        if installed_status is not None:
            self.installed_status = installed_status
        if schedule_info is not None:
            self.schedule_info = schedule_info

    @property
    def yaml_content(self):
        r"""Gets the yaml_content of this ShowAgentDaemonsetDetailInfoResponse.

        原始yaml

        :return: The yaml_content of this ShowAgentDaemonsetDetailInfoResponse.
        :rtype: str
        """
        return self._yaml_content

    @yaml_content.setter
    def yaml_content(self, yaml_content):
        r"""Sets the yaml_content of this ShowAgentDaemonsetDetailInfoResponse.

        原始yaml

        :param yaml_content: The yaml_content of this ShowAgentDaemonsetDetailInfoResponse.
        :type yaml_content: str
        """
        self._yaml_content = yaml_content

    @property
    def node_num(self):
        r"""Gets the node_num of this ShowAgentDaemonsetDetailInfoResponse.

        节点总数

        :return: The node_num of this ShowAgentDaemonsetDetailInfoResponse.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this ShowAgentDaemonsetDetailInfoResponse.

        节点总数

        :param node_num: The node_num of this ShowAgentDaemonsetDetailInfoResponse.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def runtime_info(self):
        r"""Gets the runtime_info of this ShowAgentDaemonsetDetailInfoResponse.

        容器运行时配置

        :return: The runtime_info of this ShowAgentDaemonsetDetailInfoResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        """
        return self._runtime_info

    @runtime_info.setter
    def runtime_info(self, runtime_info):
        r"""Sets the runtime_info of this ShowAgentDaemonsetDetailInfoResponse.

        容器运行时配置

        :param runtime_info: The runtime_info of this ShowAgentDaemonsetDetailInfoResponse.
        :type runtime_info: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        """
        self._runtime_info = runtime_info

    @property
    def cluster_status(self):
        r"""Gets the cluster_status of this ShowAgentDaemonsetDetailInfoResponse.

        **参数解释**: 集群状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。  - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。  - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。  - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常，需联系管理员进行回滚重试。  - Empty：集群无任何资源。  **默认取值**: 不涉及 

        :return: The cluster_status of this ShowAgentDaemonsetDetailInfoResponse.
        :rtype: str
        """
        return self._cluster_status

    @cluster_status.setter
    def cluster_status(self, cluster_status):
        r"""Sets the cluster_status of this ShowAgentDaemonsetDetailInfoResponse.

        **参数解释**: 集群状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。  - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。  - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。  - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常，需联系管理员进行回滚重试。  - Empty：集群无任何资源。  **默认取值**: 不涉及 

        :param cluster_status: The cluster_status of this ShowAgentDaemonsetDetailInfoResponse.
        :type cluster_status: str
        """
        self._cluster_status = cluster_status

    @property
    def ds_info(self):
        r"""Gets the ds_info of this ShowAgentDaemonsetDetailInfoResponse.

        :return: The ds_info of this ShowAgentDaemonsetDetailInfoResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ClusterInfoResponseDsInfo`
        """
        return self._ds_info

    @ds_info.setter
    def ds_info(self, ds_info):
        r"""Sets the ds_info of this ShowAgentDaemonsetDetailInfoResponse.

        :param ds_info: The ds_info of this ShowAgentDaemonsetDetailInfoResponse.
        :type ds_info: :class:`huaweicloudsdkhss.v5.ClusterInfoResponseDsInfo`
        """
        self._ds_info = ds_info

    @property
    def installed_status(self):
        r"""Gets the installed_status of this ShowAgentDaemonsetDetailInfoResponse.

        **参数解释**: 集群ds安装状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - installing：安装中。 - install_success：安装成功。 - install_failed：安装失败。 - partially_success：部分安装成功。 - upgrade_success：升级成功。  - upgrade_failed：升级失败。 - upgrading：升级中。 - none：未安装。  **默认取值**: 不涉及 

        :return: The installed_status of this ShowAgentDaemonsetDetailInfoResponse.
        :rtype: str
        """
        return self._installed_status

    @installed_status.setter
    def installed_status(self, installed_status):
        r"""Sets the installed_status of this ShowAgentDaemonsetDetailInfoResponse.

        **参数解释**: 集群ds安装状态 **约束限制**: 不涉及 **取值范围**: 包含如下： - installing：安装中。 - install_success：安装成功。 - install_failed：安装失败。 - partially_success：部分安装成功。 - upgrade_success：升级成功。  - upgrade_failed：升级失败。 - upgrading：升级中。 - none：未安装。  **默认取值**: 不涉及 

        :param installed_status: The installed_status of this ShowAgentDaemonsetDetailInfoResponse.
        :type installed_status: str
        """
        self._installed_status = installed_status

    @property
    def schedule_info(self):
        r"""Gets the schedule_info of this ShowAgentDaemonsetDetailInfoResponse.

        :return: The schedule_info of this ShowAgentDaemonsetDetailInfoResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.CreateDaemonsetRequestBodyScheduleInfo`
        """
        return self._schedule_info

    @schedule_info.setter
    def schedule_info(self, schedule_info):
        r"""Sets the schedule_info of this ShowAgentDaemonsetDetailInfoResponse.

        :param schedule_info: The schedule_info of this ShowAgentDaemonsetDetailInfoResponse.
        :type schedule_info: :class:`huaweicloudsdkhss.v5.CreateDaemonsetRequestBodyScheduleInfo`
        """
        self._schedule_info = schedule_info

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
        if not isinstance(other, ShowAgentDaemonsetDetailInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
