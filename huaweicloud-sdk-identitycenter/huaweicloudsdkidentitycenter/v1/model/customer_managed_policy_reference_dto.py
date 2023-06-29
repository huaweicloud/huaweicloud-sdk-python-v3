# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerManagedPolicyReferenceDto:

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
        'path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path'
    }

    def __init__(self, name=None, path=None):
        """CustomerManagedPolicyReferenceDto

        The model defined in huaweicloud sdk

        :param name: IAM策略名称.
        :type name: str
        :param path: IAM策略路径，默认值/.
        :type path: str
        """
        
        

        self._name = None
        self._path = None
        self.discriminator = None

        self.name = name
        if path is not None:
            self.path = path

    @property
    def name(self):
        """Gets the name of this CustomerManagedPolicyReferenceDto.

        IAM策略名称.

        :return: The name of this CustomerManagedPolicyReferenceDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerManagedPolicyReferenceDto.

        IAM策略名称.

        :param name: The name of this CustomerManagedPolicyReferenceDto.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        """Gets the path of this CustomerManagedPolicyReferenceDto.

        IAM策略路径，默认值/.

        :return: The path of this CustomerManagedPolicyReferenceDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CustomerManagedPolicyReferenceDto.

        IAM策略路径，默认值/.

        :param path: The path of this CustomerManagedPolicyReferenceDto.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, CustomerManagedPolicyReferenceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other