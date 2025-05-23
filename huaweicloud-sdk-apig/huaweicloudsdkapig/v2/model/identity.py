# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Identity:

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
        'location': 'str',
        'validation': 'str'
    }

    attribute_map = {
        'name': 'name',
        'location': 'location',
        'validation': 'validation'
    }

    def __init__(self, name=None, location=None, validation=None):
        r"""Identity

        The model defined in huaweicloud sdk

        :param name: 参数名称
        :type name: str
        :param location: 参数位置
        :type location: str
        :param validation: 参数校验表达式，默认为null，不做校验
        :type validation: str
        """
        
        

        self._name = None
        self._location = None
        self._validation = None
        self.discriminator = None

        self.name = name
        self.location = location
        if validation is not None:
            self.validation = validation

    @property
    def name(self):
        r"""Gets the name of this Identity.

        参数名称

        :return: The name of this Identity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Identity.

        参数名称

        :param name: The name of this Identity.
        :type name: str
        """
        self._name = name

    @property
    def location(self):
        r"""Gets the location of this Identity.

        参数位置

        :return: The location of this Identity.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this Identity.

        参数位置

        :param location: The location of this Identity.
        :type location: str
        """
        self._location = location

    @property
    def validation(self):
        r"""Gets the validation of this Identity.

        参数校验表达式，默认为null，不做校验

        :return: The validation of this Identity.
        :rtype: str
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        r"""Sets the validation of this Identity.

        参数校验表达式，默认为null，不做校验

        :param validation: The validation of this Identity.
        :type validation: str
        """
        self._validation = validation

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
        if not isinstance(other, Identity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
