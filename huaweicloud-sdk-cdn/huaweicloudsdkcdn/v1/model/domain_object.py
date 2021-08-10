# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainObject:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'flux': 'list[int]'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'flux': 'flux'
    }

    def __init__(self, domain_name=None, flux=None):
        """DomainObject - a model defined in huaweicloud sdk"""
        
        

        self._domain_name = None
        self._flux = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if flux is not None:
            self.flux = flux

    @property
    def domain_name(self):
        """Gets the domain_name of this DomainObject.

        域名

        :return: The domain_name of this DomainObject.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DomainObject.

        域名

        :param domain_name: The domain_name of this DomainObject.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def flux(self):
        """Gets the flux of this DomainObject.

        数据结束时间戳，可能与请求时间不一致，可能不返回

        :return: The flux of this DomainObject.
        :rtype: list[int]
        """
        return self._flux

    @flux.setter
    def flux(self, flux):
        """Sets the flux of this DomainObject.

        数据结束时间戳，可能与请求时间不一致，可能不返回

        :param flux: The flux of this DomainObject.
        :type: list[int]
        """
        self._flux = flux

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
        if not isinstance(other, DomainObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
