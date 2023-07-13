# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceParamHistoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'histories': 'list[ParamGroupHistoryResult]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'histories': 'histories'
    }

    def __init__(self, total_count=None, histories=None):
        """ListInstanceParamHistoriesResponse

        The model defined in huaweicloud sdk

        :param total_count: 历史记录总数
        :type total_count: int
        :param histories: host列表
        :type histories: list[:class:`huaweicloudsdkrds.v3.ParamGroupHistoryResult`]
        """
        
        super(ListInstanceParamHistoriesResponse, self).__init__()

        self._total_count = None
        self._histories = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if histories is not None:
            self.histories = histories

    @property
    def total_count(self):
        """Gets the total_count of this ListInstanceParamHistoriesResponse.

        历史记录总数

        :return: The total_count of this ListInstanceParamHistoriesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListInstanceParamHistoriesResponse.

        历史记录总数

        :param total_count: The total_count of this ListInstanceParamHistoriesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def histories(self):
        """Gets the histories of this ListInstanceParamHistoriesResponse.

        host列表

        :return: The histories of this ListInstanceParamHistoriesResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ParamGroupHistoryResult`]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        """Sets the histories of this ListInstanceParamHistoriesResponse.

        host列表

        :param histories: The histories of this ListInstanceParamHistoriesResponse.
        :type histories: list[:class:`huaweicloudsdkrds.v3.ParamGroupHistoryResult`]
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
        if not isinstance(other, ListInstanceParamHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
