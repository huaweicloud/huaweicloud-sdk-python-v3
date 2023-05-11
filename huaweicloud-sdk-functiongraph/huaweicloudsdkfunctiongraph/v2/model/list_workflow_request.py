# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowRequest:

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
        'offset': 'int',
        'enterprise_project': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'workflow_name': 'workflow_name',
        'limit': 'limit',
        'offset': 'offset',
        'enterprise_project': 'enterprise_project',
        'mode': 'mode'
    }

    def __init__(self, workflow_name=None, limit=None, offset=None, enterprise_project=None, mode=None):
        """ListWorkflowRequest

        The model defined in huaweicloud sdk

        :param workflow_name: 函数流名称
        :type workflow_name: str
        :param limit: 分页查询，每页显示的条目数量，默认值为200 limit大于200时，按照200处理
        :type limit: int
        :param offset: 分页查询，分页的偏移量，默认值为0 offset小于0时，按照0处理
        :type offset: int
        :param enterprise_project: 企业项目ID
        :type enterprise_project: str
        :param mode: 函数流模式 \&quot;NORMAL\&quot;标准函数流 \&quot;EXPRESS\&quot;快速函数流
        :type mode: str
        """
        
        

        self._workflow_name = None
        self._limit = None
        self._offset = None
        self._enterprise_project = None
        self._mode = None
        self.discriminator = None

        if workflow_name is not None:
            self.workflow_name = workflow_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project
        if mode is not None:
            self.mode = mode

    @property
    def workflow_name(self):
        """Gets the workflow_name of this ListWorkflowRequest.

        函数流名称

        :return: The workflow_name of this ListWorkflowRequest.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this ListWorkflowRequest.

        函数流名称

        :param workflow_name: The workflow_name of this ListWorkflowRequest.
        :type workflow_name: str
        """
        self._workflow_name = workflow_name

    @property
    def limit(self):
        """Gets the limit of this ListWorkflowRequest.

        分页查询，每页显示的条目数量，默认值为200 limit大于200时，按照200处理

        :return: The limit of this ListWorkflowRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWorkflowRequest.

        分页查询，每页显示的条目数量，默认值为200 limit大于200时，按照200处理

        :param limit: The limit of this ListWorkflowRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListWorkflowRequest.

        分页查询，分页的偏移量，默认值为0 offset小于0时，按照0处理

        :return: The offset of this ListWorkflowRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListWorkflowRequest.

        分页查询，分页的偏移量，默认值为0 offset小于0时，按照0处理

        :param offset: The offset of this ListWorkflowRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project(self):
        """Gets the enterprise_project of this ListWorkflowRequest.

        企业项目ID

        :return: The enterprise_project of this ListWorkflowRequest.
        :rtype: str
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        """Sets the enterprise_project of this ListWorkflowRequest.

        企业项目ID

        :param enterprise_project: The enterprise_project of this ListWorkflowRequest.
        :type enterprise_project: str
        """
        self._enterprise_project = enterprise_project

    @property
    def mode(self):
        """Gets the mode of this ListWorkflowRequest.

        函数流模式 \"NORMAL\"标准函数流 \"EXPRESS\"快速函数流

        :return: The mode of this ListWorkflowRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ListWorkflowRequest.

        函数流模式 \"NORMAL\"标准函数流 \"EXPRESS\"快速函数流

        :param mode: The mode of this ListWorkflowRequest.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, ListWorkflowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
