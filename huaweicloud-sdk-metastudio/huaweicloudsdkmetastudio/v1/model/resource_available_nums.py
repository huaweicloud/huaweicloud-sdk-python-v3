# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceAvailableNums:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flexus': 'int',
        'basic': 'int',
        'middle': 'int',
        'middle_on_demand': 'int',
        'advance': 'int',
        'third_party_cmww': 'int'
    }

    attribute_map = {
        'flexus': 'flexus',
        'basic': 'basic',
        'middle': 'middle',
        'middle_on_demand': 'middle_on_demand',
        'advance': 'advance',
        'third_party_cmww': 'third_party_cmww'
    }

    def __init__(self, flexus=None, basic=None, middle=None, middle_on_demand=None, advance=None, third_party_cmww=None):
        r"""ResourceAvailableNums

        The model defined in huaweicloud sdk

        :param flexus: flexus版资源数。
        :type flexus: int
        :param basic: 基础版资源数。
        :type basic: int
        :param middle: 进阶版资源数。
        :type middle: int
        :param middle_on_demand: 进阶测试版资源数。
        :type middle_on_demand: int
        :param advance: 高级版资源数。
        :type advance: int
        :param third_party_cmww: 出门问问资源数。
        :type third_party_cmww: int
        """
        
        

        self._flexus = None
        self._basic = None
        self._middle = None
        self._middle_on_demand = None
        self._advance = None
        self._third_party_cmww = None
        self.discriminator = None

        if flexus is not None:
            self.flexus = flexus
        if basic is not None:
            self.basic = basic
        if middle is not None:
            self.middle = middle
        if middle_on_demand is not None:
            self.middle_on_demand = middle_on_demand
        if advance is not None:
            self.advance = advance
        if third_party_cmww is not None:
            self.third_party_cmww = third_party_cmww

    @property
    def flexus(self):
        r"""Gets the flexus of this ResourceAvailableNums.

        flexus版资源数。

        :return: The flexus of this ResourceAvailableNums.
        :rtype: int
        """
        return self._flexus

    @flexus.setter
    def flexus(self, flexus):
        r"""Sets the flexus of this ResourceAvailableNums.

        flexus版资源数。

        :param flexus: The flexus of this ResourceAvailableNums.
        :type flexus: int
        """
        self._flexus = flexus

    @property
    def basic(self):
        r"""Gets the basic of this ResourceAvailableNums.

        基础版资源数。

        :return: The basic of this ResourceAvailableNums.
        :rtype: int
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        r"""Sets the basic of this ResourceAvailableNums.

        基础版资源数。

        :param basic: The basic of this ResourceAvailableNums.
        :type basic: int
        """
        self._basic = basic

    @property
    def middle(self):
        r"""Gets the middle of this ResourceAvailableNums.

        进阶版资源数。

        :return: The middle of this ResourceAvailableNums.
        :rtype: int
        """
        return self._middle

    @middle.setter
    def middle(self, middle):
        r"""Sets the middle of this ResourceAvailableNums.

        进阶版资源数。

        :param middle: The middle of this ResourceAvailableNums.
        :type middle: int
        """
        self._middle = middle

    @property
    def middle_on_demand(self):
        r"""Gets the middle_on_demand of this ResourceAvailableNums.

        进阶测试版资源数。

        :return: The middle_on_demand of this ResourceAvailableNums.
        :rtype: int
        """
        return self._middle_on_demand

    @middle_on_demand.setter
    def middle_on_demand(self, middle_on_demand):
        r"""Sets the middle_on_demand of this ResourceAvailableNums.

        进阶测试版资源数。

        :param middle_on_demand: The middle_on_demand of this ResourceAvailableNums.
        :type middle_on_demand: int
        """
        self._middle_on_demand = middle_on_demand

    @property
    def advance(self):
        r"""Gets the advance of this ResourceAvailableNums.

        高级版资源数。

        :return: The advance of this ResourceAvailableNums.
        :rtype: int
        """
        return self._advance

    @advance.setter
    def advance(self, advance):
        r"""Sets the advance of this ResourceAvailableNums.

        高级版资源数。

        :param advance: The advance of this ResourceAvailableNums.
        :type advance: int
        """
        self._advance = advance

    @property
    def third_party_cmww(self):
        r"""Gets the third_party_cmww of this ResourceAvailableNums.

        出门问问资源数。

        :return: The third_party_cmww of this ResourceAvailableNums.
        :rtype: int
        """
        return self._third_party_cmww

    @third_party_cmww.setter
    def third_party_cmww(self, third_party_cmww):
        r"""Sets the third_party_cmww of this ResourceAvailableNums.

        出门问问资源数。

        :param third_party_cmww: The third_party_cmww of this ResourceAvailableNums.
        :type third_party_cmww: int
        """
        self._third_party_cmww = third_party_cmww

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
        if not isinstance(other, ResourceAvailableNums):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
