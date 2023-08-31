# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeIegPasswordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ieg_id': 'str',
        'body': 'ChangePasswordBody'
    }

    attribute_map = {
        'ieg_id': 'ieg_id',
        'body': 'body'
    }

    def __init__(self, ieg_id=None, body=None):
        """ChangeIegPasswordRequest

        The model defined in huaweicloud sdk

        :param ieg_id: 智能企业网关ID
        :type ieg_id: str
        :param body: Body of the ChangeIegPasswordRequest
        :type body: :class:`huaweicloudsdkec.v1.ChangePasswordBody`
        """
        
        

        self._ieg_id = None
        self._body = None
        self.discriminator = None

        self.ieg_id = ieg_id
        if body is not None:
            self.body = body

    @property
    def ieg_id(self):
        """Gets the ieg_id of this ChangeIegPasswordRequest.

        智能企业网关ID

        :return: The ieg_id of this ChangeIegPasswordRequest.
        :rtype: str
        """
        return self._ieg_id

    @ieg_id.setter
    def ieg_id(self, ieg_id):
        """Sets the ieg_id of this ChangeIegPasswordRequest.

        智能企业网关ID

        :param ieg_id: The ieg_id of this ChangeIegPasswordRequest.
        :type ieg_id: str
        """
        self._ieg_id = ieg_id

    @property
    def body(self):
        """Gets the body of this ChangeIegPasswordRequest.

        :return: The body of this ChangeIegPasswordRequest.
        :rtype: :class:`huaweicloudsdkec.v1.ChangePasswordBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ChangeIegPasswordRequest.

        :param body: The body of this ChangeIegPasswordRequest.
        :type body: :class:`huaweicloudsdkec.v1.ChangePasswordBody`
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
        if not isinstance(other, ChangeIegPasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
