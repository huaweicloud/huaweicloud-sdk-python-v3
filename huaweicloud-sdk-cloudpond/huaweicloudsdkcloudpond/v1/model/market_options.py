# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MarketOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'ChargeMode',
        'prepaid_options': 'PrepaidOptions'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'prepaid_options': 'prepaid_options'
    }

    def __init__(self, charge_mode=None, prepaid_options=None):
        """MarketOptions

        The model defined in huaweicloud sdk

        :param charge_mode: 
        :type charge_mode: :class:`huaweicloudsdkcloudpond.v1.ChargeMode`
        :param prepaid_options: 
        :type prepaid_options: :class:`huaweicloudsdkcloudpond.v1.PrepaidOptions`
        """
        
        

        self._charge_mode = None
        self._prepaid_options = None
        self.discriminator = None

        if charge_mode is not None:
            self.charge_mode = charge_mode
        if prepaid_options is not None:
            self.prepaid_options = prepaid_options

    @property
    def charge_mode(self):
        """Gets the charge_mode of this MarketOptions.

        :return: The charge_mode of this MarketOptions.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ChargeMode`
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this MarketOptions.

        :param charge_mode: The charge_mode of this MarketOptions.
        :type charge_mode: :class:`huaweicloudsdkcloudpond.v1.ChargeMode`
        """
        self._charge_mode = charge_mode

    @property
    def prepaid_options(self):
        """Gets the prepaid_options of this MarketOptions.

        :return: The prepaid_options of this MarketOptions.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.PrepaidOptions`
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        """Sets the prepaid_options of this MarketOptions.

        :param prepaid_options: The prepaid_options of this MarketOptions.
        :type prepaid_options: :class:`huaweicloudsdkcloudpond.v1.PrepaidOptions`
        """
        self._prepaid_options = prepaid_options

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
        if not isinstance(other, MarketOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
