# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVifPeerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vif_peer': 'VifPeer'
    }

    attribute_map = {
        'vif_peer': 'vif_peer'
    }

    def __init__(self, vif_peer=None):
        """UpdateVifPeerResponse

        The model defined in huaweicloud sdk

        :param vif_peer: 
        :type vif_peer: :class:`huaweicloudsdkdc.v3.VifPeer`
        """
        
        super(UpdateVifPeerResponse, self).__init__()

        self._vif_peer = None
        self.discriminator = None

        if vif_peer is not None:
            self.vif_peer = vif_peer

    @property
    def vif_peer(self):
        """Gets the vif_peer of this UpdateVifPeerResponse.

        :return: The vif_peer of this UpdateVifPeerResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.VifPeer`
        """
        return self._vif_peer

    @vif_peer.setter
    def vif_peer(self, vif_peer):
        """Sets the vif_peer of this UpdateVifPeerResponse.

        :param vif_peer: The vif_peer of this UpdateVifPeerResponse.
        :type vif_peer: :class:`huaweicloudsdkdc.v3.VifPeer`
        """
        self._vif_peer = vif_peer

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
        if not isinstance(other, UpdateVifPeerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
