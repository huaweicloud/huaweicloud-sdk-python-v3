# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchModifySlowProcessThresholdRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'slow_process_threshold': 'int'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'slow_process_threshold': 'slow_process_threshold'
    }

    def __init__(self, instance_ids=None, slow_process_threshold=None):
        r"""BatchModifySlowProcessThresholdRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: **参数解释**：  批量修改慢会话阈值的实例ID列表。实例ID只能由英文字母、数字组成，后缀为in07，长度为36个字符。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  列表不能为空，且列表长度小于等于100。
        :type instance_ids: list[str]
        :param slow_process_threshold: **参数解释**：  实例慢会话阈值。单位为秒。  **约束限制**：   不涉及。  **取值范围**：  1-86400。  **默认取值**：  不涉及。
        :type slow_process_threshold: int
        """
        
        

        self._instance_ids = None
        self._slow_process_threshold = None
        self.discriminator = None

        self.instance_ids = instance_ids
        self.slow_process_threshold = slow_process_threshold

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this BatchModifySlowProcessThresholdRequestBody.

        **参数解释**：  批量修改慢会话阈值的实例ID列表。实例ID只能由英文字母、数字组成，后缀为in07，长度为36个字符。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  列表不能为空，且列表长度小于等于100。

        :return: The instance_ids of this BatchModifySlowProcessThresholdRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this BatchModifySlowProcessThresholdRequestBody.

        **参数解释**：  批量修改慢会话阈值的实例ID列表。实例ID只能由英文字母、数字组成，后缀为in07，长度为36个字符。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  列表不能为空，且列表长度小于等于100。

        :param instance_ids: The instance_ids of this BatchModifySlowProcessThresholdRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def slow_process_threshold(self):
        r"""Gets the slow_process_threshold of this BatchModifySlowProcessThresholdRequestBody.

        **参数解释**：  实例慢会话阈值。单位为秒。  **约束限制**：   不涉及。  **取值范围**：  1-86400。  **默认取值**：  不涉及。

        :return: The slow_process_threshold of this BatchModifySlowProcessThresholdRequestBody.
        :rtype: int
        """
        return self._slow_process_threshold

    @slow_process_threshold.setter
    def slow_process_threshold(self, slow_process_threshold):
        r"""Sets the slow_process_threshold of this BatchModifySlowProcessThresholdRequestBody.

        **参数解释**：  实例慢会话阈值。单位为秒。  **约束限制**：   不涉及。  **取值范围**：  1-86400。  **默认取值**：  不涉及。

        :param slow_process_threshold: The slow_process_threshold of this BatchModifySlowProcessThresholdRequestBody.
        :type slow_process_threshold: int
        """
        self._slow_process_threshold = slow_process_threshold

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
        if not isinstance(other, BatchModifySlowProcessThresholdRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
