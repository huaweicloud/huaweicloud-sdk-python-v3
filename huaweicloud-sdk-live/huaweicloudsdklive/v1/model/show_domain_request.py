# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain=None, enterprise_project_id=None):
        """ShowDomainRequest

        The model defined in huaweicloud sdk

        :param domain: 直播域名，如果不设置此字段，则返回租户所有的域名信息
        :type domain: str
        :param enterprise_project_id: 企业项目ID，如果不设置此字段，则不进行该字段过滤，返回所有域名信息
        :type enterprise_project_id: str
        """
        
        

        self._domain = None
        self._enterprise_project_id = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain(self):
        """Gets the domain of this ShowDomainRequest.

        直播域名，如果不设置此字段，则返回租户所有的域名信息

        :return: The domain of this ShowDomainRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ShowDomainRequest.

        直播域名，如果不设置此字段，则返回租户所有的域名信息

        :param domain: The domain of this ShowDomainRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowDomainRequest.

        企业项目ID，如果不设置此字段，则不进行该字段过滤，返回所有域名信息

        :return: The enterprise_project_id of this ShowDomainRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowDomainRequest.

        企业项目ID，如果不设置此字段，则不进行该字段过滤，返回所有域名信息

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainRequest.
        :type enterprise_project_id: str
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
        if not isinstance(other, ShowDomainRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
