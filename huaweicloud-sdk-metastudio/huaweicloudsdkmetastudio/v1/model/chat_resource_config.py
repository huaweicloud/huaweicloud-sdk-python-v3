# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChatResourceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'count_resource': 'int'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'count_resource': 'count_resource'
    }

    def __init__(self, resource_id=None, count_resource=None):
        r"""ChatResourceConfig

        The model defined in huaweicloud sdk

        :param resource_id: 资源id
        :type resource_id: str
        :param count_resource: 资源数量
        :type count_resource: int
        """
        
        

        self._resource_id = None
        self._count_resource = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if count_resource is not None:
            self.count_resource = count_resource

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ChatResourceConfig.

        资源id

        :return: The resource_id of this ChatResourceConfig.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ChatResourceConfig.

        资源id

        :param resource_id: The resource_id of this ChatResourceConfig.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def count_resource(self):
        r"""Gets the count_resource of this ChatResourceConfig.

        资源数量

        :return: The count_resource of this ChatResourceConfig.
        :rtype: int
        """
        return self._count_resource

    @count_resource.setter
    def count_resource(self, count_resource):
        r"""Sets the count_resource of this ChatResourceConfig.

        资源数量

        :param count_resource: The count_resource of this ChatResourceConfig.
        :type count_resource: int
        """
        self._count_resource = count_resource

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
        if not isinstance(other, ChatResourceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
