# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIssueV4Request:

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
        'issue_id': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'issue_id': 'issue_id'
    }

    def __init__(self, project_id=None, issue_id=None):
        """ShowIssueV4Request

        The model defined in huaweicloud sdk

        :param project_id: devcloud项目的32位id
        :type project_id: str
        :param issue_id: 工作项id
        :type issue_id: int
        """
        
        

        self._project_id = None
        self._issue_id = None
        self.discriminator = None

        self.project_id = project_id
        self.issue_id = issue_id

    @property
    def project_id(self):
        """Gets the project_id of this ShowIssueV4Request.

        devcloud项目的32位id

        :return: The project_id of this ShowIssueV4Request.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowIssueV4Request.

        devcloud项目的32位id

        :param project_id: The project_id of this ShowIssueV4Request.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def issue_id(self):
        """Gets the issue_id of this ShowIssueV4Request.

        工作项id

        :return: The issue_id of this ShowIssueV4Request.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this ShowIssueV4Request.

        工作项id

        :param issue_id: The issue_id of this ShowIssueV4Request.
        :type issue_id: int
        """
        self._issue_id = issue_id

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
        if not isinstance(other, ShowIssueV4Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
