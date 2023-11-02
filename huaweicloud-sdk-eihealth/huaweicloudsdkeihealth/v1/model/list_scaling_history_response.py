# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScalingHistoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'histories': 'list[ScalingHistory]'
    }

    attribute_map = {
        'count': 'count',
        'histories': 'histories'
    }

    def __init__(self, count=None, histories=None):
        """ListScalingHistoryResponse

        The model defined in huaweicloud sdk

        :param count: 伸缩历史总数
        :type count: int
        :param histories: 伸缩历史列表
        :type histories: list[:class:`huaweicloudsdkeihealth.v1.ScalingHistory`]
        """
        
        super(ListScalingHistoryResponse, self).__init__()

        self._count = None
        self._histories = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if histories is not None:
            self.histories = histories

    @property
    def count(self):
        """Gets the count of this ListScalingHistoryResponse.

        伸缩历史总数

        :return: The count of this ListScalingHistoryResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListScalingHistoryResponse.

        伸缩历史总数

        :param count: The count of this ListScalingHistoryResponse.
        :type count: int
        """
        self._count = count

    @property
    def histories(self):
        """Gets the histories of this ListScalingHistoryResponse.

        伸缩历史列表

        :return: The histories of this ListScalingHistoryResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ScalingHistory`]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        """Sets the histories of this ListScalingHistoryResponse.

        伸缩历史列表

        :param histories: The histories of this ListScalingHistoryResponse.
        :type histories: list[:class:`huaweicloudsdkeihealth.v1.ScalingHistory`]
        """
        self._histories = histories

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
        if not isinstance(other, ListScalingHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
