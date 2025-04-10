# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeerSite:

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
        'link_id': 'str',
        'region_id': 'str',
        'site_code': 'str',
        'project_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'link_id': 'link_id',
        'region_id': 'region_id',
        'site_code': 'site_code',
        'project_id': 'project_id',
        'type': 'type'
    }

    def __init__(self, gateway_id=None, link_id=None, region_id=None, site_code=None, project_id=None, type=None):
        r"""PeerSite

        The model defined in huaweicloud sdk

        :param gateway_id: 对端网关的ID
        :type gateway_id: str
        :param link_id: 对端网关连接的ID(如：对端为ER时为attachment ID,对端为GDGW时为对端的PeerLink Id
        :type link_id: str
        :param region_id: 对端网关所在的Region
        :type region_id: str
        :param site_code: 专线全域接入网关对应的站点位置
        :type site_code: str
        :param project_id: 对等体站点的项目ID
        :type project_id: str
        :param type: 对等体的类型 - ER 企业路由器 - GDGW 全域接入网关
        :type type: str
        """
        
        

        self._gateway_id = None
        self._link_id = None
        self._region_id = None
        self._site_code = None
        self._project_id = None
        self._type = None
        self.discriminator = None

        if gateway_id is not None:
            self.gateway_id = gateway_id
        if link_id is not None:
            self.link_id = link_id
        if region_id is not None:
            self.region_id = region_id
        if site_code is not None:
            self.site_code = site_code
        if project_id is not None:
            self.project_id = project_id
        if type is not None:
            self.type = type

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this PeerSite.

        对端网关的ID

        :return: The gateway_id of this PeerSite.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this PeerSite.

        对端网关的ID

        :param gateway_id: The gateway_id of this PeerSite.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def link_id(self):
        r"""Gets the link_id of this PeerSite.

        对端网关连接的ID(如：对端为ER时为attachment ID,对端为GDGW时为对端的PeerLink Id

        :return: The link_id of this PeerSite.
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        r"""Sets the link_id of this PeerSite.

        对端网关连接的ID(如：对端为ER时为attachment ID,对端为GDGW时为对端的PeerLink Id

        :param link_id: The link_id of this PeerSite.
        :type link_id: str
        """
        self._link_id = link_id

    @property
    def region_id(self):
        r"""Gets the region_id of this PeerSite.

        对端网关所在的Region

        :return: The region_id of this PeerSite.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this PeerSite.

        对端网关所在的Region

        :param region_id: The region_id of this PeerSite.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def site_code(self):
        r"""Gets the site_code of this PeerSite.

        专线全域接入网关对应的站点位置

        :return: The site_code of this PeerSite.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this PeerSite.

        专线全域接入网关对应的站点位置

        :param site_code: The site_code of this PeerSite.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def project_id(self):
        r"""Gets the project_id of this PeerSite.

        对等体站点的项目ID

        :return: The project_id of this PeerSite.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PeerSite.

        对等体站点的项目ID

        :param project_id: The project_id of this PeerSite.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        r"""Gets the type of this PeerSite.

        对等体的类型 - ER 企业路由器 - GDGW 全域接入网关

        :return: The type of this PeerSite.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PeerSite.

        对等体的类型 - ER 企业路由器 - GDGW 全域接入网关

        :param type: The type of this PeerSite.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, PeerSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
