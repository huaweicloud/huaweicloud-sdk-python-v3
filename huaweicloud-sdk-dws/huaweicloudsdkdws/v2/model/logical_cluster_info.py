# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicalClusterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logical_cluster_id': 'str',
        'logical_cluster_name': 'str',
        'cluster_rings': 'list[ClusterRing]',
        'status': 'str',
        'first_logical_cluster': 'bool',
        'action_info': 'ActionInfo',
        'edit_enable': 'bool',
        'restart_enable': 'bool',
        'delete_enable': 'bool',
        'add_to_elastic': 'bool',
        'mode': 'str',
        'waiting_for_killing': 'int',
        'cluster_type': 'str'
    }

    attribute_map = {
        'logical_cluster_id': 'logical_cluster_id',
        'logical_cluster_name': 'logical_cluster_name',
        'cluster_rings': 'cluster_rings',
        'status': 'status',
        'first_logical_cluster': 'first_logical_cluster',
        'action_info': 'action_info',
        'edit_enable': 'edit_enable',
        'restart_enable': 'restart_enable',
        'delete_enable': 'delete_enable',
        'add_to_elastic': 'add_to_elastic',
        'mode': 'mode',
        'waiting_for_killing': 'waiting_for_killing',
        'cluster_type': 'cluster_type'
    }

    def __init__(self, logical_cluster_id=None, logical_cluster_name=None, cluster_rings=None, status=None, first_logical_cluster=None, action_info=None, edit_enable=None, restart_enable=None, delete_enable=None, add_to_elastic=None, mode=None, waiting_for_killing=None, cluster_type=None):
        r"""LogicalClusterInfo

        The model defined in huaweicloud sdk

        :param logical_cluster_id: **参数解释**： 逻辑集群ID。 **取值范围**： 不涉及。
        :type logical_cluster_id: str
        :param logical_cluster_name: **参数解释**： 逻辑集群名称。 **取值范围**： 不涉及。
        :type logical_cluster_name: str
        :param cluster_rings: **参数解释**： 逻辑集群主机信息。 **取值范围**： 不涉及。
        :type cluster_rings: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        :param status: **参数解释**： 逻辑集群状态。 **取值范围**： 不涉及。
        :type status: str
        :param first_logical_cluster: **参数解释**： 是否为第一个逻辑集群。历史版本中第1个创建或者转换的逻辑集群不能删除，因为其中包含了一些系统视图。 **取值范围**： 不涉及。
        :type first_logical_cluster: bool
        :param action_info: 
        :type action_info: :class:`huaweicloudsdkdws.v2.ActionInfo`
        :param edit_enable: **参数解释**： 是否允许编辑。 **取值范围**： 不涉及。
        :type edit_enable: bool
        :param restart_enable: **参数解释**： 是否允许重启。 **取值范围**： 不涉及。
        :type restart_enable: bool
        :param delete_enable: **参数解释**： 是否允许删除。 **取值范围**： 不涉及。
        :type delete_enable: bool
        :param add_to_elastic: **参数解释**： 是否允许弹性伸缩。 **取值范围**： 不涉及。
        :type add_to_elastic: bool
        :param mode: **参数解释**： 逻辑集群模式。 **取值范围**： 不涉及。
        :type mode: str
        :param waiting_for_killing: **参数解释**： 作业等待时间。 **取值范围**： 不涉及。
        :type waiting_for_killing: int
        :param cluster_type: **参数解释**： 集群类型。 **取值范围**： 不涉及。
        :type cluster_type: str
        """
        
        

        self._logical_cluster_id = None
        self._logical_cluster_name = None
        self._cluster_rings = None
        self._status = None
        self._first_logical_cluster = None
        self._action_info = None
        self._edit_enable = None
        self._restart_enable = None
        self._delete_enable = None
        self._add_to_elastic = None
        self._mode = None
        self._waiting_for_killing = None
        self._cluster_type = None
        self.discriminator = None

        if logical_cluster_id is not None:
            self.logical_cluster_id = logical_cluster_id
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        if cluster_rings is not None:
            self.cluster_rings = cluster_rings
        if status is not None:
            self.status = status
        if first_logical_cluster is not None:
            self.first_logical_cluster = first_logical_cluster
        if action_info is not None:
            self.action_info = action_info
        if edit_enable is not None:
            self.edit_enable = edit_enable
        if restart_enable is not None:
            self.restart_enable = restart_enable
        if delete_enable is not None:
            self.delete_enable = delete_enable
        if add_to_elastic is not None:
            self.add_to_elastic = add_to_elastic
        if mode is not None:
            self.mode = mode
        if waiting_for_killing is not None:
            self.waiting_for_killing = waiting_for_killing
        if cluster_type is not None:
            self.cluster_type = cluster_type

    @property
    def logical_cluster_id(self):
        r"""Gets the logical_cluster_id of this LogicalClusterInfo.

        **参数解释**： 逻辑集群ID。 **取值范围**： 不涉及。

        :return: The logical_cluster_id of this LogicalClusterInfo.
        :rtype: str
        """
        return self._logical_cluster_id

    @logical_cluster_id.setter
    def logical_cluster_id(self, logical_cluster_id):
        r"""Sets the logical_cluster_id of this LogicalClusterInfo.

        **参数解释**： 逻辑集群ID。 **取值范围**： 不涉及。

        :param logical_cluster_id: The logical_cluster_id of this LogicalClusterInfo.
        :type logical_cluster_id: str
        """
        self._logical_cluster_id = logical_cluster_id

    @property
    def logical_cluster_name(self):
        r"""Gets the logical_cluster_name of this LogicalClusterInfo.

        **参数解释**： 逻辑集群名称。 **取值范围**： 不涉及。

        :return: The logical_cluster_name of this LogicalClusterInfo.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        r"""Sets the logical_cluster_name of this LogicalClusterInfo.

        **参数解释**： 逻辑集群名称。 **取值范围**： 不涉及。

        :param logical_cluster_name: The logical_cluster_name of this LogicalClusterInfo.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def cluster_rings(self):
        r"""Gets the cluster_rings of this LogicalClusterInfo.

        **参数解释**： 逻辑集群主机信息。 **取值范围**： 不涉及。

        :return: The cluster_rings of this LogicalClusterInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        """
        return self._cluster_rings

    @cluster_rings.setter
    def cluster_rings(self, cluster_rings):
        r"""Sets the cluster_rings of this LogicalClusterInfo.

        **参数解释**： 逻辑集群主机信息。 **取值范围**： 不涉及。

        :param cluster_rings: The cluster_rings of this LogicalClusterInfo.
        :type cluster_rings: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        """
        self._cluster_rings = cluster_rings

    @property
    def status(self):
        r"""Gets the status of this LogicalClusterInfo.

        **参数解释**： 逻辑集群状态。 **取值范围**： 不涉及。

        :return: The status of this LogicalClusterInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this LogicalClusterInfo.

        **参数解释**： 逻辑集群状态。 **取值范围**： 不涉及。

        :param status: The status of this LogicalClusterInfo.
        :type status: str
        """
        self._status = status

    @property
    def first_logical_cluster(self):
        r"""Gets the first_logical_cluster of this LogicalClusterInfo.

        **参数解释**： 是否为第一个逻辑集群。历史版本中第1个创建或者转换的逻辑集群不能删除，因为其中包含了一些系统视图。 **取值范围**： 不涉及。

        :return: The first_logical_cluster of this LogicalClusterInfo.
        :rtype: bool
        """
        return self._first_logical_cluster

    @first_logical_cluster.setter
    def first_logical_cluster(self, first_logical_cluster):
        r"""Sets the first_logical_cluster of this LogicalClusterInfo.

        **参数解释**： 是否为第一个逻辑集群。历史版本中第1个创建或者转换的逻辑集群不能删除，因为其中包含了一些系统视图。 **取值范围**： 不涉及。

        :param first_logical_cluster: The first_logical_cluster of this LogicalClusterInfo.
        :type first_logical_cluster: bool
        """
        self._first_logical_cluster = first_logical_cluster

    @property
    def action_info(self):
        r"""Gets the action_info of this LogicalClusterInfo.

        :return: The action_info of this LogicalClusterInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.ActionInfo`
        """
        return self._action_info

    @action_info.setter
    def action_info(self, action_info):
        r"""Sets the action_info of this LogicalClusterInfo.

        :param action_info: The action_info of this LogicalClusterInfo.
        :type action_info: :class:`huaweicloudsdkdws.v2.ActionInfo`
        """
        self._action_info = action_info

    @property
    def edit_enable(self):
        r"""Gets the edit_enable of this LogicalClusterInfo.

        **参数解释**： 是否允许编辑。 **取值范围**： 不涉及。

        :return: The edit_enable of this LogicalClusterInfo.
        :rtype: bool
        """
        return self._edit_enable

    @edit_enable.setter
    def edit_enable(self, edit_enable):
        r"""Sets the edit_enable of this LogicalClusterInfo.

        **参数解释**： 是否允许编辑。 **取值范围**： 不涉及。

        :param edit_enable: The edit_enable of this LogicalClusterInfo.
        :type edit_enable: bool
        """
        self._edit_enable = edit_enable

    @property
    def restart_enable(self):
        r"""Gets the restart_enable of this LogicalClusterInfo.

        **参数解释**： 是否允许重启。 **取值范围**： 不涉及。

        :return: The restart_enable of this LogicalClusterInfo.
        :rtype: bool
        """
        return self._restart_enable

    @restart_enable.setter
    def restart_enable(self, restart_enable):
        r"""Sets the restart_enable of this LogicalClusterInfo.

        **参数解释**： 是否允许重启。 **取值范围**： 不涉及。

        :param restart_enable: The restart_enable of this LogicalClusterInfo.
        :type restart_enable: bool
        """
        self._restart_enable = restart_enable

    @property
    def delete_enable(self):
        r"""Gets the delete_enable of this LogicalClusterInfo.

        **参数解释**： 是否允许删除。 **取值范围**： 不涉及。

        :return: The delete_enable of this LogicalClusterInfo.
        :rtype: bool
        """
        return self._delete_enable

    @delete_enable.setter
    def delete_enable(self, delete_enable):
        r"""Sets the delete_enable of this LogicalClusterInfo.

        **参数解释**： 是否允许删除。 **取值范围**： 不涉及。

        :param delete_enable: The delete_enable of this LogicalClusterInfo.
        :type delete_enable: bool
        """
        self._delete_enable = delete_enable

    @property
    def add_to_elastic(self):
        r"""Gets the add_to_elastic of this LogicalClusterInfo.

        **参数解释**： 是否允许弹性伸缩。 **取值范围**： 不涉及。

        :return: The add_to_elastic of this LogicalClusterInfo.
        :rtype: bool
        """
        return self._add_to_elastic

    @add_to_elastic.setter
    def add_to_elastic(self, add_to_elastic):
        r"""Sets the add_to_elastic of this LogicalClusterInfo.

        **参数解释**： 是否允许弹性伸缩。 **取值范围**： 不涉及。

        :param add_to_elastic: The add_to_elastic of this LogicalClusterInfo.
        :type add_to_elastic: bool
        """
        self._add_to_elastic = add_to_elastic

    @property
    def mode(self):
        r"""Gets the mode of this LogicalClusterInfo.

        **参数解释**： 逻辑集群模式。 **取值范围**： 不涉及。

        :return: The mode of this LogicalClusterInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this LogicalClusterInfo.

        **参数解释**： 逻辑集群模式。 **取值范围**： 不涉及。

        :param mode: The mode of this LogicalClusterInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def waiting_for_killing(self):
        r"""Gets the waiting_for_killing of this LogicalClusterInfo.

        **参数解释**： 作业等待时间。 **取值范围**： 不涉及。

        :return: The waiting_for_killing of this LogicalClusterInfo.
        :rtype: int
        """
        return self._waiting_for_killing

    @waiting_for_killing.setter
    def waiting_for_killing(self, waiting_for_killing):
        r"""Sets the waiting_for_killing of this LogicalClusterInfo.

        **参数解释**： 作业等待时间。 **取值范围**： 不涉及。

        :param waiting_for_killing: The waiting_for_killing of this LogicalClusterInfo.
        :type waiting_for_killing: int
        """
        self._waiting_for_killing = waiting_for_killing

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this LogicalClusterInfo.

        **参数解释**： 集群类型。 **取值范围**： 不涉及。

        :return: The cluster_type of this LogicalClusterInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this LogicalClusterInfo.

        **参数解释**： 集群类型。 **取值范围**： 不涉及。

        :param cluster_type: The cluster_type of this LogicalClusterInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

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
        if not isinstance(other, LogicalClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
