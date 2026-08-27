# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelGroupProviderSimpleResp:

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
        'provider_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'provider_name': 'provider_name'
    }

    def __init__(self, id=None, provider_name=None):
        r"""ModelGroupProviderSimpleResp

        The model defined in huaweicloud sdk

        :param id: 供应商id。
        :type id: str
        :param provider_name: 供应商名称。
        :type provider_name: str
        """
        
        

        self._id = None
        self._provider_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if provider_name is not None:
            self.provider_name = provider_name

    @property
    def id(self):
        r"""Gets the id of this ModelGroupProviderSimpleResp.

        供应商id。

        :return: The id of this ModelGroupProviderSimpleResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelGroupProviderSimpleResp.

        供应商id。

        :param id: The id of this ModelGroupProviderSimpleResp.
        :type id: str
        """
        self._id = id

    @property
    def provider_name(self):
        r"""Gets the provider_name of this ModelGroupProviderSimpleResp.

        供应商名称。

        :return: The provider_name of this ModelGroupProviderSimpleResp.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this ModelGroupProviderSimpleResp.

        供应商名称。

        :param provider_name: The provider_name of this ModelGroupProviderSimpleResp.
        :type provider_name: str
        """
        self._provider_name = provider_name

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
        if not isinstance(other, ModelGroupProviderSimpleResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
