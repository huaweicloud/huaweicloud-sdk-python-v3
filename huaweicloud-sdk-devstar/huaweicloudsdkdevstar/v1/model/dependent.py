# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Dependent:

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
        'dependent_services': 'list[ResouceInfo]'
    }

    attribute_map = {
        'name': 'name',
        'dependent_services': 'dependent_services'
    }

    def __init__(self, name=None, dependent_services=None):
        """Dependent

        The model defined in huaweicloud sdk

        :param name: 部署方式。
        :type name: str
        :param dependent_services: 依赖云资源信息
        :type dependent_services: list[:class:`huaweicloudsdkdevstar.v1.ResouceInfo`]
        """
        
        

        self._name = None
        self._dependent_services = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if dependent_services is not None:
            self.dependent_services = dependent_services

    @property
    def name(self):
        """Gets the name of this Dependent.

        部署方式。

        :return: The name of this Dependent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dependent.

        部署方式。

        :param name: The name of this Dependent.
        :type name: str
        """
        self._name = name

    @property
    def dependent_services(self):
        """Gets the dependent_services of this Dependent.

        依赖云资源信息

        :return: The dependent_services of this Dependent.
        :rtype: list[:class:`huaweicloudsdkdevstar.v1.ResouceInfo`]
        """
        return self._dependent_services

    @dependent_services.setter
    def dependent_services(self, dependent_services):
        """Sets the dependent_services of this Dependent.

        依赖云资源信息

        :param dependent_services: The dependent_services of this Dependent.
        :type dependent_services: list[:class:`huaweicloudsdkdevstar.v1.ResouceInfo`]
        """
        self._dependent_services = dependent_services

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
        if not isinstance(other, Dependent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
