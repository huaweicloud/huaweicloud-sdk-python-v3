# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkJobStateResponse(SdkResponse):

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
        'state': 'FlinkJobState'
    }

    attribute_map = {
        'job_id': 'job_id',
        'state': 'state'
    }

    def __init__(self, job_id=None, state=None):
        r"""ShowFlinkJobStateResponse

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 
        :type job_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkaidatalake.v2.FlinkJobState`
        """
        
        super().__init__()

        self._job_id = None
        self._state = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if state is not None:
            self.state = state

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowFlinkJobStateResponse.

        **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :return: The job_id of this ShowFlinkJobStateResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowFlinkJobStateResponse.

        **参数解释**：Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :param job_id: The job_id of this ShowFlinkJobStateResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        r"""Gets the state of this ShowFlinkJobStateResponse.

        :return: The state of this ShowFlinkJobStateResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkJobState`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowFlinkJobStateResponse.

        :param state: The state of this ShowFlinkJobStateResponse.
        :type state: :class:`huaweicloudsdkaidatalake.v2.FlinkJobState`
        """
        self._state = state

    def to_dict(self):
        import warnings
        warnings.warn("ShowFlinkJobStateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowFlinkJobStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
