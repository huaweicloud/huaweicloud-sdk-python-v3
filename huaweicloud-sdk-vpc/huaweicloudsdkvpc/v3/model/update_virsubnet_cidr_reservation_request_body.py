# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVirsubnetCidrReservationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dry_run': 'bool',
        'virsubnet_cidr_reservation': 'UpdateVirsubnetCidrReservationOption'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'virsubnet_cidr_reservation': 'virsubnet_cidr_reservation'
    }

    def __init__(self, dry_run=None, virsubnet_cidr_reservation=None):
        r"""UpdateVirsubnetCidrReservationRequestBody

        The model defined in huaweicloud sdk

        :param dry_run: **参数解释**： 是否只预检此次请求。 **约束限制**： 不涉及。 **取值范围**： - true：发送检查请求，不会更新子网预留网段。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 - false：发送正常请求，并直接更新子网预留网段。 **默认取值**： false
        :type dry_run: bool
        :param virsubnet_cidr_reservation: 
        :type virsubnet_cidr_reservation: :class:`huaweicloudsdkvpc.v3.UpdateVirsubnetCidrReservationOption`
        """
        
        

        self._dry_run = None
        self._virsubnet_cidr_reservation = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        self.virsubnet_cidr_reservation = virsubnet_cidr_reservation

    @property
    def dry_run(self):
        r"""Gets the dry_run of this UpdateVirsubnetCidrReservationRequestBody.

        **参数解释**： 是否只预检此次请求。 **约束限制**： 不涉及。 **取值范围**： - true：发送检查请求，不会更新子网预留网段。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 - false：发送正常请求，并直接更新子网预留网段。 **默认取值**： false

        :return: The dry_run of this UpdateVirsubnetCidrReservationRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this UpdateVirsubnetCidrReservationRequestBody.

        **参数解释**： 是否只预检此次请求。 **约束限制**： 不涉及。 **取值范围**： - true：发送检查请求，不会更新子网预留网段。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 - false：发送正常请求，并直接更新子网预留网段。 **默认取值**： false

        :param dry_run: The dry_run of this UpdateVirsubnetCidrReservationRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def virsubnet_cidr_reservation(self):
        r"""Gets the virsubnet_cidr_reservation of this UpdateVirsubnetCidrReservationRequestBody.

        :return: The virsubnet_cidr_reservation of this UpdateVirsubnetCidrReservationRequestBody.
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateVirsubnetCidrReservationOption`
        """
        return self._virsubnet_cidr_reservation

    @virsubnet_cidr_reservation.setter
    def virsubnet_cidr_reservation(self, virsubnet_cidr_reservation):
        r"""Sets the virsubnet_cidr_reservation of this UpdateVirsubnetCidrReservationRequestBody.

        :param virsubnet_cidr_reservation: The virsubnet_cidr_reservation of this UpdateVirsubnetCidrReservationRequestBody.
        :type virsubnet_cidr_reservation: :class:`huaweicloudsdkvpc.v3.UpdateVirsubnetCidrReservationOption`
        """
        self._virsubnet_cidr_reservation = virsubnet_cidr_reservation

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
        if not isinstance(other, UpdateVirsubnetCidrReservationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
