# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsInputSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offline_config': 'OpsOfflineConfig'
    }

    attribute_map = {
        'offline_config': 'offline_config'
    }

    def __init__(self, offline_config=None):
        r"""OpsInputSource

        The model defined in huaweicloud sdk

        :param offline_config: 
        :type offline_config: :class:`huaweicloudsdkagentarts.v1.OpsOfflineConfig`
        """
        
        

        self._offline_config = None
        self.discriminator = None

        if offline_config is not None:
            self.offline_config = offline_config

    @property
    def offline_config(self):
        r"""Gets the offline_config of this OpsInputSource.

        :return: The offline_config of this OpsInputSource.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsOfflineConfig`
        """
        return self._offline_config

    @offline_config.setter
    def offline_config(self, offline_config):
        r"""Sets the offline_config of this OpsInputSource.

        :param offline_config: The offline_config of this OpsInputSource.
        :type offline_config: :class:`huaweicloudsdkagentarts.v1.OpsOfflineConfig`
        """
        self._offline_config = offline_config

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
        if not isinstance(other, OpsInputSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
