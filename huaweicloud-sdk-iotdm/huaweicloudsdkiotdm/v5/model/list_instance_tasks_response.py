# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'Page',
        'tasks': 'list[InstanceTask]'
    }

    attribute_map = {
        'page': 'page',
        'tasks': 'tasks'
    }

    def __init__(self, page=None, tasks=None):
        r"""ListInstanceTasksResponse

        The model defined in huaweicloud sdk

        :param page: 
        :type page: :class:`huaweicloudsdkiotdm.v5.Page`
        :param tasks: 实例任务列表
        :type tasks: list[:class:`huaweicloudsdkiotdm.v5.InstanceTask`]
        """
        
        super(ListInstanceTasksResponse, self).__init__()

        self._page = None
        self._tasks = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if tasks is not None:
            self.tasks = tasks

    @property
    def page(self):
        r"""Gets the page of this ListInstanceTasksResponse.

        :return: The page of this ListInstanceTasksResponse.
        :rtype: :class:`huaweicloudsdkiotdm.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListInstanceTasksResponse.

        :param page: The page of this ListInstanceTasksResponse.
        :type page: :class:`huaweicloudsdkiotdm.v5.Page`
        """
        self._page = page

    @property
    def tasks(self):
        r"""Gets the tasks of this ListInstanceTasksResponse.

        实例任务列表

        :return: The tasks of this ListInstanceTasksResponse.
        :rtype: list[:class:`huaweicloudsdkiotdm.v5.InstanceTask`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListInstanceTasksResponse.

        实例任务列表

        :param tasks: The tasks of this ListInstanceTasksResponse.
        :type tasks: list[:class:`huaweicloudsdkiotdm.v5.InstanceTask`]
        """
        self._tasks = tasks

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
        if not isinstance(other, ListInstanceTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
