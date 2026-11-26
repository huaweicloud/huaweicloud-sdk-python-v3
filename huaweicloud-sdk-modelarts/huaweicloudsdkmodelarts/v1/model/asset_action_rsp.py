# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetActionRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_type': 'str',
        'action_dir': 'str'
    }

    attribute_map = {
        'action_type': 'action_type',
        'action_dir': 'action_dir'
    }

    def __init__(self, action_type=None, action_dir=None):
        r"""AssetActionRsp

        The model defined in huaweicloud sdk

        :param action_type: **参数解释**：资产action类型。 **取值范围**：不涉及。
        :type action_type: str
        :param action_dir: **参数解释**：资产action配置文件地址。 **取值范围**：不涉及。
        :type action_dir: str
        """
        
        

        self._action_type = None
        self._action_dir = None
        self.discriminator = None

        if action_type is not None:
            self.action_type = action_type
        if action_dir is not None:
            self.action_dir = action_dir

    @property
    def action_type(self):
        r"""Gets the action_type of this AssetActionRsp.

        **参数解释**：资产action类型。 **取值范围**：不涉及。

        :return: The action_type of this AssetActionRsp.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this AssetActionRsp.

        **参数解释**：资产action类型。 **取值范围**：不涉及。

        :param action_type: The action_type of this AssetActionRsp.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def action_dir(self):
        r"""Gets the action_dir of this AssetActionRsp.

        **参数解释**：资产action配置文件地址。 **取值范围**：不涉及。

        :return: The action_dir of this AssetActionRsp.
        :rtype: str
        """
        return self._action_dir

    @action_dir.setter
    def action_dir(self, action_dir):
        r"""Sets the action_dir of this AssetActionRsp.

        **参数解释**：资产action配置文件地址。 **取值范围**：不涉及。

        :param action_dir: The action_dir of this AssetActionRsp.
        :type action_dir: str
        """
        self._action_dir = action_dir

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
        if not isinstance(other, AssetActionRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
