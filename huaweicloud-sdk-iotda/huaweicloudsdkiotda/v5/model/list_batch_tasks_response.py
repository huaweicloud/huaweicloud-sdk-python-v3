# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBatchTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batchtasks': 'list[Task]',
        'page': 'Page'
    }

    attribute_map = {
        'batchtasks': 'batchtasks',
        'page': 'page'
    }

    def __init__(self, batchtasks=None, page=None):
        r"""ListBatchTasksResponse

        The model defined in huaweicloud sdk

        :param batchtasks: 批量任务列表。
        :type batchtasks: list[:class:`huaweicloudsdkiotda.v5.Task`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super(ListBatchTasksResponse, self).__init__()

        self._batchtasks = None
        self._page = None
        self.discriminator = None

        if batchtasks is not None:
            self.batchtasks = batchtasks
        if page is not None:
            self.page = page

    @property
    def batchtasks(self):
        r"""Gets the batchtasks of this ListBatchTasksResponse.

        批量任务列表。

        :return: The batchtasks of this ListBatchTasksResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.Task`]
        """
        return self._batchtasks

    @batchtasks.setter
    def batchtasks(self, batchtasks):
        r"""Sets the batchtasks of this ListBatchTasksResponse.

        批量任务列表。

        :param batchtasks: The batchtasks of this ListBatchTasksResponse.
        :type batchtasks: list[:class:`huaweicloudsdkiotda.v5.Task`]
        """
        self._batchtasks = batchtasks

    @property
    def page(self):
        r"""Gets the page of this ListBatchTasksResponse.

        :return: The page of this ListBatchTasksResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListBatchTasksResponse.

        :param page: The page of this ListBatchTasksResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

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
        if not isinstance(other, ListBatchTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
