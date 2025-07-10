# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemFlowRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'issue_category': 'str',
        'flow_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'issue_category': 'issue_category',
        'flow_code': 'flow_code'
    }

    def __init__(self, id=None, issue_category=None, flow_code=None):
        r"""WorkItemFlowRequestBody

        The model defined in huaweicloud sdk

        :param id: 工作项唯一Id
        :type id: str
        :param issue_category: 工作项类型
        :type issue_category: str
        :param flow_code: 工作项流转code
        :type flow_code: str
        """
        
        

        self._id = None
        self._issue_category = None
        self._flow_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if issue_category is not None:
            self.issue_category = issue_category
        if flow_code is not None:
            self.flow_code = flow_code

    @property
    def id(self):
        r"""Gets the id of this WorkItemFlowRequestBody.

        工作项唯一Id

        :return: The id of this WorkItemFlowRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkItemFlowRequestBody.

        工作项唯一Id

        :param id: The id of this WorkItemFlowRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def issue_category(self):
        r"""Gets the issue_category of this WorkItemFlowRequestBody.

        工作项类型

        :return: The issue_category of this WorkItemFlowRequestBody.
        :rtype: str
        """
        return self._issue_category

    @issue_category.setter
    def issue_category(self, issue_category):
        r"""Sets the issue_category of this WorkItemFlowRequestBody.

        工作项类型

        :param issue_category: The issue_category of this WorkItemFlowRequestBody.
        :type issue_category: str
        """
        self._issue_category = issue_category

    @property
    def flow_code(self):
        r"""Gets the flow_code of this WorkItemFlowRequestBody.

        工作项流转code

        :return: The flow_code of this WorkItemFlowRequestBody.
        :rtype: str
        """
        return self._flow_code

    @flow_code.setter
    def flow_code(self, flow_code):
        r"""Sets the flow_code of this WorkItemFlowRequestBody.

        工作项流转code

        :param flow_code: The flow_code of this WorkItemFlowRequestBody.
        :type flow_code: str
        """
        self._flow_code = flow_code

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
        if not isinstance(other, WorkItemFlowRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
