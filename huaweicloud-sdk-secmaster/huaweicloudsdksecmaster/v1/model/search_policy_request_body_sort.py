# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchPolicyRequestBodySort:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sort_by': 'str',
        'order': 'str'
    }

    attribute_map = {
        'sort_by': 'sort_by',
        'order': 'order'
    }

    def __init__(self, sort_by=None, order=None):
        r"""SearchPolicyRequestBodySort

        The model defined in huaweicloud sdk

        :param sort_by: 排序字段
        :type sort_by: str
        :param order: 顺序或倒序
        :type order: str
        """
        
        

        self._sort_by = None
        self._order = None
        self.discriminator = None

        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order

    @property
    def sort_by(self):
        r"""Gets the sort_by of this SearchPolicyRequestBodySort.

        排序字段

        :return: The sort_by of this SearchPolicyRequestBodySort.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this SearchPolicyRequestBodySort.

        排序字段

        :param sort_by: The sort_by of this SearchPolicyRequestBodySort.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        r"""Gets the order of this SearchPolicyRequestBodySort.

        顺序或倒序

        :return: The order of this SearchPolicyRequestBodySort.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this SearchPolicyRequestBodySort.

        顺序或倒序

        :param order: The order of this SearchPolicyRequestBodySort.
        :type order: str
        """
        self._order = order

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchPolicyRequestBodySort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
