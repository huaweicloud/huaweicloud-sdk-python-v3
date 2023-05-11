# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussChargeInfoListResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str'
    }

    attribute_map = {
        'charge_mode': 'charge_mode'
    }

    def __init__(self, charge_mode=None):
        """OpenGaussChargeInfoListResponse

        The model defined in huaweicloud sdk

        :param charge_mode: 计费模式。  取值范围：  postPaid：后付费，即按需付费。  prePaid：预付费，即包年/包月。
        :type charge_mode: str
        """
        
        

        self._charge_mode = None
        self.discriminator = None

        self.charge_mode = charge_mode

    @property
    def charge_mode(self):
        """Gets the charge_mode of this OpenGaussChargeInfoListResponse.

        计费模式。  取值范围：  postPaid：后付费，即按需付费。  prePaid：预付费，即包年/包月。

        :return: The charge_mode of this OpenGaussChargeInfoListResponse.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this OpenGaussChargeInfoListResponse.

        计费模式。  取值范围：  postPaid：后付费，即按需付费。  prePaid：预付费，即包年/包月。

        :param charge_mode: The charge_mode of this OpenGaussChargeInfoListResponse.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

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
        if not isinstance(other, OpenGaussChargeInfoListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
