# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePeerLinkRequestBodyPeerLinkPeerSite:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'gateway_id': 'str',
        'project_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'gateway_id': 'gateway_id',
        'project_id': 'project_id',
        'region_id': 'region_id'
    }

    def __init__(self, type=None, gateway_id=None, project_id=None, region_id=None):
        """CreatePeerLinkRequestBodyPeerLinkPeerSite

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param gateway_id: 
        :type gateway_id: str
        :param project_id: 
        :type project_id: str
        :param region_id: 
        :type region_id: str
        """
        
        

        self._type = None
        self._gateway_id = None
        self._project_id = None
        self._region_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.gateway_id = gateway_id
        self.project_id = project_id
        self.region_id = region_id

    @property
    def type(self):
        """Gets the type of this CreatePeerLinkRequestBodyPeerLinkPeerSite.

        :return: The type of this CreatePeerLinkRequestBodyPeerLinkPeerSite.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreatePeerLinkRequestBodyPeerLinkPeerSite.

        :param type: The type of this CreatePeerLinkRequestBodyPeerLinkPeerSite.
        :type type: str
        """
        self._type = type

    @property
    def gateway_id(self):
        """Gets the gateway_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.

        :return: The gateway_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.

        :param gateway_id: The gateway_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def project_id(self):
        """Gets the project_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.

        :return: The project_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.

        :param project_id: The project_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.

        :return: The region_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.

        :param region_id: The region_id of this CreatePeerLinkRequestBodyPeerLinkPeerSite.
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
        if not isinstance(other, CreatePeerLinkRequestBodyPeerLinkPeerSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
