# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClustersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'detail': 'str',
        'status': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'detail': 'detail',
        'status': 'status',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, detail=None, status=None, type=None, version=None):
        """ListClustersRequest

        The model defined in huaweicloud sdk

        :param detail: 查询集群详细信息。  若设置为true，获取集群下节点总数(totalNodesNumber)、正常节点数(activeNodesNumber)、CPU总量(totalNodesCPU)、内存总量(totalNodesMemory)、已安装插件列表(installedAddonInstances)，已安装插件列表中包含名称(addonTemplateName)、版本号(version)、插件的状态信息(status)，放入到annotation中。 
        :type detail: str
        :param status: 集群状态，取值如下 - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常。 - Hibernating：休眠中，表示集群正处于休眠过程中。 - Hibernation：已休眠，表示集群正处于休眠状态。 - Awaking：唤醒中，表示集群正处于从休眠状态唤醒的过程中。 - Empty：集群无任何资源（已废弃）
        :type status: str
        :param type: 集群类型： - VirtualMachine：CCE集群 - ARM64：鲲鹏集群
        :type type: str
        :param version: 集群版本过滤
        :type version: str
        """
        
        

        self._detail = None
        self._status = None
        self._type = None
        self._version = None
        self.discriminator = None

        if detail is not None:
            self.detail = detail
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def detail(self):
        """Gets the detail of this ListClustersRequest.

        查询集群详细信息。  若设置为true，获取集群下节点总数(totalNodesNumber)、正常节点数(activeNodesNumber)、CPU总量(totalNodesCPU)、内存总量(totalNodesMemory)、已安装插件列表(installedAddonInstances)，已安装插件列表中包含名称(addonTemplateName)、版本号(version)、插件的状态信息(status)，放入到annotation中。 

        :return: The detail of this ListClustersRequest.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ListClustersRequest.

        查询集群详细信息。  若设置为true，获取集群下节点总数(totalNodesNumber)、正常节点数(activeNodesNumber)、CPU总量(totalNodesCPU)、内存总量(totalNodesMemory)、已安装插件列表(installedAddonInstances)，已安装插件列表中包含名称(addonTemplateName)、版本号(version)、插件的状态信息(status)，放入到annotation中。 

        :param detail: The detail of this ListClustersRequest.
        :type detail: str
        """
        self._detail = detail

    @property
    def status(self):
        """Gets the status of this ListClustersRequest.

        集群状态，取值如下 - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常。 - Hibernating：休眠中，表示集群正处于休眠过程中。 - Hibernation：已休眠，表示集群正处于休眠状态。 - Awaking：唤醒中，表示集群正处于从休眠状态唤醒的过程中。 - Empty：集群无任何资源（已废弃）

        :return: The status of this ListClustersRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListClustersRequest.

        集群状态，取值如下 - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常。 - Hibernating：休眠中，表示集群正处于休眠过程中。 - Hibernation：已休眠，表示集群正处于休眠状态。 - Awaking：唤醒中，表示集群正处于从休眠状态唤醒的过程中。 - Empty：集群无任何资源（已废弃）

        :param status: The status of this ListClustersRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ListClustersRequest.

        集群类型： - VirtualMachine：CCE集群 - ARM64：鲲鹏集群

        :return: The type of this ListClustersRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListClustersRequest.

        集群类型： - VirtualMachine：CCE集群 - ARM64：鲲鹏集群

        :param type: The type of this ListClustersRequest.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListClustersRequest.

        集群版本过滤

        :return: The version of this ListClustersRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListClustersRequest.

        集群版本过滤

        :param version: The version of this ListClustersRequest.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ListClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
