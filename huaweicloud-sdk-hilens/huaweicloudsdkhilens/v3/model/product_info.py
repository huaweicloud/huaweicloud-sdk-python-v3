# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service_type': 'str',
        'resource_spec_code': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'resource_spec_code': 'resource_spec_code',
        'resource_type': 'resource_type'
    }

    def __init__(self, cloud_service_type=None, resource_spec_code=None, resource_type=None):
        """ProductInfo

        The model defined in huaweicloud sdk

        :param cloud_service_type: 
        :type cloud_service_type: str
        :param resource_spec_code: 
        :type resource_spec_code: str
        :param resource_type: 
        :type resource_type: str
        """
        
        

        self._cloud_service_type = None
        self._resource_spec_code = None
        self._resource_type = None
        self.discriminator = None

        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this ProductInfo.

        :return: The cloud_service_type of this ProductInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this ProductInfo.

        :param cloud_service_type: The cloud_service_type of this ProductInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this ProductInfo.

        :return: The resource_spec_code of this ProductInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this ProductInfo.

        :param resource_spec_code: The resource_spec_code of this ProductInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_type(self):
        """Gets the resource_type of this ProductInfo.

        :return: The resource_type of this ProductInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ProductInfo.

        :param resource_type: The resource_type of this ProductInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
