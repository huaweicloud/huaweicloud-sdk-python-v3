# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupSumDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'open_merge_requests_count': 'int'
    }

    attribute_map = {
        'open_merge_requests_count': 'open_merge_requests_count'
    }

    def __init__(self, open_merge_requests_count=None):
        r"""GroupSumDto

        The model defined in huaweicloud sdk

        :param open_merge_requests_count: 打开状态MR计数
        :type open_merge_requests_count: int
        """
        
        

        self._open_merge_requests_count = None
        self.discriminator = None

        if open_merge_requests_count is not None:
            self.open_merge_requests_count = open_merge_requests_count

    @property
    def open_merge_requests_count(self):
        r"""Gets the open_merge_requests_count of this GroupSumDto.

        打开状态MR计数

        :return: The open_merge_requests_count of this GroupSumDto.
        :rtype: int
        """
        return self._open_merge_requests_count

    @open_merge_requests_count.setter
    def open_merge_requests_count(self, open_merge_requests_count):
        r"""Sets the open_merge_requests_count of this GroupSumDto.

        打开状态MR计数

        :param open_merge_requests_count: The open_merge_requests_count of this GroupSumDto.
        :type open_merge_requests_count: int
        """
        self._open_merge_requests_count = open_merge_requests_count

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
        if not isinstance(other, GroupSumDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
