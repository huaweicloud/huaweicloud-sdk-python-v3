# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStandardSnapshotResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'snapshot_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'snapshot_id': 'snapshot_id'
    }

    def __init__(self, job_id=None, snapshot_id=None):
        r"""CreateStandardSnapshotResponse

        The model defined in huaweicloud sdk

        :param job_id: **参数解释** 任务ID。 如果需要查询job的状态，请参考：[\&quot;[查询job的状态](https://support.huaweicloud.com/api-evs/evs_04_0054.html)\&quot;](tag:hws)[\&quot;[查询job的状态](https://support.huaweicloud.com/intl/zh-cn/api-evs/evs_04_0054.html)\&quot;](tag:hws_hk)。        **取值范围**  不涉及。
        :type job_id: str
        :param snapshot_id: **参数解释** 快照ID。 **取值范围** 不涉及。
        :type snapshot_id: str
        """
        
        super().__init__()

        self._job_id = None
        self._snapshot_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateStandardSnapshotResponse.

        **参数解释** 任务ID。 如果需要查询job的状态，请参考：[\"[查询job的状态](https://support.huaweicloud.com/api-evs/evs_04_0054.html)\"](tag:hws)[\"[查询job的状态](https://support.huaweicloud.com/intl/zh-cn/api-evs/evs_04_0054.html)\"](tag:hws_hk)。        **取值范围**  不涉及。

        :return: The job_id of this CreateStandardSnapshotResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateStandardSnapshotResponse.

        **参数解释** 任务ID。 如果需要查询job的状态，请参考：[\"[查询job的状态](https://support.huaweicloud.com/api-evs/evs_04_0054.html)\"](tag:hws)[\"[查询job的状态](https://support.huaweicloud.com/intl/zh-cn/api-evs/evs_04_0054.html)\"](tag:hws_hk)。        **取值范围**  不涉及。

        :param job_id: The job_id of this CreateStandardSnapshotResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def snapshot_id(self):
        r"""Gets the snapshot_id of this CreateStandardSnapshotResponse.

        **参数解释** 快照ID。 **取值范围** 不涉及。

        :return: The snapshot_id of this CreateStandardSnapshotResponse.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        r"""Sets the snapshot_id of this CreateStandardSnapshotResponse.

        **参数解释** 快照ID。 **取值范围** 不涉及。

        :param snapshot_id: The snapshot_id of this CreateStandardSnapshotResponse.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateStandardSnapshotResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateStandardSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
