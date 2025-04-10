# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateChannelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_id': 'str'
    }

    attribute_map = {
        'operation_id': 'operation_id'
    }

    def __init__(self, operation_id=None):
        r"""BatchCreateChannelsResponse

        The model defined in huaweicloud sdk

        :param operation_id: 操作记录id
        :type operation_id: str
        """
        
        super(BatchCreateChannelsResponse, self).__init__()

        self._operation_id = None
        self.discriminator = None

        if operation_id is not None:
            self.operation_id = operation_id

    @property
    def operation_id(self):
        r"""Gets the operation_id of this BatchCreateChannelsResponse.

        操作记录id

        :return: The operation_id of this BatchCreateChannelsResponse.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        r"""Sets the operation_id of this BatchCreateChannelsResponse.

        操作记录id

        :param operation_id: The operation_id of this BatchCreateChannelsResponse.
        :type operation_id: str
        """
        self._operation_id = operation_id

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
        if not isinstance(other, BatchCreateChannelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
