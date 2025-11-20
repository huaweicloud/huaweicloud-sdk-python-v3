# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckTaskRisk:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_name': 'str',
        'level': 'str',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'risk_name': 'riskName',
        'level': 'level',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, risk_name=None, level=None, status=None, message=None):
        r"""CheckTaskRisk

        The model defined in huaweicloud sdk

        :param risk_name: **参数解释：** 风险项名称 **取值范围：** 不涉及 
        :type risk_name: str
        :param level: **参数解释：** 风险等级 **取值范围：** - Warning: 中危，允许跳过 - Fatal: 高危，不允许跳过  
        :type level: str
        :param status: **参数解释：** 风险项检查状态 **取值范围：** - Init: 风险项检查状态，初始化 - Running: 风险项检查状态，检查中 - Failed: 风险项检查状态，检查完成有风险 - Success: 风险项检查状态，检查完成无风险  
        :type status: str
        :param message: **参数解释：** 风险检查结果说明 **取值范围：** 不涉及 
        :type message: str
        """
        
        

        self._risk_name = None
        self._level = None
        self._status = None
        self._message = None
        self.discriminator = None

        self.risk_name = risk_name
        self.level = level
        self.status = status
        if message is not None:
            self.message = message

    @property
    def risk_name(self):
        r"""Gets the risk_name of this CheckTaskRisk.

        **参数解释：** 风险项名称 **取值范围：** 不涉及 

        :return: The risk_name of this CheckTaskRisk.
        :rtype: str
        """
        return self._risk_name

    @risk_name.setter
    def risk_name(self, risk_name):
        r"""Sets the risk_name of this CheckTaskRisk.

        **参数解释：** 风险项名称 **取值范围：** 不涉及 

        :param risk_name: The risk_name of this CheckTaskRisk.
        :type risk_name: str
        """
        self._risk_name = risk_name

    @property
    def level(self):
        r"""Gets the level of this CheckTaskRisk.

        **参数解释：** 风险等级 **取值范围：** - Warning: 中危，允许跳过 - Fatal: 高危，不允许跳过  

        :return: The level of this CheckTaskRisk.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CheckTaskRisk.

        **参数解释：** 风险等级 **取值范围：** - Warning: 中危，允许跳过 - Fatal: 高危，不允许跳过  

        :param level: The level of this CheckTaskRisk.
        :type level: str
        """
        self._level = level

    @property
    def status(self):
        r"""Gets the status of this CheckTaskRisk.

        **参数解释：** 风险项检查状态 **取值范围：** - Init: 风险项检查状态，初始化 - Running: 风险项检查状态，检查中 - Failed: 风险项检查状态，检查完成有风险 - Success: 风险项检查状态，检查完成无风险  

        :return: The status of this CheckTaskRisk.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CheckTaskRisk.

        **参数解释：** 风险项检查状态 **取值范围：** - Init: 风险项检查状态，初始化 - Running: 风险项检查状态，检查中 - Failed: 风险项检查状态，检查完成有风险 - Success: 风险项检查状态，检查完成无风险  

        :param status: The status of this CheckTaskRisk.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this CheckTaskRisk.

        **参数解释：** 风险检查结果说明 **取值范围：** 不涉及 

        :return: The message of this CheckTaskRisk.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CheckTaskRisk.

        **参数解释：** 风险检查结果说明 **取值范围：** 不涉及 

        :param message: The message of this CheckTaskRisk.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, CheckTaskRisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
