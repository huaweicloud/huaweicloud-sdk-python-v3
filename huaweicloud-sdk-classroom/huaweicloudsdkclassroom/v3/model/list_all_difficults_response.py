# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllDifficultsResponse(SdkResponse):

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
        'data': 'list[DifficultInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'data': 'data'
    }

    def __init__(self, total_count=None, data=None):
        r"""ListAllDifficultsResponse

        The model defined in huaweicloud sdk

        :param total_count: 所有难度数量
        :type total_count: int
        :param data: 难度信息
        :type data: list[:class:`huaweicloudsdkclassroom.v3.DifficultInfo`]
        """
        
        super(ListAllDifficultsResponse, self).__init__()

        self._total_count = None
        self._data = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if data is not None:
            self.data = data

    @property
    def total_count(self):
        r"""Gets the total_count of this ListAllDifficultsResponse.

        所有难度数量

        :return: The total_count of this ListAllDifficultsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListAllDifficultsResponse.

        所有难度数量

        :param total_count: The total_count of this ListAllDifficultsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def data(self):
        r"""Gets the data of this ListAllDifficultsResponse.

        难度信息

        :return: The data of this ListAllDifficultsResponse.
        :rtype: list[:class:`huaweicloudsdkclassroom.v3.DifficultInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListAllDifficultsResponse.

        难度信息

        :param data: The data of this ListAllDifficultsResponse.
        :type data: list[:class:`huaweicloudsdkclassroom.v3.DifficultInfo`]
        """
        self._data = data

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
        if not isinstance(other, ListAllDifficultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
