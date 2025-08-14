# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetApplicationAssignmentConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'assignment_required': 'bool'
    }

    attribute_map = {
        'assignment_required': 'assignment_required'
    }

    def __init__(self, assignment_required=None):
        r"""GetApplicationAssignmentConfigurationResponse

        The model defined in huaweicloud sdk

        :param assignment_required: 应用程序是否需要分配
        :type assignment_required: bool
        """
        
        super(GetApplicationAssignmentConfigurationResponse, self).__init__()

        self._assignment_required = None
        self.discriminator = None

        if assignment_required is not None:
            self.assignment_required = assignment_required

    @property
    def assignment_required(self):
        r"""Gets the assignment_required of this GetApplicationAssignmentConfigurationResponse.

        应用程序是否需要分配

        :return: The assignment_required of this GetApplicationAssignmentConfigurationResponse.
        :rtype: bool
        """
        return self._assignment_required

    @assignment_required.setter
    def assignment_required(self, assignment_required):
        r"""Sets the assignment_required of this GetApplicationAssignmentConfigurationResponse.

        应用程序是否需要分配

        :param assignment_required: The assignment_required of this GetApplicationAssignmentConfigurationResponse.
        :type assignment_required: bool
        """
        self._assignment_required = assignment_required

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
        if not isinstance(other, GetApplicationAssignmentConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
