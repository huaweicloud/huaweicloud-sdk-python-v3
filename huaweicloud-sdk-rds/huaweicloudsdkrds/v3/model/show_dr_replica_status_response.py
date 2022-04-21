# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDrReplicaStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'replica_state': 'str',
        'wal_write_receive_delay_in_mb': 'str',
        'wal_write_replay_delay_in_mb': 'str',
        'wal_receive_replay_delay_in_ms': 'str'
    }

    attribute_map = {
        'replica_state': 'replica_state',
        'wal_write_receive_delay_in_mb': 'wal_write_receive_delay_in_mb',
        'wal_write_replay_delay_in_mb': 'wal_write_replay_delay_in_mb',
        'wal_receive_replay_delay_in_ms': 'wal_receive_replay_delay_in_ms'
    }

    def __init__(self, replica_state=None, wal_write_receive_delay_in_mb=None, wal_write_replay_delay_in_mb=None, wal_receive_replay_delay_in_ms=None):
        """ShowDrReplicaStatusResponse

        The model defined in huaweicloud sdk

        :param replica_state: 同步状态，取值范围是0或-1，0表示正常，-1表示异常。
        :type replica_state: str
        :param wal_write_receive_delay_in_mb: 发送延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前接收wal日志位点的差值。
        :type wal_write_receive_delay_in_mb: str
        :param wal_write_replay_delay_in_mb: 端到端延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前回放wal日志位点的差值。
        :type wal_write_replay_delay_in_mb: str
        :param wal_receive_replay_delay_in_ms: 回放延迟时间（ms），即数据在灾备上回放的延迟时间。
        :type wal_receive_replay_delay_in_ms: str
        """
        
        super(ShowDrReplicaStatusResponse, self).__init__()

        self._replica_state = None
        self._wal_write_receive_delay_in_mb = None
        self._wal_write_replay_delay_in_mb = None
        self._wal_receive_replay_delay_in_ms = None
        self.discriminator = None

        if replica_state is not None:
            self.replica_state = replica_state
        if wal_write_receive_delay_in_mb is not None:
            self.wal_write_receive_delay_in_mb = wal_write_receive_delay_in_mb
        if wal_write_replay_delay_in_mb is not None:
            self.wal_write_replay_delay_in_mb = wal_write_replay_delay_in_mb
        if wal_receive_replay_delay_in_ms is not None:
            self.wal_receive_replay_delay_in_ms = wal_receive_replay_delay_in_ms

    @property
    def replica_state(self):
        """Gets the replica_state of this ShowDrReplicaStatusResponse.

        同步状态，取值范围是0或-1，0表示正常，-1表示异常。

        :return: The replica_state of this ShowDrReplicaStatusResponse.
        :rtype: str
        """
        return self._replica_state

    @replica_state.setter
    def replica_state(self, replica_state):
        """Sets the replica_state of this ShowDrReplicaStatusResponse.

        同步状态，取值范围是0或-1，0表示正常，-1表示异常。

        :param replica_state: The replica_state of this ShowDrReplicaStatusResponse.
        :type replica_state: str
        """
        self._replica_state = replica_state

    @property
    def wal_write_receive_delay_in_mb(self):
        """Gets the wal_write_receive_delay_in_mb of this ShowDrReplicaStatusResponse.

        发送延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前接收wal日志位点的差值。

        :return: The wal_write_receive_delay_in_mb of this ShowDrReplicaStatusResponse.
        :rtype: str
        """
        return self._wal_write_receive_delay_in_mb

    @wal_write_receive_delay_in_mb.setter
    def wal_write_receive_delay_in_mb(self, wal_write_receive_delay_in_mb):
        """Sets the wal_write_receive_delay_in_mb of this ShowDrReplicaStatusResponse.

        发送延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前接收wal日志位点的差值。

        :param wal_write_receive_delay_in_mb: The wal_write_receive_delay_in_mb of this ShowDrReplicaStatusResponse.
        :type wal_write_receive_delay_in_mb: str
        """
        self._wal_write_receive_delay_in_mb = wal_write_receive_delay_in_mb

    @property
    def wal_write_replay_delay_in_mb(self):
        """Gets the wal_write_replay_delay_in_mb of this ShowDrReplicaStatusResponse.

        端到端延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前回放wal日志位点的差值。

        :return: The wal_write_replay_delay_in_mb of this ShowDrReplicaStatusResponse.
        :rtype: str
        """
        return self._wal_write_replay_delay_in_mb

    @wal_write_replay_delay_in_mb.setter
    def wal_write_replay_delay_in_mb(self, wal_write_replay_delay_in_mb):
        """Sets the wal_write_replay_delay_in_mb of this ShowDrReplicaStatusResponse.

        端到端延迟大小（MB），即主实例当前wal日志写入位点与灾备实例当前回放wal日志位点的差值。

        :param wal_write_replay_delay_in_mb: The wal_write_replay_delay_in_mb of this ShowDrReplicaStatusResponse.
        :type wal_write_replay_delay_in_mb: str
        """
        self._wal_write_replay_delay_in_mb = wal_write_replay_delay_in_mb

    @property
    def wal_receive_replay_delay_in_ms(self):
        """Gets the wal_receive_replay_delay_in_ms of this ShowDrReplicaStatusResponse.

        回放延迟时间（ms），即数据在灾备上回放的延迟时间。

        :return: The wal_receive_replay_delay_in_ms of this ShowDrReplicaStatusResponse.
        :rtype: str
        """
        return self._wal_receive_replay_delay_in_ms

    @wal_receive_replay_delay_in_ms.setter
    def wal_receive_replay_delay_in_ms(self, wal_receive_replay_delay_in_ms):
        """Sets the wal_receive_replay_delay_in_ms of this ShowDrReplicaStatusResponse.

        回放延迟时间（ms），即数据在灾备上回放的延迟时间。

        :param wal_receive_replay_delay_in_ms: The wal_receive_replay_delay_in_ms of this ShowDrReplicaStatusResponse.
        :type wal_receive_replay_delay_in_ms: str
        """
        self._wal_receive_replay_delay_in_ms = wal_receive_replay_delay_in_ms

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
        if not isinstance(other, ShowDrReplicaStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
