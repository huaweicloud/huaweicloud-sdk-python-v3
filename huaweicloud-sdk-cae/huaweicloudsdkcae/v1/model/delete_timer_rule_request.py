# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTimerRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_enterprise_project_id': 'str',
        'x_environment_id': 'str',
        'timer_rule_id': 'str'
    }

    attribute_map = {
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'x_environment_id': 'X-Environment-ID',
        'timer_rule_id': 'timer_rule_id'
    }

    def __init__(self, x_enterprise_project_id=None, x_environment_id=None, timer_rule_id=None):
        r"""DeleteTimerRuleRequest

        The model defined in huaweicloud sdk

        :param x_enterprise_project_id: 企业项目ID。  - 创建环境时，环境会绑定企业项目ID。      - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。     - 该字段不传（或传为字符串“0”）时，则查询默认企业项目下的资源。  &gt; 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。
        :type x_enterprise_project_id: str
        :param x_environment_id: 环境ID。      - 获取环境ID，通过《[云应用引擎API参考](https://support.huaweicloud.com/api-cae/ListEnvironments.html)》的“获取环境列表”章节获取环境信息。     - 请求响应成功后在响应体的items数组中的一个元素即为一个环境的信息，其中id字段即是环境ID。
        :type x_environment_id: str
        :param timer_rule_id: 定时启停规则ID。
        :type timer_rule_id: str
        """
        
        

        self._x_enterprise_project_id = None
        self._x_environment_id = None
        self._timer_rule_id = None
        self.discriminator = None

        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id
        self.x_environment_id = x_environment_id
        self.timer_rule_id = timer_rule_id

    @property
    def x_enterprise_project_id(self):
        r"""Gets the x_enterprise_project_id of this DeleteTimerRuleRequest.

        企业项目ID。  - 创建环境时，环境会绑定企业项目ID。      - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。     - 该字段不传（或传为字符串“0”）时，则查询默认企业项目下的资源。  > 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。

        :return: The x_enterprise_project_id of this DeleteTimerRuleRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        r"""Sets the x_enterprise_project_id of this DeleteTimerRuleRequest.

        企业项目ID。  - 创建环境时，环境会绑定企业项目ID。      - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。     - 该字段不传（或传为字符串“0”）时，则查询默认企业项目下的资源。  > 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。

        :param x_enterprise_project_id: The x_enterprise_project_id of this DeleteTimerRuleRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def x_environment_id(self):
        r"""Gets the x_environment_id of this DeleteTimerRuleRequest.

        环境ID。      - 获取环境ID，通过《[云应用引擎API参考](https://support.huaweicloud.com/api-cae/ListEnvironments.html)》的“获取环境列表”章节获取环境信息。     - 请求响应成功后在响应体的items数组中的一个元素即为一个环境的信息，其中id字段即是环境ID。

        :return: The x_environment_id of this DeleteTimerRuleRequest.
        :rtype: str
        """
        return self._x_environment_id

    @x_environment_id.setter
    def x_environment_id(self, x_environment_id):
        r"""Sets the x_environment_id of this DeleteTimerRuleRequest.

        环境ID。      - 获取环境ID，通过《[云应用引擎API参考](https://support.huaweicloud.com/api-cae/ListEnvironments.html)》的“获取环境列表”章节获取环境信息。     - 请求响应成功后在响应体的items数组中的一个元素即为一个环境的信息，其中id字段即是环境ID。

        :param x_environment_id: The x_environment_id of this DeleteTimerRuleRequest.
        :type x_environment_id: str
        """
        self._x_environment_id = x_environment_id

    @property
    def timer_rule_id(self):
        r"""Gets the timer_rule_id of this DeleteTimerRuleRequest.

        定时启停规则ID。

        :return: The timer_rule_id of this DeleteTimerRuleRequest.
        :rtype: str
        """
        return self._timer_rule_id

    @timer_rule_id.setter
    def timer_rule_id(self, timer_rule_id):
        r"""Sets the timer_rule_id of this DeleteTimerRuleRequest.

        定时启停规则ID。

        :param timer_rule_id: The timer_rule_id of this DeleteTimerRuleRequest.
        :type timer_rule_id: str
        """
        self._timer_rule_id = timer_rule_id

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
        if not isinstance(other, DeleteTimerRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
