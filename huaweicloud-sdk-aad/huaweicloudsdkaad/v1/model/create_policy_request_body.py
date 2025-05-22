# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePolicyRequestBody:

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
        'package_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'package_id': 'package_id',
        'description': 'description'
    }

    def __init__(self, name=None, package_id=None, description=None):
        r"""CreatePolicyRequestBody

        The model defined in huaweicloud sdk

        :param name: 策略名
        :type name: str
        :param package_id: 实例id
        :type package_id: str
        :param description: 描述
        :type description: str
        """
        
        

        self._name = None
        self._package_id = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.package_id = package_id
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this CreatePolicyRequestBody.

        策略名

        :return: The name of this CreatePolicyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePolicyRequestBody.

        策略名

        :param name: The name of this CreatePolicyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def package_id(self):
        r"""Gets the package_id of this CreatePolicyRequestBody.

        实例id

        :return: The package_id of this CreatePolicyRequestBody.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        r"""Sets the package_id of this CreatePolicyRequestBody.

        实例id

        :param package_id: The package_id of this CreatePolicyRequestBody.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def description(self):
        r"""Gets the description of this CreatePolicyRequestBody.

        描述

        :return: The description of this CreatePolicyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePolicyRequestBody.

        描述

        :param description: The description of this CreatePolicyRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreatePolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
