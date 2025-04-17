# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'first_dimension_name': 'str',
        'first_dimension_value': 'str',
        'resource_name': 'str'
    }

    attribute_map = {
        'first_dimension_name': 'first_dimension_name',
        'first_dimension_value': 'first_dimension_value',
        'resource_name': 'resource_name'
    }

    def __init__(self, first_dimension_name=None, first_dimension_value=None, resource_name=None):
        r"""ProductInstance

        The model defined in huaweicloud sdk

        :param first_dimension_name: 资源首层维度，如：弹性云服务器，则维度为instance_id；”。
        :type first_dimension_name: str
        :param first_dimension_value: 资源首层维度值，为资源的实例ID，如：4270ff17-aba3-4138-89fa-820594c39755。
        :type first_dimension_value: str
        :param resource_name: 资源名称
        :type resource_name: str
        """
        
        

        self._first_dimension_name = None
        self._first_dimension_value = None
        self._resource_name = None
        self.discriminator = None

        self.first_dimension_name = first_dimension_name
        self.first_dimension_value = first_dimension_value
        self.resource_name = resource_name

    @property
    def first_dimension_name(self):
        r"""Gets the first_dimension_name of this ProductInstance.

        资源首层维度，如：弹性云服务器，则维度为instance_id；”。

        :return: The first_dimension_name of this ProductInstance.
        :rtype: str
        """
        return self._first_dimension_name

    @first_dimension_name.setter
    def first_dimension_name(self, first_dimension_name):
        r"""Sets the first_dimension_name of this ProductInstance.

        资源首层维度，如：弹性云服务器，则维度为instance_id；”。

        :param first_dimension_name: The first_dimension_name of this ProductInstance.
        :type first_dimension_name: str
        """
        self._first_dimension_name = first_dimension_name

    @property
    def first_dimension_value(self):
        r"""Gets the first_dimension_value of this ProductInstance.

        资源首层维度值，为资源的实例ID，如：4270ff17-aba3-4138-89fa-820594c39755。

        :return: The first_dimension_value of this ProductInstance.
        :rtype: str
        """
        return self._first_dimension_value

    @first_dimension_value.setter
    def first_dimension_value(self, first_dimension_value):
        r"""Sets the first_dimension_value of this ProductInstance.

        资源首层维度值，为资源的实例ID，如：4270ff17-aba3-4138-89fa-820594c39755。

        :param first_dimension_value: The first_dimension_value of this ProductInstance.
        :type first_dimension_value: str
        """
        self._first_dimension_value = first_dimension_value

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ProductInstance.

        资源名称

        :return: The resource_name of this ProductInstance.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ProductInstance.

        资源名称

        :param resource_name: The resource_name of this ProductInstance.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, ProductInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
