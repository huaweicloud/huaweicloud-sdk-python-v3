# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RiskHandleInfoBaseLineInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_risk_host_num': 'int',
        'config_risk_num': 'int',
        'passed_rate': 'float',
        'beat_rate': 'float',
        'weak_pwd_num': 'int',
        'passed_num': 'int',
        'total_config_risk_num': 'int',
        'version_recommend': 'str'
    }

    attribute_map = {
        'config_risk_host_num': 'config_risk_host_num',
        'config_risk_num': 'config_risk_num',
        'passed_rate': 'passed_rate',
        'beat_rate': 'beat_rate',
        'weak_pwd_num': 'weak_pwd_num',
        'passed_num': 'passed_num',
        'total_config_risk_num': 'total_config_risk_num',
        'version_recommend': 'version_recommend'
    }

    def __init__(self, config_risk_host_num=None, config_risk_num=None, passed_rate=None, beat_rate=None, weak_pwd_num=None, passed_num=None, total_config_risk_num=None, version_recommend=None):
        r"""RiskHandleInfoBaseLineInfo

        The model defined in huaweicloud sdk

        :param config_risk_host_num: **参数解释**: 存在配置风险的主机数 **取值范围**: 最小值0，最大值2147483647 
        :type config_risk_host_num: int
        :param config_risk_num: **参数解释**: 存在的配置风险数 **取值范围**: 最小值0，最大值2147483647 
        :type config_risk_num: int
        :param passed_rate: **参数解释**: 通过率 **取值范围**: 最小值0，最大值1 
        :type passed_rate: float
        :param beat_rate: **参数解释**: 通过率击败的用户率 **取值范围**: 最小值0，最大值1 
        :type beat_rate: float
        :param weak_pwd_num: **参数解释**: 弱口令数 **取值范围**: 最小值0，最大值2147483647 
        :type weak_pwd_num: int
        :param passed_num: **参数解释**: 通过量 **取值范围**: 最小值0，最大值2147483647 
        :type passed_num: int
        :param total_config_risk_num: **参数解释**: 总的风险数 **取值范围**: 最小值0，最大值2147483647 
        :type total_config_risk_num: int
        :param version_recommend: **参数解释**: 推荐版本，只支持企业版 hss.version.enterprise **取值范围**: 字符长度1-32位 
        :type version_recommend: str
        """
        
        

        self._config_risk_host_num = None
        self._config_risk_num = None
        self._passed_rate = None
        self._beat_rate = None
        self._weak_pwd_num = None
        self._passed_num = None
        self._total_config_risk_num = None
        self._version_recommend = None
        self.discriminator = None

        if config_risk_host_num is not None:
            self.config_risk_host_num = config_risk_host_num
        if config_risk_num is not None:
            self.config_risk_num = config_risk_num
        if passed_rate is not None:
            self.passed_rate = passed_rate
        if beat_rate is not None:
            self.beat_rate = beat_rate
        if weak_pwd_num is not None:
            self.weak_pwd_num = weak_pwd_num
        if passed_num is not None:
            self.passed_num = passed_num
        if total_config_risk_num is not None:
            self.total_config_risk_num = total_config_risk_num
        if version_recommend is not None:
            self.version_recommend = version_recommend

    @property
    def config_risk_host_num(self):
        r"""Gets the config_risk_host_num of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 存在配置风险的主机数 **取值范围**: 最小值0，最大值2147483647 

        :return: The config_risk_host_num of this RiskHandleInfoBaseLineInfo.
        :rtype: int
        """
        return self._config_risk_host_num

    @config_risk_host_num.setter
    def config_risk_host_num(self, config_risk_host_num):
        r"""Sets the config_risk_host_num of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 存在配置风险的主机数 **取值范围**: 最小值0，最大值2147483647 

        :param config_risk_host_num: The config_risk_host_num of this RiskHandleInfoBaseLineInfo.
        :type config_risk_host_num: int
        """
        self._config_risk_host_num = config_risk_host_num

    @property
    def config_risk_num(self):
        r"""Gets the config_risk_num of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 存在的配置风险数 **取值范围**: 最小值0，最大值2147483647 

        :return: The config_risk_num of this RiskHandleInfoBaseLineInfo.
        :rtype: int
        """
        return self._config_risk_num

    @config_risk_num.setter
    def config_risk_num(self, config_risk_num):
        r"""Sets the config_risk_num of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 存在的配置风险数 **取值范围**: 最小值0，最大值2147483647 

        :param config_risk_num: The config_risk_num of this RiskHandleInfoBaseLineInfo.
        :type config_risk_num: int
        """
        self._config_risk_num = config_risk_num

    @property
    def passed_rate(self):
        r"""Gets the passed_rate of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 通过率 **取值范围**: 最小值0，最大值1 

        :return: The passed_rate of this RiskHandleInfoBaseLineInfo.
        :rtype: float
        """
        return self._passed_rate

    @passed_rate.setter
    def passed_rate(self, passed_rate):
        r"""Sets the passed_rate of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 通过率 **取值范围**: 最小值0，最大值1 

        :param passed_rate: The passed_rate of this RiskHandleInfoBaseLineInfo.
        :type passed_rate: float
        """
        self._passed_rate = passed_rate

    @property
    def beat_rate(self):
        r"""Gets the beat_rate of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 通过率击败的用户率 **取值范围**: 最小值0，最大值1 

        :return: The beat_rate of this RiskHandleInfoBaseLineInfo.
        :rtype: float
        """
        return self._beat_rate

    @beat_rate.setter
    def beat_rate(self, beat_rate):
        r"""Sets the beat_rate of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 通过率击败的用户率 **取值范围**: 最小值0，最大值1 

        :param beat_rate: The beat_rate of this RiskHandleInfoBaseLineInfo.
        :type beat_rate: float
        """
        self._beat_rate = beat_rate

    @property
    def weak_pwd_num(self):
        r"""Gets the weak_pwd_num of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 弱口令数 **取值范围**: 最小值0，最大值2147483647 

        :return: The weak_pwd_num of this RiskHandleInfoBaseLineInfo.
        :rtype: int
        """
        return self._weak_pwd_num

    @weak_pwd_num.setter
    def weak_pwd_num(self, weak_pwd_num):
        r"""Sets the weak_pwd_num of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 弱口令数 **取值范围**: 最小值0，最大值2147483647 

        :param weak_pwd_num: The weak_pwd_num of this RiskHandleInfoBaseLineInfo.
        :type weak_pwd_num: int
        """
        self._weak_pwd_num = weak_pwd_num

    @property
    def passed_num(self):
        r"""Gets the passed_num of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 通过量 **取值范围**: 最小值0，最大值2147483647 

        :return: The passed_num of this RiskHandleInfoBaseLineInfo.
        :rtype: int
        """
        return self._passed_num

    @passed_num.setter
    def passed_num(self, passed_num):
        r"""Sets the passed_num of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 通过量 **取值范围**: 最小值0，最大值2147483647 

        :param passed_num: The passed_num of this RiskHandleInfoBaseLineInfo.
        :type passed_num: int
        """
        self._passed_num = passed_num

    @property
    def total_config_risk_num(self):
        r"""Gets the total_config_risk_num of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 总的风险数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_config_risk_num of this RiskHandleInfoBaseLineInfo.
        :rtype: int
        """
        return self._total_config_risk_num

    @total_config_risk_num.setter
    def total_config_risk_num(self, total_config_risk_num):
        r"""Sets the total_config_risk_num of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 总的风险数 **取值范围**: 最小值0，最大值2147483647 

        :param total_config_risk_num: The total_config_risk_num of this RiskHandleInfoBaseLineInfo.
        :type total_config_risk_num: int
        """
        self._total_config_risk_num = total_config_risk_num

    @property
    def version_recommend(self):
        r"""Gets the version_recommend of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 推荐版本，只支持企业版 hss.version.enterprise **取值范围**: 字符长度1-32位 

        :return: The version_recommend of this RiskHandleInfoBaseLineInfo.
        :rtype: str
        """
        return self._version_recommend

    @version_recommend.setter
    def version_recommend(self, version_recommend):
        r"""Sets the version_recommend of this RiskHandleInfoBaseLineInfo.

        **参数解释**: 推荐版本，只支持企业版 hss.version.enterprise **取值范围**: 字符长度1-32位 

        :param version_recommend: The version_recommend of this RiskHandleInfoBaseLineInfo.
        :type version_recommend: str
        """
        self._version_recommend = version_recommend

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
        if not isinstance(other, RiskHandleInfoBaseLineInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
