# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIssuedCouponQuotasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_id': 'str',
        'indirect_partner_id': 'str',
        'parent_quota_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'quota_id': 'quota_id',
        'indirect_partner_id': 'indirect_partner_id',
        'parent_quota_id': 'parent_quota_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, quota_id=None, indirect_partner_id=None, parent_quota_id=None, offset=None, limit=None):
        """ListIssuedCouponQuotasRequest

        The model defined in huaweicloud sdk

        :param quota_id: 云经销商的代金券额度ID。获取方法请参见查询优惠券额度。此参数不携带或携带值为空时，不作为筛选条件。
        :type quota_id: str
        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。如果需要查询云经销商伙伴的代金券额度，必须携带该字段。除此之外，此参数不做处理。
        :type indirect_partner_id: str
        :param parent_quota_id: 父额度ID，即华为云总经销商用于发放给云经销商代金券额度的额度ID。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。
        :type parent_quota_id: str
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询记录数。默认值为10。
        :type limit: int
        """
        
        

        self._quota_id = None
        self._indirect_partner_id = None
        self._parent_quota_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if quota_id is not None:
            self.quota_id = quota_id
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if parent_quota_id is not None:
            self.parent_quota_id = parent_quota_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def quota_id(self):
        """Gets the quota_id of this ListIssuedCouponQuotasRequest.

        云经销商的代金券额度ID。获取方法请参见查询优惠券额度。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The quota_id of this ListIssuedCouponQuotasRequest.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this ListIssuedCouponQuotasRequest.

        云经销商的代金券额度ID。获取方法请参见查询优惠券额度。此参数不携带或携带值为空时，不作为筛选条件。

        :param quota_id: The quota_id of this ListIssuedCouponQuotasRequest.
        :type quota_id: str
        """
        self._quota_id = quota_id

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListIssuedCouponQuotasRequest.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。如果需要查询云经销商伙伴的代金券额度，必须携带该字段。除此之外，此参数不做处理。

        :return: The indirect_partner_id of this ListIssuedCouponQuotasRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListIssuedCouponQuotasRequest.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。如果需要查询云经销商伙伴的代金券额度，必须携带该字段。除此之外，此参数不做处理。

        :param indirect_partner_id: The indirect_partner_id of this ListIssuedCouponQuotasRequest.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def parent_quota_id(self):
        """Gets the parent_quota_id of this ListIssuedCouponQuotasRequest.

        父额度ID，即华为云总经销商用于发放给云经销商代金券额度的额度ID。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :return: The parent_quota_id of this ListIssuedCouponQuotasRequest.
        :rtype: str
        """
        return self._parent_quota_id

    @parent_quota_id.setter
    def parent_quota_id(self, parent_quota_id):
        """Sets the parent_quota_id of this ListIssuedCouponQuotasRequest.

        父额度ID，即华为云总经销商用于发放给云经销商代金券额度的额度ID。此参数不携带时，不作为筛选条件；携带值为空或携带值为空串时，作为筛选条件。

        :param parent_quota_id: The parent_quota_id of this ListIssuedCouponQuotasRequest.
        :type parent_quota_id: str
        """
        self._parent_quota_id = parent_quota_id

    @property
    def offset(self):
        """Gets the offset of this ListIssuedCouponQuotasRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListIssuedCouponQuotasRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIssuedCouponQuotasRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListIssuedCouponQuotasRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListIssuedCouponQuotasRequest.

        每次查询记录数。默认值为10。

        :return: The limit of this ListIssuedCouponQuotasRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIssuedCouponQuotasRequest.

        每次查询记录数。默认值为10。

        :param limit: The limit of this ListIssuedCouponQuotasRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListIssuedCouponQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
