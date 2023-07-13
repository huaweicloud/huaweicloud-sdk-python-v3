# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowExecutionsRequest:

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
        'x_enterprise_project_id': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'x_enterprise_project_id': 'x_enterprise_project_id'
    }

    def __init__(self, workflow_id=None, x_enterprise_project_id=None):
        """ListWorkflowExecutionsRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 任务id，从工作流命令列表中获取的工作流id。
        :type workflow_id: str
        :param x_enterprise_project_id: 所属的企业项目id。
        :type x_enterprise_project_id: str
        """
        
        

        self._workflow_id = None
        self._x_enterprise_project_id = None
        self.discriminator = None

        self.workflow_id = workflow_id
        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this ListWorkflowExecutionsRequest.

        任务id，从工作流命令列表中获取的工作流id。

        :return: The workflow_id of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this ListWorkflowExecutionsRequest.

        任务id，从工作流命令列表中获取的工作流id。

        :param workflow_id: The workflow_id of this ListWorkflowExecutionsRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this ListWorkflowExecutionsRequest.

        所属的企业项目id。

        :return: The x_enterprise_project_id of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this ListWorkflowExecutionsRequest.

        所属的企业项目id。

        :param x_enterprise_project_id: The x_enterprise_project_id of this ListWorkflowExecutionsRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

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
        if not isinstance(other, ListWorkflowExecutionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
