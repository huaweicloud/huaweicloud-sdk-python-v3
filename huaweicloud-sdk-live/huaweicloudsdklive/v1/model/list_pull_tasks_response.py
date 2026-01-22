# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPullTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_infos': 'list[LivePullTaskInfo]',
        'request_id': 'str',
        'total': 'int'
    }

    attribute_map = {
        'task_infos': 'task_infos',
        'request_id': 'request_id',
        'total': 'total'
    }

    def __init__(self, task_infos=None, request_id=None, total=None):
        r"""ListPullTasksResponse

        The model defined in huaweicloud sdk

        :param task_infos: 直播拉流任务列表
        :type task_infos: list[:class:`huaweicloudsdklive.v1.LivePullTaskInfo`]
        :param request_id: 请求id
        :type request_id: str
        :param total: 任务条目数
        :type total: int
        """
        
        super().__init__()

        self._task_infos = None
        self._request_id = None
        self._total = None
        self.discriminator = None

        if task_infos is not None:
            self.task_infos = task_infos
        if request_id is not None:
            self.request_id = request_id
        if total is not None:
            self.total = total

    @property
    def task_infos(self):
        r"""Gets the task_infos of this ListPullTasksResponse.

        直播拉流任务列表

        :return: The task_infos of this ListPullTasksResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.LivePullTaskInfo`]
        """
        return self._task_infos

    @task_infos.setter
    def task_infos(self, task_infos):
        r"""Sets the task_infos of this ListPullTasksResponse.

        直播拉流任务列表

        :param task_infos: The task_infos of this ListPullTasksResponse.
        :type task_infos: list[:class:`huaweicloudsdklive.v1.LivePullTaskInfo`]
        """
        self._task_infos = task_infos

    @property
    def request_id(self):
        r"""Gets the request_id of this ListPullTasksResponse.

        请求id

        :return: The request_id of this ListPullTasksResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListPullTasksResponse.

        请求id

        :param request_id: The request_id of this ListPullTasksResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def total(self):
        r"""Gets the total of this ListPullTasksResponse.

        任务条目数

        :return: The total of this ListPullTasksResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListPullTasksResponse.

        任务条目数

        :param total: The total of this ListPullTasksResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListPullTasksResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListPullTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
