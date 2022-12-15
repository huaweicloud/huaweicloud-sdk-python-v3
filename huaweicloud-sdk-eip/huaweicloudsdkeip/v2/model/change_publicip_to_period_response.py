# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangePublicipToPeriodResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_ids': 'list[str]',
        'order_id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'publicip_ids': 'publicip_ids',
        'order_id': 'order_id',
        'request_id': 'request_id'
    }

    def __init__(self, publicip_ids=None, order_id=None, request_id=None):
        """ChangePublicipToPeriodResponse

        The model defined in huaweicloud sdk

        :param publicip_ids: 转包IP列表
        :type publicip_ids: list[str]
        :param order_id: 订单ID
        :type order_id: str
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(ChangePublicipToPeriodResponse, self).__init__()

        self._publicip_ids = None
        self._order_id = None
        self._request_id = None
        self.discriminator = None

        if publicip_ids is not None:
            self.publicip_ids = publicip_ids
        if order_id is not None:
            self.order_id = order_id
        if request_id is not None:
            self.request_id = request_id

    @property
    def publicip_ids(self):
        """Gets the publicip_ids of this ChangePublicipToPeriodResponse.

        转包IP列表

        :return: The publicip_ids of this ChangePublicipToPeriodResponse.
        :rtype: list[str]
        """
        return self._publicip_ids

    @publicip_ids.setter
    def publicip_ids(self, publicip_ids):
        """Sets the publicip_ids of this ChangePublicipToPeriodResponse.

        转包IP列表

        :param publicip_ids: The publicip_ids of this ChangePublicipToPeriodResponse.
        :type publicip_ids: list[str]
        """
        self._publicip_ids = publicip_ids

    @property
    def order_id(self):
        """Gets the order_id of this ChangePublicipToPeriodResponse.

        订单ID

        :return: The order_id of this ChangePublicipToPeriodResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ChangePublicipToPeriodResponse.

        订单ID

        :param order_id: The order_id of this ChangePublicipToPeriodResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def request_id(self):
        """Gets the request_id of this ChangePublicipToPeriodResponse.

        请求ID

        :return: The request_id of this ChangePublicipToPeriodResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ChangePublicipToPeriodResponse.

        请求ID

        :param request_id: The request_id of this ChangePublicipToPeriodResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ChangePublicipToPeriodResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
