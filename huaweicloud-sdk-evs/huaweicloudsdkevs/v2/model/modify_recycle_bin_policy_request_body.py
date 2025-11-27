# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyRecycleBinPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch': 'bool',
        'threshold_time': 'int',
        'keep_time': 'int'
    }

    attribute_map = {
        'switch': 'switch',
        'threshold_time': 'threshold_time',
        'keep_time': 'keep_time'
    }

    def __init__(self, switch=None, threshold_time=None, keep_time=None):
        r"""ModifyRecycleBinPolicyRequestBody

        The model defined in huaweicloud sdk

        :param switch: **参数解释** 回收站开关。 **约束限制** 不涉及。 **取值范围** - true：表示打开回收站。 - false：表示关闭回收站。 **默认取值** 不涉及。
        :type switch: bool
        :param threshold_time: **参数解释** 回收站门槛时间，云硬盘创建多少天后删除才会放入回收站。 **约束限制** 不涉及。 **取值范围** 1-1000 **默认取值** 7
        :type threshold_time: int
        :param keep_time: **参数解释** 回收站的云硬盘保存期限（天），云硬盘进入回收站后多少天才会被彻底删除。 **约束限制** 不涉及。 **取值范围** 1-365 **默认取值** 7
        :type keep_time: int
        """
        
        

        self._switch = None
        self._threshold_time = None
        self._keep_time = None
        self.discriminator = None

        if switch is not None:
            self.switch = switch
        if threshold_time is not None:
            self.threshold_time = threshold_time
        if keep_time is not None:
            self.keep_time = keep_time

    @property
    def switch(self):
        r"""Gets the switch of this ModifyRecycleBinPolicyRequestBody.

        **参数解释** 回收站开关。 **约束限制** 不涉及。 **取值范围** - true：表示打开回收站。 - false：表示关闭回收站。 **默认取值** 不涉及。

        :return: The switch of this ModifyRecycleBinPolicyRequestBody.
        :rtype: bool
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        r"""Sets the switch of this ModifyRecycleBinPolicyRequestBody.

        **参数解释** 回收站开关。 **约束限制** 不涉及。 **取值范围** - true：表示打开回收站。 - false：表示关闭回收站。 **默认取值** 不涉及。

        :param switch: The switch of this ModifyRecycleBinPolicyRequestBody.
        :type switch: bool
        """
        self._switch = switch

    @property
    def threshold_time(self):
        r"""Gets the threshold_time of this ModifyRecycleBinPolicyRequestBody.

        **参数解释** 回收站门槛时间，云硬盘创建多少天后删除才会放入回收站。 **约束限制** 不涉及。 **取值范围** 1-1000 **默认取值** 7

        :return: The threshold_time of this ModifyRecycleBinPolicyRequestBody.
        :rtype: int
        """
        return self._threshold_time

    @threshold_time.setter
    def threshold_time(self, threshold_time):
        r"""Sets the threshold_time of this ModifyRecycleBinPolicyRequestBody.

        **参数解释** 回收站门槛时间，云硬盘创建多少天后删除才会放入回收站。 **约束限制** 不涉及。 **取值范围** 1-1000 **默认取值** 7

        :param threshold_time: The threshold_time of this ModifyRecycleBinPolicyRequestBody.
        :type threshold_time: int
        """
        self._threshold_time = threshold_time

    @property
    def keep_time(self):
        r"""Gets the keep_time of this ModifyRecycleBinPolicyRequestBody.

        **参数解释** 回收站的云硬盘保存期限（天），云硬盘进入回收站后多少天才会被彻底删除。 **约束限制** 不涉及。 **取值范围** 1-365 **默认取值** 7

        :return: The keep_time of this ModifyRecycleBinPolicyRequestBody.
        :rtype: int
        """
        return self._keep_time

    @keep_time.setter
    def keep_time(self, keep_time):
        r"""Sets the keep_time of this ModifyRecycleBinPolicyRequestBody.

        **参数解释** 回收站的云硬盘保存期限（天），云硬盘进入回收站后多少天才会被彻底删除。 **约束限制** 不涉及。 **取值范围** 1-365 **默认取值** 7

        :param keep_time: The keep_time of this ModifyRecycleBinPolicyRequestBody.
        :type keep_time: int
        """
        self._keep_time = keep_time

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
        if not isinstance(other, ModifyRecycleBinPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
