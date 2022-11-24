# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'dns_name': 'str',
        'dns_type': 'str',
        'ipv4_address': 'str',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'dns_name': 'dns_name',
        'dns_type': 'dns_type',
        'ipv4_address': 'ipv4_address',
        'status': 'status'
    }

    def __init__(self, instance_id=None, dns_name=None, dns_type=None, ipv4_address=None, status=None):
        """ShowDomainNameResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param dns_name: 实例域名。
        :type dns_name: str
        :param dns_type: 实例域名类型，当前只支持private。
        :type dns_type: str
        :param ipv4_address: 实例内网IPv4地址。
        :type ipv4_address: str
        :param status: 域名状态
        :type status: str
        """
        
        super(ShowDomainNameResponse, self).__init__()

        self._instance_id = None
        self._dns_name = None
        self._dns_type = None
        self._ipv4_address = None
        self._status = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if dns_name is not None:
            self.dns_name = dns_name
        if dns_type is not None:
            self.dns_type = dns_type
        if ipv4_address is not None:
            self.ipv4_address = ipv4_address
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowDomainNameResponse.

        实例ID。

        :return: The instance_id of this ShowDomainNameResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowDomainNameResponse.

        实例ID。

        :param instance_id: The instance_id of this ShowDomainNameResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def dns_name(self):
        """Gets the dns_name of this ShowDomainNameResponse.

        实例域名。

        :return: The dns_name of this ShowDomainNameResponse.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this ShowDomainNameResponse.

        实例域名。

        :param dns_name: The dns_name of this ShowDomainNameResponse.
        :type dns_name: str
        """
        self._dns_name = dns_name

    @property
    def dns_type(self):
        """Gets the dns_type of this ShowDomainNameResponse.

        实例域名类型，当前只支持private。

        :return: The dns_type of this ShowDomainNameResponse.
        :rtype: str
        """
        return self._dns_type

    @dns_type.setter
    def dns_type(self, dns_type):
        """Sets the dns_type of this ShowDomainNameResponse.

        实例域名类型，当前只支持private。

        :param dns_type: The dns_type of this ShowDomainNameResponse.
        :type dns_type: str
        """
        self._dns_type = dns_type

    @property
    def ipv4_address(self):
        """Gets the ipv4_address of this ShowDomainNameResponse.

        实例内网IPv4地址。

        :return: The ipv4_address of this ShowDomainNameResponse.
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """Sets the ipv4_address of this ShowDomainNameResponse.

        实例内网IPv4地址。

        :param ipv4_address: The ipv4_address of this ShowDomainNameResponse.
        :type ipv4_address: str
        """
        self._ipv4_address = ipv4_address

    @property
    def status(self):
        """Gets the status of this ShowDomainNameResponse.

        域名状态

        :return: The status of this ShowDomainNameResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDomainNameResponse.

        域名状态

        :param status: The status of this ShowDomainNameResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ShowDomainNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
