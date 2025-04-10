# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteInfo:

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
        'delete_num': 'int'
    }

    attribute_map = {
        'total_num': 'total_num',
        'delete_num': 'delete_num'
    }

    def __init__(self, total_num=None, delete_num=None):
        r"""DeleteInfo

        The model defined in huaweicloud sdk

        :param total_num: 符合条件的结果总数。
        :type total_num: int
        :param delete_num: 本次删除的结果总数，目前一次请求最多删除100条结果。
        :type delete_num: int
        """
        
        

        self._total_num = None
        self._delete_num = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if delete_num is not None:
            self.delete_num = delete_num

    @property
    def total_num(self):
        r"""Gets the total_num of this DeleteInfo.

        符合条件的结果总数。

        :return: The total_num of this DeleteInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this DeleteInfo.

        符合条件的结果总数。

        :param total_num: The total_num of this DeleteInfo.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def delete_num(self):
        r"""Gets the delete_num of this DeleteInfo.

        本次删除的结果总数，目前一次请求最多删除100条结果。

        :return: The delete_num of this DeleteInfo.
        :rtype: int
        """
        return self._delete_num

    @delete_num.setter
    def delete_num(self, delete_num):
        r"""Sets the delete_num of this DeleteInfo.

        本次删除的结果总数，目前一次请求最多删除100条结果。

        :param delete_num: The delete_num of this DeleteInfo.
        :type delete_num: int
        """
        self._delete_num = delete_num

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
        if not isinstance(other, DeleteInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
