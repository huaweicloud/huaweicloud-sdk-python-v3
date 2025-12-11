# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteVirsubnetCidrReservationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virsubnet_cidr_reservation_id': 'str'
    }

    attribute_map = {
        'virsubnet_cidr_reservation_id': 'virsubnet_cidr_reservation_id'
    }

    def __init__(self, virsubnet_cidr_reservation_id=None):
        r"""DeleteVirsubnetCidrReservationRequest

        The model defined in huaweicloud sdk

        :param virsubnet_cidr_reservation_id: **参数解释**： 子网预留网段的资源ID。 **取值范围**： 不涉及。
        :type virsubnet_cidr_reservation_id: str
        """
        
        

        self._virsubnet_cidr_reservation_id = None
        self.discriminator = None

        self.virsubnet_cidr_reservation_id = virsubnet_cidr_reservation_id

    @property
    def virsubnet_cidr_reservation_id(self):
        r"""Gets the virsubnet_cidr_reservation_id of this DeleteVirsubnetCidrReservationRequest.

        **参数解释**： 子网预留网段的资源ID。 **取值范围**： 不涉及。

        :return: The virsubnet_cidr_reservation_id of this DeleteVirsubnetCidrReservationRequest.
        :rtype: str
        """
        return self._virsubnet_cidr_reservation_id

    @virsubnet_cidr_reservation_id.setter
    def virsubnet_cidr_reservation_id(self, virsubnet_cidr_reservation_id):
        r"""Sets the virsubnet_cidr_reservation_id of this DeleteVirsubnetCidrReservationRequest.

        **参数解释**： 子网预留网段的资源ID。 **取值范围**： 不涉及。

        :param virsubnet_cidr_reservation_id: The virsubnet_cidr_reservation_id of this DeleteVirsubnetCidrReservationRequest.
        :type virsubnet_cidr_reservation_id: str
        """
        self._virsubnet_cidr_reservation_id = virsubnet_cidr_reservation_id

    def to_dict(self):
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
        if not isinstance(other, DeleteVirsubnetCidrReservationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
