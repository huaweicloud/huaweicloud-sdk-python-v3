# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckInstanceForUpgradeResponse(SdkResponse):

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
        'x_request_id': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, workflow_id=None, x_request_id=None):
        r"""CheckInstanceForUpgradeResponse

        The model defined in huaweicloud sdk

        :param workflow_id: 工作流id
        :type workflow_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CheckInstanceForUpgradeResponse, self).__init__()

        self._workflow_id = None
        self._x_request_id = None
        self.discriminator = None

        if workflow_id is not None:
            self.workflow_id = workflow_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this CheckInstanceForUpgradeResponse.

        工作流id

        :return: The workflow_id of this CheckInstanceForUpgradeResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this CheckInstanceForUpgradeResponse.

        工作流id

        :param workflow_id: The workflow_id of this CheckInstanceForUpgradeResponse.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CheckInstanceForUpgradeResponse.

        :return: The x_request_id of this CheckInstanceForUpgradeResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CheckInstanceForUpgradeResponse.

        :param x_request_id: The x_request_id of this CheckInstanceForUpgradeResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CheckInstanceForUpgradeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
