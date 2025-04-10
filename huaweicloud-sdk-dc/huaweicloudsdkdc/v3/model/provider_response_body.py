# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProviderResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'short_name': 'str',
        'type': 'str',
        'provider_value': 'ProviderValueBody',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'short_name': 'short_name',
        'type': 'type',
        'provider_value': 'provider_value',
        'description': 'description'
    }

    def __init__(self, id=None, short_name=None, type=None, provider_value=None, description=None):
        r"""ProviderResponseBody

        The model defined in huaweicloud sdk

        :param id: 运营商id
        :type id: str
        :param short_name: 运营商简写
        :type short_name: str
        :param type: 运营商类型
        :type type: str
        :param provider_value: 
        :type provider_value: :class:`huaweicloudsdkdc.v3.ProviderValueBody`
        :param description: 运营商说明
        :type description: str
        """
        
        

        self._id = None
        self._short_name = None
        self._type = None
        self._provider_value = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if short_name is not None:
            self.short_name = short_name
        if type is not None:
            self.type = type
        if provider_value is not None:
            self.provider_value = provider_value
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this ProviderResponseBody.

        运营商id

        :return: The id of this ProviderResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProviderResponseBody.

        运营商id

        :param id: The id of this ProviderResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def short_name(self):
        r"""Gets the short_name of this ProviderResponseBody.

        运营商简写

        :return: The short_name of this ProviderResponseBody.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        r"""Sets the short_name of this ProviderResponseBody.

        运营商简写

        :param short_name: The short_name of this ProviderResponseBody.
        :type short_name: str
        """
        self._short_name = short_name

    @property
    def type(self):
        r"""Gets the type of this ProviderResponseBody.

        运营商类型

        :return: The type of this ProviderResponseBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ProviderResponseBody.

        运营商类型

        :param type: The type of this ProviderResponseBody.
        :type type: str
        """
        self._type = type

    @property
    def provider_value(self):
        r"""Gets the provider_value of this ProviderResponseBody.

        :return: The provider_value of this ProviderResponseBody.
        :rtype: :class:`huaweicloudsdkdc.v3.ProviderValueBody`
        """
        return self._provider_value

    @provider_value.setter
    def provider_value(self, provider_value):
        r"""Sets the provider_value of this ProviderResponseBody.

        :param provider_value: The provider_value of this ProviderResponseBody.
        :type provider_value: :class:`huaweicloudsdkdc.v3.ProviderValueBody`
        """
        self._provider_value = provider_value

    @property
    def description(self):
        r"""Gets the description of this ProviderResponseBody.

        运营商说明

        :return: The description of this ProviderResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProviderResponseBody.

        运营商说明

        :param description: The description of this ProviderResponseBody.
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
        if not isinstance(other, ProviderResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
