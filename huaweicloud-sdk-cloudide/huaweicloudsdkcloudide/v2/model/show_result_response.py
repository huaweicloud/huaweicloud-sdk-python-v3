# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_status': 'RequestStatus',
        'tasks': 'list[TaskModel]',
        'request_type': 'str'
    }

    attribute_map = {
        'request_status': 'request_status',
        'tasks': 'tasks',
        'request_type': 'request_type'
    }

    def __init__(self, request_status=None, tasks=None, request_type=None):
        r"""ShowResultResponse

        The model defined in huaweicloud sdk

        :param request_status: 
        :type request_status: :class:`huaweicloudsdkcloudide.v2.RequestStatus`
        :param tasks: task list
        :type tasks: list[:class:`huaweicloudsdkcloudide.v2.TaskModel`]
        :param request_type: the type of the request
        :type request_type: str
        """
        
        super(ShowResultResponse, self).__init__()

        self._request_status = None
        self._tasks = None
        self._request_type = None
        self.discriminator = None

        if request_status is not None:
            self.request_status = request_status
        if tasks is not None:
            self.tasks = tasks
        if request_type is not None:
            self.request_type = request_type

    @property
    def request_status(self):
        r"""Gets the request_status of this ShowResultResponse.

        :return: The request_status of this ShowResultResponse.
        :rtype: :class:`huaweicloudsdkcloudide.v2.RequestStatus`
        """
        return self._request_status

    @request_status.setter
    def request_status(self, request_status):
        r"""Sets the request_status of this ShowResultResponse.

        :param request_status: The request_status of this ShowResultResponse.
        :type request_status: :class:`huaweicloudsdkcloudide.v2.RequestStatus`
        """
        self._request_status = request_status

    @property
    def tasks(self):
        r"""Gets the tasks of this ShowResultResponse.

        task list

        :return: The tasks of this ShowResultResponse.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.TaskModel`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ShowResultResponse.

        task list

        :param tasks: The tasks of this ShowResultResponse.
        :type tasks: list[:class:`huaweicloudsdkcloudide.v2.TaskModel`]
        """
        self._tasks = tasks

    @property
    def request_type(self):
        r"""Gets the request_type of this ShowResultResponse.

        the type of the request

        :return: The request_type of this ShowResultResponse.
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        r"""Sets the request_type of this ShowResultResponse.

        the type of the request

        :param request_type: The request_type of this ShowResultResponse.
        :type request_type: str
        """
        self._request_type = request_type

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
        if not isinstance(other, ShowResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
