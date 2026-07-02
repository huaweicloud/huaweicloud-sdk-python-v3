# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckScheduleTaskExistResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exist': 'bool',
        'scheduled_tasks': 'list[ScheduledTaskV3]'
    }

    attribute_map = {
        'exist': 'exist',
        'scheduled_tasks': 'scheduled_tasks'
    }

    def __init__(self, exist=None, scheduled_tasks=None):
        r"""CheckScheduleTaskExistResponse

        The model defined in huaweicloud sdk

        :param exist: **参数解释**：  定时任务类型是否存在。 **取值范围**： - true：指定的定时任务类型已存在。 - false：指定的定时任务类型不存在。
        :type exist: bool
        :param scheduled_tasks: **参数解释**：  定时任务详情列表。当 &#x60;exist&#x60; 为 true 时，此列表包含已存在的任务信息。  **取值范围**： 不涉及。
        :type scheduled_tasks: list[:class:`huaweicloudsdkgaussdb.v3.ScheduledTaskV3`]
        """
        
        super().__init__()

        self._exist = None
        self._scheduled_tasks = None
        self.discriminator = None

        if exist is not None:
            self.exist = exist
        if scheduled_tasks is not None:
            self.scheduled_tasks = scheduled_tasks

    @property
    def exist(self):
        r"""Gets the exist of this CheckScheduleTaskExistResponse.

        **参数解释**：  定时任务类型是否存在。 **取值范围**： - true：指定的定时任务类型已存在。 - false：指定的定时任务类型不存在。

        :return: The exist of this CheckScheduleTaskExistResponse.
        :rtype: bool
        """
        return self._exist

    @exist.setter
    def exist(self, exist):
        r"""Sets the exist of this CheckScheduleTaskExistResponse.

        **参数解释**：  定时任务类型是否存在。 **取值范围**： - true：指定的定时任务类型已存在。 - false：指定的定时任务类型不存在。

        :param exist: The exist of this CheckScheduleTaskExistResponse.
        :type exist: bool
        """
        self._exist = exist

    @property
    def scheduled_tasks(self):
        r"""Gets the scheduled_tasks of this CheckScheduleTaskExistResponse.

        **参数解释**：  定时任务详情列表。当 `exist` 为 true 时，此列表包含已存在的任务信息。  **取值范围**： 不涉及。

        :return: The scheduled_tasks of this CheckScheduleTaskExistResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ScheduledTaskV3`]
        """
        return self._scheduled_tasks

    @scheduled_tasks.setter
    def scheduled_tasks(self, scheduled_tasks):
        r"""Sets the scheduled_tasks of this CheckScheduleTaskExistResponse.

        **参数解释**：  定时任务详情列表。当 `exist` 为 true 时，此列表包含已存在的任务信息。  **取值范围**： 不涉及。

        :param scheduled_tasks: The scheduled_tasks of this CheckScheduleTaskExistResponse.
        :type scheduled_tasks: list[:class:`huaweicloudsdkgaussdb.v3.ScheduledTaskV3`]
        """
        self._scheduled_tasks = scheduled_tasks

    def to_dict(self):
        import warnings
        warnings.warn("CheckScheduleTaskExistResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CheckScheduleTaskExistResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
