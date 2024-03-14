# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRefreshTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'refresh_task': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'refresh_task': 'refresh_task',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, refresh_task=None, x_request_id=None):
        """CreateRefreshTasksResponse

        The model defined in huaweicloud sdk

        :param refresh_task: 任务ID。
        :type refresh_task: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateRefreshTasksResponse, self).__init__()

        self._refresh_task = None
        self._x_request_id = None
        self.discriminator = None

        if refresh_task is not None:
            self.refresh_task = refresh_task
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def refresh_task(self):
        """Gets the refresh_task of this CreateRefreshTasksResponse.

        任务ID。

        :return: The refresh_task of this CreateRefreshTasksResponse.
        :rtype: str
        """
        return self._refresh_task

    @refresh_task.setter
    def refresh_task(self, refresh_task):
        """Sets the refresh_task of this CreateRefreshTasksResponse.

        任务ID。

        :param refresh_task: The refresh_task of this CreateRefreshTasksResponse.
        :type refresh_task: str
        """
        self._refresh_task = refresh_task

    @property
    def x_request_id(self):
        """Gets the x_request_id of this CreateRefreshTasksResponse.

        :return: The x_request_id of this CreateRefreshTasksResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this CreateRefreshTasksResponse.

        :param x_request_id: The x_request_id of this CreateRefreshTasksResponse.
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
        if not isinstance(other, CreateRefreshTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
