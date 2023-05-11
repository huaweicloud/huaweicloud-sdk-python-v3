# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Action:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_name': 'str',
        'action_agency': 'str',
        'function': 'str',
        'function_template': 'str',
        'action_template_name': 'str',
        'action_template_category': 'str',
        'action_template_provider_name': 'str',
        'invocation_mode': 'str',
        'timeout': 'int',
        'payload_filter': 'str',
        'dynamic_source': 'dict(str, object)',
        'results': 'list[ActionResult]'
    }

    attribute_map = {
        'action_name': 'action_name',
        'action_agency': 'action_agency',
        'function': 'function',
        'function_template': 'function_template',
        'action_template_name': 'action_template_name',
        'action_template_category': 'action_template_category',
        'action_template_provider_name': 'action_template_provider_name',
        'invocation_mode': 'invocation_mode',
        'timeout': 'timeout',
        'payload_filter': 'payload_filter',
        'dynamic_source': 'dynamic_source',
        'results': 'results'
    }

    def __init__(self, action_name=None, action_agency=None, function=None, function_template=None, action_template_name=None, action_template_category=None, action_template_provider_name=None, invocation_mode=None, timeout=None, payload_filter=None, dynamic_source=None, results=None):
        """Action

        The model defined in huaweicloud sdk

        :param action_name: 节点名称
        :type action_name: str
        :param action_agency: 节点使用的委托
        :type action_agency: str
        :param function: 节点相关联的函数URN
        :type function: str
        :param function_template: 算子模板使用的URM
        :type function_template: str
        :param action_template_name: 节点使用的算子名称
        :type action_template_name: str
        :param action_template_category: 节点使用的模板类别
        :type action_template_category: str
        :param action_template_provider_name: 节点使用的模板提供方
        :type action_template_provider_name: str
        :param invocation_mode: 触发模式
        :type invocation_mode: str
        :param timeout: 超时时间
        :type timeout: int
        :param payload_filter: 动态参数与inputs参数相关联使用的filter。默认为\&quot;$\&quot;
        :type payload_filter: str
        :param dynamic_source: 节点使用的动态参数
        :type dynamic_source: dict(str, object)
        :param results: action错误处理
        :type results: list[:class:`huaweicloudsdkdwr.v3.ActionResult`]
        """
        
        

        self._action_name = None
        self._action_agency = None
        self._function = None
        self._function_template = None
        self._action_template_name = None
        self._action_template_category = None
        self._action_template_provider_name = None
        self._invocation_mode = None
        self._timeout = None
        self._payload_filter = None
        self._dynamic_source = None
        self._results = None
        self.discriminator = None

        self.action_name = action_name
        self.action_agency = action_agency
        self.function = function
        self.function_template = function_template
        if action_template_name is not None:
            self.action_template_name = action_template_name
        if action_template_category is not None:
            self.action_template_category = action_template_category
        if action_template_provider_name is not None:
            self.action_template_provider_name = action_template_provider_name
        self.invocation_mode = invocation_mode
        self.timeout = timeout
        if payload_filter is not None:
            self.payload_filter = payload_filter
        self.dynamic_source = dynamic_source
        if results is not None:
            self.results = results

    @property
    def action_name(self):
        """Gets the action_name of this Action.

        节点名称

        :return: The action_name of this Action.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this Action.

        节点名称

        :param action_name: The action_name of this Action.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def action_agency(self):
        """Gets the action_agency of this Action.

        节点使用的委托

        :return: The action_agency of this Action.
        :rtype: str
        """
        return self._action_agency

    @action_agency.setter
    def action_agency(self, action_agency):
        """Sets the action_agency of this Action.

        节点使用的委托

        :param action_agency: The action_agency of this Action.
        :type action_agency: str
        """
        self._action_agency = action_agency

    @property
    def function(self):
        """Gets the function of this Action.

        节点相关联的函数URN

        :return: The function of this Action.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this Action.

        节点相关联的函数URN

        :param function: The function of this Action.
        :type function: str
        """
        self._function = function

    @property
    def function_template(self):
        """Gets the function_template of this Action.

        算子模板使用的URM

        :return: The function_template of this Action.
        :rtype: str
        """
        return self._function_template

    @function_template.setter
    def function_template(self, function_template):
        """Sets the function_template of this Action.

        算子模板使用的URM

        :param function_template: The function_template of this Action.
        :type function_template: str
        """
        self._function_template = function_template

    @property
    def action_template_name(self):
        """Gets the action_template_name of this Action.

        节点使用的算子名称

        :return: The action_template_name of this Action.
        :rtype: str
        """
        return self._action_template_name

    @action_template_name.setter
    def action_template_name(self, action_template_name):
        """Sets the action_template_name of this Action.

        节点使用的算子名称

        :param action_template_name: The action_template_name of this Action.
        :type action_template_name: str
        """
        self._action_template_name = action_template_name

    @property
    def action_template_category(self):
        """Gets the action_template_category of this Action.

        节点使用的模板类别

        :return: The action_template_category of this Action.
        :rtype: str
        """
        return self._action_template_category

    @action_template_category.setter
    def action_template_category(self, action_template_category):
        """Sets the action_template_category of this Action.

        节点使用的模板类别

        :param action_template_category: The action_template_category of this Action.
        :type action_template_category: str
        """
        self._action_template_category = action_template_category

    @property
    def action_template_provider_name(self):
        """Gets the action_template_provider_name of this Action.

        节点使用的模板提供方

        :return: The action_template_provider_name of this Action.
        :rtype: str
        """
        return self._action_template_provider_name

    @action_template_provider_name.setter
    def action_template_provider_name(self, action_template_provider_name):
        """Sets the action_template_provider_name of this Action.

        节点使用的模板提供方

        :param action_template_provider_name: The action_template_provider_name of this Action.
        :type action_template_provider_name: str
        """
        self._action_template_provider_name = action_template_provider_name

    @property
    def invocation_mode(self):
        """Gets the invocation_mode of this Action.

        触发模式

        :return: The invocation_mode of this Action.
        :rtype: str
        """
        return self._invocation_mode

    @invocation_mode.setter
    def invocation_mode(self, invocation_mode):
        """Sets the invocation_mode of this Action.

        触发模式

        :param invocation_mode: The invocation_mode of this Action.
        :type invocation_mode: str
        """
        self._invocation_mode = invocation_mode

    @property
    def timeout(self):
        """Gets the timeout of this Action.

        超时时间

        :return: The timeout of this Action.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Action.

        超时时间

        :param timeout: The timeout of this Action.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def payload_filter(self):
        """Gets the payload_filter of this Action.

        动态参数与inputs参数相关联使用的filter。默认为\"$\"

        :return: The payload_filter of this Action.
        :rtype: str
        """
        return self._payload_filter

    @payload_filter.setter
    def payload_filter(self, payload_filter):
        """Sets the payload_filter of this Action.

        动态参数与inputs参数相关联使用的filter。默认为\"$\"

        :param payload_filter: The payload_filter of this Action.
        :type payload_filter: str
        """
        self._payload_filter = payload_filter

    @property
    def dynamic_source(self):
        """Gets the dynamic_source of this Action.

        节点使用的动态参数

        :return: The dynamic_source of this Action.
        :rtype: dict(str, object)
        """
        return self._dynamic_source

    @dynamic_source.setter
    def dynamic_source(self, dynamic_source):
        """Sets the dynamic_source of this Action.

        节点使用的动态参数

        :param dynamic_source: The dynamic_source of this Action.
        :type dynamic_source: dict(str, object)
        """
        self._dynamic_source = dynamic_source

    @property
    def results(self):
        """Gets the results of this Action.

        action错误处理

        :return: The results of this Action.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.ActionResult`]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this Action.

        action错误处理

        :param results: The results of this Action.
        :type results: list[:class:`huaweicloudsdkdwr.v3.ActionResult`]
        """
        self._results = results

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
        if not isinstance(other, Action):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
