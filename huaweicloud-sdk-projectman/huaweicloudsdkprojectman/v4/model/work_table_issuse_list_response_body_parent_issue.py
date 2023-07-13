# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkTableIssuseListResponseBodyParentIssue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'subject': 'str'
    }

    attribute_map = {
        'id': 'id',
        'subject': 'subject'
    }

    def __init__(self, id=None, subject=None):
        """WorkTableIssuseListResponseBodyParentIssue

        The model defined in huaweicloud sdk

        :param id: 父工作项id
        :type id: int
        :param subject: 父工作项标题
        :type subject: str
        """
        
        

        self._id = None
        self._subject = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if subject is not None:
            self.subject = subject

    @property
    def id(self):
        """Gets the id of this WorkTableIssuseListResponseBodyParentIssue.

        父工作项id

        :return: The id of this WorkTableIssuseListResponseBodyParentIssue.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkTableIssuseListResponseBodyParentIssue.

        父工作项id

        :param id: The id of this WorkTableIssuseListResponseBodyParentIssue.
        :type id: int
        """
        self._id = id

    @property
    def subject(self):
        """Gets the subject of this WorkTableIssuseListResponseBodyParentIssue.

        父工作项标题

        :return: The subject of this WorkTableIssuseListResponseBodyParentIssue.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this WorkTableIssuseListResponseBodyParentIssue.

        父工作项标题

        :param subject: The subject of this WorkTableIssuseListResponseBodyParentIssue.
        :type subject: str
        """
        self._subject = subject

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
        if not isinstance(other, WorkTableIssuseListResponseBodyParentIssue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
