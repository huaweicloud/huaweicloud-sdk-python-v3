# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTrialsStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trial_num': 'int',
        'unprotected_num': 'int',
        'asset': 'int',
        'vulnerability': 'int',
        'intrusion': 'int',
        'baseline': 'int'
    }

    attribute_map = {
        'trial_num': 'trial_num',
        'unprotected_num': 'unprotected_num',
        'asset': 'asset',
        'vulnerability': 'vulnerability',
        'intrusion': 'intrusion',
        'baseline': 'baseline'
    }

    def __init__(self, trial_num=None, unprotected_num=None, asset=None, vulnerability=None, intrusion=None, baseline=None):
        r"""ShowTrialsStatisticsResponse

        The model defined in huaweicloud sdk

        :param trial_num: **参数解释**: 试用主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type trial_num: int
        :param unprotected_num: **参数解释**: 未防护数 **取值范围**: 最小值0，最大值2147483647 
        :type unprotected_num: int
        :param asset: **参数解释**: 资产风险个数 **取值范围**: 最小值0，最大值2147483647 
        :type asset: int
        :param vulnerability: **参数解释**: 漏洞风险个数 **取值范围**: 最小值0，最大值2147483647 
        :type vulnerability: int
        :param intrusion: **参数解释**: 入侵事件个数 **取值范围**: 最小值0，最大值2147483647 
        :type intrusion: int
        :param baseline: **参数解释**: 基线检测风险个数 **取值范围**: 最小值0，最大值2147483647 
        :type baseline: int
        """
        
        super().__init__()

        self._trial_num = None
        self._unprotected_num = None
        self._asset = None
        self._vulnerability = None
        self._intrusion = None
        self._baseline = None
        self.discriminator = None

        if trial_num is not None:
            self.trial_num = trial_num
        if unprotected_num is not None:
            self.unprotected_num = unprotected_num
        if asset is not None:
            self.asset = asset
        if vulnerability is not None:
            self.vulnerability = vulnerability
        if intrusion is not None:
            self.intrusion = intrusion
        if baseline is not None:
            self.baseline = baseline

    @property
    def trial_num(self):
        r"""Gets the trial_num of this ShowTrialsStatisticsResponse.

        **参数解释**: 试用主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The trial_num of this ShowTrialsStatisticsResponse.
        :rtype: int
        """
        return self._trial_num

    @trial_num.setter
    def trial_num(self, trial_num):
        r"""Sets the trial_num of this ShowTrialsStatisticsResponse.

        **参数解释**: 试用主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param trial_num: The trial_num of this ShowTrialsStatisticsResponse.
        :type trial_num: int
        """
        self._trial_num = trial_num

    @property
    def unprotected_num(self):
        r"""Gets the unprotected_num of this ShowTrialsStatisticsResponse.

        **参数解释**: 未防护数 **取值范围**: 最小值0，最大值2147483647 

        :return: The unprotected_num of this ShowTrialsStatisticsResponse.
        :rtype: int
        """
        return self._unprotected_num

    @unprotected_num.setter
    def unprotected_num(self, unprotected_num):
        r"""Sets the unprotected_num of this ShowTrialsStatisticsResponse.

        **参数解释**: 未防护数 **取值范围**: 最小值0，最大值2147483647 

        :param unprotected_num: The unprotected_num of this ShowTrialsStatisticsResponse.
        :type unprotected_num: int
        """
        self._unprotected_num = unprotected_num

    @property
    def asset(self):
        r"""Gets the asset of this ShowTrialsStatisticsResponse.

        **参数解释**: 资产风险个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The asset of this ShowTrialsStatisticsResponse.
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        r"""Sets the asset of this ShowTrialsStatisticsResponse.

        **参数解释**: 资产风险个数 **取值范围**: 最小值0，最大值2147483647 

        :param asset: The asset of this ShowTrialsStatisticsResponse.
        :type asset: int
        """
        self._asset = asset

    @property
    def vulnerability(self):
        r"""Gets the vulnerability of this ShowTrialsStatisticsResponse.

        **参数解释**: 漏洞风险个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The vulnerability of this ShowTrialsStatisticsResponse.
        :rtype: int
        """
        return self._vulnerability

    @vulnerability.setter
    def vulnerability(self, vulnerability):
        r"""Sets the vulnerability of this ShowTrialsStatisticsResponse.

        **参数解释**: 漏洞风险个数 **取值范围**: 最小值0，最大值2147483647 

        :param vulnerability: The vulnerability of this ShowTrialsStatisticsResponse.
        :type vulnerability: int
        """
        self._vulnerability = vulnerability

    @property
    def intrusion(self):
        r"""Gets the intrusion of this ShowTrialsStatisticsResponse.

        **参数解释**: 入侵事件个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The intrusion of this ShowTrialsStatisticsResponse.
        :rtype: int
        """
        return self._intrusion

    @intrusion.setter
    def intrusion(self, intrusion):
        r"""Sets the intrusion of this ShowTrialsStatisticsResponse.

        **参数解释**: 入侵事件个数 **取值范围**: 最小值0，最大值2147483647 

        :param intrusion: The intrusion of this ShowTrialsStatisticsResponse.
        :type intrusion: int
        """
        self._intrusion = intrusion

    @property
    def baseline(self):
        r"""Gets the baseline of this ShowTrialsStatisticsResponse.

        **参数解释**: 基线检测风险个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The baseline of this ShowTrialsStatisticsResponse.
        :rtype: int
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this ShowTrialsStatisticsResponse.

        **参数解释**: 基线检测风险个数 **取值范围**: 最小值0，最大值2147483647 

        :param baseline: The baseline of this ShowTrialsStatisticsResponse.
        :type baseline: int
        """
        self._baseline = baseline

    def to_dict(self):
        import warnings
        warnings.warn("ShowTrialsStatisticsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowTrialsStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
