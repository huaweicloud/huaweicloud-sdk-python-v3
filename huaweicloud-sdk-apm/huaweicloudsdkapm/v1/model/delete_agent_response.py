# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAgentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_status': 'int'
    }

    attribute_map = {
        'delete_status': 'delete_status'
    }

    def __init__(self, delete_status=None):
        r"""DeleteAgentResponse

        The model defined in huaweicloud sdk

        :param delete_status: 删除状态。
        :type delete_status: int
        """
        
        super(DeleteAgentResponse, self).__init__()

        self._delete_status = None
        self.discriminator = None

        if delete_status is not None:
            self.delete_status = delete_status

    @property
    def delete_status(self):
        r"""Gets the delete_status of this DeleteAgentResponse.

        删除状态。

        :return: The delete_status of this DeleteAgentResponse.
        :rtype: int
        """
        return self._delete_status

    @delete_status.setter
    def delete_status(self, delete_status):
        r"""Sets the delete_status of this DeleteAgentResponse.

        删除状态。

        :param delete_status: The delete_status of this DeleteAgentResponse.
        :type delete_status: int
        """
        self._delete_status = delete_status

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
        if not isinstance(other, DeleteAgentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
