# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCostsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'time_condition': 'TimeCondition',
        'groupby': 'list[GroupBy]',
        'cost_type': 'str',
        'amount_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'filters': 'list[FilterV2]'
    }

    attribute_map = {
        'time_condition': 'time_condition',
        'groupby': 'groupby',
        'cost_type': 'cost_type',
        'amount_type': 'amount_type',
        'offset': 'offset',
        'limit': 'limit',
        'filters': 'filters'
    }

    def __init__(self, time_condition=None, groupby=None, cost_type=None, amount_type=None, offset=None, limit=None, filters=None):
        """ListCostsReq

        The model defined in huaweicloud sdk

        :param time_condition: 
        :type time_condition: :class:`huaweicloudsdkbss.v2.TimeCondition`
        :param groupby: 查询维度，具体请参见表 GroupBy。
        :type groupby: list[:class:`huaweicloudsdkbss.v2.GroupBy`]
        :param cost_type: 成本类型。UNBLENDED_COST：原始成本AMORTIZED_COST：摊销成本
        :type cost_type: str
        :param amount_type: 展示的金额类型。PAYMENT_AMOUNT：应付NET_AMOUNT：实付
        :type amount_type: str
        :param offset: 偏移量。从0开始，默认为0
        :type offset: int
        :param limit: 每次查询的记录数，默认为10
        :type limit: int
        :param filters: 过滤条件，具体请参见表 过滤条件。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。
        :type filters: list[:class:`huaweicloudsdkbss.v2.FilterV2`]
        """
        
        

        self._time_condition = None
        self._groupby = None
        self._cost_type = None
        self._amount_type = None
        self._offset = None
        self._limit = None
        self._filters = None
        self.discriminator = None

        self.time_condition = time_condition
        self.groupby = groupby
        self.cost_type = cost_type
        self.amount_type = amount_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if filters is not None:
            self.filters = filters

    @property
    def time_condition(self):
        """Gets the time_condition of this ListCostsReq.


        :return: The time_condition of this ListCostsReq.
        :rtype: :class:`huaweicloudsdkbss.v2.TimeCondition`
        """
        return self._time_condition

    @time_condition.setter
    def time_condition(self, time_condition):
        """Sets the time_condition of this ListCostsReq.


        :param time_condition: The time_condition of this ListCostsReq.
        :type time_condition: :class:`huaweicloudsdkbss.v2.TimeCondition`
        """
        self._time_condition = time_condition

    @property
    def groupby(self):
        """Gets the groupby of this ListCostsReq.

        查询维度，具体请参见表 GroupBy。

        :return: The groupby of this ListCostsReq.
        :rtype: list[:class:`huaweicloudsdkbss.v2.GroupBy`]
        """
        return self._groupby

    @groupby.setter
    def groupby(self, groupby):
        """Sets the groupby of this ListCostsReq.

        查询维度，具体请参见表 GroupBy。

        :param groupby: The groupby of this ListCostsReq.
        :type groupby: list[:class:`huaweicloudsdkbss.v2.GroupBy`]
        """
        self._groupby = groupby

    @property
    def cost_type(self):
        """Gets the cost_type of this ListCostsReq.

        成本类型。UNBLENDED_COST：原始成本AMORTIZED_COST：摊销成本

        :return: The cost_type of this ListCostsReq.
        :rtype: str
        """
        return self._cost_type

    @cost_type.setter
    def cost_type(self, cost_type):
        """Sets the cost_type of this ListCostsReq.

        成本类型。UNBLENDED_COST：原始成本AMORTIZED_COST：摊销成本

        :param cost_type: The cost_type of this ListCostsReq.
        :type cost_type: str
        """
        self._cost_type = cost_type

    @property
    def amount_type(self):
        """Gets the amount_type of this ListCostsReq.

        展示的金额类型。PAYMENT_AMOUNT：应付NET_AMOUNT：实付

        :return: The amount_type of this ListCostsReq.
        :rtype: str
        """
        return self._amount_type

    @amount_type.setter
    def amount_type(self, amount_type):
        """Sets the amount_type of this ListCostsReq.

        展示的金额类型。PAYMENT_AMOUNT：应付NET_AMOUNT：实付

        :param amount_type: The amount_type of this ListCostsReq.
        :type amount_type: str
        """
        self._amount_type = amount_type

    @property
    def offset(self):
        """Gets the offset of this ListCostsReq.

        偏移量。从0开始，默认为0

        :return: The offset of this ListCostsReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCostsReq.

        偏移量。从0开始，默认为0

        :param offset: The offset of this ListCostsReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCostsReq.

        每次查询的记录数，默认为10

        :return: The limit of this ListCostsReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCostsReq.

        每次查询的记录数，默认为10

        :param limit: The limit of this ListCostsReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def filters(self):
        """Gets the filters of this ListCostsReq.

        过滤条件，具体请参见表 过滤条件。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。

        :return: The filters of this ListCostsReq.
        :rtype: list[:class:`huaweicloudsdkbss.v2.FilterV2`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ListCostsReq.

        过滤条件，具体请参见表 过滤条件。此参数不携带或携带值为空列表或携带值为null时，不作为筛选条件。

        :param filters: The filters of this ListCostsReq.
        :type filters: list[:class:`huaweicloudsdkbss.v2.FilterV2`]
        """
        self._filters = filters

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
        if not isinstance(other, ListCostsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
