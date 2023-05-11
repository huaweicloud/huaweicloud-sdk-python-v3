# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowTriggersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflow_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort'
    }

    def __init__(self, workflow_id=None, offset=None, limit=None, sort=None):
        """ListWorkflowTriggersRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 目标函数流的id
        :type workflow_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量不能小于0
        :type offset: int
        :param limit: 每页显示的条目数量，不能小于1或大于1000
        :type limit: int
        :param sort: 指定查询排序
        :type sort: str
        """
        
        

        self._workflow_id = None
        self._offset = None
        self._limit = None
        self._sort = None
        self.discriminator = None

        self.workflow_id = workflow_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort is not None:
            self.sort = sort

    @property
    def workflow_id(self):
        """Gets the workflow_id of this ListWorkflowTriggersRequest.

        目标函数流的id

        :return: The workflow_id of this ListWorkflowTriggersRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this ListWorkflowTriggersRequest.

        目标函数流的id

        :param workflow_id: The workflow_id of this ListWorkflowTriggersRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def offset(self):
        """Gets the offset of this ListWorkflowTriggersRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :return: The offset of this ListWorkflowTriggersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListWorkflowTriggersRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :param offset: The offset of this ListWorkflowTriggersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListWorkflowTriggersRequest.

        每页显示的条目数量，不能小于1或大于1000

        :return: The limit of this ListWorkflowTriggersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWorkflowTriggersRequest.

        每页显示的条目数量，不能小于1或大于1000

        :param limit: The limit of this ListWorkflowTriggersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort(self):
        """Gets the sort of this ListWorkflowTriggersRequest.

        指定查询排序

        :return: The sort of this ListWorkflowTriggersRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListWorkflowTriggersRequest.

        指定查询排序

        :param sort: The sort of this ListWorkflowTriggersRequest.
        :type sort: str
        """
        self._sort = sort

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
        if not isinstance(other, ListWorkflowTriggersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
