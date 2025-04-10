# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlayDomainStreamInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'data_list': 'list[PlayDomainStreamInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'time': 'time',
        'data_list': 'data_list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, time=None, data_list=None, x_request_id=None):
        r"""ListPlayDomainStreamInfoResponse

        The model defined in huaweicloud sdk

        :param time: 采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。
        :type time: str
        :param data_list: 采样数据列表
        :type data_list: list[:class:`huaweicloudsdklive.v2.PlayDomainStreamInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListPlayDomainStreamInfoResponse, self).__init__()

        self._time = None
        self._data_list = None
        self._x_request_id = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if data_list is not None:
            self.data_list = data_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def time(self):
        r"""Gets the time of this ListPlayDomainStreamInfoResponse.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The time of this ListPlayDomainStreamInfoResponse.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ListPlayDomainStreamInfoResponse.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param time: The time of this ListPlayDomainStreamInfoResponse.
        :type time: str
        """
        self._time = time

    @property
    def data_list(self):
        r"""Gets the data_list of this ListPlayDomainStreamInfoResponse.

        采样数据列表

        :return: The data_list of this ListPlayDomainStreamInfoResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.PlayDomainStreamInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListPlayDomainStreamInfoResponse.

        采样数据列表

        :param data_list: The data_list of this ListPlayDomainStreamInfoResponse.
        :type data_list: list[:class:`huaweicloudsdklive.v2.PlayDomainStreamInfo`]
        """
        self._data_list = data_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListPlayDomainStreamInfoResponse.

        :return: The x_request_id of this ListPlayDomainStreamInfoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListPlayDomainStreamInfoResponse.

        :param x_request_id: The x_request_id of this ListPlayDomainStreamInfoResponse.
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
        if not isinstance(other, ListPlayDomainStreamInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
