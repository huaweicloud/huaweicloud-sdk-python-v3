# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstancesPeriodOrderResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'code': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'code': 'code',
        'order_id': 'order_id'
    }

    def __init__(self, description=None, code=None, order_id=None):
        r"""CreateInstancesPeriodOrderResponse

        The model defined in huaweicloud sdk

        :param description: 描述
        :type description: str
        :param code: 返回码
        :type code: str
        :param order_id: 订单ID
        :type order_id: str
        """
        
        super(CreateInstancesPeriodOrderResponse, self).__init__()

        self._description = None
        self._code = None
        self._order_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if code is not None:
            self.code = code
        if order_id is not None:
            self.order_id = order_id

    @property
    def description(self):
        r"""Gets the description of this CreateInstancesPeriodOrderResponse.

        描述

        :return: The description of this CreateInstancesPeriodOrderResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateInstancesPeriodOrderResponse.

        描述

        :param description: The description of this CreateInstancesPeriodOrderResponse.
        :type description: str
        """
        self._description = description

    @property
    def code(self):
        r"""Gets the code of this CreateInstancesPeriodOrderResponse.

        返回码

        :return: The code of this CreateInstancesPeriodOrderResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CreateInstancesPeriodOrderResponse.

        返回码

        :param code: The code of this CreateInstancesPeriodOrderResponse.
        :type code: str
        """
        self._code = code

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateInstancesPeriodOrderResponse.

        订单ID

        :return: The order_id of this CreateInstancesPeriodOrderResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateInstancesPeriodOrderResponse.

        订单ID

        :param order_id: The order_id of this CreateInstancesPeriodOrderResponse.
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
        if not isinstance(other, CreateInstancesPeriodOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
