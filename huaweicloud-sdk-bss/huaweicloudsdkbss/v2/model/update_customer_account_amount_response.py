# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomerAccountAmountResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transfer_id': 'str'
    }

    attribute_map = {
        'transfer_id': 'transfer_id'
    }

    def __init__(self, transfer_id=None):
        r"""UpdateCustomerAccountAmountResponse

        The model defined in huaweicloud sdk

        :param transfer_id: 事务流水ID，只有成功响应才会返回。
        :type transfer_id: str
        """
        
        super(UpdateCustomerAccountAmountResponse, self).__init__()

        self._transfer_id = None
        self.discriminator = None

        if transfer_id is not None:
            self.transfer_id = transfer_id

    @property
    def transfer_id(self):
        r"""Gets the transfer_id of this UpdateCustomerAccountAmountResponse.

        事务流水ID，只有成功响应才会返回。

        :return: The transfer_id of this UpdateCustomerAccountAmountResponse.
        :rtype: str
        """
        return self._transfer_id

    @transfer_id.setter
    def transfer_id(self, transfer_id):
        r"""Sets the transfer_id of this UpdateCustomerAccountAmountResponse.

        事务流水ID，只有成功响应才会返回。

        :param transfer_id: The transfer_id of this UpdateCustomerAccountAmountResponse.
        :type transfer_id: str
        """
        self._transfer_id = transfer_id

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
        if not isinstance(other, UpdateCustomerAccountAmountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
