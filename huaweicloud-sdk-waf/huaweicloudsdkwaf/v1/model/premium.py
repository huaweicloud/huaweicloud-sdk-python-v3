# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Premium:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'purchased': 'bool',
        'total': 'int',
        'elb': 'int',
        'dedicated': 'int'
    }

    attribute_map = {
        'purchased': 'purchased',
        'total': 'total',
        'elb': 'elb',
        'dedicated': 'dedicated'
    }

    def __init__(self, purchased=None, total=None, elb=None, dedicated=None):
        r"""Premium

        The model defined in huaweicloud sdk

        :param purchased: **参数解释：** 是否开通独享模式 **取值范围：** 不涉及
        :type purchased: bool
        :param total: **参数解释：** 独享实例数量，包括elb **取值范围：** 不涉及
        :type total: int
        :param elb: **参数解释：** elb实例数量 **取值范围：** 不涉及
        :type elb: int
        :param dedicated: **参数解释：** 独享WAF实例数量 **取值范围：** 不涉及
        :type dedicated: int
        """
        
        

        self._purchased = None
        self._total = None
        self._elb = None
        self._dedicated = None
        self.discriminator = None

        if purchased is not None:
            self.purchased = purchased
        if total is not None:
            self.total = total
        if elb is not None:
            self.elb = elb
        if dedicated is not None:
            self.dedicated = dedicated

    @property
    def purchased(self):
        r"""Gets the purchased of this Premium.

        **参数解释：** 是否开通独享模式 **取值范围：** 不涉及

        :return: The purchased of this Premium.
        :rtype: bool
        """
        return self._purchased

    @purchased.setter
    def purchased(self, purchased):
        r"""Sets the purchased of this Premium.

        **参数解释：** 是否开通独享模式 **取值范围：** 不涉及

        :param purchased: The purchased of this Premium.
        :type purchased: bool
        """
        self._purchased = purchased

    @property
    def total(self):
        r"""Gets the total of this Premium.

        **参数解释：** 独享实例数量，包括elb **取值范围：** 不涉及

        :return: The total of this Premium.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this Premium.

        **参数解释：** 独享实例数量，包括elb **取值范围：** 不涉及

        :param total: The total of this Premium.
        :type total: int
        """
        self._total = total

    @property
    def elb(self):
        r"""Gets the elb of this Premium.

        **参数解释：** elb实例数量 **取值范围：** 不涉及

        :return: The elb of this Premium.
        :rtype: int
        """
        return self._elb

    @elb.setter
    def elb(self, elb):
        r"""Sets the elb of this Premium.

        **参数解释：** elb实例数量 **取值范围：** 不涉及

        :param elb: The elb of this Premium.
        :type elb: int
        """
        self._elb = elb

    @property
    def dedicated(self):
        r"""Gets the dedicated of this Premium.

        **参数解释：** 独享WAF实例数量 **取值范围：** 不涉及

        :return: The dedicated of this Premium.
        :rtype: int
        """
        return self._dedicated

    @dedicated.setter
    def dedicated(self, dedicated):
        r"""Sets the dedicated of this Premium.

        **参数解释：** 独享WAF实例数量 **取值范围：** 不涉及

        :param dedicated: The dedicated of this Premium.
        :type dedicated: int
        """
        self._dedicated = dedicated

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
        if not isinstance(other, Premium):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
