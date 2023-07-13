# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_id': 'str'
    }

    attribute_map = {
        'restore_id': 'restore_id'
    }

    def __init__(self, restore_id=None):
        """RestoreInstanceResponse

        The model defined in huaweicloud sdk

        :param restore_id: 恢复记录ID。
        :type restore_id: str
        """
        
        super(RestoreInstanceResponse, self).__init__()

        self._restore_id = None
        self.discriminator = None

        if restore_id is not None:
            self.restore_id = restore_id

    @property
    def restore_id(self):
        """Gets the restore_id of this RestoreInstanceResponse.

        恢复记录ID。

        :return: The restore_id of this RestoreInstanceResponse.
        :rtype: str
        """
        return self._restore_id

    @restore_id.setter
    def restore_id(self, restore_id):
        """Sets the restore_id of this RestoreInstanceResponse.

        恢复记录ID。

        :param restore_id: The restore_id of this RestoreInstanceResponse.
        :type restore_id: str
        """
        self._restore_id = restore_id

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
        if not isinstance(other, RestoreInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
