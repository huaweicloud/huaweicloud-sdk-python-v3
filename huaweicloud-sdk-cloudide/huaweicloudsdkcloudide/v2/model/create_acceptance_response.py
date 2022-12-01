# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAcceptanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'acceptance_id': 'int'
    }

    attribute_map = {
        'acceptance_id': 'acceptance_id'
    }

    def __init__(self, acceptance_id=None):
        """CreateAcceptanceResponse

        The model defined in huaweicloud sdk

        :param acceptance_id: acceptance_id
        :type acceptance_id: int
        """
        
        super(CreateAcceptanceResponse, self).__init__()

        self._acceptance_id = None
        self.discriminator = None

        if acceptance_id is not None:
            self.acceptance_id = acceptance_id

    @property
    def acceptance_id(self):
        """Gets the acceptance_id of this CreateAcceptanceResponse.

        acceptance_id

        :return: The acceptance_id of this CreateAcceptanceResponse.
        :rtype: int
        """
        return self._acceptance_id

    @acceptance_id.setter
    def acceptance_id(self, acceptance_id):
        """Sets the acceptance_id of this CreateAcceptanceResponse.

        acceptance_id

        :param acceptance_id: The acceptance_id of this CreateAcceptanceResponse.
        :type acceptance_id: int
        """
        self._acceptance_id = acceptance_id

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
        if not isinstance(other, CreateAcceptanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
