# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterEndpointsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_endpoints': 'PublicEndpointResponse',
        'private_endpoints': 'PrivateEndpointResponse',
        'public_ip_infos': 'list[PublicIpInfoResponse]'
    }

    attribute_map = {
        'public_endpoints': 'public_endpoints',
        'private_endpoints': 'private_endpoints',
        'public_ip_infos': 'public_ip_infos'
    }

    def __init__(self, public_endpoints=None, private_endpoints=None, public_ip_infos=None):
        r"""ListClusterEndpointsResponse

        The model defined in huaweicloud sdk

        :param public_endpoints: 
        :type public_endpoints: :class:`huaweicloudsdkdws.v2.PublicEndpointResponse`
        :param private_endpoints: 
        :type private_endpoints: :class:`huaweicloudsdkdws.v2.PrivateEndpointResponse`
        :param public_ip_infos: **参数解释**： 公网IP详细信息，显示每个节点当前是否绑定公网IP及对应状态。 **取值范围**： 不涉及。
        :type public_ip_infos: list[:class:`huaweicloudsdkdws.v2.PublicIpInfoResponse`]
        """
        
        super(ListClusterEndpointsResponse, self).__init__()

        self._public_endpoints = None
        self._private_endpoints = None
        self._public_ip_infos = None
        self.discriminator = None

        if public_endpoints is not None:
            self.public_endpoints = public_endpoints
        if private_endpoints is not None:
            self.private_endpoints = private_endpoints
        if public_ip_infos is not None:
            self.public_ip_infos = public_ip_infos

    @property
    def public_endpoints(self):
        r"""Gets the public_endpoints of this ListClusterEndpointsResponse.

        :return: The public_endpoints of this ListClusterEndpointsResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.PublicEndpointResponse`
        """
        return self._public_endpoints

    @public_endpoints.setter
    def public_endpoints(self, public_endpoints):
        r"""Sets the public_endpoints of this ListClusterEndpointsResponse.

        :param public_endpoints: The public_endpoints of this ListClusterEndpointsResponse.
        :type public_endpoints: :class:`huaweicloudsdkdws.v2.PublicEndpointResponse`
        """
        self._public_endpoints = public_endpoints

    @property
    def private_endpoints(self):
        r"""Gets the private_endpoints of this ListClusterEndpointsResponse.

        :return: The private_endpoints of this ListClusterEndpointsResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.PrivateEndpointResponse`
        """
        return self._private_endpoints

    @private_endpoints.setter
    def private_endpoints(self, private_endpoints):
        r"""Sets the private_endpoints of this ListClusterEndpointsResponse.

        :param private_endpoints: The private_endpoints of this ListClusterEndpointsResponse.
        :type private_endpoints: :class:`huaweicloudsdkdws.v2.PrivateEndpointResponse`
        """
        self._private_endpoints = private_endpoints

    @property
    def public_ip_infos(self):
        r"""Gets the public_ip_infos of this ListClusterEndpointsResponse.

        **参数解释**： 公网IP详细信息，显示每个节点当前是否绑定公网IP及对应状态。 **取值范围**： 不涉及。

        :return: The public_ip_infos of this ListClusterEndpointsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.PublicIpInfoResponse`]
        """
        return self._public_ip_infos

    @public_ip_infos.setter
    def public_ip_infos(self, public_ip_infos):
        r"""Sets the public_ip_infos of this ListClusterEndpointsResponse.

        **参数解释**： 公网IP详细信息，显示每个节点当前是否绑定公网IP及对应状态。 **取值范围**： 不涉及。

        :param public_ip_infos: The public_ip_infos of this ListClusterEndpointsResponse.
        :type public_ip_infos: list[:class:`huaweicloudsdkdws.v2.PublicIpInfoResponse`]
        """
        self._public_ip_infos = public_ip_infos

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
        if not isinstance(other, ListClusterEndpointsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
