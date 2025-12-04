# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRebuildSlaveStatusResponse(SdkResponse):

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
        'workflow_id': 'str',
        'last_rebuild_time': 'str',
        'next_rebuild_time': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'workflow_id': 'workflow_id',
        'last_rebuild_time': 'last_rebuild_time',
        'next_rebuild_time': 'next_rebuild_time'
    }

    def __init__(self, instance_id=None, workflow_id=None, last_rebuild_time=None, next_rebuild_time=None):
        r"""ShowRebuildSlaveStatusResponse

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param workflow_id: **参数解释**：  任务流ID  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type workflow_id: str
        :param last_rebuild_time: **参数解释**：  上一次重建的时间  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type last_rebuild_time: str
        :param next_rebuild_time: **参数解释**：  下次允许重建的时间  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type next_rebuild_time: str
        """
        
        super().__init__()

        self._instance_id = None
        self._workflow_id = None
        self._last_rebuild_time = None
        self._next_rebuild_time = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if last_rebuild_time is not None:
            self.last_rebuild_time = last_rebuild_time
        if next_rebuild_time is not None:
            self.next_rebuild_time = next_rebuild_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowRebuildSlaveStatusResponse.

        **参数解释**：  实例ID  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this ShowRebuildSlaveStatusResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowRebuildSlaveStatusResponse.

        **参数解释**：  实例ID  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ShowRebuildSlaveStatusResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this ShowRebuildSlaveStatusResponse.

        **参数解释**：  任务流ID  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The workflow_id of this ShowRebuildSlaveStatusResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this ShowRebuildSlaveStatusResponse.

        **参数解释**：  任务流ID  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param workflow_id: The workflow_id of this ShowRebuildSlaveStatusResponse.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def last_rebuild_time(self):
        r"""Gets the last_rebuild_time of this ShowRebuildSlaveStatusResponse.

        **参数解释**：  上一次重建的时间  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The last_rebuild_time of this ShowRebuildSlaveStatusResponse.
        :rtype: str
        """
        return self._last_rebuild_time

    @last_rebuild_time.setter
    def last_rebuild_time(self, last_rebuild_time):
        r"""Sets the last_rebuild_time of this ShowRebuildSlaveStatusResponse.

        **参数解释**：  上一次重建的时间  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param last_rebuild_time: The last_rebuild_time of this ShowRebuildSlaveStatusResponse.
        :type last_rebuild_time: str
        """
        self._last_rebuild_time = last_rebuild_time

    @property
    def next_rebuild_time(self):
        r"""Gets the next_rebuild_time of this ShowRebuildSlaveStatusResponse.

        **参数解释**：  下次允许重建的时间  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The next_rebuild_time of this ShowRebuildSlaveStatusResponse.
        :rtype: str
        """
        return self._next_rebuild_time

    @next_rebuild_time.setter
    def next_rebuild_time(self, next_rebuild_time):
        r"""Sets the next_rebuild_time of this ShowRebuildSlaveStatusResponse.

        **参数解释**：  下次允许重建的时间  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param next_rebuild_time: The next_rebuild_time of this ShowRebuildSlaveStatusResponse.
        :type next_rebuild_time: str
        """
        self._next_rebuild_time = next_rebuild_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowRebuildSlaveStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRebuildSlaveStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
