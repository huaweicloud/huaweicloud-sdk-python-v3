# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResolveTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolve_tasks': 'list[ListResolveTaskResult]',
        'page_info': 'Page'
    }

    attribute_map = {
        'resolve_tasks': 'resolve_tasks',
        'page_info': 'page_info'
    }

    def __init__(self, resolve_tasks=None, page_info=None):
        r"""ListResolveTasksResponse

        The model defined in huaweicloud sdk

        :param resolve_tasks: 解析任务列表。
        :type resolve_tasks: list[:class:`huaweicloudsdkkoomessage.v1.ListResolveTaskResult`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        
        super(ListResolveTasksResponse, self).__init__()

        self._resolve_tasks = None
        self._page_info = None
        self.discriminator = None

        if resolve_tasks is not None:
            self.resolve_tasks = resolve_tasks
        if page_info is not None:
            self.page_info = page_info

    @property
    def resolve_tasks(self):
        r"""Gets the resolve_tasks of this ListResolveTasksResponse.

        解析任务列表。

        :return: The resolve_tasks of this ListResolveTasksResponse.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.ListResolveTaskResult`]
        """
        return self._resolve_tasks

    @resolve_tasks.setter
    def resolve_tasks(self, resolve_tasks):
        r"""Sets the resolve_tasks of this ListResolveTasksResponse.

        解析任务列表。

        :param resolve_tasks: The resolve_tasks of this ListResolveTasksResponse.
        :type resolve_tasks: list[:class:`huaweicloudsdkkoomessage.v1.ListResolveTaskResult`]
        """
        self._resolve_tasks = resolve_tasks

    @property
    def page_info(self):
        r"""Gets the page_info of this ListResolveTasksResponse.

        :return: The page_info of this ListResolveTasksResponse.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListResolveTasksResponse.

        :param page_info: The page_info of this ListResolveTasksResponse.
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListResolveTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
