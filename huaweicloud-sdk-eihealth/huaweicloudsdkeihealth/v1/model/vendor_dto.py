# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VendorDto:

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
        'domain_id': 'str',
        'name': 'str',
        'logo': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'name': 'name',
        'logo': 'logo'
    }

    def __init__(self, id=None, domain_id=None, name=None, logo=None):
        """VendorDto

        The model defined in huaweicloud sdk

        :param id: 供应商id
        :type id: str
        :param domain_id: 账号id
        :type domain_id: str
        :param name: 名称
        :type name: str
        :param logo: logo图片base64编码
        :type logo: str
        """
        
        

        self._id = None
        self._domain_id = None
        self._name = None
        self._logo = None
        self.discriminator = None

        self.id = id
        self.domain_id = domain_id
        self.name = name
        self.logo = logo

    @property
    def id(self):
        """Gets the id of this VendorDto.

        供应商id

        :return: The id of this VendorDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VendorDto.

        供应商id

        :param id: The id of this VendorDto.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        """Gets the domain_id of this VendorDto.

        账号id

        :return: The domain_id of this VendorDto.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this VendorDto.

        账号id

        :param domain_id: The domain_id of this VendorDto.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this VendorDto.

        名称

        :return: The name of this VendorDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VendorDto.

        名称

        :param name: The name of this VendorDto.
        :type name: str
        """
        self._name = name

    @property
    def logo(self):
        """Gets the logo of this VendorDto.

        logo图片base64编码

        :return: The logo of this VendorDto.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this VendorDto.

        logo图片base64编码

        :param logo: The logo of this VendorDto.
        :type logo: str
        """
        self._logo = logo

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
        if not isinstance(other, VendorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
