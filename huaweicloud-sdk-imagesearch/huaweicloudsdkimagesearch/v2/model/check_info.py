# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'return_num': 'int',
        'last_item': 'SearchAfterParam'
    }

    attribute_map = {
        'total_num': 'total_num',
        'return_num': 'return_num',
        'last_item': 'last_item'
    }

    def __init__(self, total_num=None, return_num=None, last_item=None):
        """CheckInfo

        The model defined in huaweicloud sdk

        :param total_num: 符合条件的结果总数。
        :type total_num: int
        :param return_num: 返回的结果总数。
        :type return_num: int
        :param last_item: 
        :type last_item: :class:`huaweicloudsdkimagesearch.v2.SearchAfterParam`
        """
        
        

        self._total_num = None
        self._return_num = None
        self._last_item = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if return_num is not None:
            self.return_num = return_num
        if last_item is not None:
            self.last_item = last_item

    @property
    def total_num(self):
        """Gets the total_num of this CheckInfo.

        符合条件的结果总数。

        :return: The total_num of this CheckInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this CheckInfo.

        符合条件的结果总数。

        :param total_num: The total_num of this CheckInfo.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def return_num(self):
        """Gets the return_num of this CheckInfo.

        返回的结果总数。

        :return: The return_num of this CheckInfo.
        :rtype: int
        """
        return self._return_num

    @return_num.setter
    def return_num(self, return_num):
        """Sets the return_num of this CheckInfo.

        返回的结果总数。

        :param return_num: The return_num of this CheckInfo.
        :type return_num: int
        """
        self._return_num = return_num

    @property
    def last_item(self):
        """Gets the last_item of this CheckInfo.

        :return: The last_item of this CheckInfo.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.SearchAfterParam`
        """
        return self._last_item

    @last_item.setter
    def last_item(self, last_item):
        """Sets the last_item of this CheckInfo.

        :param last_item: The last_item of this CheckInfo.
        :type last_item: :class:`huaweicloudsdkimagesearch.v2.SearchAfterParam`
        """
        self._last_item = last_item

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
        if not isinstance(other, CheckInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
