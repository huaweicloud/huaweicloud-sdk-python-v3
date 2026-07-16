# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpsSynthesisTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str'
    }

    attribute_map = {
        'status': 'status'
    }

    def __init__(self, status=None):
        r"""UpdateOpsSynthesisTaskRequestBody

        The model defined in huaweicloud sdk

        :param status: **参数解释：** 用户希望任务切换到的目标状态，用于控制任务的启动或紧急停止。 **约束限制：** 枚举值。 **取值范围：** running（启动或恢复任务执行，任务将从暂停或初始状态开始运行）、stopped（强制终止任务，任务将立即停止执行并释放资源）。 **默认取值：** 不涉及。 
        :type status: str
        """
        
        

        self._status = None
        self.discriminator = None

        self.status = status

    @property
    def status(self):
        r"""Gets the status of this UpdateOpsSynthesisTaskRequestBody.

        **参数解释：** 用户希望任务切换到的目标状态，用于控制任务的启动或紧急停止。 **约束限制：** 枚举值。 **取值范围：** running（启动或恢复任务执行，任务将从暂停或初始状态开始运行）、stopped（强制终止任务，任务将立即停止执行并释放资源）。 **默认取值：** 不涉及。 

        :return: The status of this UpdateOpsSynthesisTaskRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateOpsSynthesisTaskRequestBody.

        **参数解释：** 用户希望任务切换到的目标状态，用于控制任务的启动或紧急停止。 **约束限制：** 枚举值。 **取值范围：** running（启动或恢复任务执行，任务将从暂停或初始状态开始运行）、stopped（强制终止任务，任务将立即停止执行并释放资源）。 **默认取值：** 不涉及。 

        :param status: The status of this UpdateOpsSynthesisTaskRequestBody.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, UpdateOpsSynthesisTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
