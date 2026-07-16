# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunStorageConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sfs_turbo': 'list[CoreRunSfsTurboStorageConfig]'
    }

    attribute_map = {
        'sfs_turbo': 'sfs_turbo'
    }

    def __init__(self, sfs_turbo=None):
        r"""CoreRunStorageConfig

        The model defined in huaweicloud sdk

        :param sfs_turbo: **参数解释**: SFS Turbo存储挂载配置列表。
        :type sfs_turbo: list[:class:`huaweicloudsdkagentarts.v1.CoreRunSfsTurboStorageConfig`]
        """
        
        

        self._sfs_turbo = None
        self.discriminator = None

        if sfs_turbo is not None:
            self.sfs_turbo = sfs_turbo

    @property
    def sfs_turbo(self):
        r"""Gets the sfs_turbo of this CoreRunStorageConfig.

        **参数解释**: SFS Turbo存储挂载配置列表。

        :return: The sfs_turbo of this CoreRunStorageConfig.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunSfsTurboStorageConfig`]
        """
        return self._sfs_turbo

    @sfs_turbo.setter
    def sfs_turbo(self, sfs_turbo):
        r"""Sets the sfs_turbo of this CoreRunStorageConfig.

        **参数解释**: SFS Turbo存储挂载配置列表。

        :param sfs_turbo: The sfs_turbo of this CoreRunStorageConfig.
        :type sfs_turbo: list[:class:`huaweicloudsdkagentarts.v1.CoreRunSfsTurboStorageConfig`]
        """
        self._sfs_turbo = sfs_turbo

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
        if not isinstance(other, CoreRunStorageConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
