# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVifPeerDetectionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'vif_peer_detections': 'list[VifPeerDetection]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'vif_peer_detections': 'vif_peer_detections'
    }

    def __init__(self, request_id=None, vif_peer_detections=None):
        r"""ListVifPeerDetectionsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求id
        :type request_id: str
        :param vif_peer_detections: 
        :type vif_peer_detections: list[:class:`huaweicloudsdkdc.v3.VifPeerDetection`]
        """
        
        super().__init__()

        self._request_id = None
        self._vif_peer_detections = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if vif_peer_detections is not None:
            self.vif_peer_detections = vif_peer_detections

    @property
    def request_id(self):
        r"""Gets the request_id of this ListVifPeerDetectionsResponse.

        请求id

        :return: The request_id of this ListVifPeerDetectionsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListVifPeerDetectionsResponse.

        请求id

        :param request_id: The request_id of this ListVifPeerDetectionsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def vif_peer_detections(self):
        r"""Gets the vif_peer_detections of this ListVifPeerDetectionsResponse.

        :return: The vif_peer_detections of this ListVifPeerDetectionsResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.VifPeerDetection`]
        """
        return self._vif_peer_detections

    @vif_peer_detections.setter
    def vif_peer_detections(self, vif_peer_detections):
        r"""Sets the vif_peer_detections of this ListVifPeerDetectionsResponse.

        :param vif_peer_detections: The vif_peer_detections of this ListVifPeerDetectionsResponse.
        :type vif_peer_detections: list[:class:`huaweicloudsdkdc.v3.VifPeerDetection`]
        """
        self._vif_peer_detections = vif_peer_detections

    def to_dict(self):
        import warnings
        warnings.warn("ListVifPeerDetectionsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListVifPeerDetectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
