# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpcep_service_name': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'vpcep_service_name': 'vpcep_service_name',
        'domain': 'domain'
    }

    def __init__(self, vpcep_service_name=None, domain=None):
        r"""AccessInfo

        The model defined in huaweicloud sdk

        :param vpcep_service_name: 服务名称
        :type vpcep_service_name: str
        :param domain: 分组独立域名
        :type domain: str
        """
        
        

        self._vpcep_service_name = None
        self._domain = None
        self.discriminator = None

        if vpcep_service_name is not None:
            self.vpcep_service_name = vpcep_service_name
        if domain is not None:
            self.domain = domain

    @property
    def vpcep_service_name(self):
        r"""Gets the vpcep_service_name of this AccessInfo.

        服务名称

        :return: The vpcep_service_name of this AccessInfo.
        :rtype: str
        """
        return self._vpcep_service_name

    @vpcep_service_name.setter
    def vpcep_service_name(self, vpcep_service_name):
        r"""Sets the vpcep_service_name of this AccessInfo.

        服务名称

        :param vpcep_service_name: The vpcep_service_name of this AccessInfo.
        :type vpcep_service_name: str
        """
        self._vpcep_service_name = vpcep_service_name

    @property
    def domain(self):
        r"""Gets the domain of this AccessInfo.

        分组独立域名

        :return: The domain of this AccessInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this AccessInfo.

        分组独立域名

        :param domain: The domain of this AccessInfo.
        :type domain: str
        """
        self._domain = domain

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
        if not isinstance(other, AccessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
