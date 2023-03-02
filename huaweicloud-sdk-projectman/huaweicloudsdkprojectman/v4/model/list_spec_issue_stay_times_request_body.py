# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpecIssueStayTimesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'issue_ids': 'list[str]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'issue_ids': 'issue_ids'
    }

    def __init__(self, project_id=None, issue_ids=None):
        """ListSpecIssueStayTimesRequestBody

        The model defined in huaweicloud sdk

        :param project_id: 项目uuid
        :type project_id: str
        :param issue_ids: 工作项id字符串列表
        :type issue_ids: list[str]
        """
        
        

        self._project_id = None
        self._issue_ids = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if issue_ids is not None:
            self.issue_ids = issue_ids

    @property
    def project_id(self):
        """Gets the project_id of this ListSpecIssueStayTimesRequestBody.

        项目uuid

        :return: The project_id of this ListSpecIssueStayTimesRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListSpecIssueStayTimesRequestBody.

        项目uuid

        :param project_id: The project_id of this ListSpecIssueStayTimesRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def issue_ids(self):
        """Gets the issue_ids of this ListSpecIssueStayTimesRequestBody.

        工作项id字符串列表

        :return: The issue_ids of this ListSpecIssueStayTimesRequestBody.
        :rtype: list[str]
        """
        return self._issue_ids

    @issue_ids.setter
    def issue_ids(self, issue_ids):
        """Sets the issue_ids of this ListSpecIssueStayTimesRequestBody.

        工作项id字符串列表

        :param issue_ids: The issue_ids of this ListSpecIssueStayTimesRequestBody.
        :type issue_ids: list[str]
        """
        self._issue_ids = issue_ids

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
        if not isinstance(other, ListSpecIssueStayTimesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
