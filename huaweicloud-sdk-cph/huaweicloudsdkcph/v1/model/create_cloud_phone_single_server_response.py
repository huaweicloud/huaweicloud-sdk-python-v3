# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCloudPhoneSingleServerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'order_id': 'str',
        'product_id': 'str',
        'server_ids': 'list[str]',
        'error_msg': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'order_id': 'order_id',
        'product_id': 'product_id',
        'server_ids': 'server_ids',
        'error_msg': 'error_msg',
        'error_code': 'error_code'
    }

    def __init__(self, request_id=None, order_id=None, product_id=None, server_ids=None, error_msg=None, error_code=None):
        """CreateCloudPhoneSingleServerResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param order_id: 订单ID，不超过64个字节。
        :type order_id: str
        :param product_id: 产品ID，不超过64个字节。
        :type product_id: str
        :param server_ids: 服务器ID列表。
        :type server_ids: list[str]
        :param error_msg: 任务错误码说明。
        :type error_msg: str
        :param error_code: 任务错误码。
        :type error_code: str
        """
        
        super(CreateCloudPhoneSingleServerResponse, self).__init__()

        self._request_id = None
        self._order_id = None
        self._product_id = None
        self._server_ids = None
        self._error_msg = None
        self._error_code = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if server_ids is not None:
            self.server_ids = server_ids
        if error_msg is not None:
            self.error_msg = error_msg
        if error_code is not None:
            self.error_code = error_code

    @property
    def request_id(self):
        """Gets the request_id of this CreateCloudPhoneSingleServerResponse.

        请求的唯一标识ID。

        :return: The request_id of this CreateCloudPhoneSingleServerResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateCloudPhoneSingleServerResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this CreateCloudPhoneSingleServerResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def order_id(self):
        """Gets the order_id of this CreateCloudPhoneSingleServerResponse.

        订单ID，不超过64个字节。

        :return: The order_id of this CreateCloudPhoneSingleServerResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreateCloudPhoneSingleServerResponse.

        订单ID，不超过64个字节。

        :param order_id: The order_id of this CreateCloudPhoneSingleServerResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this CreateCloudPhoneSingleServerResponse.

        产品ID，不超过64个字节。

        :return: The product_id of this CreateCloudPhoneSingleServerResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateCloudPhoneSingleServerResponse.

        产品ID，不超过64个字节。

        :param product_id: The product_id of this CreateCloudPhoneSingleServerResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def server_ids(self):
        """Gets the server_ids of this CreateCloudPhoneSingleServerResponse.

        服务器ID列表。

        :return: The server_ids of this CreateCloudPhoneSingleServerResponse.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        """Sets the server_ids of this CreateCloudPhoneSingleServerResponse.

        服务器ID列表。

        :param server_ids: The server_ids of this CreateCloudPhoneSingleServerResponse.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

    @property
    def error_msg(self):
        """Gets the error_msg of this CreateCloudPhoneSingleServerResponse.

        任务错误码说明。

        :return: The error_msg of this CreateCloudPhoneSingleServerResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CreateCloudPhoneSingleServerResponse.

        任务错误码说明。

        :param error_msg: The error_msg of this CreateCloudPhoneSingleServerResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_code(self):
        """Gets the error_code of this CreateCloudPhoneSingleServerResponse.

        任务错误码。

        :return: The error_code of this CreateCloudPhoneSingleServerResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CreateCloudPhoneSingleServerResponse.

        任务错误码。

        :param error_code: The error_code of this CreateCloudPhoneSingleServerResponse.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, CreateCloudPhoneSingleServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
