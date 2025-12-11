# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVirsubnetCidrReservationResponse(SdkResponse):

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
        'virsubnet_cidr_reservation': 'VirsubnetCidrReservation'
    }

    attribute_map = {
        'request_id': 'request_id',
        'virsubnet_cidr_reservation': 'virsubnet_cidr_reservation'
    }

    def __init__(self, request_id=None, virsubnet_cidr_reservation=None):
        r"""UpdateVirsubnetCidrReservationResponse

        The model defined in huaweicloud sdk

        :param request_id: **参数解释**： 请求ID。 **取值范围**： 不涉及。
        :type request_id: str
        :param virsubnet_cidr_reservation: 
        :type virsubnet_cidr_reservation: :class:`huaweicloudsdkvpc.v3.VirsubnetCidrReservation`
        """
        
        super().__init__()

        self._request_id = None
        self._virsubnet_cidr_reservation = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if virsubnet_cidr_reservation is not None:
            self.virsubnet_cidr_reservation = virsubnet_cidr_reservation

    @property
    def request_id(self):
        r"""Gets the request_id of this UpdateVirsubnetCidrReservationResponse.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :return: The request_id of this UpdateVirsubnetCidrReservationResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this UpdateVirsubnetCidrReservationResponse.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :param request_id: The request_id of this UpdateVirsubnetCidrReservationResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def virsubnet_cidr_reservation(self):
        r"""Gets the virsubnet_cidr_reservation of this UpdateVirsubnetCidrReservationResponse.

        :return: The virsubnet_cidr_reservation of this UpdateVirsubnetCidrReservationResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.VirsubnetCidrReservation`
        """
        return self._virsubnet_cidr_reservation

    @virsubnet_cidr_reservation.setter
    def virsubnet_cidr_reservation(self, virsubnet_cidr_reservation):
        r"""Sets the virsubnet_cidr_reservation of this UpdateVirsubnetCidrReservationResponse.

        :param virsubnet_cidr_reservation: The virsubnet_cidr_reservation of this UpdateVirsubnetCidrReservationResponse.
        :type virsubnet_cidr_reservation: :class:`huaweicloudsdkvpc.v3.VirsubnetCidrReservation`
        """
        self._virsubnet_cidr_reservation = virsubnet_cidr_reservation

    def to_dict(self):
        import warnings
        warnings.warn("UpdateVirsubnetCidrReservationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateVirsubnetCidrReservationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
