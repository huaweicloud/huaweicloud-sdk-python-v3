# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteRocketMqMigrationTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_task_list': 'list[str]'
    }

    attribute_map = {
        'success_task_list': 'success_task_list'
    }

    def __init__(self, success_task_list=None):
        r"""BatchDeleteRocketMqMigrationTaskResponse

        The model defined in huaweicloud sdk

        :param success_task_list: **参数解释**： 删除成功的任务列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。
        :type success_task_list: list[str]
        """
        
        super().__init__()

        self._success_task_list = None
        self.discriminator = None

        if success_task_list is not None:
            self.success_task_list = success_task_list

    @property
    def success_task_list(self):
        r"""Gets the success_task_list of this BatchDeleteRocketMqMigrationTaskResponse.

        **参数解释**： 删除成功的任务列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。

        :return: The success_task_list of this BatchDeleteRocketMqMigrationTaskResponse.
        :rtype: list[str]
        """
        return self._success_task_list

    @success_task_list.setter
    def success_task_list(self, success_task_list):
        r"""Sets the success_task_list of this BatchDeleteRocketMqMigrationTaskResponse.

        **参数解释**： 删除成功的任务列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。

        :param success_task_list: The success_task_list of this BatchDeleteRocketMqMigrationTaskResponse.
        :type success_task_list: list[str]
        """
        self._success_task_list = success_task_list

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeleteRocketMqMigrationTaskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchDeleteRocketMqMigrationTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
