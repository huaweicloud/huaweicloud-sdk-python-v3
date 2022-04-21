# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'workflow_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workflow_name': 'workflow_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workflow_name=None, limit=None, offset=None):
        """ListWorkflowsRequest

        The model defined in huaweicloud sdk

        :param workflow_name: 函数流名称
        :type workflow_name: str
        :param limit: 分页查询，每页显示的条目数量，最大数量200，超过200后只返回200
        :type limit: int
        :param offset: 分页查询，分页的偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        """
        
        

        self._workflow_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if workflow_name is not None:
            self.workflow_name = workflow_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workflow_name(self):
        """Gets the workflow_name of this ListWorkflowsRequest.

        函数流名称

        :return: The workflow_name of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this ListWorkflowsRequest.

        函数流名称

        :param workflow_name: The workflow_name of this ListWorkflowsRequest.
        :type workflow_name: str
        """
        self._workflow_name = workflow_name

    @property
    def limit(self):
        """Gets the limit of this ListWorkflowsRequest.

        分页查询，每页显示的条目数量，最大数量200，超过200后只返回200

        :return: The limit of this ListWorkflowsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWorkflowsRequest.

        分页查询，每页显示的条目数量，最大数量200，超过200后只返回200

        :param limit: The limit of this ListWorkflowsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListWorkflowsRequest.

        分页查询，分页的偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListWorkflowsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListWorkflowsRequest.

        分页查询，分页的偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListWorkflowsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListWorkflowsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
