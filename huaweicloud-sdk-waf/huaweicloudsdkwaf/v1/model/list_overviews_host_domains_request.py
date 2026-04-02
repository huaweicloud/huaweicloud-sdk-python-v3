# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOverviewsHostDomainsRequest:

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
        '_from': 'int',
        'to': 'int',
        'host_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        '_from': 'from',
        'to': 'to',
        'host_id': 'host_id'
    }

    def __init__(self, enterprise_project_id=None, _from=None, to=None, host_id=None):
        r"""ListOverviewsHostDomainsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param _from: **参数解释：** 起始时间(毫秒时间戳)，需要和to同时使用 **约束限制：** from &lt;&#x3D; to **取值范围：** from ~ to 最大范围30天 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 结束时间(毫秒时间戳)，需要和from同时使用 **约束限制：** from ~ to 最大范围30天 **取值范围：** 不能超过当天的结束时间 **默认取值：** 不涉及
        :type to: int
        :param host_id: **参数解释：** 泛域名id，通过 ”查询独享模式域名列表“（ListPremiumHost）或者 “查询云模式防护域名列表” （ListHost）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type host_id: str
        """
        
        

        self._enterprise_project_id = None
        self.__from = None
        self._to = None
        self._host_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self._from = _from
        self.to = to
        self.host_id = host_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListOverviewsHostDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListOverviewsHostDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListOverviewsHostDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListOverviewsHostDomainsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def _from(self):
        r"""Gets the _from of this ListOverviewsHostDomainsRequest.

        **参数解释：** 起始时间(毫秒时间戳)，需要和to同时使用 **约束限制：** from <= to **取值范围：** from ~ to 最大范围30天 **默认取值：** 不涉及

        :return: The _from of this ListOverviewsHostDomainsRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListOverviewsHostDomainsRequest.

        **参数解释：** 起始时间(毫秒时间戳)，需要和to同时使用 **约束限制：** from <= to **取值范围：** from ~ to 最大范围30天 **默认取值：** 不涉及

        :param _from: The _from of this ListOverviewsHostDomainsRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListOverviewsHostDomainsRequest.

        **参数解释：** 结束时间(毫秒时间戳)，需要和from同时使用 **约束限制：** from ~ to 最大范围30天 **取值范围：** 不能超过当天的结束时间 **默认取值：** 不涉及

        :return: The to of this ListOverviewsHostDomainsRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListOverviewsHostDomainsRequest.

        **参数解释：** 结束时间(毫秒时间戳)，需要和from同时使用 **约束限制：** from ~ to 最大范围30天 **取值范围：** 不能超过当天的结束时间 **默认取值：** 不涉及

        :param to: The to of this ListOverviewsHostDomainsRequest.
        :type to: int
        """
        self._to = to

    @property
    def host_id(self):
        r"""Gets the host_id of this ListOverviewsHostDomainsRequest.

        **参数解释：** 泛域名id，通过 ”查询独享模式域名列表“（ListPremiumHost）或者 “查询云模式防护域名列表” （ListHost）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The host_id of this ListOverviewsHostDomainsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListOverviewsHostDomainsRequest.

        **参数解释：** 泛域名id，通过 ”查询独享模式域名列表“（ListPremiumHost）或者 “查询云模式防护域名列表” （ListHost）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param host_id: The host_id of this ListOverviewsHostDomainsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    def to_dict(self):
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
        if not isinstance(other, ListOverviewsHostDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
