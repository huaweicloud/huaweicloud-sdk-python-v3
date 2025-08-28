# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBotMTopnRequestResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topn_known_bots': 'list[TypedStatBucket]',
        'topn_domains': 'list[TypedStatBucket]',
        'topn_src_ips': 'list[TypedStatBucket]',
        'topn_src_ip_asns': 'list[TypedStatBucket]',
        'topn_src_ip_geolocations': 'list[TypedStatBucket]',
        'topn_ja4_fps': 'list[TypedStatBucket]'
    }

    attribute_map = {
        'topn_known_bots': 'topn_known_bots',
        'topn_domains': 'topn_domains',
        'topn_src_ips': 'topn_src_ips',
        'topn_src_ip_asns': 'topn_src_ip_asns',
        'topn_src_ip_geolocations': 'topn_src_ip_geolocations',
        'topn_ja4_fps': 'topn_ja4_fps'
    }

    def __init__(self, topn_known_bots=None, topn_domains=None, topn_src_ips=None, topn_src_ip_asns=None, topn_src_ip_geolocations=None, topn_ja4_fps=None):
        r"""ListBotMTopnRequestResponse

        The model defined in huaweicloud sdk

        :param topn_known_bots: **参数解释：** TopN已知BOT的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type topn_known_bots: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        :param topn_domains: **参数解释：** TopN被访问域名的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type topn_domains: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        :param topn_src_ips: **参数解释：** TopN攻击源IP的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type topn_src_ips: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        :param topn_src_ip_asns: **参数解释：** TopN攻击源IP所属ASN的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type topn_src_ip_asns: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        :param topn_src_ip_geolocations: **参数解释：** TopN攻击源地区的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type topn_src_ip_geolocations: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        :param topn_ja4_fps: **参数解释：** TopN JA4指纹的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type topn_ja4_fps: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        
        super(ListBotMTopnRequestResponse, self).__init__()

        self._topn_known_bots = None
        self._topn_domains = None
        self._topn_src_ips = None
        self._topn_src_ip_asns = None
        self._topn_src_ip_geolocations = None
        self._topn_ja4_fps = None
        self.discriminator = None

        if topn_known_bots is not None:
            self.topn_known_bots = topn_known_bots
        if topn_domains is not None:
            self.topn_domains = topn_domains
        if topn_src_ips is not None:
            self.topn_src_ips = topn_src_ips
        if topn_src_ip_asns is not None:
            self.topn_src_ip_asns = topn_src_ip_asns
        if topn_src_ip_geolocations is not None:
            self.topn_src_ip_geolocations = topn_src_ip_geolocations
        if topn_ja4_fps is not None:
            self.topn_ja4_fps = topn_ja4_fps

    @property
    def topn_known_bots(self):
        r"""Gets the topn_known_bots of this ListBotMTopnRequestResponse.

        **参数解释：** TopN已知BOT的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The topn_known_bots of this ListBotMTopnRequestResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        return self._topn_known_bots

    @topn_known_bots.setter
    def topn_known_bots(self, topn_known_bots):
        r"""Sets the topn_known_bots of this ListBotMTopnRequestResponse.

        **参数解释：** TopN已知BOT的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param topn_known_bots: The topn_known_bots of this ListBotMTopnRequestResponse.
        :type topn_known_bots: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        self._topn_known_bots = topn_known_bots

    @property
    def topn_domains(self):
        r"""Gets the topn_domains of this ListBotMTopnRequestResponse.

        **参数解释：** TopN被访问域名的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The topn_domains of this ListBotMTopnRequestResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        return self._topn_domains

    @topn_domains.setter
    def topn_domains(self, topn_domains):
        r"""Sets the topn_domains of this ListBotMTopnRequestResponse.

        **参数解释：** TopN被访问域名的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param topn_domains: The topn_domains of this ListBotMTopnRequestResponse.
        :type topn_domains: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        self._topn_domains = topn_domains

    @property
    def topn_src_ips(self):
        r"""Gets the topn_src_ips of this ListBotMTopnRequestResponse.

        **参数解释：** TopN攻击源IP的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The topn_src_ips of this ListBotMTopnRequestResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        return self._topn_src_ips

    @topn_src_ips.setter
    def topn_src_ips(self, topn_src_ips):
        r"""Sets the topn_src_ips of this ListBotMTopnRequestResponse.

        **参数解释：** TopN攻击源IP的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param topn_src_ips: The topn_src_ips of this ListBotMTopnRequestResponse.
        :type topn_src_ips: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        self._topn_src_ips = topn_src_ips

    @property
    def topn_src_ip_asns(self):
        r"""Gets the topn_src_ip_asns of this ListBotMTopnRequestResponse.

        **参数解释：** TopN攻击源IP所属ASN的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The topn_src_ip_asns of this ListBotMTopnRequestResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        return self._topn_src_ip_asns

    @topn_src_ip_asns.setter
    def topn_src_ip_asns(self, topn_src_ip_asns):
        r"""Sets the topn_src_ip_asns of this ListBotMTopnRequestResponse.

        **参数解释：** TopN攻击源IP所属ASN的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param topn_src_ip_asns: The topn_src_ip_asns of this ListBotMTopnRequestResponse.
        :type topn_src_ip_asns: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        self._topn_src_ip_asns = topn_src_ip_asns

    @property
    def topn_src_ip_geolocations(self):
        r"""Gets the topn_src_ip_geolocations of this ListBotMTopnRequestResponse.

        **参数解释：** TopN攻击源地区的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The topn_src_ip_geolocations of this ListBotMTopnRequestResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        return self._topn_src_ip_geolocations

    @topn_src_ip_geolocations.setter
    def topn_src_ip_geolocations(self, topn_src_ip_geolocations):
        r"""Sets the topn_src_ip_geolocations of this ListBotMTopnRequestResponse.

        **参数解释：** TopN攻击源地区的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param topn_src_ip_geolocations: The topn_src_ip_geolocations of this ListBotMTopnRequestResponse.
        :type topn_src_ip_geolocations: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        self._topn_src_ip_geolocations = topn_src_ip_geolocations

    @property
    def topn_ja4_fps(self):
        r"""Gets the topn_ja4_fps of this ListBotMTopnRequestResponse.

        **参数解释：** TopN JA4指纹的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The topn_ja4_fps of this ListBotMTopnRequestResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        return self._topn_ja4_fps

    @topn_ja4_fps.setter
    def topn_ja4_fps(self, topn_ja4_fps):
        r"""Sets the topn_ja4_fps of this ListBotMTopnRequestResponse.

        **参数解释：** TopN JA4指纹的请求统计 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param topn_ja4_fps: The topn_ja4_fps of this ListBotMTopnRequestResponse.
        :type topn_ja4_fps: list[:class:`huaweicloudsdkwaf.v1.TypedStatBucket`]
        """
        self._topn_ja4_fps = topn_ja4_fps

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
        if not isinstance(other, ListBotMTopnRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
