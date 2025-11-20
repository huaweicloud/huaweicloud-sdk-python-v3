# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckTaskStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'message': 'str',
        'risk_list': 'list[CheckTaskRisk]'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'risk_list': 'riskList'
    }

    def __init__(self, status=None, message=None, risk_list=None):
        r"""CheckTaskStatus

        The model defined in huaweicloud sdk

        :param status: **参数解释：** 插件检查状态 **取值范围：** - Init: 插件检查状态，初始化 - Running: 插件检查状态，检查中 - Failed: 插件检查状态，检查完成有风险 - Success: 插件检查状态，检查完成无风险  
        :type status: str
        :param message: **参数解释：** 插件检查结果信息 **取值范围：** 不涉及 
        :type message: str
        :param risk_list: **参数解释：** 插件检查风险项列表，不同插件对应的风险检查项不同。 **约束限制：** 不涉及 
        :type risk_list: list[:class:`huaweicloudsdkcce.v3.CheckTaskRisk`]
        """
        
        

        self._status = None
        self._message = None
        self._risk_list = None
        self.discriminator = None

        self.status = status
        self.message = message
        if risk_list is not None:
            self.risk_list = risk_list

    @property
    def status(self):
        r"""Gets the status of this CheckTaskStatus.

        **参数解释：** 插件检查状态 **取值范围：** - Init: 插件检查状态，初始化 - Running: 插件检查状态，检查中 - Failed: 插件检查状态，检查完成有风险 - Success: 插件检查状态，检查完成无风险  

        :return: The status of this CheckTaskStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CheckTaskStatus.

        **参数解释：** 插件检查状态 **取值范围：** - Init: 插件检查状态，初始化 - Running: 插件检查状态，检查中 - Failed: 插件检查状态，检查完成有风险 - Success: 插件检查状态，检查完成无风险  

        :param status: The status of this CheckTaskStatus.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this CheckTaskStatus.

        **参数解释：** 插件检查结果信息 **取值范围：** 不涉及 

        :return: The message of this CheckTaskStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CheckTaskStatus.

        **参数解释：** 插件检查结果信息 **取值范围：** 不涉及 

        :param message: The message of this CheckTaskStatus.
        :type message: str
        """
        self._message = message

    @property
    def risk_list(self):
        r"""Gets the risk_list of this CheckTaskStatus.

        **参数解释：** 插件检查风险项列表，不同插件对应的风险检查项不同。 **约束限制：** 不涉及 

        :return: The risk_list of this CheckTaskStatus.
        :rtype: list[:class:`huaweicloudsdkcce.v3.CheckTaskRisk`]
        """
        return self._risk_list

    @risk_list.setter
    def risk_list(self, risk_list):
        r"""Sets the risk_list of this CheckTaskStatus.

        **参数解释：** 插件检查风险项列表，不同插件对应的风险检查项不同。 **约束限制：** 不涉及 

        :param risk_list: The risk_list of this CheckTaskStatus.
        :type risk_list: list[:class:`huaweicloudsdkcce.v3.CheckTaskRisk`]
        """
        self._risk_list = risk_list

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
        if not isinstance(other, CheckTaskStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
