# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Framework:

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
        'version_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'version_name': 'version_name'
    }

    def __init__(self, name=None, version_name=None):
        r"""Framework

        The model defined in huaweicloud sdk

        :param name: Framework名称
        :type name: str
        :param version_name: Framework版本
        :type version_name: str
        """
        
        

        self._name = None
        self._version_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if version_name is not None:
            self.version_name = version_name

    @property
    def name(self):
        r"""Gets the name of this Framework.

        Framework名称

        :return: The name of this Framework.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Framework.

        Framework名称

        :param name: The name of this Framework.
        :type name: str
        """
        self._name = name

    @property
    def version_name(self):
        r"""Gets the version_name of this Framework.

        Framework版本

        :return: The version_name of this Framework.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this Framework.

        Framework版本

        :param version_name: The version_name of this Framework.
        :type version_name: str
        """
        self._version_name = version_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Framework):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
