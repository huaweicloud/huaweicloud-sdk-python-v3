# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExternalPeerLinkRequestBodyPeerLinkPeerSite:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway_id': 'str',
        'project_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'project_id': 'project_id',
        'region_id': 'region_id'
    }

    def __init__(self, gateway_id=None, project_id=None, region_id=None):
        r"""CreateExternalPeerLinkRequestBodyPeerLinkPeerSite

        The model defined in huaweicloud sdk

        :param gateway_id: 接入网关连接对端的实例(当前ER实例)ID
        :type gateway_id: str
        :param project_id: 对端实例(ER实例)归属的项目ID
        :type project_id: str
        :param region_id: 归属的区域ID
        :type region_id: str
        """
        
        

        self._gateway_id = None
        self._project_id = None
        self._region_id = None
        self.discriminator = None

        self.gateway_id = gateway_id
        self.project_id = project_id
        self.region_id = region_id

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.

        接入网关连接对端的实例(当前ER实例)ID

        :return: The gateway_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.

        接入网关连接对端的实例(当前ER实例)ID

        :param gateway_id: The gateway_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.

        对端实例(ER实例)归属的项目ID

        :return: The project_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.

        对端实例(ER实例)归属的项目ID

        :param project_id: The project_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.

        归属的区域ID

        :return: The region_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.

        归属的区域ID

        :param region_id: The region_id of this CreateExternalPeerLinkRequestBodyPeerLinkPeerSite.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, CreateExternalPeerLinkRequestBodyPeerLinkPeerSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
