# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemFlowRuleConfigVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'open': 'bool',
        'config_value': 'list[WorkItemFlowFieldConfigVO]'
    }

    attribute_map = {
        'code': 'code',
        'open': 'open',
        'config_value': 'config_value'
    }

    def __init__(self, code=None, open=None, config_value=None):
        r"""WorkItemFlowRuleConfigVO

        The model defined in huaweicloud sdk

        :param code: 规则编码
        :type code: str
        :param open: 规则开关
        :type open: bool
        :param config_value: 字段配置值列表
        :type config_value: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowFieldConfigVO`]
        """
        
        

        self._code = None
        self._open = None
        self._config_value = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if open is not None:
            self.open = open
        if config_value is not None:
            self.config_value = config_value

    @property
    def code(self):
        r"""Gets the code of this WorkItemFlowRuleConfigVO.

        规则编码

        :return: The code of this WorkItemFlowRuleConfigVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this WorkItemFlowRuleConfigVO.

        规则编码

        :param code: The code of this WorkItemFlowRuleConfigVO.
        :type code: str
        """
        self._code = code

    @property
    def open(self):
        r"""Gets the open of this WorkItemFlowRuleConfigVO.

        规则开关

        :return: The open of this WorkItemFlowRuleConfigVO.
        :rtype: bool
        """
        return self._open

    @open.setter
    def open(self, open):
        r"""Sets the open of this WorkItemFlowRuleConfigVO.

        规则开关

        :param open: The open of this WorkItemFlowRuleConfigVO.
        :type open: bool
        """
        self._open = open

    @property
    def config_value(self):
        r"""Gets the config_value of this WorkItemFlowRuleConfigVO.

        字段配置值列表

        :return: The config_value of this WorkItemFlowRuleConfigVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowFieldConfigVO`]
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        r"""Sets the config_value of this WorkItemFlowRuleConfigVO.

        字段配置值列表

        :param config_value: The config_value of this WorkItemFlowRuleConfigVO.
        :type config_value: list[:class:`huaweicloudsdkprojectman.v4.WorkItemFlowFieldConfigVO`]
        """
        self._config_value = config_value

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
        if not isinstance(other, WorkItemFlowRuleConfigVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
