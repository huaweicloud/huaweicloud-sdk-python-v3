# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCrossCloudDisasterInstanceMonitorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'status': 'str',
        'rpo': 'str',
        'rto': 'str',
        'rpo_threshold': 'str',
        'rto_threshold': 'str',
        'switchover_progress': 'str',
        'failover_progress': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'status': 'status',
        'rpo': 'rpo',
        'rto': 'rto',
        'rpo_threshold': 'rpo_threshold',
        'rto_threshold': 'rto_threshold',
        'switchover_progress': 'switchover_progress',
        'failover_progress': 'failover_progress'
    }

    def __init__(self, instance_id=None, status=None, rpo=None, rto=None, rpo_threshold=None, rto_threshold=None, switchover_progress=None, failover_progress=None):
        r"""ShowCrossCloudDisasterInstanceMonitorResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例id。
        :type instance_id: str
        :param status: 容灾状态。
        :type status: str
        :param rpo: 数据恢复点目标。
        :type rpo: str
        :param rto: 数据恢复时间目标。
        :type rto: str
        :param rpo_threshold: rpo阈值。
        :type rpo_threshold: str
        :param rto_threshold: rto阈值。
        :type rto_threshold: str
        :param switchover_progress: 主从切换进度。该值为一个百分数。例如：40%。
        :type switchover_progress: str
        :param failover_progress: 容灾升主进度。该值为一个百分数。例如：40%。
        :type failover_progress: str
        """
        
        super(ShowCrossCloudDisasterInstanceMonitorResponse, self).__init__()

        self._instance_id = None
        self._status = None
        self._rpo = None
        self._rto = None
        self._rpo_threshold = None
        self._rto_threshold = None
        self._switchover_progress = None
        self._failover_progress = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if rpo is not None:
            self.rpo = rpo
        if rto is not None:
            self.rto = rto
        if rpo_threshold is not None:
            self.rpo_threshold = rpo_threshold
        if rto_threshold is not None:
            self.rto_threshold = rto_threshold
        if switchover_progress is not None:
            self.switchover_progress = switchover_progress
        if failover_progress is not None:
            self.failover_progress = failover_progress

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowCrossCloudDisasterInstanceMonitorResponse.

        实例id。

        :return: The instance_id of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowCrossCloudDisasterInstanceMonitorResponse.

        实例id。

        :param instance_id: The instance_id of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this ShowCrossCloudDisasterInstanceMonitorResponse.

        容灾状态。

        :return: The status of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowCrossCloudDisasterInstanceMonitorResponse.

        容灾状态。

        :param status: The status of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :type status: str
        """
        self._status = status

    @property
    def rpo(self):
        r"""Gets the rpo of this ShowCrossCloudDisasterInstanceMonitorResponse.

        数据恢复点目标。

        :return: The rpo of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :rtype: str
        """
        return self._rpo

    @rpo.setter
    def rpo(self, rpo):
        r"""Sets the rpo of this ShowCrossCloudDisasterInstanceMonitorResponse.

        数据恢复点目标。

        :param rpo: The rpo of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :type rpo: str
        """
        self._rpo = rpo

    @property
    def rto(self):
        r"""Gets the rto of this ShowCrossCloudDisasterInstanceMonitorResponse.

        数据恢复时间目标。

        :return: The rto of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :rtype: str
        """
        return self._rto

    @rto.setter
    def rto(self, rto):
        r"""Sets the rto of this ShowCrossCloudDisasterInstanceMonitorResponse.

        数据恢复时间目标。

        :param rto: The rto of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :type rto: str
        """
        self._rto = rto

    @property
    def rpo_threshold(self):
        r"""Gets the rpo_threshold of this ShowCrossCloudDisasterInstanceMonitorResponse.

        rpo阈值。

        :return: The rpo_threshold of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :rtype: str
        """
        return self._rpo_threshold

    @rpo_threshold.setter
    def rpo_threshold(self, rpo_threshold):
        r"""Sets the rpo_threshold of this ShowCrossCloudDisasterInstanceMonitorResponse.

        rpo阈值。

        :param rpo_threshold: The rpo_threshold of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :type rpo_threshold: str
        """
        self._rpo_threshold = rpo_threshold

    @property
    def rto_threshold(self):
        r"""Gets the rto_threshold of this ShowCrossCloudDisasterInstanceMonitorResponse.

        rto阈值。

        :return: The rto_threshold of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :rtype: str
        """
        return self._rto_threshold

    @rto_threshold.setter
    def rto_threshold(self, rto_threshold):
        r"""Sets the rto_threshold of this ShowCrossCloudDisasterInstanceMonitorResponse.

        rto阈值。

        :param rto_threshold: The rto_threshold of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :type rto_threshold: str
        """
        self._rto_threshold = rto_threshold

    @property
    def switchover_progress(self):
        r"""Gets the switchover_progress of this ShowCrossCloudDisasterInstanceMonitorResponse.

        主从切换进度。该值为一个百分数。例如：40%。

        :return: The switchover_progress of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :rtype: str
        """
        return self._switchover_progress

    @switchover_progress.setter
    def switchover_progress(self, switchover_progress):
        r"""Sets the switchover_progress of this ShowCrossCloudDisasterInstanceMonitorResponse.

        主从切换进度。该值为一个百分数。例如：40%。

        :param switchover_progress: The switchover_progress of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :type switchover_progress: str
        """
        self._switchover_progress = switchover_progress

    @property
    def failover_progress(self):
        r"""Gets the failover_progress of this ShowCrossCloudDisasterInstanceMonitorResponse.

        容灾升主进度。该值为一个百分数。例如：40%。

        :return: The failover_progress of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :rtype: str
        """
        return self._failover_progress

    @failover_progress.setter
    def failover_progress(self, failover_progress):
        r"""Sets the failover_progress of this ShowCrossCloudDisasterInstanceMonitorResponse.

        容灾升主进度。该值为一个百分数。例如：40%。

        :param failover_progress: The failover_progress of this ShowCrossCloudDisasterInstanceMonitorResponse.
        :type failover_progress: str
        """
        self._failover_progress = failover_progress

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
        if not isinstance(other, ShowCrossCloudDisasterInstanceMonitorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
