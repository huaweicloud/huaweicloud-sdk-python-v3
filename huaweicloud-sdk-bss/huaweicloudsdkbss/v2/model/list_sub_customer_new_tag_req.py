# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomerNewTagReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_ids': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_ids': 'customer_ids',
        'offset': 'offset',
        'limit': 'limit',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_ids=None, offset=None, limit=None, indirect_partner_id=None):
        r"""ListSubCustomerNewTagReq

        The model defined in huaweicloud sdk

        :param customer_ids: 客户ID列表。单个客户ID最大长度：64。 此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。
        :type customer_ids: list[str]
        :param offset: 偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。 示例1，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。 示例2，查询总数20条，期望每页返回10条数据，则获取第一页数据，入参offset填写0，limit填写10；获取第二页数据，入参offset填写10，limit填写10。
        :type offset: int
        :param limit: 每次查询的客户数量。默认值为10。
        :type limit: int
        :param indirect_partner_id: 云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的客户新客标签，必须携带该字段。除此之外，此参数不做处理。
        :type indirect_partner_id: str
        """
        
        

        self._customer_ids = None
        self._offset = None
        self._limit = None
        self._indirect_partner_id = None
        self.discriminator = None

        if customer_ids is not None:
            self.customer_ids = customer_ids
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_ids(self):
        r"""Gets the customer_ids of this ListSubCustomerNewTagReq.

        客户ID列表。单个客户ID最大长度：64。 此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。

        :return: The customer_ids of this ListSubCustomerNewTagReq.
        :rtype: list[str]
        """
        return self._customer_ids

    @customer_ids.setter
    def customer_ids(self, customer_ids):
        r"""Sets the customer_ids of this ListSubCustomerNewTagReq.

        客户ID列表。单个客户ID最大长度：64。 此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。

        :param customer_ids: The customer_ids of this ListSubCustomerNewTagReq.
        :type customer_ids: list[str]
        """
        self._customer_ids = customer_ids

    @property
    def offset(self):
        r"""Gets the offset of this ListSubCustomerNewTagReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 示例1，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。 示例2，查询总数20条，期望每页返回10条数据，则获取第一页数据，入参offset填写0，limit填写10；获取第二页数据，入参offset填写10，limit填写10。

        :return: The offset of this ListSubCustomerNewTagReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubCustomerNewTagReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 示例1，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。 示例2，查询总数20条，期望每页返回10条数据，则获取第一页数据，入参offset填写0，limit填写10；获取第二页数据，入参offset填写10，limit填写10。

        :param offset: The offset of this ListSubCustomerNewTagReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubCustomerNewTagReq.

        每次查询的客户数量。默认值为10。

        :return: The limit of this ListSubCustomerNewTagReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubCustomerNewTagReq.

        每次查询的客户数量。默认值为10。

        :param limit: The limit of this ListSubCustomerNewTagReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def indirect_partner_id(self):
        r"""Gets the indirect_partner_id of this ListSubCustomerNewTagReq.

        云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的客户新客标签，必须携带该字段。除此之外，此参数不做处理。

        :return: The indirect_partner_id of this ListSubCustomerNewTagReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        r"""Sets the indirect_partner_id of this ListSubCustomerNewTagReq.

        云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的客户新客标签，必须携带该字段。除此之外，此参数不做处理。

        :param indirect_partner_id: The indirect_partner_id of this ListSubCustomerNewTagReq.
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
        if not isinstance(other, ListSubCustomerNewTagReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
