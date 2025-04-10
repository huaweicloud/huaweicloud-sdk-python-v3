# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueryHttpCodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_series': 'list[HttpCodeSummary]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'data_series': 'data_series',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, data_series=None, x_request_id=None):
        r"""ListQueryHttpCodeResponse

        The model defined in huaweicloud sdk

        :param data_series: 基于时间轴的状态码
        :type data_series: list[:class:`huaweicloudsdklive.v2.HttpCodeSummary`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListQueryHttpCodeResponse, self).__init__()

        self._data_series = None
        self._x_request_id = None
        self.discriminator = None

        if data_series is not None:
            self.data_series = data_series
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def data_series(self):
        r"""Gets the data_series of this ListQueryHttpCodeResponse.

        基于时间轴的状态码

        :return: The data_series of this ListQueryHttpCodeResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.HttpCodeSummary`]
        """
        return self._data_series

    @data_series.setter
    def data_series(self, data_series):
        r"""Sets the data_series of this ListQueryHttpCodeResponse.

        基于时间轴的状态码

        :param data_series: The data_series of this ListQueryHttpCodeResponse.
        :type data_series: list[:class:`huaweicloudsdklive.v2.HttpCodeSummary`]
        """
        self._data_series = data_series

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListQueryHttpCodeResponse.

        :return: The x_request_id of this ListQueryHttpCodeResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListQueryHttpCodeResponse.

        :param x_request_id: The x_request_id of this ListQueryHttpCodeResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListQueryHttpCodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
