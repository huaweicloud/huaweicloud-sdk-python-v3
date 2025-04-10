# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventStreamingCreateReq:

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
        'description': 'str',
        'source': 'EventStreamingSource',
        'sink': 'EventStreamingSink',
        'rule_config': 'EventStreamingCreateReqRuleConfig',
        'option': 'RunOption'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'source': 'source',
        'sink': 'sink',
        'rule_config': 'rule_config',
        'option': 'option'
    }

    def __init__(self, name=None, description=None, source=None, sink=None, rule_config=None, option=None):
        r"""EventStreamingCreateReq

        The model defined in huaweicloud sdk

        :param name: 事件流名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头
        :type name: str
        :param description: 事件流描述
        :type description: str
        :param source: 
        :type source: :class:`huaweicloudsdkeg.v1.EventStreamingSource`
        :param sink: 
        :type sink: :class:`huaweicloudsdkeg.v1.EventStreamingSink`
        :param rule_config: 
        :type rule_config: :class:`huaweicloudsdkeg.v1.EventStreamingCreateReqRuleConfig`
        :param option: 
        :type option: :class:`huaweicloudsdkeg.v1.RunOption`
        """
        
        

        self._name = None
        self._description = None
        self._source = None
        self._sink = None
        self._rule_config = None
        self._option = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.source = source
        self.sink = sink
        if rule_config is not None:
            self.rule_config = rule_config
        if option is not None:
            self.option = option

    @property
    def name(self):
        r"""Gets the name of this EventStreamingCreateReq.

        事件流名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头

        :return: The name of this EventStreamingCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EventStreamingCreateReq.

        事件流名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头

        :param name: The name of this EventStreamingCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EventStreamingCreateReq.

        事件流描述

        :return: The description of this EventStreamingCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EventStreamingCreateReq.

        事件流描述

        :param description: The description of this EventStreamingCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def source(self):
        r"""Gets the source of this EventStreamingCreateReq.

        :return: The source of this EventStreamingCreateReq.
        :rtype: :class:`huaweicloudsdkeg.v1.EventStreamingSource`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this EventStreamingCreateReq.

        :param source: The source of this EventStreamingCreateReq.
        :type source: :class:`huaweicloudsdkeg.v1.EventStreamingSource`
        """
        self._source = source

    @property
    def sink(self):
        r"""Gets the sink of this EventStreamingCreateReq.

        :return: The sink of this EventStreamingCreateReq.
        :rtype: :class:`huaweicloudsdkeg.v1.EventStreamingSink`
        """
        return self._sink

    @sink.setter
    def sink(self, sink):
        r"""Sets the sink of this EventStreamingCreateReq.

        :param sink: The sink of this EventStreamingCreateReq.
        :type sink: :class:`huaweicloudsdkeg.v1.EventStreamingSink`
        """
        self._sink = sink

    @property
    def rule_config(self):
        r"""Gets the rule_config of this EventStreamingCreateReq.

        :return: The rule_config of this EventStreamingCreateReq.
        :rtype: :class:`huaweicloudsdkeg.v1.EventStreamingCreateReqRuleConfig`
        """
        return self._rule_config

    @rule_config.setter
    def rule_config(self, rule_config):
        r"""Sets the rule_config of this EventStreamingCreateReq.

        :param rule_config: The rule_config of this EventStreamingCreateReq.
        :type rule_config: :class:`huaweicloudsdkeg.v1.EventStreamingCreateReqRuleConfig`
        """
        self._rule_config = rule_config

    @property
    def option(self):
        r"""Gets the option of this EventStreamingCreateReq.

        :return: The option of this EventStreamingCreateReq.
        :rtype: :class:`huaweicloudsdkeg.v1.RunOption`
        """
        return self._option

    @option.setter
    def option(self, option):
        r"""Sets the option of this EventStreamingCreateReq.

        :param option: The option of this EventStreamingCreateReq.
        :type option: :class:`huaweicloudsdkeg.v1.RunOption`
        """
        self._option = option

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
        if not isinstance(other, EventStreamingCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
