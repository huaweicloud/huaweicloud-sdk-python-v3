# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonthUsageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sim_card_ids': 'list[int]',
        'billing_cycles': 'list[str]'
    }

    attribute_map = {
        'sim_card_ids': 'sim_card_ids',
        'billing_cycles': 'billing_cycles'
    }

    def __init__(self, sim_card_ids=None, billing_cycles=None):
        """ShowMonthUsageReq

        The model defined in huaweicloud sdk

        :param sim_card_ids: sim卡id列表，最多支持传入500个SIM卡id。
        :type sim_card_ids: list[int]
        :param billing_cycles: 账期，最多支持传入本月在内的6个月账期，例如[2022-07, 2022-06]，不支持传入未来账期。
        :type billing_cycles: list[str]
        """
        
        

        self._sim_card_ids = None
        self._billing_cycles = None
        self.discriminator = None

        self.sim_card_ids = sim_card_ids
        self.billing_cycles = billing_cycles

    @property
    def sim_card_ids(self):
        """Gets the sim_card_ids of this ShowMonthUsageReq.

        sim卡id列表，最多支持传入500个SIM卡id。

        :return: The sim_card_ids of this ShowMonthUsageReq.
        :rtype: list[int]
        """
        return self._sim_card_ids

    @sim_card_ids.setter
    def sim_card_ids(self, sim_card_ids):
        """Sets the sim_card_ids of this ShowMonthUsageReq.

        sim卡id列表，最多支持传入500个SIM卡id。

        :param sim_card_ids: The sim_card_ids of this ShowMonthUsageReq.
        :type sim_card_ids: list[int]
        """
        self._sim_card_ids = sim_card_ids

    @property
    def billing_cycles(self):
        """Gets the billing_cycles of this ShowMonthUsageReq.

        账期，最多支持传入本月在内的6个月账期，例如[2022-07, 2022-06]，不支持传入未来账期。

        :return: The billing_cycles of this ShowMonthUsageReq.
        :rtype: list[str]
        """
        return self._billing_cycles

    @billing_cycles.setter
    def billing_cycles(self, billing_cycles):
        """Sets the billing_cycles of this ShowMonthUsageReq.

        账期，最多支持传入本月在内的6个月账期，例如[2022-07, 2022-06]，不支持传入未来账期。

        :param billing_cycles: The billing_cycles of this ShowMonthUsageReq.
        :type billing_cycles: list[str]
        """
        self._billing_cycles = billing_cycles

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
        if not isinstance(other, ShowMonthUsageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
