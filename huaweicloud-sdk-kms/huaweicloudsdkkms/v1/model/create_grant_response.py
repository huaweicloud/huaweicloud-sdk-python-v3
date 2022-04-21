# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGrantResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'grant_id': 'str'
    }

    attribute_map = {
        'grant_id': 'grant_id'
    }

    def __init__(self, grant_id=None):
        """CreateGrantResponse

        The model defined in huaweicloud sdk

        :param grant_id: 授权ID，64字节。
        :type grant_id: str
        """
        
        super(CreateGrantResponse, self).__init__()

        self._grant_id = None
        self.discriminator = None

        if grant_id is not None:
            self.grant_id = grant_id

    @property
    def grant_id(self):
        """Gets the grant_id of this CreateGrantResponse.

        授权ID，64字节。

        :return: The grant_id of this CreateGrantResponse.
        :rtype: str
        """
        return self._grant_id

    @grant_id.setter
    def grant_id(self, grant_id):
        """Sets the grant_id of this CreateGrantResponse.

        授权ID，64字节。

        :param grant_id: The grant_id of this CreateGrantResponse.
        :type grant_id: str
        """
        self._grant_id = grant_id

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
        if not isinstance(other, CreateGrantResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
