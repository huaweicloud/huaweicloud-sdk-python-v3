# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflows': 'list[WorkflowListDto]',
        'count': 'int'
    }

    attribute_map = {
        'workflows': 'workflows',
        'count': 'count'
    }

    def __init__(self, workflows=None, count=None):
        """ListWorkflowResponse

        The model defined in huaweicloud sdk

        :param workflows: 所查询类型的流程总数
        :type workflows: list[:class:`huaweicloudsdkeihealth.v1.WorkflowListDto`]
        :param count: 当前页的流程列表
        :type count: int
        """
        
        super(ListWorkflowResponse, self).__init__()

        self._workflows = None
        self._count = None
        self.discriminator = None

        if workflows is not None:
            self.workflows = workflows
        if count is not None:
            self.count = count

    @property
    def workflows(self):
        """Gets the workflows of this ListWorkflowResponse.

        所查询类型的流程总数

        :return: The workflows of this ListWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.WorkflowListDto`]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """Sets the workflows of this ListWorkflowResponse.

        所查询类型的流程总数

        :param workflows: The workflows of this ListWorkflowResponse.
        :type workflows: list[:class:`huaweicloudsdkeihealth.v1.WorkflowListDto`]
        """
        self._workflows = workflows

    @property
    def count(self):
        """Gets the count of this ListWorkflowResponse.

        当前页的流程列表

        :return: The count of this ListWorkflowResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListWorkflowResponse.

        当前页的流程列表

        :param count: The count of this ListWorkflowResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListWorkflowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
