# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckPutEventsResponse(SdkResponse):

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
        'sources': 'list[CheckPutEventsResult]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'failed_count': 'failed_count',
        'sources': 'sources',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, failed_count=None, sources=None, x_request_id=None):
        r"""CheckPutEventsResponse

        The model defined in huaweicloud sdk

        :param failed_count: 预校验发布事件失败的个数
        :type failed_count: int
        :param sources: 
        :type sources: list[:class:`huaweicloudsdkeg.v1.CheckPutEventsResult`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CheckPutEventsResponse, self).__init__()

        self._failed_count = None
        self._sources = None
        self._x_request_id = None
        self.discriminator = None

        if failed_count is not None:
            self.failed_count = failed_count
        if sources is not None:
            self.sources = sources
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def failed_count(self):
        r"""Gets the failed_count of this CheckPutEventsResponse.

        预校验发布事件失败的个数

        :return: The failed_count of this CheckPutEventsResponse.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this CheckPutEventsResponse.

        预校验发布事件失败的个数

        :param failed_count: The failed_count of this CheckPutEventsResponse.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def sources(self):
        r"""Gets the sources of this CheckPutEventsResponse.

        :return: The sources of this CheckPutEventsResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.CheckPutEventsResult`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this CheckPutEventsResponse.

        :param sources: The sources of this CheckPutEventsResponse.
        :type sources: list[:class:`huaweicloudsdkeg.v1.CheckPutEventsResult`]
        """
        self._sources = sources

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CheckPutEventsResponse.

        :return: The x_request_id of this CheckPutEventsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CheckPutEventsResponse.

        :param x_request_id: The x_request_id of this CheckPutEventsResponse.
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
        if not isinstance(other, CheckPutEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
