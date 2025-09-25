# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityRiskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_risk': 'AlarmRiskInfo',
        'baseline_risk': 'SecurityRiskResponseBaselineRisk',
        'asset_risk': 'SecurityRiskResponseAssetRisk',
        'security_protect_risk': 'SecurityRiskResponseSecurityProtectRisk',
        'vul_risk': 'SecurityRiskResponseVulRisk',
        'image_risk': 'SecurityRiskResponseImageRisk',
        'total_risk_num': 'int'
    }

    attribute_map = {
        'alarm_risk': 'alarm_risk',
        'baseline_risk': 'baseline_risk',
        'asset_risk': 'asset_risk',
        'security_protect_risk': 'security_protect_risk',
        'vul_risk': 'vul_risk',
        'image_risk': 'image_risk',
        'total_risk_num': 'total_risk_num'
    }

    def __init__(self, alarm_risk=None, baseline_risk=None, asset_risk=None, security_protect_risk=None, vul_risk=None, image_risk=None, total_risk_num=None):
        r"""ListSecurityRiskResponse

        The model defined in huaweicloud sdk

        :param alarm_risk: 
        :type alarm_risk: :class:`huaweicloudsdkhss.v5.AlarmRiskInfo`
        :param baseline_risk: 
        :type baseline_risk: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseBaselineRisk`
        :param asset_risk: 
        :type asset_risk: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseAssetRisk`
        :param security_protect_risk: 
        :type security_protect_risk: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseSecurityProtectRisk`
        :param vul_risk: 
        :type vul_risk: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseVulRisk`
        :param image_risk: 
        :type image_risk: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseImageRisk`
        :param total_risk_num: **参数解释**： 总风险数量 **取值范围**: 最小值0，最大值2147483647 
        :type total_risk_num: int
        """
        
        super(ListSecurityRiskResponse, self).__init__()

        self._alarm_risk = None
        self._baseline_risk = None
        self._asset_risk = None
        self._security_protect_risk = None
        self._vul_risk = None
        self._image_risk = None
        self._total_risk_num = None
        self.discriminator = None

        if alarm_risk is not None:
            self.alarm_risk = alarm_risk
        if baseline_risk is not None:
            self.baseline_risk = baseline_risk
        if asset_risk is not None:
            self.asset_risk = asset_risk
        if security_protect_risk is not None:
            self.security_protect_risk = security_protect_risk
        if vul_risk is not None:
            self.vul_risk = vul_risk
        if image_risk is not None:
            self.image_risk = image_risk
        if total_risk_num is not None:
            self.total_risk_num = total_risk_num

    @property
    def alarm_risk(self):
        r"""Gets the alarm_risk of this ListSecurityRiskResponse.

        :return: The alarm_risk of this ListSecurityRiskResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.AlarmRiskInfo`
        """
        return self._alarm_risk

    @alarm_risk.setter
    def alarm_risk(self, alarm_risk):
        r"""Sets the alarm_risk of this ListSecurityRiskResponse.

        :param alarm_risk: The alarm_risk of this ListSecurityRiskResponse.
        :type alarm_risk: :class:`huaweicloudsdkhss.v5.AlarmRiskInfo`
        """
        self._alarm_risk = alarm_risk

    @property
    def baseline_risk(self):
        r"""Gets the baseline_risk of this ListSecurityRiskResponse.

        :return: The baseline_risk of this ListSecurityRiskResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseBaselineRisk`
        """
        return self._baseline_risk

    @baseline_risk.setter
    def baseline_risk(self, baseline_risk):
        r"""Sets the baseline_risk of this ListSecurityRiskResponse.

        :param baseline_risk: The baseline_risk of this ListSecurityRiskResponse.
        :type baseline_risk: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseBaselineRisk`
        """
        self._baseline_risk = baseline_risk

    @property
    def asset_risk(self):
        r"""Gets the asset_risk of this ListSecurityRiskResponse.

        :return: The asset_risk of this ListSecurityRiskResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseAssetRisk`
        """
        return self._asset_risk

    @asset_risk.setter
    def asset_risk(self, asset_risk):
        r"""Sets the asset_risk of this ListSecurityRiskResponse.

        :param asset_risk: The asset_risk of this ListSecurityRiskResponse.
        :type asset_risk: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseAssetRisk`
        """
        self._asset_risk = asset_risk

    @property
    def security_protect_risk(self):
        r"""Gets the security_protect_risk of this ListSecurityRiskResponse.

        :return: The security_protect_risk of this ListSecurityRiskResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseSecurityProtectRisk`
        """
        return self._security_protect_risk

    @security_protect_risk.setter
    def security_protect_risk(self, security_protect_risk):
        r"""Sets the security_protect_risk of this ListSecurityRiskResponse.

        :param security_protect_risk: The security_protect_risk of this ListSecurityRiskResponse.
        :type security_protect_risk: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseSecurityProtectRisk`
        """
        self._security_protect_risk = security_protect_risk

    @property
    def vul_risk(self):
        r"""Gets the vul_risk of this ListSecurityRiskResponse.

        :return: The vul_risk of this ListSecurityRiskResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseVulRisk`
        """
        return self._vul_risk

    @vul_risk.setter
    def vul_risk(self, vul_risk):
        r"""Sets the vul_risk of this ListSecurityRiskResponse.

        :param vul_risk: The vul_risk of this ListSecurityRiskResponse.
        :type vul_risk: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseVulRisk`
        """
        self._vul_risk = vul_risk

    @property
    def image_risk(self):
        r"""Gets the image_risk of this ListSecurityRiskResponse.

        :return: The image_risk of this ListSecurityRiskResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseImageRisk`
        """
        return self._image_risk

    @image_risk.setter
    def image_risk(self, image_risk):
        r"""Sets the image_risk of this ListSecurityRiskResponse.

        :param image_risk: The image_risk of this ListSecurityRiskResponse.
        :type image_risk: :class:`huaweicloudsdkhss.v5.SecurityRiskResponseImageRisk`
        """
        self._image_risk = image_risk

    @property
    def total_risk_num(self):
        r"""Gets the total_risk_num of this ListSecurityRiskResponse.

        **参数解释**： 总风险数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_risk_num of this ListSecurityRiskResponse.
        :rtype: int
        """
        return self._total_risk_num

    @total_risk_num.setter
    def total_risk_num(self, total_risk_num):
        r"""Sets the total_risk_num of this ListSecurityRiskResponse.

        **参数解释**： 总风险数量 **取值范围**: 最小值0，最大值2147483647 

        :param total_risk_num: The total_risk_num of this ListSecurityRiskResponse.
        :type total_risk_num: int
        """
        self._total_risk_num = total_risk_num

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
        if not isinstance(other, ListSecurityRiskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
