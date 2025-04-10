# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeerSiteExternal:

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
        'project_id': 'str',
        'site_code': 'str',
        'type': 'str'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'link_id': 'link_id',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'site_code': 'site_code',
        'type': 'type'
    }

    def __init__(self, gateway_id=None, link_id=None, region_id=None, project_id=None, site_code=None, type=None):
        r"""PeerSiteExternal

        The model defined in huaweicloud sdk

        :param gateway_id: 全域接入网关ID
        :type gateway_id: str
        :param link_id: 连接ID
        :type link_id: str
        :param region_id: 局点ID
        :type region_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param site_code: 网点编码
        :type site_code: str
        :param type: 连接类型
        :type type: str
        """
        
        

        self._gateway_id = None
        self._link_id = None
        self._region_id = None
        self._project_id = None
        self._site_code = None
        self._type = None
        self.discriminator = None

        if gateway_id is not None:
            self.gateway_id = gateway_id
        if link_id is not None:
            self.link_id = link_id
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if site_code is not None:
            self.site_code = site_code
        if type is not None:
            self.type = type

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this PeerSiteExternal.

        全域接入网关ID

        :return: The gateway_id of this PeerSiteExternal.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this PeerSiteExternal.

        全域接入网关ID

        :param gateway_id: The gateway_id of this PeerSiteExternal.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def link_id(self):
        r"""Gets the link_id of this PeerSiteExternal.

        连接ID

        :return: The link_id of this PeerSiteExternal.
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        r"""Sets the link_id of this PeerSiteExternal.

        连接ID

        :param link_id: The link_id of this PeerSiteExternal.
        :type link_id: str
        """
        self._link_id = link_id

    @property
    def region_id(self):
        r"""Gets the region_id of this PeerSiteExternal.

        局点ID

        :return: The region_id of this PeerSiteExternal.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this PeerSiteExternal.

        局点ID

        :param region_id: The region_id of this PeerSiteExternal.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this PeerSiteExternal.

        项目ID

        :return: The project_id of this PeerSiteExternal.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PeerSiteExternal.

        项目ID

        :param project_id: The project_id of this PeerSiteExternal.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def site_code(self):
        r"""Gets the site_code of this PeerSiteExternal.

        网点编码

        :return: The site_code of this PeerSiteExternal.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this PeerSiteExternal.

        网点编码

        :param site_code: The site_code of this PeerSiteExternal.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def type(self):
        r"""Gets the type of this PeerSiteExternal.

        连接类型

        :return: The type of this PeerSiteExternal.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PeerSiteExternal.

        连接类型

        :param type: The type of this PeerSiteExternal.
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
        if not isinstance(other, PeerSiteExternal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
