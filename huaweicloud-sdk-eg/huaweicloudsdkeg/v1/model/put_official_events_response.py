# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutOfficialEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed_count': 'int',
        'events': 'list[PutEventsRespEvents]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'failed_count': 'failed_count',
        'events': 'events',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, failed_count=None, events=None, x_request_id=None):
        r"""PutOfficialEventsResponse

        The model defined in huaweicloud sdk

        :param failed_count: 发布失败的事件个数
        :type failed_count: int
        :param events: 事件列表
        :type events: list[:class:`huaweicloudsdkeg.v1.PutEventsRespEvents`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(PutOfficialEventsResponse, self).__init__()

        self._failed_count = None
        self._events = None
        self._x_request_id = None
        self.discriminator = None

        if failed_count is not None:
            self.failed_count = failed_count
        if events is not None:
            self.events = events
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def failed_count(self):
        r"""Gets the failed_count of this PutOfficialEventsResponse.

        发布失败的事件个数

        :return: The failed_count of this PutOfficialEventsResponse.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this PutOfficialEventsResponse.

        发布失败的事件个数

        :param failed_count: The failed_count of this PutOfficialEventsResponse.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def events(self):
        r"""Gets the events of this PutOfficialEventsResponse.

        事件列表

        :return: The events of this PutOfficialEventsResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.PutEventsRespEvents`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this PutOfficialEventsResponse.

        事件列表

        :param events: The events of this PutOfficialEventsResponse.
        :type events: list[:class:`huaweicloudsdkeg.v1.PutEventsRespEvents`]
        """
        self._events = events

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this PutOfficialEventsResponse.

        :return: The x_request_id of this PutOfficialEventsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this PutOfficialEventsResponse.

        :param x_request_id: The x_request_id of this PutOfficialEventsResponse.
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
        if not isinstance(other, PutOfficialEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
