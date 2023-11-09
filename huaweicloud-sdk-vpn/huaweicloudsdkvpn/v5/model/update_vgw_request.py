# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVgwRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vgw_id': 'str',
        'body': 'UpdateVgwRequestBody'
    }

    attribute_map = {
        'vgw_id': 'vgw_id',
        'body': 'body'
    }

    def __init__(self, vgw_id=None, body=None):
        """UpdateVgwRequest

        The model defined in huaweicloud sdk

        :param vgw_id: VPN网关实例ID
        :type vgw_id: str
        :param body: Body of the UpdateVgwRequest
        :type body: :class:`huaweicloudsdkvpn.v5.UpdateVgwRequestBody`
        """
        
        

        self._vgw_id = None
        self._body = None
        self.discriminator = None

        self.vgw_id = vgw_id
        if body is not None:
            self.body = body

    @property
    def vgw_id(self):
        """Gets the vgw_id of this UpdateVgwRequest.

        VPN网关实例ID

        :return: The vgw_id of this UpdateVgwRequest.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        """Sets the vgw_id of this UpdateVgwRequest.

        VPN网关实例ID

        :param vgw_id: The vgw_id of this UpdateVgwRequest.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def body(self):
        """Gets the body of this UpdateVgwRequest.

        :return: The body of this UpdateVgwRequest.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVgwRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateVgwRequest.

        :param body: The body of this UpdateVgwRequest.
        :type body: :class:`huaweicloudsdkvpn.v5.UpdateVgwRequestBody`
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
        if not isinstance(other, UpdateVgwRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
