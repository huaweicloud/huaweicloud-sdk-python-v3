# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataobjectSearch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'sort_by': 'str',
        'order': 'str',
        'from_date': 'str',
        'to_date': 'str',
        'condition': 'DataobjectSearchCondition'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'sort_by': 'sort_by',
        'order': 'order',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'condition': 'condition'
    }

    def __init__(self, limit=None, offset=None, sort_by=None, order=None, from_date=None, to_date=None, condition=None):
        """DataobjectSearch

        The model defined in huaweicloud sdk

        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param sort_by: sortby
        :type sort_by: str
        :param order: order
        :type order: str
        :param from_date: search start time
        :type from_date: str
        :param to_date: search end time
        :type to_date: str
        :param condition: 
        :type condition: :class:`huaweicloudsdksa.v2.DataobjectSearchCondition`
        """
        
        

        self._limit = None
        self._offset = None
        self._sort_by = None
        self._order = None
        self._from_date = None
        self._to_date = None
        self._condition = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if condition is not None:
            self.condition = condition

    @property
    def limit(self):
        """Gets the limit of this DataobjectSearch.

        limit

        :return: The limit of this DataobjectSearch.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this DataobjectSearch.

        limit

        :param limit: The limit of this DataobjectSearch.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this DataobjectSearch.

        offset

        :return: The offset of this DataobjectSearch.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this DataobjectSearch.

        offset

        :param offset: The offset of this DataobjectSearch.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_by(self):
        """Gets the sort_by of this DataobjectSearch.

        sortby

        :return: The sort_by of this DataobjectSearch.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this DataobjectSearch.

        sortby

        :param sort_by: The sort_by of this DataobjectSearch.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        """Gets the order of this DataobjectSearch.

        order

        :return: The order of this DataobjectSearch.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this DataobjectSearch.

        order

        :param order: The order of this DataobjectSearch.
        :type order: str
        """
        self._order = order

    @property
    def from_date(self):
        """Gets the from_date of this DataobjectSearch.

        search start time

        :return: The from_date of this DataobjectSearch.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this DataobjectSearch.

        search start time

        :param from_date: The from_date of this DataobjectSearch.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this DataobjectSearch.

        search end time

        :return: The to_date of this DataobjectSearch.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this DataobjectSearch.

        search end time

        :param to_date: The to_date of this DataobjectSearch.
        :type to_date: str
        """
        self._to_date = to_date

    @property
    def condition(self):
        """Gets the condition of this DataobjectSearch.

        :return: The condition of this DataobjectSearch.
        :rtype: :class:`huaweicloudsdksa.v2.DataobjectSearchCondition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this DataobjectSearch.

        :param condition: The condition of this DataobjectSearch.
        :type condition: :class:`huaweicloudsdksa.v2.DataobjectSearchCondition`
        """
        self._condition = condition

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
        if not isinstance(other, DataobjectSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
