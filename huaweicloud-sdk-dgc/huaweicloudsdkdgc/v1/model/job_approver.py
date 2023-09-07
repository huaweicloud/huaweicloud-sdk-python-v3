# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobApprover:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approver_name': 'str'
    }

    attribute_map = {
        'approver_name': 'approverName'
    }

    def __init__(self, approver_name=None):
        """JobApprover

        The model defined in huaweicloud sdk

        :param approver_name: 审批人名称
        :type approver_name: str
        """
        
        

        self._approver_name = None
        self.discriminator = None

        self.approver_name = approver_name

    @property
    def approver_name(self):
        """Gets the approver_name of this JobApprover.

        审批人名称

        :return: The approver_name of this JobApprover.
        :rtype: str
        """
        return self._approver_name

    @approver_name.setter
    def approver_name(self, approver_name):
        """Sets the approver_name of this JobApprover.

        审批人名称

        :param approver_name: The approver_name of this JobApprover.
        :type approver_name: str
        """
        self._approver_name = approver_name

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
        if not isinstance(other, JobApprover):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
