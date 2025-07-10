# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowTemplateFlowsVO:

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
        'name': 'str',
        'before_rule_validator': 'list[WorkflowTemplateConfigsVO]',
        'before_rule_configs': 'list[WorkflowTemplateConfigsVO]',
        'from_code': 'str',
        'to_code': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'before_rule_validator': 'before_rule_validator',
        'before_rule_configs': 'before_rule_configs',
        'from_code': 'from_code',
        'to_code': 'to_code'
    }

    def __init__(self, code=None, name=None, before_rule_validator=None, before_rule_configs=None, from_code=None, to_code=None):
        r"""WorkflowTemplateFlowsVO

        The model defined in huaweicloud sdk

        :param code: 流转线编码
        :type code: str
        :param name: 流转线名称
        :type name: str
        :param before_rule_validator: 流转前校验配置
        :type before_rule_validator: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateConfigsVO`]
        :param before_rule_configs: 流转中界面配置
        :type before_rule_configs: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateConfigsVO`]
        :param from_code: 流转线的入口状态
        :type from_code: str
        :param to_code: 流转线的出口状态
        :type to_code: str
        """
        
        

        self._code = None
        self._name = None
        self._before_rule_validator = None
        self._before_rule_configs = None
        self._from_code = None
        self._to_code = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if before_rule_validator is not None:
            self.before_rule_validator = before_rule_validator
        if before_rule_configs is not None:
            self.before_rule_configs = before_rule_configs
        if from_code is not None:
            self.from_code = from_code
        if to_code is not None:
            self.to_code = to_code

    @property
    def code(self):
        r"""Gets the code of this WorkflowTemplateFlowsVO.

        流转线编码

        :return: The code of this WorkflowTemplateFlowsVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this WorkflowTemplateFlowsVO.

        流转线编码

        :param code: The code of this WorkflowTemplateFlowsVO.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        r"""Gets the name of this WorkflowTemplateFlowsVO.

        流转线名称

        :return: The name of this WorkflowTemplateFlowsVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkflowTemplateFlowsVO.

        流转线名称

        :param name: The name of this WorkflowTemplateFlowsVO.
        :type name: str
        """
        self._name = name

    @property
    def before_rule_validator(self):
        r"""Gets the before_rule_validator of this WorkflowTemplateFlowsVO.

        流转前校验配置

        :return: The before_rule_validator of this WorkflowTemplateFlowsVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateConfigsVO`]
        """
        return self._before_rule_validator

    @before_rule_validator.setter
    def before_rule_validator(self, before_rule_validator):
        r"""Sets the before_rule_validator of this WorkflowTemplateFlowsVO.

        流转前校验配置

        :param before_rule_validator: The before_rule_validator of this WorkflowTemplateFlowsVO.
        :type before_rule_validator: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateConfigsVO`]
        """
        self._before_rule_validator = before_rule_validator

    @property
    def before_rule_configs(self):
        r"""Gets the before_rule_configs of this WorkflowTemplateFlowsVO.

        流转中界面配置

        :return: The before_rule_configs of this WorkflowTemplateFlowsVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateConfigsVO`]
        """
        return self._before_rule_configs

    @before_rule_configs.setter
    def before_rule_configs(self, before_rule_configs):
        r"""Sets the before_rule_configs of this WorkflowTemplateFlowsVO.

        流转中界面配置

        :param before_rule_configs: The before_rule_configs of this WorkflowTemplateFlowsVO.
        :type before_rule_configs: list[:class:`huaweicloudsdkprojectman.v4.WorkflowTemplateConfigsVO`]
        """
        self._before_rule_configs = before_rule_configs

    @property
    def from_code(self):
        r"""Gets the from_code of this WorkflowTemplateFlowsVO.

        流转线的入口状态

        :return: The from_code of this WorkflowTemplateFlowsVO.
        :rtype: str
        """
        return self._from_code

    @from_code.setter
    def from_code(self, from_code):
        r"""Sets the from_code of this WorkflowTemplateFlowsVO.

        流转线的入口状态

        :param from_code: The from_code of this WorkflowTemplateFlowsVO.
        :type from_code: str
        """
        self._from_code = from_code

    @property
    def to_code(self):
        r"""Gets the to_code of this WorkflowTemplateFlowsVO.

        流转线的出口状态

        :return: The to_code of this WorkflowTemplateFlowsVO.
        :rtype: str
        """
        return self._to_code

    @to_code.setter
    def to_code(self, to_code):
        r"""Sets the to_code of this WorkflowTemplateFlowsVO.

        流转线的出口状态

        :param to_code: The to_code of this WorkflowTemplateFlowsVO.
        :type to_code: str
        """
        self._to_code = to_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowTemplateFlowsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
