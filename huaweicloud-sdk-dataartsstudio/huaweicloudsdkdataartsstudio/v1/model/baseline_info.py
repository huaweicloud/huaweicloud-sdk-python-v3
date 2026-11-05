# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaselineInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'baseline_id': 'str',
        'baseline_name': 'str',
        'sla_time': 'int',
        'exp_time': 'int'
    }

    attribute_map = {
        'baseline_id': 'baseline_id',
        'baseline_name': 'baseline_name',
        'sla_time': 'sla_time',
        'exp_time': 'exp_time'
    }

    def __init__(self, baseline_id=None, baseline_name=None, sla_time=None, exp_time=None):
        r"""BaselineInfo

        The model defined in huaweicloud sdk

        :param baseline_id: **参数解释**： 基线ID。 **取值范围**： 长度为1~64个字符。
        :type baseline_id: str
        :param baseline_name: **参数解释**： 基线名称。 **取值范围**： 长度为1~1024个字符。
        :type baseline_name: str
        :param sla_time: **参数解释**： 基线承诺时间，单位毫秒。 **取值范围**： 不涉及。
        :type sla_time: int
        :param exp_time: **参数解释**： 基线预警时间，单位毫秒。 **取值范围**： 不涉及。
        :type exp_time: int
        """
        
        

        self._baseline_id = None
        self._baseline_name = None
        self._sla_time = None
        self._exp_time = None
        self.discriminator = None

        if baseline_id is not None:
            self.baseline_id = baseline_id
        if baseline_name is not None:
            self.baseline_name = baseline_name
        if sla_time is not None:
            self.sla_time = sla_time
        if exp_time is not None:
            self.exp_time = exp_time

    @property
    def baseline_id(self):
        r"""Gets the baseline_id of this BaselineInfo.

        **参数解释**： 基线ID。 **取值范围**： 长度为1~64个字符。

        :return: The baseline_id of this BaselineInfo.
        :rtype: str
        """
        return self._baseline_id

    @baseline_id.setter
    def baseline_id(self, baseline_id):
        r"""Sets the baseline_id of this BaselineInfo.

        **参数解释**： 基线ID。 **取值范围**： 长度为1~64个字符。

        :param baseline_id: The baseline_id of this BaselineInfo.
        :type baseline_id: str
        """
        self._baseline_id = baseline_id

    @property
    def baseline_name(self):
        r"""Gets the baseline_name of this BaselineInfo.

        **参数解释**： 基线名称。 **取值范围**： 长度为1~1024个字符。

        :return: The baseline_name of this BaselineInfo.
        :rtype: str
        """
        return self._baseline_name

    @baseline_name.setter
    def baseline_name(self, baseline_name):
        r"""Sets the baseline_name of this BaselineInfo.

        **参数解释**： 基线名称。 **取值范围**： 长度为1~1024个字符。

        :param baseline_name: The baseline_name of this BaselineInfo.
        :type baseline_name: str
        """
        self._baseline_name = baseline_name

    @property
    def sla_time(self):
        r"""Gets the sla_time of this BaselineInfo.

        **参数解释**： 基线承诺时间，单位毫秒。 **取值范围**： 不涉及。

        :return: The sla_time of this BaselineInfo.
        :rtype: int
        """
        return self._sla_time

    @sla_time.setter
    def sla_time(self, sla_time):
        r"""Sets the sla_time of this BaselineInfo.

        **参数解释**： 基线承诺时间，单位毫秒。 **取值范围**： 不涉及。

        :param sla_time: The sla_time of this BaselineInfo.
        :type sla_time: int
        """
        self._sla_time = sla_time

    @property
    def exp_time(self):
        r"""Gets the exp_time of this BaselineInfo.

        **参数解释**： 基线预警时间，单位毫秒。 **取值范围**： 不涉及。

        :return: The exp_time of this BaselineInfo.
        :rtype: int
        """
        return self._exp_time

    @exp_time.setter
    def exp_time(self, exp_time):
        r"""Sets the exp_time of this BaselineInfo.

        **参数解释**： 基线预警时间，单位毫秒。 **取值范围**： 不涉及。

        :param exp_time: The exp_time of this BaselineInfo.
        :type exp_time: int
        """
        self._exp_time = exp_time

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
        if not isinstance(other, BaselineInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
