# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRiskConfigCheckRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'check_name': 'str',
        'standard': 'str',
        'result_type': 'str',
        'check_rule_name': 'str',
        'severity': 'str',
        'host_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'check_name': 'check_name',
        'standard': 'standard',
        'result_type': 'result_type',
        'check_rule_name': 'check_rule_name',
        'severity': 'severity',
        'host_id': 'host_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, check_name=None, standard=None, result_type=None, check_rule_name=None, severity=None, host_id=None, limit=None, offset=None):
        r"""ListRiskConfigCheckRulesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param check_name: 配置检查（基线）的名称，例如SSH、CentOS 7、Windows
        :type check_name: str
        :param standard: 标准类型，包含如下: - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准
        :type standard: str
        :param result_type: 结果类型，包含如下： - safe ： 已通过 - unhandled : 未通过，且未忽略的 - ignored : 未通过，且已忽略的
        :type result_type: str
        :param check_rule_name: 检查项（检查规则）名称，支持模糊匹配
        :type check_rule_name: str
        :param severity: 风险等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急
        :type severity: str
        :param host_id: 主机ID，不赋值时，查租户所有主机
        :type host_id: str
        :param limit: 每页数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._check_name = None
        self._standard = None
        self._result_type = None
        self._check_rule_name = None
        self._severity = None
        self._host_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.check_name = check_name
        self.standard = standard
        if result_type is not None:
            self.result_type = result_type
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if severity is not None:
            self.severity = severity
        if host_id is not None:
            self.host_id = host_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListRiskConfigCheckRulesRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListRiskConfigCheckRulesRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListRiskConfigCheckRulesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def check_name(self):
        r"""Gets the check_name of this ListRiskConfigCheckRulesRequest.

        配置检查（基线）的名称，例如SSH、CentOS 7、Windows

        :return: The check_name of this ListRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ListRiskConfigCheckRulesRequest.

        配置检查（基线）的名称，例如SSH、CentOS 7、Windows

        :param check_name: The check_name of this ListRiskConfigCheckRulesRequest.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def standard(self):
        r"""Gets the standard of this ListRiskConfigCheckRulesRequest.

        标准类型，包含如下: - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准

        :return: The standard of this ListRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ListRiskConfigCheckRulesRequest.

        标准类型，包含如下: - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准

        :param standard: The standard of this ListRiskConfigCheckRulesRequest.
        :type standard: str
        """
        self._standard = standard

    @property
    def result_type(self):
        r"""Gets the result_type of this ListRiskConfigCheckRulesRequest.

        结果类型，包含如下： - safe ： 已通过 - unhandled : 未通过，且未忽略的 - ignored : 未通过，且已忽略的

        :return: The result_type of this ListRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        r"""Sets the result_type of this ListRiskConfigCheckRulesRequest.

        结果类型，包含如下： - safe ： 已通过 - unhandled : 未通过，且未忽略的 - ignored : 未通过，且已忽略的

        :param result_type: The result_type of this ListRiskConfigCheckRulesRequest.
        :type result_type: str
        """
        self._result_type = result_type

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this ListRiskConfigCheckRulesRequest.

        检查项（检查规则）名称，支持模糊匹配

        :return: The check_rule_name of this ListRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this ListRiskConfigCheckRulesRequest.

        检查项（检查规则）名称，支持模糊匹配

        :param check_rule_name: The check_rule_name of this ListRiskConfigCheckRulesRequest.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def severity(self):
        r"""Gets the severity of this ListRiskConfigCheckRulesRequest.

        风险等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :return: The severity of this ListRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListRiskConfigCheckRulesRequest.

        风险等级，包含如下:   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :param severity: The severity of this ListRiskConfigCheckRulesRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def host_id(self):
        r"""Gets the host_id of this ListRiskConfigCheckRulesRequest.

        主机ID，不赋值时，查租户所有主机

        :return: The host_id of this ListRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListRiskConfigCheckRulesRequest.

        主机ID，不赋值时，查租户所有主机

        :param host_id: The host_id of this ListRiskConfigCheckRulesRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def limit(self):
        r"""Gets the limit of this ListRiskConfigCheckRulesRequest.

        每页数量

        :return: The limit of this ListRiskConfigCheckRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRiskConfigCheckRulesRequest.

        每页数量

        :param limit: The limit of this ListRiskConfigCheckRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListRiskConfigCheckRulesRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListRiskConfigCheckRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRiskConfigCheckRulesRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListRiskConfigCheckRulesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListRiskConfigCheckRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
