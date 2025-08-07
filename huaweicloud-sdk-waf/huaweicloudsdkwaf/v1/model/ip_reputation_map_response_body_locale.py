# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpReputationMapResponseBodyLocale:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dr_peng': 'str',
        'google': 'str',
        'tencent': 'str',
        'mei_tuan': 'str',
        'microsoft': 'str',
        'ali_cloud': 'str',
        'amazon': 'str',
        'vnet': 'str',
        'hw': 'str'
    }

    attribute_map = {
        'dr_peng': 'Dr.Peng',
        'google': 'Google',
        'tencent': 'Tencent',
        'mei_tuan': 'MeiTuan',
        'microsoft': 'Microsoft',
        'ali_cloud': 'AliCloud',
        'amazon': 'Amazon',
        'vnet': 'VNET',
        'hw': 'HW'
    }

    def __init__(self, dr_peng=None, google=None, tencent=None, mei_tuan=None, microsoft=None, ali_cloud=None, amazon=None, vnet=None, hw=None):
        r"""IpReputationMapResponseBodyLocale

        The model defined in huaweicloud sdk

        :param dr_peng: **参数解释：** 鹏博士，一家提供互联网数据中心、云计算等服务的企业 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type dr_peng: str
        :param google: **参数解释：** 谷歌公司，全球知名的科技企业，提供搜索引擎、云计算等服务 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type google: str
        :param tencent: **参数解释：** 腾讯，中国知名的互联网企业，提供社交、游戏、金融等服务 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tencent: str
        :param mei_tuan: **参数解释：** 美团网，中国领先的生活服务电子商务平台 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type mei_tuan: str
        :param microsoft: **参数解释：** 微软公司，全球知名的科技企业，提供操作系统、办公软件等服务 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type microsoft: str
        :param ali_cloud: **参数解释：** 阿里云，阿里巴巴集团旗下的云计算品牌 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ali_cloud: str
        :param amazon: **参数解释：** 亚马逊，全球知名的电子商务和云计算企业 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type amazon: str
        :param vnet: **参数解释：** 世纪互联，中国领先的电信中立互联网基础设施服务提供商 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type vnet: str
        :param hw: **参数解释：** 华为，全球知名的通信技术企业 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type hw: str
        """
        
        

        self._dr_peng = None
        self._google = None
        self._tencent = None
        self._mei_tuan = None
        self._microsoft = None
        self._ali_cloud = None
        self._amazon = None
        self._vnet = None
        self._hw = None
        self.discriminator = None

        if dr_peng is not None:
            self.dr_peng = dr_peng
        if google is not None:
            self.google = google
        if tencent is not None:
            self.tencent = tencent
        if mei_tuan is not None:
            self.mei_tuan = mei_tuan
        if microsoft is not None:
            self.microsoft = microsoft
        if ali_cloud is not None:
            self.ali_cloud = ali_cloud
        if amazon is not None:
            self.amazon = amazon
        if vnet is not None:
            self.vnet = vnet
        if hw is not None:
            self.hw = hw

    @property
    def dr_peng(self):
        r"""Gets the dr_peng of this IpReputationMapResponseBodyLocale.

        **参数解释：** 鹏博士，一家提供互联网数据中心、云计算等服务的企业 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The dr_peng of this IpReputationMapResponseBodyLocale.
        :rtype: str
        """
        return self._dr_peng

    @dr_peng.setter
    def dr_peng(self, dr_peng):
        r"""Sets the dr_peng of this IpReputationMapResponseBodyLocale.

        **参数解释：** 鹏博士，一家提供互联网数据中心、云计算等服务的企业 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param dr_peng: The dr_peng of this IpReputationMapResponseBodyLocale.
        :type dr_peng: str
        """
        self._dr_peng = dr_peng

    @property
    def google(self):
        r"""Gets the google of this IpReputationMapResponseBodyLocale.

        **参数解释：** 谷歌公司，全球知名的科技企业，提供搜索引擎、云计算等服务 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The google of this IpReputationMapResponseBodyLocale.
        :rtype: str
        """
        return self._google

    @google.setter
    def google(self, google):
        r"""Sets the google of this IpReputationMapResponseBodyLocale.

        **参数解释：** 谷歌公司，全球知名的科技企业，提供搜索引擎、云计算等服务 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param google: The google of this IpReputationMapResponseBodyLocale.
        :type google: str
        """
        self._google = google

    @property
    def tencent(self):
        r"""Gets the tencent of this IpReputationMapResponseBodyLocale.

        **参数解释：** 腾讯，中国知名的互联网企业，提供社交、游戏、金融等服务 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tencent of this IpReputationMapResponseBodyLocale.
        :rtype: str
        """
        return self._tencent

    @tencent.setter
    def tencent(self, tencent):
        r"""Sets the tencent of this IpReputationMapResponseBodyLocale.

        **参数解释：** 腾讯，中国知名的互联网企业，提供社交、游戏、金融等服务 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tencent: The tencent of this IpReputationMapResponseBodyLocale.
        :type tencent: str
        """
        self._tencent = tencent

    @property
    def mei_tuan(self):
        r"""Gets the mei_tuan of this IpReputationMapResponseBodyLocale.

        **参数解释：** 美团网，中国领先的生活服务电子商务平台 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The mei_tuan of this IpReputationMapResponseBodyLocale.
        :rtype: str
        """
        return self._mei_tuan

    @mei_tuan.setter
    def mei_tuan(self, mei_tuan):
        r"""Sets the mei_tuan of this IpReputationMapResponseBodyLocale.

        **参数解释：** 美团网，中国领先的生活服务电子商务平台 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param mei_tuan: The mei_tuan of this IpReputationMapResponseBodyLocale.
        :type mei_tuan: str
        """
        self._mei_tuan = mei_tuan

    @property
    def microsoft(self):
        r"""Gets the microsoft of this IpReputationMapResponseBodyLocale.

        **参数解释：** 微软公司，全球知名的科技企业，提供操作系统、办公软件等服务 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The microsoft of this IpReputationMapResponseBodyLocale.
        :rtype: str
        """
        return self._microsoft

    @microsoft.setter
    def microsoft(self, microsoft):
        r"""Sets the microsoft of this IpReputationMapResponseBodyLocale.

        **参数解释：** 微软公司，全球知名的科技企业，提供操作系统、办公软件等服务 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param microsoft: The microsoft of this IpReputationMapResponseBodyLocale.
        :type microsoft: str
        """
        self._microsoft = microsoft

    @property
    def ali_cloud(self):
        r"""Gets the ali_cloud of this IpReputationMapResponseBodyLocale.

        **参数解释：** 阿里云，阿里巴巴集团旗下的云计算品牌 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ali_cloud of this IpReputationMapResponseBodyLocale.
        :rtype: str
        """
        return self._ali_cloud

    @ali_cloud.setter
    def ali_cloud(self, ali_cloud):
        r"""Sets the ali_cloud of this IpReputationMapResponseBodyLocale.

        **参数解释：** 阿里云，阿里巴巴集团旗下的云计算品牌 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ali_cloud: The ali_cloud of this IpReputationMapResponseBodyLocale.
        :type ali_cloud: str
        """
        self._ali_cloud = ali_cloud

    @property
    def amazon(self):
        r"""Gets the amazon of this IpReputationMapResponseBodyLocale.

        **参数解释：** 亚马逊，全球知名的电子商务和云计算企业 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The amazon of this IpReputationMapResponseBodyLocale.
        :rtype: str
        """
        return self._amazon

    @amazon.setter
    def amazon(self, amazon):
        r"""Sets the amazon of this IpReputationMapResponseBodyLocale.

        **参数解释：** 亚马逊，全球知名的电子商务和云计算企业 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param amazon: The amazon of this IpReputationMapResponseBodyLocale.
        :type amazon: str
        """
        self._amazon = amazon

    @property
    def vnet(self):
        r"""Gets the vnet of this IpReputationMapResponseBodyLocale.

        **参数解释：** 世纪互联，中国领先的电信中立互联网基础设施服务提供商 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The vnet of this IpReputationMapResponseBodyLocale.
        :rtype: str
        """
        return self._vnet

    @vnet.setter
    def vnet(self, vnet):
        r"""Sets the vnet of this IpReputationMapResponseBodyLocale.

        **参数解释：** 世纪互联，中国领先的电信中立互联网基础设施服务提供商 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param vnet: The vnet of this IpReputationMapResponseBodyLocale.
        :type vnet: str
        """
        self._vnet = vnet

    @property
    def hw(self):
        r"""Gets the hw of this IpReputationMapResponseBodyLocale.

        **参数解释：** 华为，全球知名的通信技术企业 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The hw of this IpReputationMapResponseBodyLocale.
        :rtype: str
        """
        return self._hw

    @hw.setter
    def hw(self, hw):
        r"""Sets the hw of this IpReputationMapResponseBodyLocale.

        **参数解释：** 华为，全球知名的通信技术企业 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param hw: The hw of this IpReputationMapResponseBodyLocale.
        :type hw: str
        """
        self._hw = hw

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
        if not isinstance(other, IpReputationMapResponseBodyLocale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
