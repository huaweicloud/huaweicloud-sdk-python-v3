# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDictionaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'size': 'int',
        'dictionaries': 'list[Dictionary]'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'dictionaries': 'dictionaries'
    }

    def __init__(self, total=None, size=None, dictionaries=None):
        """ListDictionaryResponse

        The model defined in huaweicloud sdk

        :param total: 总数，与分页无关
        :type total: int
        :param size: 当前页的数量，小于等于请求里指定的limit
        :type size: int
        :param dictionaries: 字典列表
        :type dictionaries: list[:class:`huaweicloudsdkroma.v2.Dictionary`]
        """
        
        super(ListDictionaryResponse, self).__init__()

        self._total = None
        self._size = None
        self._dictionaries = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if dictionaries is not None:
            self.dictionaries = dictionaries

    @property
    def total(self):
        """Gets the total of this ListDictionaryResponse.

        总数，与分页无关

        :return: The total of this ListDictionaryResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListDictionaryResponse.

        总数，与分页无关

        :param total: The total of this ListDictionaryResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        """Gets the size of this ListDictionaryResponse.

        当前页的数量，小于等于请求里指定的limit

        :return: The size of this ListDictionaryResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListDictionaryResponse.

        当前页的数量，小于等于请求里指定的limit

        :param size: The size of this ListDictionaryResponse.
        :type size: int
        """
        self._size = size

    @property
    def dictionaries(self):
        """Gets the dictionaries of this ListDictionaryResponse.

        字典列表

        :return: The dictionaries of this ListDictionaryResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.Dictionary`]
        """
        return self._dictionaries

    @dictionaries.setter
    def dictionaries(self, dictionaries):
        """Sets the dictionaries of this ListDictionaryResponse.

        字典列表

        :param dictionaries: The dictionaries of this ListDictionaryResponse.
        :type dictionaries: list[:class:`huaweicloudsdkroma.v2.Dictionary`]
        """
        self._dictionaries = dictionaries

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
        if not isinstance(other, ListDictionaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
