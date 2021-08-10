# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePremiumHostResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'policyid': 'str',
        'hostname': 'str',
        'domainid': 'str',
        'projectid': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'hostname': 'hostname',
        'domainid': 'domainid',
        'projectid': 'projectid',
        'protocol': 'protocol'
    }

    def __init__(self, id=None, policyid=None, hostname=None, domainid=None, projectid=None, protocol=None):
        """CreatePremiumHostResponse - a model defined in huaweicloud sdk"""
        
        super(CreatePremiumHostResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._hostname = None
        self._domainid = None
        self._projectid = None
        self._protocol = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if hostname is not None:
            self.hostname = hostname
        if domainid is not None:
            self.domainid = domainid
        if projectid is not None:
            self.projectid = projectid
        if protocol is not None:
            self.protocol = protocol

    @property
    def id(self):
        """Gets the id of this CreatePremiumHostResponse.

        域名id

        :return: The id of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatePremiumHostResponse.

        域名id

        :param id: The id of this CreatePremiumHostResponse.
        :type: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this CreatePremiumHostResponse.

        策略id

        :return: The policyid of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreatePremiumHostResponse.

        策略id

        :param policyid: The policyid of this CreatePremiumHostResponse.
        :type: str
        """
        self._policyid = policyid

    @property
    def hostname(self):
        """Gets the hostname of this CreatePremiumHostResponse.

        策略id

        :return: The hostname of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreatePremiumHostResponse.

        策略id

        :param hostname: The hostname of this CreatePremiumHostResponse.
        :type: str
        """
        self._hostname = hostname

    @property
    def domainid(self):
        """Gets the domainid of this CreatePremiumHostResponse.

        租户id

        :return: The domainid of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._domainid

    @domainid.setter
    def domainid(self, domainid):
        """Sets the domainid of this CreatePremiumHostResponse.

        租户id

        :param domainid: The domainid of this CreatePremiumHostResponse.
        :type: str
        """
        self._domainid = domainid

    @property
    def projectid(self):
        """Gets the projectid of this CreatePremiumHostResponse.

        项目projectid

        :return: The projectid of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._projectid

    @projectid.setter
    def projectid(self, projectid):
        """Sets the projectid of this CreatePremiumHostResponse.

        项目projectid

        :param projectid: The projectid of this CreatePremiumHostResponse.
        :type: str
        """
        self._projectid = projectid

    @property
    def protocol(self):
        """Gets the protocol of this CreatePremiumHostResponse.

        http协议

        :return: The protocol of this CreatePremiumHostResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreatePremiumHostResponse.

        http协议

        :param protocol: The protocol of this CreatePremiumHostResponse.
        :type: str
        """
        self._protocol = protocol

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
        if not isinstance(other, CreatePremiumHostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
