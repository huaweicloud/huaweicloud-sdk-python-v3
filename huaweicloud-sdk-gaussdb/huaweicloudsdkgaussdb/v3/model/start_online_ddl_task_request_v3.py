# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartOnlineDDLTaskRequestV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_clear': 'bool',
        'task_content': 'list[StartOnlineTaskContentItem]'
    }

    attribute_map = {
        'auto_clear': 'auto_clear',
        'task_content': 'task_content'
    }

    def __init__(self, auto_clear=None, task_content=None):
        r"""StartOnlineDDLTaskRequestV3

        The model defined in huaweicloud sdk

        :param auto_clear: **参数解释**：  是否开启自动清理临时表。  **约束限制**：  不涉及。  **取值范围**： - true：开启自动清理临时表。 - false：关闭自动清理临时表。  **默认取值**：  false。
        :type auto_clear: bool
        :param task_content: **参数解释**：  无锁变更任务详细内容。  **约束限制**：  不涉及。
        :type task_content: list[:class:`huaweicloudsdkgaussdb.v3.StartOnlineTaskContentItem`]
        """
        
        

        self._auto_clear = None
        self._task_content = None
        self.discriminator = None

        if auto_clear is not None:
            self.auto_clear = auto_clear
        self.task_content = task_content

    @property
    def auto_clear(self):
        r"""Gets the auto_clear of this StartOnlineDDLTaskRequestV3.

        **参数解释**：  是否开启自动清理临时表。  **约束限制**：  不涉及。  **取值范围**： - true：开启自动清理临时表。 - false：关闭自动清理临时表。  **默认取值**：  false。

        :return: The auto_clear of this StartOnlineDDLTaskRequestV3.
        :rtype: bool
        """
        return self._auto_clear

    @auto_clear.setter
    def auto_clear(self, auto_clear):
        r"""Sets the auto_clear of this StartOnlineDDLTaskRequestV3.

        **参数解释**：  是否开启自动清理临时表。  **约束限制**：  不涉及。  **取值范围**： - true：开启自动清理临时表。 - false：关闭自动清理临时表。  **默认取值**：  false。

        :param auto_clear: The auto_clear of this StartOnlineDDLTaskRequestV3.
        :type auto_clear: bool
        """
        self._auto_clear = auto_clear

    @property
    def task_content(self):
        r"""Gets the task_content of this StartOnlineDDLTaskRequestV3.

        **参数解释**：  无锁变更任务详细内容。  **约束限制**：  不涉及。

        :return: The task_content of this StartOnlineDDLTaskRequestV3.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.StartOnlineTaskContentItem`]
        """
        return self._task_content

    @task_content.setter
    def task_content(self, task_content):
        r"""Sets the task_content of this StartOnlineDDLTaskRequestV3.

        **参数解释**：  无锁变更任务详细内容。  **约束限制**：  不涉及。

        :param task_content: The task_content of this StartOnlineDDLTaskRequestV3.
        :type task_content: list[:class:`huaweicloudsdkgaussdb.v3.StartOnlineTaskContentItem`]
        """
        self._task_content = task_content

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
        if not isinstance(other, StartOnlineDDLTaskRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
