# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePeriodElasticResourcePoolSpecChangeOrderResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'order_id': 'order_id'
    }

    def __init__(self, is_success=None, message=None, order_id=None):
        r"""CreatePeriodElasticResourcePoolSpecChangeOrderResponse

        The model defined in huaweicloud sdk

        :param is_success: 
        :type is_success: bool
        :param message: 
        :type message: str
        :param order_id: 订单id
        :type order_id: str
        """
        
        super(CreatePeriodElasticResourcePoolSpecChangeOrderResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._order_id = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if order_id is not None:
            self.order_id = order_id

    @property
    def is_success(self):
        r"""Gets the is_success of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.

        :return: The is_success of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.

        :param is_success: The is_success of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.

        :return: The message of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.

        :param message: The message of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.
        :type message: str
        """
        self._message = message

    @property
    def order_id(self):
        r"""Gets the order_id of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.

        订单id

        :return: The order_id of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.

        订单id

        :param order_id: The order_id of this CreatePeriodElasticResourcePoolSpecChangeOrderResponse.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, CreatePeriodElasticResourcePoolSpecChangeOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
