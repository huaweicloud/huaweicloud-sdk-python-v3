# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVirsubnetCidrReservationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virsubnet_cidr_reservations': 'list[VirsubnetCidrReservation]',
        'request_id': 'str',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'virsubnet_cidr_reservations': 'virsubnet_cidr_reservations',
        'request_id': 'request_id',
        'page_info': 'page_info'
    }

    def __init__(self, virsubnet_cidr_reservations=None, request_id=None, page_info=None):
        r"""ListVirsubnetCidrReservationsResponse

        The model defined in huaweicloud sdk

        :param virsubnet_cidr_reservations: **参数解释**： 查询子网预留网段列表的响应体。 **取值范围**： 不涉及。
        :type virsubnet_cidr_reservations: list[:class:`huaweicloudsdkvpc.v3.VirsubnetCidrReservation`]
        :param request_id: **参数解释**： 请求ID。 **取值范围**： 不涉及。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        
        super().__init__()

        self._virsubnet_cidr_reservations = None
        self._request_id = None
        self._page_info = None
        self.discriminator = None

        if virsubnet_cidr_reservations is not None:
            self.virsubnet_cidr_reservations = virsubnet_cidr_reservations
        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info

    @property
    def virsubnet_cidr_reservations(self):
        r"""Gets the virsubnet_cidr_reservations of this ListVirsubnetCidrReservationsResponse.

        **参数解释**： 查询子网预留网段列表的响应体。 **取值范围**： 不涉及。

        :return: The virsubnet_cidr_reservations of this ListVirsubnetCidrReservationsResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.VirsubnetCidrReservation`]
        """
        return self._virsubnet_cidr_reservations

    @virsubnet_cidr_reservations.setter
    def virsubnet_cidr_reservations(self, virsubnet_cidr_reservations):
        r"""Sets the virsubnet_cidr_reservations of this ListVirsubnetCidrReservationsResponse.

        **参数解释**： 查询子网预留网段列表的响应体。 **取值范围**： 不涉及。

        :param virsubnet_cidr_reservations: The virsubnet_cidr_reservations of this ListVirsubnetCidrReservationsResponse.
        :type virsubnet_cidr_reservations: list[:class:`huaweicloudsdkvpc.v3.VirsubnetCidrReservation`]
        """
        self._virsubnet_cidr_reservations = virsubnet_cidr_reservations

    @property
    def request_id(self):
        r"""Gets the request_id of this ListVirsubnetCidrReservationsResponse.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :return: The request_id of this ListVirsubnetCidrReservationsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListVirsubnetCidrReservationsResponse.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :param request_id: The request_id of this ListVirsubnetCidrReservationsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListVirsubnetCidrReservationsResponse.

        :return: The page_info of this ListVirsubnetCidrReservationsResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListVirsubnetCidrReservationsResponse.

        :param page_info: The page_info of this ListVirsubnetCidrReservationsResponse.
        :type page_info: :class:`huaweicloudsdkvpc.v3.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListVirsubnetCidrReservationsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListVirsubnetCidrReservationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
