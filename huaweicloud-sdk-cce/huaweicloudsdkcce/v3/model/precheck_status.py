# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrecheckStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'expire_time_stamp': 'str',
        'message': 'str',
        'cluster_check_status': 'ClusterCheckStatus',
        'addon_check_status': 'AddonCheckStatus',
        'node_check_status': 'NodeCheckStatus'
    }

    attribute_map = {
        'phase': 'phase',
        'expire_time_stamp': 'expireTimeStamp',
        'message': 'message',
        'cluster_check_status': 'clusterCheckStatus',
        'addon_check_status': 'addonCheckStatus',
        'node_check_status': 'nodeCheckStatus'
    }

    def __init__(self, phase=None, expire_time_stamp=None, message=None, cluster_check_status=None, addon_check_status=None, node_check_status=None):
        """PrecheckStatus

        The model defined in huaweicloud sdk

        :param phase: 状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败 - Error 错误
        :type phase: str
        :param expire_time_stamp: 检查结果过期时间
        :type expire_time_stamp: str
        :param message: 信息，一般是执行错误的日志信息
        :type message: str
        :param cluster_check_status: 
        :type cluster_check_status: :class:`huaweicloudsdkcce.v3.ClusterCheckStatus`
        :param addon_check_status: 
        :type addon_check_status: :class:`huaweicloudsdkcce.v3.AddonCheckStatus`
        :param node_check_status: 
        :type node_check_status: :class:`huaweicloudsdkcce.v3.NodeCheckStatus`
        """
        
        

        self._phase = None
        self._expire_time_stamp = None
        self._message = None
        self._cluster_check_status = None
        self._addon_check_status = None
        self._node_check_status = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if expire_time_stamp is not None:
            self.expire_time_stamp = expire_time_stamp
        if message is not None:
            self.message = message
        if cluster_check_status is not None:
            self.cluster_check_status = cluster_check_status
        if addon_check_status is not None:
            self.addon_check_status = addon_check_status
        if node_check_status is not None:
            self.node_check_status = node_check_status

    @property
    def phase(self):
        """Gets the phase of this PrecheckStatus.

        状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败 - Error 错误

        :return: The phase of this PrecheckStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this PrecheckStatus.

        状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败 - Error 错误

        :param phase: The phase of this PrecheckStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def expire_time_stamp(self):
        """Gets the expire_time_stamp of this PrecheckStatus.

        检查结果过期时间

        :return: The expire_time_stamp of this PrecheckStatus.
        :rtype: str
        """
        return self._expire_time_stamp

    @expire_time_stamp.setter
    def expire_time_stamp(self, expire_time_stamp):
        """Sets the expire_time_stamp of this PrecheckStatus.

        检查结果过期时间

        :param expire_time_stamp: The expire_time_stamp of this PrecheckStatus.
        :type expire_time_stamp: str
        """
        self._expire_time_stamp = expire_time_stamp

    @property
    def message(self):
        """Gets the message of this PrecheckStatus.

        信息，一般是执行错误的日志信息

        :return: The message of this PrecheckStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PrecheckStatus.

        信息，一般是执行错误的日志信息

        :param message: The message of this PrecheckStatus.
        :type message: str
        """
        self._message = message

    @property
    def cluster_check_status(self):
        """Gets the cluster_check_status of this PrecheckStatus.

        :return: The cluster_check_status of this PrecheckStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterCheckStatus`
        """
        return self._cluster_check_status

    @cluster_check_status.setter
    def cluster_check_status(self, cluster_check_status):
        """Sets the cluster_check_status of this PrecheckStatus.

        :param cluster_check_status: The cluster_check_status of this PrecheckStatus.
        :type cluster_check_status: :class:`huaweicloudsdkcce.v3.ClusterCheckStatus`
        """
        self._cluster_check_status = cluster_check_status

    @property
    def addon_check_status(self):
        """Gets the addon_check_status of this PrecheckStatus.

        :return: The addon_check_status of this PrecheckStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.AddonCheckStatus`
        """
        return self._addon_check_status

    @addon_check_status.setter
    def addon_check_status(self, addon_check_status):
        """Sets the addon_check_status of this PrecheckStatus.

        :param addon_check_status: The addon_check_status of this PrecheckStatus.
        :type addon_check_status: :class:`huaweicloudsdkcce.v3.AddonCheckStatus`
        """
        self._addon_check_status = addon_check_status

    @property
    def node_check_status(self):
        """Gets the node_check_status of this PrecheckStatus.

        :return: The node_check_status of this PrecheckStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeCheckStatus`
        """
        return self._node_check_status

    @node_check_status.setter
    def node_check_status(self, node_check_status):
        """Sets the node_check_status of this PrecheckStatus.

        :param node_check_status: The node_check_status of this PrecheckStatus.
        :type node_check_status: :class:`huaweicloudsdkcce.v3.NodeCheckStatus`
        """
        self._node_check_status = node_check_status

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
        if not isinstance(other, PrecheckStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
