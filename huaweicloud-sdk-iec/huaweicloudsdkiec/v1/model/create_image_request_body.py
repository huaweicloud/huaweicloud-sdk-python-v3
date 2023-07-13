# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageRequestBody:

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
        'instance_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'instance_id': 'instance_id'
    }

    def __init__(self, name=None, instance_id=None):
        """CreateImageRequestBody

        The model defined in huaweicloud sdk

        :param name: 边缘私有镜像名称。
        :type name: str
        :param instance_id: 边缘实例名称。
        :type instance_id: str
        """
        
        

        self._name = None
        self._instance_id = None
        self.discriminator = None

        self.name = name
        self.instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this CreateImageRequestBody.

        边缘私有镜像名称。

        :return: The name of this CreateImageRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateImageRequestBody.

        边缘私有镜像名称。

        :param name: The name of this CreateImageRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateImageRequestBody.

        边缘实例名称。

        :return: The instance_id of this CreateImageRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateImageRequestBody.

        边缘实例名称。

        :param instance_id: The instance_id of this CreateImageRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, CreateImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
