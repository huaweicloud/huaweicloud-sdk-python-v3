# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestartEncodeServerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'encode_server_ids': 'list[str]'
    }

    attribute_map = {
        'encode_server_ids': 'encode_server_ids'
    }

    def __init__(self, encode_server_ids=None):
        """RestartEncodeServerRequestBody

        The model defined in huaweicloud sdk

        :param encode_server_ids: 待重启的编码服务的ID
        :type encode_server_ids: list[str]
        """
        
        

        self._encode_server_ids = None
        self.discriminator = None

        self.encode_server_ids = encode_server_ids

    @property
    def encode_server_ids(self):
        """Gets the encode_server_ids of this RestartEncodeServerRequestBody.

        待重启的编码服务的ID

        :return: The encode_server_ids of this RestartEncodeServerRequestBody.
        :rtype: list[str]
        """
        return self._encode_server_ids

    @encode_server_ids.setter
    def encode_server_ids(self, encode_server_ids):
        """Sets the encode_server_ids of this RestartEncodeServerRequestBody.

        待重启的编码服务的ID

        :param encode_server_ids: The encode_server_ids of this RestartEncodeServerRequestBody.
        :type encode_server_ids: list[str]
        """
        self._encode_server_ids = encode_server_ids

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
        if not isinstance(other, RestartEncodeServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
