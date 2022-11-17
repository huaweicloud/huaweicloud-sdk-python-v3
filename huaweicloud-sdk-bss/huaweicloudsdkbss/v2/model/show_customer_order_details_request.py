# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomerOrderDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'order_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'order_id': 'order_id',
        'limit': 'limit',
        'offset': 'offset',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, x_language=None, order_id=None, limit=None, offset=None, indirect_partner_id=None):
        """ShowCustomerOrderDetailsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言：中文：zh_CN 英文：en_US 缺省为zh_CN
        :type x_language: str
        :param order_id: 订单ID。
        :type order_id: str
        :param limit: 每页大小。默认值为10。
        :type limit: int
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。华为云总经销商（一级经销商）查询云经销商的客户订单详情时，需要携带该参数；除此之外，此参数不做处理。否则只能查询自己客户的订单详情。
        :type indirect_partner_id: str
        """
        
        

        self._x_language = None
        self._order_id = None
        self._limit = None
        self._offset = None
        self._indirect_partner_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.order_id = order_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def x_language(self):
        """Gets the x_language of this ShowCustomerOrderDetailsRequest.

        语言：中文：zh_CN 英文：en_US 缺省为zh_CN

        :return: The x_language of this ShowCustomerOrderDetailsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowCustomerOrderDetailsRequest.

        语言：中文：zh_CN 英文：en_US 缺省为zh_CN

        :param x_language: The x_language of this ShowCustomerOrderDetailsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def order_id(self):
        """Gets the order_id of this ShowCustomerOrderDetailsRequest.

        订单ID。

        :return: The order_id of this ShowCustomerOrderDetailsRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShowCustomerOrderDetailsRequest.

        订单ID。

        :param order_id: The order_id of this ShowCustomerOrderDetailsRequest.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def limit(self):
        """Gets the limit of this ShowCustomerOrderDetailsRequest.

        每页大小。默认值为10。

        :return: The limit of this ShowCustomerOrderDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowCustomerOrderDetailsRequest.

        每页大小。默认值为10。

        :param limit: The limit of this ShowCustomerOrderDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowCustomerOrderDetailsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ShowCustomerOrderDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowCustomerOrderDetailsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ShowCustomerOrderDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ShowCustomerOrderDetailsRequest.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。华为云总经销商（一级经销商）查询云经销商的客户订单详情时，需要携带该参数；除此之外，此参数不做处理。否则只能查询自己客户的订单详情。

        :return: The indirect_partner_id of this ShowCustomerOrderDetailsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ShowCustomerOrderDetailsRequest.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。华为云总经销商（一级经销商）查询云经销商的客户订单详情时，需要携带该参数；除此之外，此参数不做处理。否则只能查询自己客户的订单详情。

        :param indirect_partner_id: The indirect_partner_id of this ShowCustomerOrderDetailsRequest.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        if not isinstance(other, ShowCustomerOrderDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
