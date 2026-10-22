# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAuraJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'storages_config': 'StoragesConfig'
    }

    attribute_map = {
        'type': 'type',
        'storages_config': 'storages_config'
    }

    def __init__(self, type=None, storages_config=None):
        r"""CreateAuraJob

        The model defined in huaweicloud sdk

        :param type: **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：AuraJob。 **默认取值**：不涉及。 
        :type type: str
        :param storages_config: 
        :type storages_config: :class:`huaweicloudsdkaidatalake.v2.StoragesConfig`
        """
        
        

        self._type = None
        self._storages_config = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if storages_config is not None:
            self.storages_config = storages_config

    @property
    def type(self):
        r"""Gets the type of this CreateAuraJob.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：AuraJob。 **默认取值**：不涉及。 

        :return: The type of this CreateAuraJob.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateAuraJob.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：AuraJob。 **默认取值**：不涉及。 

        :param type: The type of this CreateAuraJob.
        :type type: str
        """
        self._type = type

    @property
    def storages_config(self):
        r"""Gets the storages_config of this CreateAuraJob.

        :return: The storages_config of this CreateAuraJob.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.StoragesConfig`
        """
        return self._storages_config

    @storages_config.setter
    def storages_config(self, storages_config):
        r"""Sets the storages_config of this CreateAuraJob.

        :param storages_config: The storages_config of this CreateAuraJob.
        :type storages_config: :class:`huaweicloudsdkaidatalake.v2.StoragesConfig`
        """
        self._storages_config = storages_config

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
        if not isinstance(other, CreateAuraJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
