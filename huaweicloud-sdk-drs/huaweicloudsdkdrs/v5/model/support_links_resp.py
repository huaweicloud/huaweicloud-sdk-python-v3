# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportLinksResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'support_links': 'list[SupportLinkInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'support_links': 'support_links'
    }

    def __init__(self, total_count=None, support_links=None):
        r"""SupportLinksResp

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**：  列表中的项目总数，与分页无关。表示满足查询条件的记录总数量，用于分页计算。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type total_count: int
        :param support_links: **参数解释**：  DRS支持的数据复制链路列表，每条链路包含引擎类型、网络类型、迁移模式等组合信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type support_links: list[:class:`huaweicloudsdkdrs.v5.SupportLinkInfo`]
        """
        
        

        self._total_count = None
        self._support_links = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if support_links is not None:
            self.support_links = support_links

    @property
    def total_count(self):
        r"""Gets the total_count of this SupportLinksResp.

        **参数解释**：  列表中的项目总数，与分页无关。表示满足查询条件的记录总数量，用于分页计算。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The total_count of this SupportLinksResp.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this SupportLinksResp.

        **参数解释**：  列表中的项目总数，与分页无关。表示满足查询条件的记录总数量，用于分页计算。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param total_count: The total_count of this SupportLinksResp.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def support_links(self):
        r"""Gets the support_links of this SupportLinksResp.

        **参数解释**：  DRS支持的数据复制链路列表，每条链路包含引擎类型、网络类型、迁移模式等组合信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The support_links of this SupportLinksResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.SupportLinkInfo`]
        """
        return self._support_links

    @support_links.setter
    def support_links(self, support_links):
        r"""Sets the support_links of this SupportLinksResp.

        **参数解释**：  DRS支持的数据复制链路列表，每条链路包含引擎类型、网络类型、迁移模式等组合信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param support_links: The support_links of this SupportLinksResp.
        :type support_links: list[:class:`huaweicloudsdkdrs.v5.SupportLinkInfo`]
        """
        self._support_links = support_links

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
        if not isinstance(other, SupportLinksResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
