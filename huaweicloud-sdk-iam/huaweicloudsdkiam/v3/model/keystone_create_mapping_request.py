# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneCreateMappingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'body': 'KeystoneCreateMappingRequestBody'
    }

    attribute_map = {
        'id': 'id',
        'body': 'body'
    }

    def __init__(self, id=None, body=None):
        """KeystoneCreateMappingRequest

        The model defined in huaweicloud sdk

        :param id: 待注册的映射ID。
        :type id: str
        :param body: Body of the KeystoneCreateMappingRequest
        :type body: :class:`huaweicloudsdkiam.v3.KeystoneCreateMappingRequestBody`
        """
        
        

        self._id = None
        self._body = None
        self.discriminator = None

        self.id = id
        if body is not None:
            self.body = body

    @property
    def id(self):
        """Gets the id of this KeystoneCreateMappingRequest.

        待注册的映射ID。

        :return: The id of this KeystoneCreateMappingRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KeystoneCreateMappingRequest.

        待注册的映射ID。

        :param id: The id of this KeystoneCreateMappingRequest.
        :type id: str
        """
        self._id = id

    @property
    def body(self):
        """Gets the body of this KeystoneCreateMappingRequest.

        :return: The body of this KeystoneCreateMappingRequest.
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateMappingRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this KeystoneCreateMappingRequest.

        :param body: The body of this KeystoneCreateMappingRequest.
        :type body: :class:`huaweicloudsdkiam.v3.KeystoneCreateMappingRequestBody`
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
        if not isinstance(other, KeystoneCreateMappingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
