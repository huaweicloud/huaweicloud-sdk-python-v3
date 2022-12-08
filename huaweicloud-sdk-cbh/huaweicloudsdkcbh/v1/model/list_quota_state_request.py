# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQuotaStateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, availability_zone=None, resource_spec_code=None):
        """ListQuotaStateRequest

        The model defined in huaweicloud sdk

        :param availability_zone: 可用区（cn-north-7a）
        :type availability_zone: str
        :param resource_spec_code: 资源规格（cbh.basic.50）
        :type resource_spec_code: str
        """
        
        

        self._availability_zone = None
        self._resource_spec_code = None
        self.discriminator = None

        self.availability_zone = availability_zone
        self.resource_spec_code = resource_spec_code

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListQuotaStateRequest.

        可用区（cn-north-7a）

        :return: The availability_zone of this ListQuotaStateRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListQuotaStateRequest.

        可用区（cn-north-7a）

        :param availability_zone: The availability_zone of this ListQuotaStateRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this ListQuotaStateRequest.

        资源规格（cbh.basic.50）

        :return: The resource_spec_code of this ListQuotaStateRequest.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this ListQuotaStateRequest.

        资源规格（cbh.basic.50）

        :param resource_spec_code: The resource_spec_code of this ListQuotaStateRequest.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
        if not isinstance(other, ListQuotaStateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
