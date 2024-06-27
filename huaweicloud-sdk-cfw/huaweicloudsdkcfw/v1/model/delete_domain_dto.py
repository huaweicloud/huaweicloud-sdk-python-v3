# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDomainDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'domain_address_ids': 'list[str]'
    }

    attribute_map = {
        'object_id': 'object_id',
        'domain_address_ids': 'domain_address_ids'
    }

    def __init__(self, object_id=None, domain_address_ids=None):
        """DeleteDomainDto

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。
        :type object_id: str
        :param domain_address_ids: 域名id列表
        :type domain_address_ids: list[str]
        """
        
        

        self._object_id = None
        self._domain_address_ids = None
        self.discriminator = None

        self.object_id = object_id
        self.domain_address_ids = domain_address_ids

    @property
    def object_id(self):
        """Gets the object_id of this DeleteDomainDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。

        :return: The object_id of this DeleteDomainDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this DeleteDomainDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。

        :param object_id: The object_id of this DeleteDomainDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def domain_address_ids(self):
        """Gets the domain_address_ids of this DeleteDomainDto.

        域名id列表

        :return: The domain_address_ids of this DeleteDomainDto.
        :rtype: list[str]
        """
        return self._domain_address_ids

    @domain_address_ids.setter
    def domain_address_ids(self, domain_address_ids):
        """Sets the domain_address_ids of this DeleteDomainDto.

        域名id列表

        :param domain_address_ids: The domain_address_ids of this DeleteDomainDto.
        :type domain_address_ids: list[str]
        """
        self._domain_address_ids = domain_address_ids

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
        if not isinstance(other, DeleteDomainDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
