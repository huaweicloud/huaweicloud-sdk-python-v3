# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpdAttachmentByWorkItemIdRequest:

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
        'issue_id': 'str',
        'source_project_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'issue_id': 'issue_id',
        'source_project_id': 'source_project_id'
    }

    def __init__(self, project_id=None, issue_id=None, source_project_id=None):
        r"""ShowIpdAttachmentByWorkItemIdRequest

        The model defined in huaweicloud sdk

        :param project_id: 工作项所属项目Id
        :type project_id: str
        :param issue_id: 工作项Id
        :type issue_id: str
        :param source_project_id: 原始需求跨项目时，提出项目Id
        :type source_project_id: str
        """
        
        

        self._project_id = None
        self._issue_id = None
        self._source_project_id = None
        self.discriminator = None

        self.project_id = project_id
        self.issue_id = issue_id
        if source_project_id is not None:
            self.source_project_id = source_project_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowIpdAttachmentByWorkItemIdRequest.

        工作项所属项目Id

        :return: The project_id of this ShowIpdAttachmentByWorkItemIdRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowIpdAttachmentByWorkItemIdRequest.

        工作项所属项目Id

        :param project_id: The project_id of this ShowIpdAttachmentByWorkItemIdRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def issue_id(self):
        r"""Gets the issue_id of this ShowIpdAttachmentByWorkItemIdRequest.

        工作项Id

        :return: The issue_id of this ShowIpdAttachmentByWorkItemIdRequest.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this ShowIpdAttachmentByWorkItemIdRequest.

        工作项Id

        :param issue_id: The issue_id of this ShowIpdAttachmentByWorkItemIdRequest.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def source_project_id(self):
        r"""Gets the source_project_id of this ShowIpdAttachmentByWorkItemIdRequest.

        原始需求跨项目时，提出项目Id

        :return: The source_project_id of this ShowIpdAttachmentByWorkItemIdRequest.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        r"""Sets the source_project_id of this ShowIpdAttachmentByWorkItemIdRequest.

        原始需求跨项目时，提出项目Id

        :param source_project_id: The source_project_id of this ShowIpdAttachmentByWorkItemIdRequest.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

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
        if not isinstance(other, ShowIpdAttachmentByWorkItemIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
