# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeNodePoolSpecNodeTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'life_cycle': 'NodeLifecycleConfig',
        'login': 'Login',
        'volume_config': 'VolumeConfig'
    }

    attribute_map = {
        'life_cycle': 'lifeCycle',
        'login': 'login',
        'volume_config': 'volumeConfig'
    }

    def __init__(self, life_cycle=None, login=None, volume_config=None):
        r"""UpgradeNodePoolSpecNodeTemplate

        The model defined in huaweicloud sdk

        :param life_cycle: 
        :type life_cycle: :class:`huaweicloudsdkcce.v3.NodeLifecycleConfig`
        :param login: 
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        :param volume_config: 
        :type volume_config: :class:`huaweicloudsdkcce.v3.VolumeConfig`
        """
        
        

        self._life_cycle = None
        self._login = None
        self._volume_config = None
        self.discriminator = None

        self.life_cycle = life_cycle
        self.login = login
        if volume_config is not None:
            self.volume_config = volume_config

    @property
    def life_cycle(self):
        r"""Gets the life_cycle of this UpgradeNodePoolSpecNodeTemplate.

        :return: The life_cycle of this UpgradeNodePoolSpecNodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeLifecycleConfig`
        """
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        r"""Sets the life_cycle of this UpgradeNodePoolSpecNodeTemplate.

        :param life_cycle: The life_cycle of this UpgradeNodePoolSpecNodeTemplate.
        :type life_cycle: :class:`huaweicloudsdkcce.v3.NodeLifecycleConfig`
        """
        self._life_cycle = life_cycle

    @property
    def login(self):
        r"""Gets the login of this UpgradeNodePoolSpecNodeTemplate.

        :return: The login of this UpgradeNodePoolSpecNodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.Login`
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this UpgradeNodePoolSpecNodeTemplate.

        :param login: The login of this UpgradeNodePoolSpecNodeTemplate.
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        """
        self._login = login

    @property
    def volume_config(self):
        r"""Gets the volume_config of this UpgradeNodePoolSpecNodeTemplate.

        :return: The volume_config of this UpgradeNodePoolSpecNodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.VolumeConfig`
        """
        return self._volume_config

    @volume_config.setter
    def volume_config(self, volume_config):
        r"""Sets the volume_config of this UpgradeNodePoolSpecNodeTemplate.

        :param volume_config: The volume_config of this UpgradeNodePoolSpecNodeTemplate.
        :type volume_config: :class:`huaweicloudsdkcce.v3.VolumeConfig`
        """
        self._volume_config = volume_config

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
        if not isinstance(other, UpgradeNodePoolSpecNodeTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
