# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainSetInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'set_id': 'str',
        'domain_set_type': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'set_id': 'set_id',
        'domain_set_type': 'domain_set_type'
    }

    def __init__(self, name=None, description=None, set_id=None, domain_set_type=None):
        """UpdateDomainSetInfoDto

        The model defined in huaweicloud sdk

        :param name: 域名组名称UUID
        :type name: str
        :param description: 描述
        :type description: str
        :param set_id: 域名组id
        :type set_id: str
        :param domain_set_type: 域名组类型，0表示URL过滤，1表示地址解析
        :type domain_set_type: int
        """
        
        

        self._name = None
        self._description = None
        self._set_id = None
        self._domain_set_type = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if set_id is not None:
            self.set_id = set_id
        if domain_set_type is not None:
            self.domain_set_type = domain_set_type

    @property
    def name(self):
        """Gets the name of this UpdateDomainSetInfoDto.

        域名组名称UUID

        :return: The name of this UpdateDomainSetInfoDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDomainSetInfoDto.

        域名组名称UUID

        :param name: The name of this UpdateDomainSetInfoDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateDomainSetInfoDto.

        描述

        :return: The description of this UpdateDomainSetInfoDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDomainSetInfoDto.

        描述

        :param description: The description of this UpdateDomainSetInfoDto.
        :type description: str
        """
        self._description = description

    @property
    def set_id(self):
        """Gets the set_id of this UpdateDomainSetInfoDto.

        域名组id

        :return: The set_id of this UpdateDomainSetInfoDto.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this UpdateDomainSetInfoDto.

        域名组id

        :param set_id: The set_id of this UpdateDomainSetInfoDto.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def domain_set_type(self):
        """Gets the domain_set_type of this UpdateDomainSetInfoDto.

        域名组类型，0表示URL过滤，1表示地址解析

        :return: The domain_set_type of this UpdateDomainSetInfoDto.
        :rtype: int
        """
        return self._domain_set_type

    @domain_set_type.setter
    def domain_set_type(self, domain_set_type):
        """Sets the domain_set_type of this UpdateDomainSetInfoDto.

        域名组类型，0表示URL过滤，1表示地址解析

        :param domain_set_type: The domain_set_type of this UpdateDomainSetInfoDto.
        :type domain_set_type: int
        """
        self._domain_set_type = domain_set_type

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
        if not isinstance(other, UpdateDomainSetInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
