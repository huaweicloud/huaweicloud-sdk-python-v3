# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyHlsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'push_domain': 'str',
        'application': 'list[PushDomainApplication]'
    }

    attribute_map = {
        'push_domain': 'push_domain',
        'application': 'application'
    }

    def __init__(self, push_domain=None, application=None):
        r"""ModifyHlsConfig

        The model defined in huaweicloud sdk

        :param push_domain: 推流域名
        :type push_domain: str
        :param application: 推流域名APP配置
        :type application: list[:class:`huaweicloudsdklive.v1.PushDomainApplication`]
        """
        
        

        self._push_domain = None
        self._application = None
        self.discriminator = None

        self.push_domain = push_domain
        self.application = application

    @property
    def push_domain(self):
        r"""Gets the push_domain of this ModifyHlsConfig.

        推流域名

        :return: The push_domain of this ModifyHlsConfig.
        :rtype: str
        """
        return self._push_domain

    @push_domain.setter
    def push_domain(self, push_domain):
        r"""Sets the push_domain of this ModifyHlsConfig.

        推流域名

        :param push_domain: The push_domain of this ModifyHlsConfig.
        :type push_domain: str
        """
        self._push_domain = push_domain

    @property
    def application(self):
        r"""Gets the application of this ModifyHlsConfig.

        推流域名APP配置

        :return: The application of this ModifyHlsConfig.
        :rtype: list[:class:`huaweicloudsdklive.v1.PushDomainApplication`]
        """
        return self._application

    @application.setter
    def application(self, application):
        r"""Sets the application of this ModifyHlsConfig.

        推流域名APP配置

        :param application: The application of this ModifyHlsConfig.
        :type application: list[:class:`huaweicloudsdklive.v1.PushDomainApplication`]
        """
        self._application = application

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
        if not isinstance(other, ModifyHlsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
