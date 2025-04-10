# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVifPeerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vif_peer_id': 'str',
        'body': 'UpdateVifPeerRequestBody'
    }

    attribute_map = {
        'vif_peer_id': 'vif_peer_id',
        'body': 'body'
    }

    def __init__(self, vif_peer_id=None, body=None):
        r"""UpdateVifPeerRequest

        The model defined in huaweicloud sdk

        :param vif_peer_id: 虚拟接口对等体ID
        :type vif_peer_id: str
        :param body: Body of the UpdateVifPeerRequest
        :type body: :class:`huaweicloudsdkdc.v3.UpdateVifPeerRequestBody`
        """
        
        

        self._vif_peer_id = None
        self._body = None
        self.discriminator = None

        self.vif_peer_id = vif_peer_id
        if body is not None:
            self.body = body

    @property
    def vif_peer_id(self):
        r"""Gets the vif_peer_id of this UpdateVifPeerRequest.

        虚拟接口对等体ID

        :return: The vif_peer_id of this UpdateVifPeerRequest.
        :rtype: str
        """
        return self._vif_peer_id

    @vif_peer_id.setter
    def vif_peer_id(self, vif_peer_id):
        r"""Sets the vif_peer_id of this UpdateVifPeerRequest.

        虚拟接口对等体ID

        :param vif_peer_id: The vif_peer_id of this UpdateVifPeerRequest.
        :type vif_peer_id: str
        """
        self._vif_peer_id = vif_peer_id

    @property
    def body(self):
        r"""Gets the body of this UpdateVifPeerRequest.

        :return: The body of this UpdateVifPeerRequest.
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateVifPeerRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateVifPeerRequest.

        :param body: The body of this UpdateVifPeerRequest.
        :type body: :class:`huaweicloudsdkdc.v3.UpdateVifPeerRequestBody`
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
        if not isinstance(other, UpdateVifPeerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
