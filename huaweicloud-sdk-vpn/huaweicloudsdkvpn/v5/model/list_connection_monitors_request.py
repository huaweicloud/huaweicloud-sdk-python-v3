# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectionMonitorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_connection_id': 'str',
        'enterprise_project_id': 'list[str]'
    }

    attribute_map = {
        'vpn_connection_id': 'vpn_connection_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, vpn_connection_id=None, enterprise_project_id=None):
        """ListConnectionMonitorsRequest

        The model defined in huaweicloud sdk

        :param vpn_connection_id: VPN连接Id
        :type vpn_connection_id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: list[str]
        """
        
        

        self._vpn_connection_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if vpn_connection_id is not None:
            self.vpn_connection_id = vpn_connection_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def vpn_connection_id(self):
        """Gets the vpn_connection_id of this ListConnectionMonitorsRequest.

        VPN连接Id

        :return: The vpn_connection_id of this ListConnectionMonitorsRequest.
        :rtype: str
        """
        return self._vpn_connection_id

    @vpn_connection_id.setter
    def vpn_connection_id(self, vpn_connection_id):
        """Sets the vpn_connection_id of this ListConnectionMonitorsRequest.

        VPN连接Id

        :param vpn_connection_id: The vpn_connection_id of this ListConnectionMonitorsRequest.
        :type vpn_connection_id: str
        """
        self._vpn_connection_id = vpn_connection_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListConnectionMonitorsRequest.

        企业项目id

        :return: The enterprise_project_id of this ListConnectionMonitorsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListConnectionMonitorsRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListConnectionMonitorsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListConnectionMonitorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
