# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrantAccessServiceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_services': 'list[AccessServiceInfo]'
    }

    attribute_map = {
        'access_services': 'access_services'
    }

    def __init__(self, access_services=None):
        r"""GrantAccessServiceRequestBody

        The model defined in huaweicloud sdk

        :param access_services: 接入服务授权信息列表
        :type access_services: list[:class:`huaweicloudsdklakeformation.v1.AccessServiceInfo`]
        """
        
        

        self._access_services = None
        self.discriminator = None

        self.access_services = access_services

    @property
    def access_services(self):
        r"""Gets the access_services of this GrantAccessServiceRequestBody.

        接入服务授权信息列表

        :return: The access_services of this GrantAccessServiceRequestBody.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.AccessServiceInfo`]
        """
        return self._access_services

    @access_services.setter
    def access_services(self, access_services):
        r"""Sets the access_services of this GrantAccessServiceRequestBody.

        接入服务授权信息列表

        :param access_services: The access_services of this GrantAccessServiceRequestBody.
        :type access_services: list[:class:`huaweicloudsdklakeformation.v1.AccessServiceInfo`]
        """
        self._access_services = access_services

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
        if not isinstance(other, GrantAccessServiceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
