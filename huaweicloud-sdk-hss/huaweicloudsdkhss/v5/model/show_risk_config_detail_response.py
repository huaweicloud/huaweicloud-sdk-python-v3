# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRiskConfigDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'severity': 'str',
        'check_type': 'str',
        'check_type_desc': 'str',
        'check_rule_num': 'int',
        'failed_rule_num': 'int',
        'passed_rule_num': 'int',
        'ignored_rule_num': 'int',
        'host_num': 'int'
    }

    attribute_map = {
        'severity': 'severity',
        'check_type': 'check_type',
        'check_type_desc': 'check_type_desc',
        'check_rule_num': 'check_rule_num',
        'failed_rule_num': 'failed_rule_num',
        'passed_rule_num': 'passed_rule_num',
        'ignored_rule_num': 'ignored_rule_num',
        'host_num': 'host_num'
    }

    def __init__(self, severity=None, check_type=None, check_type_desc=None, check_rule_num=None, failed_rule_num=None, passed_rule_num=None, ignored_rule_num=None, host_num=None):
        r"""ShowRiskConfigDetailResponse

        The model defined in huaweicloud sdk

        :param severity: 风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危
        :type severity: str
        :param check_type: 配置检查（基线）的类型,例如SSH、CentOS 7、Windows Server 2019 R2、Windows Server 2016 R2、MySQL5-Windows
        :type check_type: str
        :param check_type_desc: 对配置检查（基线）类型的描述信息，概括当前基线包含的检查项是根据什么标准制定的，能够审计哪些方面的问题。
        :type check_type_desc: str
        :param check_rule_num: 当前配置检查（基线）类型下，用户共检测了多少个检查项。例如标准类型为hw_standard的SSH基线，主机安全提供了17个检查项，但用户所有主机都只检测了SSH基线的其中5个检查项，check_rule_num就是5。用户有一台主机进行了全量检查项检测，check_rule_num就是17。
        :type check_rule_num: int
        :param failed_rule_num: 未通过的检查项数量，check_rule_num中只要有一台主机没通过某个检查项，这个检查项就会被计算在failed_rule_num中
        :type failed_rule_num: int
        :param passed_rule_num: 已通过的检查项数量，check_rule_num中只要有一台主机通过了某个检查项，这个检查项就会被计算在passed_rule_num中
        :type passed_rule_num: int
        :param ignored_rule_num: 已忽略的检查项数量，check_rule_num中只要有一台主机忽略了某个检查项，这个检查项就会被计算在ignored_rule_num中
        :type ignored_rule_num: int
        :param host_num: 受影响的服务器的数量，进行了当前基线检测的服务器数量
        :type host_num: int
        """
        
        super(ShowRiskConfigDetailResponse, self).__init__()

        self._severity = None
        self._check_type = None
        self._check_type_desc = None
        self._check_rule_num = None
        self._failed_rule_num = None
        self._passed_rule_num = None
        self._ignored_rule_num = None
        self._host_num = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if check_type is not None:
            self.check_type = check_type
        if check_type_desc is not None:
            self.check_type_desc = check_type_desc
        if check_rule_num is not None:
            self.check_rule_num = check_rule_num
        if failed_rule_num is not None:
            self.failed_rule_num = failed_rule_num
        if passed_rule_num is not None:
            self.passed_rule_num = passed_rule_num
        if ignored_rule_num is not None:
            self.ignored_rule_num = ignored_rule_num
        if host_num is not None:
            self.host_num = host_num

    @property
    def severity(self):
        r"""Gets the severity of this ShowRiskConfigDetailResponse.

        风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危

        :return: The severity of this ShowRiskConfigDetailResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ShowRiskConfigDetailResponse.

        风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危

        :param severity: The severity of this ShowRiskConfigDetailResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def check_type(self):
        r"""Gets the check_type of this ShowRiskConfigDetailResponse.

        配置检查（基线）的类型,例如SSH、CentOS 7、Windows Server 2019 R2、Windows Server 2016 R2、MySQL5-Windows

        :return: The check_type of this ShowRiskConfigDetailResponse.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this ShowRiskConfigDetailResponse.

        配置检查（基线）的类型,例如SSH、CentOS 7、Windows Server 2019 R2、Windows Server 2016 R2、MySQL5-Windows

        :param check_type: The check_type of this ShowRiskConfigDetailResponse.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def check_type_desc(self):
        r"""Gets the check_type_desc of this ShowRiskConfigDetailResponse.

        对配置检查（基线）类型的描述信息，概括当前基线包含的检查项是根据什么标准制定的，能够审计哪些方面的问题。

        :return: The check_type_desc of this ShowRiskConfigDetailResponse.
        :rtype: str
        """
        return self._check_type_desc

    @check_type_desc.setter
    def check_type_desc(self, check_type_desc):
        r"""Sets the check_type_desc of this ShowRiskConfigDetailResponse.

        对配置检查（基线）类型的描述信息，概括当前基线包含的检查项是根据什么标准制定的，能够审计哪些方面的问题。

        :param check_type_desc: The check_type_desc of this ShowRiskConfigDetailResponse.
        :type check_type_desc: str
        """
        self._check_type_desc = check_type_desc

    @property
    def check_rule_num(self):
        r"""Gets the check_rule_num of this ShowRiskConfigDetailResponse.

        当前配置检查（基线）类型下，用户共检测了多少个检查项。例如标准类型为hw_standard的SSH基线，主机安全提供了17个检查项，但用户所有主机都只检测了SSH基线的其中5个检查项，check_rule_num就是5。用户有一台主机进行了全量检查项检测，check_rule_num就是17。

        :return: The check_rule_num of this ShowRiskConfigDetailResponse.
        :rtype: int
        """
        return self._check_rule_num

    @check_rule_num.setter
    def check_rule_num(self, check_rule_num):
        r"""Sets the check_rule_num of this ShowRiskConfigDetailResponse.

        当前配置检查（基线）类型下，用户共检测了多少个检查项。例如标准类型为hw_standard的SSH基线，主机安全提供了17个检查项，但用户所有主机都只检测了SSH基线的其中5个检查项，check_rule_num就是5。用户有一台主机进行了全量检查项检测，check_rule_num就是17。

        :param check_rule_num: The check_rule_num of this ShowRiskConfigDetailResponse.
        :type check_rule_num: int
        """
        self._check_rule_num = check_rule_num

    @property
    def failed_rule_num(self):
        r"""Gets the failed_rule_num of this ShowRiskConfigDetailResponse.

        未通过的检查项数量，check_rule_num中只要有一台主机没通过某个检查项，这个检查项就会被计算在failed_rule_num中

        :return: The failed_rule_num of this ShowRiskConfigDetailResponse.
        :rtype: int
        """
        return self._failed_rule_num

    @failed_rule_num.setter
    def failed_rule_num(self, failed_rule_num):
        r"""Sets the failed_rule_num of this ShowRiskConfigDetailResponse.

        未通过的检查项数量，check_rule_num中只要有一台主机没通过某个检查项，这个检查项就会被计算在failed_rule_num中

        :param failed_rule_num: The failed_rule_num of this ShowRiskConfigDetailResponse.
        :type failed_rule_num: int
        """
        self._failed_rule_num = failed_rule_num

    @property
    def passed_rule_num(self):
        r"""Gets the passed_rule_num of this ShowRiskConfigDetailResponse.

        已通过的检查项数量，check_rule_num中只要有一台主机通过了某个检查项，这个检查项就会被计算在passed_rule_num中

        :return: The passed_rule_num of this ShowRiskConfigDetailResponse.
        :rtype: int
        """
        return self._passed_rule_num

    @passed_rule_num.setter
    def passed_rule_num(self, passed_rule_num):
        r"""Sets the passed_rule_num of this ShowRiskConfigDetailResponse.

        已通过的检查项数量，check_rule_num中只要有一台主机通过了某个检查项，这个检查项就会被计算在passed_rule_num中

        :param passed_rule_num: The passed_rule_num of this ShowRiskConfigDetailResponse.
        :type passed_rule_num: int
        """
        self._passed_rule_num = passed_rule_num

    @property
    def ignored_rule_num(self):
        r"""Gets the ignored_rule_num of this ShowRiskConfigDetailResponse.

        已忽略的检查项数量，check_rule_num中只要有一台主机忽略了某个检查项，这个检查项就会被计算在ignored_rule_num中

        :return: The ignored_rule_num of this ShowRiskConfigDetailResponse.
        :rtype: int
        """
        return self._ignored_rule_num

    @ignored_rule_num.setter
    def ignored_rule_num(self, ignored_rule_num):
        r"""Sets the ignored_rule_num of this ShowRiskConfigDetailResponse.

        已忽略的检查项数量，check_rule_num中只要有一台主机忽略了某个检查项，这个检查项就会被计算在ignored_rule_num中

        :param ignored_rule_num: The ignored_rule_num of this ShowRiskConfigDetailResponse.
        :type ignored_rule_num: int
        """
        self._ignored_rule_num = ignored_rule_num

    @property
    def host_num(self):
        r"""Gets the host_num of this ShowRiskConfigDetailResponse.

        受影响的服务器的数量，进行了当前基线检测的服务器数量

        :return: The host_num of this ShowRiskConfigDetailResponse.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ShowRiskConfigDetailResponse.

        受影响的服务器的数量，进行了当前基线检测的服务器数量

        :param host_num: The host_num of this ShowRiskConfigDetailResponse.
        :type host_num: int
        """
        self._host_num = host_num

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
        if not isinstance(other, ShowRiskConfigDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
