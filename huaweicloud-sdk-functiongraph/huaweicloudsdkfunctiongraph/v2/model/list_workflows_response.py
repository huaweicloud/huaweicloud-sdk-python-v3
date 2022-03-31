# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'size': 'int',
        'workflows': 'list[ListWorkflowsResult]'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'workflows': 'workflows'
    }

    def __init__(self, total=None, size=None, workflows=None):
        """ListWorkflowsResponse - a model defined in huaweicloud sdk"""
        
        super(ListWorkflowsResponse, self).__init__()

        self._total = None
        self._size = None
        self._workflows = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if workflows is not None:
            self.workflows = workflows

    @property
    def total(self):
        """Gets the total of this ListWorkflowsResponse.

        返回所有满足条件的对象个数

        :return: The total of this ListWorkflowsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListWorkflowsResponse.

        返回所有满足条件的对象个数

        :param total: The total of this ListWorkflowsResponse.
        :type: int
        """
        self._total = total

    @property
    def size(self):
        """Gets the size of this ListWorkflowsResponse.

        返回对象的大小

        :return: The size of this ListWorkflowsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListWorkflowsResponse.

        返回对象的大小

        :param size: The size of this ListWorkflowsResponse.
        :type: int
        """
        self._size = size

    @property
    def workflows(self):
        """Gets the workflows of this ListWorkflowsResponse.

        返回的实体对象

        :return: The workflows of this ListWorkflowsResponse.
        :rtype: list[ListWorkflowsResult]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """Sets the workflows of this ListWorkflowsResponse.

        返回的实体对象

        :param workflows: The workflows of this ListWorkflowsResponse.
        :type: list[ListWorkflowsResult]
        """
        self._workflows = workflows

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
        if not isinstance(other, ListWorkflowsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other