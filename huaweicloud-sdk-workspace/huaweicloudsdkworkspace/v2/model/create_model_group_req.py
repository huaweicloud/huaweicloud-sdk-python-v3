# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModelGroupReq:

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
        'description': 'str',
        'provider_ids': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'provider_ids': 'provider_ids'
    }

    def __init__(self, name=None, description=None, provider_ids=None):
        r"""CreateModelGroupReq

        The model defined in huaweicloud sdk

        :param name: 分组名称。
        :type name: str
        :param description: 分组描述。
        :type description: str
        :param provider_ids: 初始关联的供应商ID列表（可选）。
        :type provider_ids: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._provider_ids = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if provider_ids is not None:
            self.provider_ids = provider_ids

    @property
    def name(self):
        r"""Gets the name of this CreateModelGroupReq.

        分组名称。

        :return: The name of this CreateModelGroupReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateModelGroupReq.

        分组名称。

        :param name: The name of this CreateModelGroupReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateModelGroupReq.

        分组描述。

        :return: The description of this CreateModelGroupReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateModelGroupReq.

        分组描述。

        :param description: The description of this CreateModelGroupReq.
        :type description: str
        """
        self._description = description

    @property
    def provider_ids(self):
        r"""Gets the provider_ids of this CreateModelGroupReq.

        初始关联的供应商ID列表（可选）。

        :return: The provider_ids of this CreateModelGroupReq.
        :rtype: list[str]
        """
        return self._provider_ids

    @provider_ids.setter
    def provider_ids(self, provider_ids):
        r"""Sets the provider_ids of this CreateModelGroupReq.

        初始关联的供应商ID列表（可选）。

        :param provider_ids: The provider_ids of this CreateModelGroupReq.
        :type provider_ids: list[str]
        """
        self._provider_ids = provider_ids

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
        if not isinstance(other, CreateModelGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
