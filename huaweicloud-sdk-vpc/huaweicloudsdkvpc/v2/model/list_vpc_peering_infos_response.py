# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcPeeringInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peering_infos': 'list[VpcPeering]',
        'peering_infos_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'peering_infos': 'peering_infos',
        'peering_infos_links': 'peering_infos_links'
    }

    def __init__(self, peering_infos=None, peering_infos_links=None):
        r"""ListVpcPeeringInfosResponse

        The model defined in huaweicloud sdk

        :param peering_infos: 对等连接信息对象列表
        :type peering_infos: list[:class:`huaweicloudsdkvpc.v2.VpcPeering`]
        :param peering_infos_links: 分页信息
        :type peering_infos_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        
        super().__init__()

        self._peering_infos = None
        self._peering_infos_links = None
        self.discriminator = None

        if peering_infos is not None:
            self.peering_infos = peering_infos
        if peering_infos_links is not None:
            self.peering_infos_links = peering_infos_links

    @property
    def peering_infos(self):
        r"""Gets the peering_infos of this ListVpcPeeringInfosResponse.

        对等连接信息对象列表

        :return: The peering_infos of this ListVpcPeeringInfosResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.VpcPeering`]
        """
        return self._peering_infos

    @peering_infos.setter
    def peering_infos(self, peering_infos):
        r"""Sets the peering_infos of this ListVpcPeeringInfosResponse.

        对等连接信息对象列表

        :param peering_infos: The peering_infos of this ListVpcPeeringInfosResponse.
        :type peering_infos: list[:class:`huaweicloudsdkvpc.v2.VpcPeering`]
        """
        self._peering_infos = peering_infos

    @property
    def peering_infos_links(self):
        r"""Gets the peering_infos_links of this ListVpcPeeringInfosResponse.

        分页信息

        :return: The peering_infos_links of this ListVpcPeeringInfosResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        return self._peering_infos_links

    @peering_infos_links.setter
    def peering_infos_links(self, peering_infos_links):
        r"""Sets the peering_infos_links of this ListVpcPeeringInfosResponse.

        分页信息

        :param peering_infos_links: The peering_infos_links of this ListVpcPeeringInfosResponse.
        :type peering_infos_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        self._peering_infos_links = peering_infos_links

    def to_dict(self):
        import warnings
        warnings.warn("ListVpcPeeringInfosResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListVpcPeeringInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
