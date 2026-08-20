# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateSnapshotRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issues': 'list[BatchCreateSnapshotRequestIssues]'
    }

    attribute_map = {
        'issues': 'issues'
    }

    def __init__(self, issues=None):
        r"""BatchCreateSnapshotRequest

        The model defined in huaweicloud sdk

        :param issues: 需要创建快照的工作项数组。 每次最多支持对50个工作项创建快照。
        :type issues: list[:class:`huaweicloudsdkprojectman.v4.BatchCreateSnapshotRequestIssues`]
        """
        
        

        self._issues = None
        self.discriminator = None

        self.issues = issues

    @property
    def issues(self):
        r"""Gets the issues of this BatchCreateSnapshotRequest.

        需要创建快照的工作项数组。 每次最多支持对50个工作项创建快照。

        :return: The issues of this BatchCreateSnapshotRequest.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.BatchCreateSnapshotRequestIssues`]
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        r"""Sets the issues of this BatchCreateSnapshotRequest.

        需要创建快照的工作项数组。 每次最多支持对50个工作项创建快照。

        :param issues: The issues of this BatchCreateSnapshotRequest.
        :type issues: list[:class:`huaweicloudsdkprojectman.v4.BatchCreateSnapshotRequestIssues`]
        """
        self._issues = issues

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
        if not isinstance(other, BatchCreateSnapshotRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
