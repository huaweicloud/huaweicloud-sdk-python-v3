# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCoreSpaceNetworkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_access_enable': 'bool',
        'private_access_config': 'CoreSpacePrivateNetworkRequestBody'
    }

    attribute_map = {
        'public_access_enable': 'public_access_enable',
        'private_access_config': 'private_access_config'
    }

    def __init__(self, public_access_enable=None, private_access_config=None):
        r"""CreateCoreSpaceNetworkRequestBody

        The model defined in huaweicloud sdk

        :param public_access_enable: **参数解释：** 是否开启公网访问。 **约束限制：** 不涉及。 **取值范围：** - true: 开启公网访问 - false: 关闭公网访问 **默认取值：** false 
        :type public_access_enable: bool
        :param private_access_config: 
        :type private_access_config: :class:`huaweicloudsdkagentarts.v1.CoreSpacePrivateNetworkRequestBody`
        """
        
        

        self._public_access_enable = None
        self._private_access_config = None
        self.discriminator = None

        if public_access_enable is not None:
            self.public_access_enable = public_access_enable
        if private_access_config is not None:
            self.private_access_config = private_access_config

    @property
    def public_access_enable(self):
        r"""Gets the public_access_enable of this CreateCoreSpaceNetworkRequestBody.

        **参数解释：** 是否开启公网访问。 **约束限制：** 不涉及。 **取值范围：** - true: 开启公网访问 - false: 关闭公网访问 **默认取值：** false 

        :return: The public_access_enable of this CreateCoreSpaceNetworkRequestBody.
        :rtype: bool
        """
        return self._public_access_enable

    @public_access_enable.setter
    def public_access_enable(self, public_access_enable):
        r"""Sets the public_access_enable of this CreateCoreSpaceNetworkRequestBody.

        **参数解释：** 是否开启公网访问。 **约束限制：** 不涉及。 **取值范围：** - true: 开启公网访问 - false: 关闭公网访问 **默认取值：** false 

        :param public_access_enable: The public_access_enable of this CreateCoreSpaceNetworkRequestBody.
        :type public_access_enable: bool
        """
        self._public_access_enable = public_access_enable

    @property
    def private_access_config(self):
        r"""Gets the private_access_config of this CreateCoreSpaceNetworkRequestBody.

        :return: The private_access_config of this CreateCoreSpaceNetworkRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreSpacePrivateNetworkRequestBody`
        """
        return self._private_access_config

    @private_access_config.setter
    def private_access_config(self, private_access_config):
        r"""Sets the private_access_config of this CreateCoreSpaceNetworkRequestBody.

        :param private_access_config: The private_access_config of this CreateCoreSpaceNetworkRequestBody.
        :type private_access_config: :class:`huaweicloudsdkagentarts.v1.CoreSpacePrivateNetworkRequestBody`
        """
        self._private_access_config = private_access_config

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
        if not isinstance(other, CreateCoreSpaceNetworkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
