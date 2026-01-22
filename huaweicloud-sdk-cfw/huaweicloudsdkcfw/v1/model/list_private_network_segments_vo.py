# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateNetworkSegmentsVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'private_network_list': 'list[PrivateNetworkSegmentVO]',
        'total': 'int',
        'quota': 'int',
        'support_az_list': 'list[str]'
    }

    attribute_map = {
        'private_network_list': 'private_network_list',
        'total': 'total',
        'quota': 'quota',
        'support_az_list': 'support_az_list'
    }

    def __init__(self, private_network_list=None, total=None, quota=None, support_az_list=None):
        r"""ListPrivateNetworkSegmentsVO

        The model defined in huaweicloud sdk

        :param private_network_list: **参数解释**： 私网网段列表 **取值范围**： 不涉及
        :type private_network_list: list[:class:`huaweicloudsdkcfw.v1.PrivateNetworkSegmentVO`]
        :param total: **参数解释**： 总条数 **取值范围**： 不涉及
        :type total: int
        :param quota: **参数解释**： 私网网段配额 **取值范围**： 不涉及
        :type quota: int
        :param support_az_list: **参数解释**： 支持的可用区列表 **取值范围**： 不涉及
        :type support_az_list: list[str]
        """
        
        

        self._private_network_list = None
        self._total = None
        self._quota = None
        self._support_az_list = None
        self.discriminator = None

        if private_network_list is not None:
            self.private_network_list = private_network_list
        if total is not None:
            self.total = total
        if quota is not None:
            self.quota = quota
        if support_az_list is not None:
            self.support_az_list = support_az_list

    @property
    def private_network_list(self):
        r"""Gets the private_network_list of this ListPrivateNetworkSegmentsVO.

        **参数解释**： 私网网段列表 **取值范围**： 不涉及

        :return: The private_network_list of this ListPrivateNetworkSegmentsVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.PrivateNetworkSegmentVO`]
        """
        return self._private_network_list

    @private_network_list.setter
    def private_network_list(self, private_network_list):
        r"""Sets the private_network_list of this ListPrivateNetworkSegmentsVO.

        **参数解释**： 私网网段列表 **取值范围**： 不涉及

        :param private_network_list: The private_network_list of this ListPrivateNetworkSegmentsVO.
        :type private_network_list: list[:class:`huaweicloudsdkcfw.v1.PrivateNetworkSegmentVO`]
        """
        self._private_network_list = private_network_list

    @property
    def total(self):
        r"""Gets the total of this ListPrivateNetworkSegmentsVO.

        **参数解释**： 总条数 **取值范围**： 不涉及

        :return: The total of this ListPrivateNetworkSegmentsVO.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListPrivateNetworkSegmentsVO.

        **参数解释**： 总条数 **取值范围**： 不涉及

        :param total: The total of this ListPrivateNetworkSegmentsVO.
        :type total: int
        """
        self._total = total

    @property
    def quota(self):
        r"""Gets the quota of this ListPrivateNetworkSegmentsVO.

        **参数解释**： 私网网段配额 **取值范围**： 不涉及

        :return: The quota of this ListPrivateNetworkSegmentsVO.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ListPrivateNetworkSegmentsVO.

        **参数解释**： 私网网段配额 **取值范围**： 不涉及

        :param quota: The quota of this ListPrivateNetworkSegmentsVO.
        :type quota: int
        """
        self._quota = quota

    @property
    def support_az_list(self):
        r"""Gets the support_az_list of this ListPrivateNetworkSegmentsVO.

        **参数解释**： 支持的可用区列表 **取值范围**： 不涉及

        :return: The support_az_list of this ListPrivateNetworkSegmentsVO.
        :rtype: list[str]
        """
        return self._support_az_list

    @support_az_list.setter
    def support_az_list(self, support_az_list):
        r"""Sets the support_az_list of this ListPrivateNetworkSegmentsVO.

        **参数解释**： 支持的可用区列表 **取值范围**： 不涉及

        :param support_az_list: The support_az_list of this ListPrivateNetworkSegmentsVO.
        :type support_az_list: list[str]
        """
        self._support_az_list = support_az_list

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
        if not isinstance(other, ListPrivateNetworkSegmentsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
