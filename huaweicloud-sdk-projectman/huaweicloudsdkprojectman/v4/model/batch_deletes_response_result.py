# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeletesResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_issue': 'BatchDeletesResponseResultDeleteIssue'
    }

    attribute_map = {
        'delete_issue': 'delete_issue'
    }

    def __init__(self, delete_issue=None):
        r"""BatchDeletesResponseResult

        The model defined in huaweicloud sdk

        :param delete_issue: 
        :type delete_issue: :class:`huaweicloudsdkprojectman.v4.BatchDeletesResponseResultDeleteIssue`
        """
        
        

        self._delete_issue = None
        self.discriminator = None

        if delete_issue is not None:
            self.delete_issue = delete_issue

    @property
    def delete_issue(self):
        r"""Gets the delete_issue of this BatchDeletesResponseResult.

        :return: The delete_issue of this BatchDeletesResponseResult.
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchDeletesResponseResultDeleteIssue`
        """
        return self._delete_issue

    @delete_issue.setter
    def delete_issue(self, delete_issue):
        r"""Sets the delete_issue of this BatchDeletesResponseResult.

        :param delete_issue: The delete_issue of this BatchDeletesResponseResult.
        :type delete_issue: :class:`huaweicloudsdkprojectman.v4.BatchDeletesResponseResultDeleteIssue`
        """
        self._delete_issue = delete_issue

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchDeletesResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
