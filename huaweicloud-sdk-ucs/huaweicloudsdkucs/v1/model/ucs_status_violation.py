# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UCSStatusViolation:

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
        'audit_timestamp': 'str',
        'cluster_violations': 'list[StatusViolation]',
        'cluster_events': 'list[StatusEvent]',
        'warn_events': 'list[StatusEvent]'
    }

    attribute_map = {
        'cluster_id': 'clusterID',
        'audit_timestamp': 'auditTimestamp',
        'cluster_violations': 'clusterViolations',
        'cluster_events': 'clusterEvents',
        'warn_events': 'warnEvents'
    }

    def __init__(self, cluster_id=None, audit_timestamp=None, cluster_violations=None, cluster_events=None, warn_events=None):
        r"""UCSStatusViolation

        The model defined in huaweicloud sdk

        :param cluster_id: 进行审计的集群ID
        :type cluster_id: str
        :param audit_timestamp: 审计时间
        :type audit_timestamp: str
        :param cluster_violations: 违规状态列表
        :type cluster_violations: list[:class:`huaweicloudsdkucs.v1.StatusViolation`]
        :param cluster_events: 拦截事件列表
        :type cluster_events: list[:class:`huaweicloudsdkucs.v1.StatusEvent`]
        :param warn_events: 告警事件列表
        :type warn_events: list[:class:`huaweicloudsdkucs.v1.StatusEvent`]
        """
        
        

        self._cluster_id = None
        self._audit_timestamp = None
        self._cluster_violations = None
        self._cluster_events = None
        self._warn_events = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if audit_timestamp is not None:
            self.audit_timestamp = audit_timestamp
        if cluster_violations is not None:
            self.cluster_violations = cluster_violations
        if cluster_events is not None:
            self.cluster_events = cluster_events
        if warn_events is not None:
            self.warn_events = warn_events

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UCSStatusViolation.

        进行审计的集群ID

        :return: The cluster_id of this UCSStatusViolation.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UCSStatusViolation.

        进行审计的集群ID

        :param cluster_id: The cluster_id of this UCSStatusViolation.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def audit_timestamp(self):
        r"""Gets the audit_timestamp of this UCSStatusViolation.

        审计时间

        :return: The audit_timestamp of this UCSStatusViolation.
        :rtype: str
        """
        return self._audit_timestamp

    @audit_timestamp.setter
    def audit_timestamp(self, audit_timestamp):
        r"""Sets the audit_timestamp of this UCSStatusViolation.

        审计时间

        :param audit_timestamp: The audit_timestamp of this UCSStatusViolation.
        :type audit_timestamp: str
        """
        self._audit_timestamp = audit_timestamp

    @property
    def cluster_violations(self):
        r"""Gets the cluster_violations of this UCSStatusViolation.

        违规状态列表

        :return: The cluster_violations of this UCSStatusViolation.
        :rtype: list[:class:`huaweicloudsdkucs.v1.StatusViolation`]
        """
        return self._cluster_violations

    @cluster_violations.setter
    def cluster_violations(self, cluster_violations):
        r"""Sets the cluster_violations of this UCSStatusViolation.

        违规状态列表

        :param cluster_violations: The cluster_violations of this UCSStatusViolation.
        :type cluster_violations: list[:class:`huaweicloudsdkucs.v1.StatusViolation`]
        """
        self._cluster_violations = cluster_violations

    @property
    def cluster_events(self):
        r"""Gets the cluster_events of this UCSStatusViolation.

        拦截事件列表

        :return: The cluster_events of this UCSStatusViolation.
        :rtype: list[:class:`huaweicloudsdkucs.v1.StatusEvent`]
        """
        return self._cluster_events

    @cluster_events.setter
    def cluster_events(self, cluster_events):
        r"""Sets the cluster_events of this UCSStatusViolation.

        拦截事件列表

        :param cluster_events: The cluster_events of this UCSStatusViolation.
        :type cluster_events: list[:class:`huaweicloudsdkucs.v1.StatusEvent`]
        """
        self._cluster_events = cluster_events

    @property
    def warn_events(self):
        r"""Gets the warn_events of this UCSStatusViolation.

        告警事件列表

        :return: The warn_events of this UCSStatusViolation.
        :rtype: list[:class:`huaweicloudsdkucs.v1.StatusEvent`]
        """
        return self._warn_events

    @warn_events.setter
    def warn_events(self, warn_events):
        r"""Sets the warn_events of this UCSStatusViolation.

        告警事件列表

        :param warn_events: The warn_events of this UCSStatusViolation.
        :type warn_events: list[:class:`huaweicloudsdkucs.v1.StatusEvent`]
        """
        self._warn_events = warn_events

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UCSStatusViolation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
