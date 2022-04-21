# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Org:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'org_msp_id': 'str',
        'org_domain': 'str',
        'peers': 'dict(str, Node)'
    }

    attribute_map = {
        'org_msp_id': 'org_msp_id',
        'org_domain': 'org_domain',
        'peers': 'peers'
    }

    def __init__(self, org_msp_id=None, org_domain=None, peers=None):
        """Org

        The model defined in huaweicloud sdk

        :param org_msp_id: 组织MSP标识
        :type org_msp_id: str
        :param org_domain: 组织域名
        :type org_domain: str
        :param peers: key:节点名称，value：节点详细信息
        :type peers: dict(str, Node)
        """
        
        

        self._org_msp_id = None
        self._org_domain = None
        self._peers = None
        self.discriminator = None

        if org_msp_id is not None:
            self.org_msp_id = org_msp_id
        if org_domain is not None:
            self.org_domain = org_domain
        if peers is not None:
            self.peers = peers

    @property
    def org_msp_id(self):
        """Gets the org_msp_id of this Org.

        组织MSP标识

        :return: The org_msp_id of this Org.
        :rtype: str
        """
        return self._org_msp_id

    @org_msp_id.setter
    def org_msp_id(self, org_msp_id):
        """Sets the org_msp_id of this Org.

        组织MSP标识

        :param org_msp_id: The org_msp_id of this Org.
        :type org_msp_id: str
        """
        self._org_msp_id = org_msp_id

    @property
    def org_domain(self):
        """Gets the org_domain of this Org.

        组织域名

        :return: The org_domain of this Org.
        :rtype: str
        """
        return self._org_domain

    @org_domain.setter
    def org_domain(self, org_domain):
        """Sets the org_domain of this Org.

        组织域名

        :param org_domain: The org_domain of this Org.
        :type org_domain: str
        """
        self._org_domain = org_domain

    @property
    def peers(self):
        """Gets the peers of this Org.

        key:节点名称，value：节点详细信息

        :return: The peers of this Org.
        :rtype: dict(str, Node)
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """Sets the peers of this Org.

        key:节点名称，value：节点详细信息

        :param peers: The peers of this Org.
        :type peers: dict(str, Node)
        """
        self._peers = peers

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
        if not isinstance(other, Org):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
