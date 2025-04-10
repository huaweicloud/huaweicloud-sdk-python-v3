# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSmartLiveResponse(SdkResponse):

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
        'smart_live_jobs': 'list[SmartLiveJob]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'smart_live_jobs': 'smart_live_jobs',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, count=None, smart_live_jobs=None, x_request_id=None):
        r"""ListSmartLiveResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 数字人直播任务总数。
        :type count: int
        :param smart_live_jobs: 数字人直播任务列表。
        :type smart_live_jobs: list[:class:`huaweicloudsdkmetastudio.v1.SmartLiveJob`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListSmartLiveResponse, self).__init__()

        self._count = None
        self._smart_live_jobs = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if smart_live_jobs is not None:
            self.smart_live_jobs = smart_live_jobs
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        r"""Gets the count of this ListSmartLiveResponse.

        **参数解释**： 数字人直播任务总数。

        :return: The count of this ListSmartLiveResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSmartLiveResponse.

        **参数解释**： 数字人直播任务总数。

        :param count: The count of this ListSmartLiveResponse.
        :type count: int
        """
        self._count = count

    @property
    def smart_live_jobs(self):
        r"""Gets the smart_live_jobs of this ListSmartLiveResponse.

        数字人直播任务列表。

        :return: The smart_live_jobs of this ListSmartLiveResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SmartLiveJob`]
        """
        return self._smart_live_jobs

    @smart_live_jobs.setter
    def smart_live_jobs(self, smart_live_jobs):
        r"""Sets the smart_live_jobs of this ListSmartLiveResponse.

        数字人直播任务列表。

        :param smart_live_jobs: The smart_live_jobs of this ListSmartLiveResponse.
        :type smart_live_jobs: list[:class:`huaweicloudsdkmetastudio.v1.SmartLiveJob`]
        """
        self._smart_live_jobs = smart_live_jobs

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListSmartLiveResponse.

        :return: The x_request_id of this ListSmartLiveResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListSmartLiveResponse.

        :param x_request_id: The x_request_id of this ListSmartLiveResponse.
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
        if not isinstance(other, ListSmartLiveResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
