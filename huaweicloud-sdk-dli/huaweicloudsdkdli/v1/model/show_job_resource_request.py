# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobResourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_name': 'str',
        'group': 'str'
    }

    attribute_map = {
        'resource_name': 'resource_name',
        'group': 'group'
    }

    def __init__(self, resource_name=None, group=None):
        """ShowJobResourceRequest

        The model defined in huaweicloud sdk

        :param resource_name: 资源名。
        :type resource_name: str
        :param group: 
        :type group: str
        """
        
        

        self._resource_name = None
        self._group = None
        self.discriminator = None

        self.resource_name = resource_name
        if group is not None:
            self.group = group

    @property
    def resource_name(self):
        """Gets the resource_name of this ShowJobResourceRequest.

        资源名。

        :return: The resource_name of this ShowJobResourceRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ShowJobResourceRequest.

        资源名。

        :param resource_name: The resource_name of this ShowJobResourceRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def group(self):
        """Gets the group of this ShowJobResourceRequest.

        :return: The group of this ShowJobResourceRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ShowJobResourceRequest.

        :param group: The group of this ShowJobResourceRequest.
        :type group: str
        """
        self._group = group

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
        if not isinstance(other, ShowJobResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
