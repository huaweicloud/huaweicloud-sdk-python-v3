# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUsageDataResponse(SdkResponse):

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
        'time_list': 'list[TimeResourceUsageInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'time_list': 'time_list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, count=None, time_list=None, x_request_id=None):
        r"""ShowUsageDataResponse

        The model defined in huaweicloud sdk

        :param count: 资源总数。
        :type count: int
        :param time_list: 资源用量列表
        :type time_list: list[:class:`huaweicloudsdkmetastudio.v1.TimeResourceUsageInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._count = None
        self._time_list = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if time_list is not None:
            self.time_list = time_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        r"""Gets the count of this ShowUsageDataResponse.

        资源总数。

        :return: The count of this ShowUsageDataResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowUsageDataResponse.

        资源总数。

        :param count: The count of this ShowUsageDataResponse.
        :type count: int
        """
        self._count = count

    @property
    def time_list(self):
        r"""Gets the time_list of this ShowUsageDataResponse.

        资源用量列表

        :return: The time_list of this ShowUsageDataResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.TimeResourceUsageInfo`]
        """
        return self._time_list

    @time_list.setter
    def time_list(self, time_list):
        r"""Sets the time_list of this ShowUsageDataResponse.

        资源用量列表

        :param time_list: The time_list of this ShowUsageDataResponse.
        :type time_list: list[:class:`huaweicloudsdkmetastudio.v1.TimeResourceUsageInfo`]
        """
        self._time_list = time_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowUsageDataResponse.

        :return: The x_request_id of this ShowUsageDataResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowUsageDataResponse.

        :param x_request_id: The x_request_id of this ShowUsageDataResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowUsageDataResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowUsageDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
