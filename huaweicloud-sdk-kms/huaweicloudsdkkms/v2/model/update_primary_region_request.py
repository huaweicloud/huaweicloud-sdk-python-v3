# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrimaryRegionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'body': 'UpdatePrimaryRegionRequestBody'
    }

    attribute_map = {
        'key_id': 'key_id',
        'body': 'body'
    }

    def __init__(self, key_id=None, body=None):
        """UpdatePrimaryRegionRequest

        The model defined in huaweicloud sdk

        :param key_id: 待更新的密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。
        :type key_id: str
        :param body: Body of the UpdatePrimaryRegionRequest
        :type body: :class:`huaweicloudsdkkms.v2.UpdatePrimaryRegionRequestBody`
        """
        
        

        self._key_id = None
        self._body = None
        self.discriminator = None

        self.key_id = key_id
        if body is not None:
            self.body = body

    @property
    def key_id(self):
        """Gets the key_id of this UpdatePrimaryRegionRequest.

        待更新的密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this UpdatePrimaryRegionRequest.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this UpdatePrimaryRegionRequest.

        待更新的密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this UpdatePrimaryRegionRequest.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def body(self):
        """Gets the body of this UpdatePrimaryRegionRequest.

        :return: The body of this UpdatePrimaryRegionRequest.
        :rtype: :class:`huaweicloudsdkkms.v2.UpdatePrimaryRegionRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdatePrimaryRegionRequest.

        :param body: The body of this UpdatePrimaryRegionRequest.
        :type body: :class:`huaweicloudsdkkms.v2.UpdatePrimaryRegionRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdatePrimaryRegionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
