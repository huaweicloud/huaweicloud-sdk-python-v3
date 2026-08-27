# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventJobResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'instance_id': 'str',
        'job_id': 'str',
        'success': 'bool',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'instance_id': 'instance_id',
        'job_id': 'job_id',
        'success': 'success',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, event_id=None, instance_id=None, job_id=None, success=None, error_code=None, error_msg=None):
        r"""EventJobResult

        The model defined in huaweicloud sdk

        :param event_id: **参数解释**：  事件ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为ev07，长度为36个字符。
        :type event_id: str
        :param instance_id: **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为in07，长度为36个字符。
        :type instance_id: str
        :param job_id: **参数解释**：  创建数据同步的任务ID。  **取值范围**：  不涉及。
        :type job_id: str
        :param success: **参数解释**：  是否下发成功。  **取值范围**：  - true：下发成功。 - false：下发失败。
        :type success: bool
        :param error_code: **参数解释**：  错误码。  **取值范围**：  不涉及。
        :type error_code: str
        :param error_msg: **参数解释**：  错误消息。  **取值范围**：  不涉及。
        :type error_msg: str
        """
        
        

        self._event_id = None
        self._instance_id = None
        self._job_id = None
        self._success = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if instance_id is not None:
            self.instance_id = instance_id
        if job_id is not None:
            self.job_id = job_id
        if success is not None:
            self.success = success
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def event_id(self):
        r"""Gets the event_id of this EventJobResult.

        **参数解释**：  事件ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为ev07，长度为36个字符。

        :return: The event_id of this EventJobResult.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this EventJobResult.

        **参数解释**：  事件ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为ev07，长度为36个字符。

        :param event_id: The event_id of this EventJobResult.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this EventJobResult.

        **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为in07，长度为36个字符。

        :return: The instance_id of this EventJobResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this EventJobResult.

        **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为in07，长度为36个字符。

        :param instance_id: The instance_id of this EventJobResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def job_id(self):
        r"""Gets the job_id of this EventJobResult.

        **参数解释**：  创建数据同步的任务ID。  **取值范围**：  不涉及。

        :return: The job_id of this EventJobResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this EventJobResult.

        **参数解释**：  创建数据同步的任务ID。  **取值范围**：  不涉及。

        :param job_id: The job_id of this EventJobResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def success(self):
        r"""Gets the success of this EventJobResult.

        **参数解释**：  是否下发成功。  **取值范围**：  - true：下发成功。 - false：下发失败。

        :return: The success of this EventJobResult.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this EventJobResult.

        **参数解释**：  是否下发成功。  **取值范围**：  - true：下发成功。 - false：下发失败。

        :param success: The success of this EventJobResult.
        :type success: bool
        """
        self._success = success

    @property
    def error_code(self):
        r"""Gets the error_code of this EventJobResult.

        **参数解释**：  错误码。  **取值范围**：  不涉及。

        :return: The error_code of this EventJobResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this EventJobResult.

        **参数解释**：  错误码。  **取值范围**：  不涉及。

        :param error_code: The error_code of this EventJobResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this EventJobResult.

        **参数解释**：  错误消息。  **取值范围**：  不涉及。

        :return: The error_msg of this EventJobResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this EventJobResult.

        **参数解释**：  错误消息。  **取值范围**：  不涉及。

        :param error_msg: The error_msg of this EventJobResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, EventJobResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
