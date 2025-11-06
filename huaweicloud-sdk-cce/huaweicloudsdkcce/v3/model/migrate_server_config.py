# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateServerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'root_volume': 'MigrateVolumeSpec'
    }

    attribute_map = {
        'root_volume': 'rootVolume'
    }

    def __init__(self, root_volume=None):
        r"""MigrateServerConfig

        The model defined in huaweicloud sdk

        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkcce.v3.MigrateVolumeSpec`
        """
        
        

        self._root_volume = None
        self.discriminator = None

        if root_volume is not None:
            self.root_volume = root_volume

    @property
    def root_volume(self):
        r"""Gets the root_volume of this MigrateServerConfig.

        :return: The root_volume of this MigrateServerConfig.
        :rtype: :class:`huaweicloudsdkcce.v3.MigrateVolumeSpec`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this MigrateServerConfig.

        :param root_volume: The root_volume of this MigrateServerConfig.
        :type root_volume: :class:`huaweicloudsdkcce.v3.MigrateVolumeSpec`
        """
        self._root_volume = root_volume

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
        if not isinstance(other, MigrateServerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
