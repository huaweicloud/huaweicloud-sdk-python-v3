# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceSecretResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secret_enable': 'bool',
        'secret_type': 'str',
        'secret_volumes': 'list[SecretVolumeResponse]',
        'group_enable': 'bool',
        'group_id': 'int'
    }

    attribute_map = {
        'secret_enable': 'secret_enable',
        'secret_type': 'secret_type',
        'secret_volumes': 'secret_volumes',
        'group_enable': 'group_enable',
        'group_id': 'group_id'
    }

    def __init__(self, secret_enable=None, secret_type=None, secret_volumes=None, group_enable=None, group_id=None):
        r"""ServiceSecretResponse

        The model defined in huaweicloud sdk

        :param secret_enable: **参数解释：** 是否启用密钥。 **取值范围：** - true：启用密钥。 - false：不启用密钥。
        :type secret_enable: bool
        :param secret_type: **参数解释：** 密钥类型。 **取值范围：** - custom：自定义密钥。 - [dew：DEW密钥。](tag:hws,hws_hk,fcs)
        :type secret_type: str
        :param secret_volumes: **参数解释：** 密钥挂载。 **约束限制：** 上限30个。
        :type secret_volumes: list[:class:`huaweicloudsdkmodelarts.v1.SecretVolumeResponse`]
        :param group_enable: **参数解释：** 是否启用镜像的用户组。 **取值范围：** - true：启用镜像的用户组。 - false：不启用镜像的用户组。
        :type group_enable: bool
        :param group_id: **参数解释：** 镜像的用户组ID。 **取值范围：** 1000~4294967294。
        :type group_id: int
        """
        
        

        self._secret_enable = None
        self._secret_type = None
        self._secret_volumes = None
        self._group_enable = None
        self._group_id = None
        self.discriminator = None

        if secret_enable is not None:
            self.secret_enable = secret_enable
        if secret_type is not None:
            self.secret_type = secret_type
        if secret_volumes is not None:
            self.secret_volumes = secret_volumes
        if group_enable is not None:
            self.group_enable = group_enable
        if group_id is not None:
            self.group_id = group_id

    @property
    def secret_enable(self):
        r"""Gets the secret_enable of this ServiceSecretResponse.

        **参数解释：** 是否启用密钥。 **取值范围：** - true：启用密钥。 - false：不启用密钥。

        :return: The secret_enable of this ServiceSecretResponse.
        :rtype: bool
        """
        return self._secret_enable

    @secret_enable.setter
    def secret_enable(self, secret_enable):
        r"""Sets the secret_enable of this ServiceSecretResponse.

        **参数解释：** 是否启用密钥。 **取值范围：** - true：启用密钥。 - false：不启用密钥。

        :param secret_enable: The secret_enable of this ServiceSecretResponse.
        :type secret_enable: bool
        """
        self._secret_enable = secret_enable

    @property
    def secret_type(self):
        r"""Gets the secret_type of this ServiceSecretResponse.

        **参数解释：** 密钥类型。 **取值范围：** - custom：自定义密钥。 - [dew：DEW密钥。](tag:hws,hws_hk,fcs)

        :return: The secret_type of this ServiceSecretResponse.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        r"""Sets the secret_type of this ServiceSecretResponse.

        **参数解释：** 密钥类型。 **取值范围：** - custom：自定义密钥。 - [dew：DEW密钥。](tag:hws,hws_hk,fcs)

        :param secret_type: The secret_type of this ServiceSecretResponse.
        :type secret_type: str
        """
        self._secret_type = secret_type

    @property
    def secret_volumes(self):
        r"""Gets the secret_volumes of this ServiceSecretResponse.

        **参数解释：** 密钥挂载。 **约束限制：** 上限30个。

        :return: The secret_volumes of this ServiceSecretResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.SecretVolumeResponse`]
        """
        return self._secret_volumes

    @secret_volumes.setter
    def secret_volumes(self, secret_volumes):
        r"""Sets the secret_volumes of this ServiceSecretResponse.

        **参数解释：** 密钥挂载。 **约束限制：** 上限30个。

        :param secret_volumes: The secret_volumes of this ServiceSecretResponse.
        :type secret_volumes: list[:class:`huaweicloudsdkmodelarts.v1.SecretVolumeResponse`]
        """
        self._secret_volumes = secret_volumes

    @property
    def group_enable(self):
        r"""Gets the group_enable of this ServiceSecretResponse.

        **参数解释：** 是否启用镜像的用户组。 **取值范围：** - true：启用镜像的用户组。 - false：不启用镜像的用户组。

        :return: The group_enable of this ServiceSecretResponse.
        :rtype: bool
        """
        return self._group_enable

    @group_enable.setter
    def group_enable(self, group_enable):
        r"""Sets the group_enable of this ServiceSecretResponse.

        **参数解释：** 是否启用镜像的用户组。 **取值范围：** - true：启用镜像的用户组。 - false：不启用镜像的用户组。

        :param group_enable: The group_enable of this ServiceSecretResponse.
        :type group_enable: bool
        """
        self._group_enable = group_enable

    @property
    def group_id(self):
        r"""Gets the group_id of this ServiceSecretResponse.

        **参数解释：** 镜像的用户组ID。 **取值范围：** 1000~4294967294。

        :return: The group_id of this ServiceSecretResponse.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ServiceSecretResponse.

        **参数解释：** 镜像的用户组ID。 **取值范围：** 1000~4294967294。

        :param group_id: The group_id of this ServiceSecretResponse.
        :type group_id: int
        """
        self._group_id = group_id

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
        if not isinstance(other, ServiceSecretResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
