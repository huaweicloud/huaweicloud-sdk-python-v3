# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTicketParamsV2CountFilters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'filters': 'list[ObjectFilterV2]'
    }

    attribute_map = {
        'name': 'name',
        'filters': 'filters'
    }

    def __init__(self, name=None, filters=None):
        r"""ListTicketParamsV2CountFilters

        The model defined in huaweicloud sdk

        :param name: 过滤名称
        :type name: str
        :param filters: 批量计数
        :type filters: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        """
        
        

        self._name = None
        self._filters = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if filters is not None:
            self.filters = filters

    @property
    def name(self):
        r"""Gets the name of this ListTicketParamsV2CountFilters.

        过滤名称

        :return: The name of this ListTicketParamsV2CountFilters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTicketParamsV2CountFilters.

        过滤名称

        :param name: The name of this ListTicketParamsV2CountFilters.
        :type name: str
        """
        self._name = name

    @property
    def filters(self):
        r"""Gets the filters of this ListTicketParamsV2CountFilters.

        批量计数

        :return: The filters of this ListTicketParamsV2CountFilters.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this ListTicketParamsV2CountFilters.

        批量计数

        :param filters: The filters of this ListTicketParamsV2CountFilters.
        :type filters: list[:class:`huaweicloudsdkcoc.v1.ObjectFilterV2`]
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
        if not isinstance(other, ListTicketParamsV2CountFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
