# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorSellPoliciesResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'flavor_id': 'str',
        'sell_status': 'str',
        'availability_zone_id': 'str',
        'sell_mode': 'str',
        'spot_options': 'FlavorSpotOptions'
    }

    attribute_map = {
        'id': 'id',
        'flavor_id': 'flavor_id',
        'sell_status': 'sell_status',
        'availability_zone_id': 'availability_zone_id',
        'sell_mode': 'sell_mode',
        'spot_options': 'spot_options'
    }

    def __init__(self, id=None, flavor_id=None, sell_status=None, availability_zone_id=None, sell_mode=None, spot_options=None):
        r"""ListFlavorSellPoliciesResult

        The model defined in huaweicloud sdk

        :param id: 云服务器规格的索引。
        :type id: int
        :param flavor_id: 云服务器规格的ID。
        :type flavor_id: str
        :param sell_status: 云服务器规格的售卖状态。  sellout：售罄。 available：可用。
        :type sell_status: str
        :param availability_zone_id: 云服务器规格的可用区。
        :type availability_zone_id: str
        :param sell_mode: 云服务器规格的付费模式。  - postPaid：按需计费实例。 - prePaid：包年/包月计费实例。 - spot：竞价实例。 - ri：预留实例。
        :type sell_mode: str
        :param spot_options: 
        :type spot_options: :class:`huaweicloudsdkecs.v2.FlavorSpotOptions`
        """
        
        

        self._id = None
        self._flavor_id = None
        self._sell_status = None
        self._availability_zone_id = None
        self._sell_mode = None
        self._spot_options = None
        self.discriminator = None

        self.id = id
        self.flavor_id = flavor_id
        self.sell_status = sell_status
        self.availability_zone_id = availability_zone_id
        self.sell_mode = sell_mode
        if spot_options is not None:
            self.spot_options = spot_options

    @property
    def id(self):
        r"""Gets the id of this ListFlavorSellPoliciesResult.

        云服务器规格的索引。

        :return: The id of this ListFlavorSellPoliciesResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListFlavorSellPoliciesResult.

        云服务器规格的索引。

        :param id: The id of this ListFlavorSellPoliciesResult.
        :type id: int
        """
        self._id = id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ListFlavorSellPoliciesResult.

        云服务器规格的ID。

        :return: The flavor_id of this ListFlavorSellPoliciesResult.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ListFlavorSellPoliciesResult.

        云服务器规格的ID。

        :param flavor_id: The flavor_id of this ListFlavorSellPoliciesResult.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def sell_status(self):
        r"""Gets the sell_status of this ListFlavorSellPoliciesResult.

        云服务器规格的售卖状态。  sellout：售罄。 available：可用。

        :return: The sell_status of this ListFlavorSellPoliciesResult.
        :rtype: str
        """
        return self._sell_status

    @sell_status.setter
    def sell_status(self, sell_status):
        r"""Sets the sell_status of this ListFlavorSellPoliciesResult.

        云服务器规格的售卖状态。  sellout：售罄。 available：可用。

        :param sell_status: The sell_status of this ListFlavorSellPoliciesResult.
        :type sell_status: str
        """
        self._sell_status = sell_status

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this ListFlavorSellPoliciesResult.

        云服务器规格的可用区。

        :return: The availability_zone_id of this ListFlavorSellPoliciesResult.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this ListFlavorSellPoliciesResult.

        云服务器规格的可用区。

        :param availability_zone_id: The availability_zone_id of this ListFlavorSellPoliciesResult.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def sell_mode(self):
        r"""Gets the sell_mode of this ListFlavorSellPoliciesResult.

        云服务器规格的付费模式。  - postPaid：按需计费实例。 - prePaid：包年/包月计费实例。 - spot：竞价实例。 - ri：预留实例。

        :return: The sell_mode of this ListFlavorSellPoliciesResult.
        :rtype: str
        """
        return self._sell_mode

    @sell_mode.setter
    def sell_mode(self, sell_mode):
        r"""Sets the sell_mode of this ListFlavorSellPoliciesResult.

        云服务器规格的付费模式。  - postPaid：按需计费实例。 - prePaid：包年/包月计费实例。 - spot：竞价实例。 - ri：预留实例。

        :param sell_mode: The sell_mode of this ListFlavorSellPoliciesResult.
        :type sell_mode: str
        """
        self._sell_mode = sell_mode

    @property
    def spot_options(self):
        r"""Gets the spot_options of this ListFlavorSellPoliciesResult.

        :return: The spot_options of this ListFlavorSellPoliciesResult.
        :rtype: :class:`huaweicloudsdkecs.v2.FlavorSpotOptions`
        """
        return self._spot_options

    @spot_options.setter
    def spot_options(self, spot_options):
        r"""Sets the spot_options of this ListFlavorSellPoliciesResult.

        :param spot_options: The spot_options of this ListFlavorSellPoliciesResult.
        :type spot_options: :class:`huaweicloudsdkecs.v2.FlavorSpotOptions`
        """
        self._spot_options = spot_options

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
        if not isinstance(other, ListFlavorSellPoliciesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
