# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrepaidParamForBatchResizeVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, is_auto_pay=None):
        r"""PrepaidParamForBatchResizeVolume

        The model defined in huaweicloud sdk

        :param is_auto_pay: Whether to pay immediately. This parameter is valid only when the disk is billed on a yearly/monthly basis. The default value is **false**. Values: - **true**: An order is immediately paid from the account balance. - **false**: An order is not paid immediately after being created.
        :type is_auto_pay: str
        """
        
        

        self._is_auto_pay = None
        self.discriminator = None

        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this PrepaidParamForBatchResizeVolume.

        Whether to pay immediately. This parameter is valid only when the disk is billed on a yearly/monthly basis. The default value is **false**. Values: - **true**: An order is immediately paid from the account balance. - **false**: An order is not paid immediately after being created.

        :return: The is_auto_pay of this PrepaidParamForBatchResizeVolume.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this PrepaidParamForBatchResizeVolume.

        Whether to pay immediately. This parameter is valid only when the disk is billed on a yearly/monthly basis. The default value is **false**. Values: - **true**: An order is immediately paid from the account balance. - **false**: An order is not paid immediately after being created.

        :param is_auto_pay: The is_auto_pay of this PrepaidParamForBatchResizeVolume.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, PrepaidParamForBatchResizeVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
