# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetSecurityGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'workflow_id': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflowId'
    }

    def __init__(self, workflow_id=None):
        """SetSecurityGroupResponse

        The model defined in huaweicloud sdk

        :param workflow_id: 任务ID
        :type workflow_id: str
        """
        
        super(SetSecurityGroupResponse, self).__init__()

        self._workflow_id = None
        self.discriminator = None

        if workflow_id is not None:
            self.workflow_id = workflow_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this SetSecurityGroupResponse.

        任务ID

        :return: The workflow_id of this SetSecurityGroupResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this SetSecurityGroupResponse.

        任务ID

        :param workflow_id: The workflow_id of this SetSecurityGroupResponse.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

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
        if not isinstance(other, SetSecurityGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
