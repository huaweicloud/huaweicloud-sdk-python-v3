# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'body': 'UpdateInstanceRequestBody'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'body': 'body'
    }

    def __init__(self, blockchain_id=None, body=None):
        r"""UpdateInstanceRequest

        The model defined in huaweicloud sdk

        :param blockchain_id: bcs 服务id
        :type blockchain_id: str
        :param body: Body of the UpdateInstanceRequest
        :type body: :class:`huaweicloudsdkbcs.v2.UpdateInstanceRequestBody`
        """
        
        

        self._blockchain_id = None
        self._body = None
        self.discriminator = None

        self.blockchain_id = blockchain_id
        if body is not None:
            self.body = body

    @property
    def blockchain_id(self):
        r"""Gets the blockchain_id of this UpdateInstanceRequest.

        bcs 服务id

        :return: The blockchain_id of this UpdateInstanceRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        r"""Sets the blockchain_id of this UpdateInstanceRequest.

        bcs 服务id

        :param blockchain_id: The blockchain_id of this UpdateInstanceRequest.
        :type blockchain_id: str
        """
        self._blockchain_id = blockchain_id

    @property
    def body(self):
        r"""Gets the body of this UpdateInstanceRequest.

        :return: The body of this UpdateInstanceRequest.
        :rtype: :class:`huaweicloudsdkbcs.v2.UpdateInstanceRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateInstanceRequest.

        :param body: The body of this UpdateInstanceRequest.
        :type body: :class:`huaweicloudsdkbcs.v2.UpdateInstanceRequestBody`
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
        if not isinstance(other, UpdateInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
