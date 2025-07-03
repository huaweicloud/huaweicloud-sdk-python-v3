# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTicketParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'string_filters': 'list[ObjectFilter]',
        'sort_filter': 'ObjectFilter'
    }

    attribute_map = {
        'string_filters': 'string_filters',
        'sort_filter': 'sort_filter'
    }

    def __init__(self, string_filters=None, sort_filter=None):
        r"""ListTicketParams

        The model defined in huaweicloud sdk

        :param string_filters: 字符串搜索条件，可根据该条件搜索到具体的工单。
        :type string_filters: list[:class:`huaweicloudsdkcoc.v1.ObjectFilter`]
        :param sort_filter: 
        :type sort_filter: :class:`huaweicloudsdkcoc.v1.ObjectFilter`
        """
        
        

        self._string_filters = None
        self._sort_filter = None
        self.discriminator = None

        self.string_filters = string_filters
        if sort_filter is not None:
            self.sort_filter = sort_filter

    @property
    def string_filters(self):
        r"""Gets the string_filters of this ListTicketParams.

        字符串搜索条件，可根据该条件搜索到具体的工单。

        :return: The string_filters of this ListTicketParams.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ObjectFilter`]
        """
        return self._string_filters

    @string_filters.setter
    def string_filters(self, string_filters):
        r"""Sets the string_filters of this ListTicketParams.

        字符串搜索条件，可根据该条件搜索到具体的工单。

        :param string_filters: The string_filters of this ListTicketParams.
        :type string_filters: list[:class:`huaweicloudsdkcoc.v1.ObjectFilter`]
        """
        self._string_filters = string_filters

    @property
    def sort_filter(self):
        r"""Gets the sort_filter of this ListTicketParams.

        :return: The sort_filter of this ListTicketParams.
        :rtype: :class:`huaweicloudsdkcoc.v1.ObjectFilter`
        """
        return self._sort_filter

    @sort_filter.setter
    def sort_filter(self, sort_filter):
        r"""Sets the sort_filter of this ListTicketParams.

        :param sort_filter: The sort_filter of this ListTicketParams.
        :type sort_filter: :class:`huaweicloudsdkcoc.v1.ObjectFilter`
        """
        self._sort_filter = sort_filter

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
        if not isinstance(other, ListTicketParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
