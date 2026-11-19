# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSnapshotPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'scheduled_task_status': 'str',
        'scheduled_task_time': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'scheduled_task_status': 'scheduled_task_status',
        'scheduled_task_time': 'scheduled_task_time'
    }

    def __init__(self, host_id=None, scheduled_task_status=None, scheduled_task_time=None):
        r"""UpdateSnapshotPolicyRequestBody

        The model defined in huaweicloud sdk

        :param host_id: 服务器id
        :type host_id: str
        :param scheduled_task_status: 是否开启定时快照 |-closed：关闭， -opened：开启
        :type scheduled_task_status: str
        :param scheduled_task_time: 主机每天定时快照的时间，支持整点，0-23, 默认时间为零点。
        :type scheduled_task_time: int
        """
        
        

        self._host_id = None
        self._scheduled_task_status = None
        self._scheduled_task_time = None
        self.discriminator = None

        self.host_id = host_id
        self.scheduled_task_status = scheduled_task_status
        if scheduled_task_time is not None:
            self.scheduled_task_time = scheduled_task_time

    @property
    def host_id(self):
        r"""Gets the host_id of this UpdateSnapshotPolicyRequestBody.

        服务器id

        :return: The host_id of this UpdateSnapshotPolicyRequestBody.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this UpdateSnapshotPolicyRequestBody.

        服务器id

        :param host_id: The host_id of this UpdateSnapshotPolicyRequestBody.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def scheduled_task_status(self):
        r"""Gets the scheduled_task_status of this UpdateSnapshotPolicyRequestBody.

        是否开启定时快照 |-closed：关闭， -opened：开启

        :return: The scheduled_task_status of this UpdateSnapshotPolicyRequestBody.
        :rtype: str
        """
        return self._scheduled_task_status

    @scheduled_task_status.setter
    def scheduled_task_status(self, scheduled_task_status):
        r"""Sets the scheduled_task_status of this UpdateSnapshotPolicyRequestBody.

        是否开启定时快照 |-closed：关闭， -opened：开启

        :param scheduled_task_status: The scheduled_task_status of this UpdateSnapshotPolicyRequestBody.
        :type scheduled_task_status: str
        """
        self._scheduled_task_status = scheduled_task_status

    @property
    def scheduled_task_time(self):
        r"""Gets the scheduled_task_time of this UpdateSnapshotPolicyRequestBody.

        主机每天定时快照的时间，支持整点，0-23, 默认时间为零点。

        :return: The scheduled_task_time of this UpdateSnapshotPolicyRequestBody.
        :rtype: int
        """
        return self._scheduled_task_time

    @scheduled_task_time.setter
    def scheduled_task_time(self, scheduled_task_time):
        r"""Sets the scheduled_task_time of this UpdateSnapshotPolicyRequestBody.

        主机每天定时快照的时间，支持整点，0-23, 默认时间为零点。

        :param scheduled_task_time: The scheduled_task_time of this UpdateSnapshotPolicyRequestBody.
        :type scheduled_task_time: int
        """
        self._scheduled_task_time = scheduled_task_time

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
        if not isinstance(other, UpdateSnapshotPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
