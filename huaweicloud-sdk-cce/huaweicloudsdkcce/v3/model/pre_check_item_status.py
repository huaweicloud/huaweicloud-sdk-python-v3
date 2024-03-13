# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreCheckItemStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'kind': 'str',
        'group': 'str',
        'level': 'str',
        'phase': 'str',
        'message': 'str',
        'risk_source': 'RiskSource',
        'error_codes': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'kind': 'kind',
        'group': 'group',
        'level': 'level',
        'phase': 'phase',
        'message': 'message',
        'risk_source': 'riskSource',
        'error_codes': 'errorCodes'
    }

    def __init__(self, name=None, kind=None, group=None, level=None, phase=None, message=None, risk_source=None, error_codes=None):
        """PreCheckItemStatus

        The model defined in huaweicloud sdk

        :param name: 检查项名称
        :type name: str
        :param kind: 检查项类型，取值如下 - Exception: 异常类，需要用户解决 - Risk：风险类，用户确认后可选择跳过
        :type kind: str
        :param group: 检查项分组，取值如下 - LimitCheck: 集群限制检查 - MasterCheck：控制节点检查 - NodeCheck：用户节点检查 - AddonCheck：插件检查 - ExecuteException：检查流程错误
        :type group: str
        :param level: 检查项风险级别，取值如下 - Info: 提示级别 - Warning：风险级别 - Fatal：严重级别
        :type level: str
        :param phase: 状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败
        :type phase: str
        :param message: 提示信息
        :type message: str
        :param risk_source: 
        :type risk_source: :class:`huaweicloudsdkcce.v3.RiskSource`
        :param error_codes: 错误码集合
        :type error_codes: list[str]
        """
        
        

        self._name = None
        self._kind = None
        self._group = None
        self._level = None
        self._phase = None
        self._message = None
        self._risk_source = None
        self._error_codes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if kind is not None:
            self.kind = kind
        if group is not None:
            self.group = group
        if level is not None:
            self.level = level
        if phase is not None:
            self.phase = phase
        if message is not None:
            self.message = message
        if risk_source is not None:
            self.risk_source = risk_source
        if error_codes is not None:
            self.error_codes = error_codes

    @property
    def name(self):
        """Gets the name of this PreCheckItemStatus.

        检查项名称

        :return: The name of this PreCheckItemStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PreCheckItemStatus.

        检查项名称

        :param name: The name of this PreCheckItemStatus.
        :type name: str
        """
        self._name = name

    @property
    def kind(self):
        """Gets the kind of this PreCheckItemStatus.

        检查项类型，取值如下 - Exception: 异常类，需要用户解决 - Risk：风险类，用户确认后可选择跳过

        :return: The kind of this PreCheckItemStatus.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PreCheckItemStatus.

        检查项类型，取值如下 - Exception: 异常类，需要用户解决 - Risk：风险类，用户确认后可选择跳过

        :param kind: The kind of this PreCheckItemStatus.
        :type kind: str
        """
        self._kind = kind

    @property
    def group(self):
        """Gets the group of this PreCheckItemStatus.

        检查项分组，取值如下 - LimitCheck: 集群限制检查 - MasterCheck：控制节点检查 - NodeCheck：用户节点检查 - AddonCheck：插件检查 - ExecuteException：检查流程错误

        :return: The group of this PreCheckItemStatus.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this PreCheckItemStatus.

        检查项分组，取值如下 - LimitCheck: 集群限制检查 - MasterCheck：控制节点检查 - NodeCheck：用户节点检查 - AddonCheck：插件检查 - ExecuteException：检查流程错误

        :param group: The group of this PreCheckItemStatus.
        :type group: str
        """
        self._group = group

    @property
    def level(self):
        """Gets the level of this PreCheckItemStatus.

        检查项风险级别，取值如下 - Info: 提示级别 - Warning：风险级别 - Fatal：严重级别

        :return: The level of this PreCheckItemStatus.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this PreCheckItemStatus.

        检查项风险级别，取值如下 - Info: 提示级别 - Warning：风险级别 - Fatal：严重级别

        :param level: The level of this PreCheckItemStatus.
        :type level: str
        """
        self._level = level

    @property
    def phase(self):
        """Gets the phase of this PreCheckItemStatus.

        状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败

        :return: The phase of this PreCheckItemStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this PreCheckItemStatus.

        状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败

        :param phase: The phase of this PreCheckItemStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def message(self):
        """Gets the message of this PreCheckItemStatus.

        提示信息

        :return: The message of this PreCheckItemStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PreCheckItemStatus.

        提示信息

        :param message: The message of this PreCheckItemStatus.
        :type message: str
        """
        self._message = message

    @property
    def risk_source(self):
        """Gets the risk_source of this PreCheckItemStatus.

        :return: The risk_source of this PreCheckItemStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.RiskSource`
        """
        return self._risk_source

    @risk_source.setter
    def risk_source(self, risk_source):
        """Sets the risk_source of this PreCheckItemStatus.

        :param risk_source: The risk_source of this PreCheckItemStatus.
        :type risk_source: :class:`huaweicloudsdkcce.v3.RiskSource`
        """
        self._risk_source = risk_source

    @property
    def error_codes(self):
        """Gets the error_codes of this PreCheckItemStatus.

        错误码集合

        :return: The error_codes of this PreCheckItemStatus.
        :rtype: list[str]
        """
        return self._error_codes

    @error_codes.setter
    def error_codes(self, error_codes):
        """Sets the error_codes of this PreCheckItemStatus.

        错误码集合

        :param error_codes: The error_codes of this PreCheckItemStatus.
        :type error_codes: list[str]
        """
        self._error_codes = error_codes

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
        if not isinstance(other, PreCheckItemStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
