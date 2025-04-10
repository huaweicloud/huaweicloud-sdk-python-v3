# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MarketModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str',
        'prepaid_info': 'MarketModelPrepaidInfo'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'prepaid_info': 'prepaid_info'
    }

    def __init__(self, charge_mode=None, prepaid_info=None):
        r"""MarketModel

        The model defined in huaweicloud sdk

        :param charge_mode: 计费类型
        :type charge_mode: str
        :param prepaid_info: 
        :type prepaid_info: :class:`huaweicloudsdkecs.v2.MarketModelPrepaidInfo`
        """
        
        

        self._charge_mode = None
        self._prepaid_info = None
        self.discriminator = None

        if charge_mode is not None:
            self.charge_mode = charge_mode
        if prepaid_info is not None:
            self.prepaid_info = prepaid_info

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this MarketModel.

        计费类型

        :return: The charge_mode of this MarketModel.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this MarketModel.

        计费类型

        :param charge_mode: The charge_mode of this MarketModel.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def prepaid_info(self):
        r"""Gets the prepaid_info of this MarketModel.

        :return: The prepaid_info of this MarketModel.
        :rtype: :class:`huaweicloudsdkecs.v2.MarketModelPrepaidInfo`
        """
        return self._prepaid_info

    @prepaid_info.setter
    def prepaid_info(self, prepaid_info):
        r"""Sets the prepaid_info of this MarketModel.

        :param prepaid_info: The prepaid_info of this MarketModel.
        :type prepaid_info: :class:`huaweicloudsdkecs.v2.MarketModelPrepaidInfo`
        """
        self._prepaid_info = prepaid_info

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
        if not isinstance(other, MarketModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
