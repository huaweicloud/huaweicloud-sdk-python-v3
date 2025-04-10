# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigValues:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'list[Configs]',
        'extended_configs': 'ExtendedConfigs'
    }

    attribute_map = {
        'configs': 'configs',
        'extended_configs': 'extended-configs'
    }

    def __init__(self, configs=None, extended_configs=None):
        r"""ConfigValues

        The model defined in huaweicloud sdk

        :param configs: 源连接参数、目的连接参数和作业任务参数，它们的配置数据结构相同，其中“inputs”里的参数不一样，详细请参见configs数据结构说明
        :type configs: list[:class:`huaweicloudsdkcdm.v1.Configs`]
        :param extended_configs: 
        :type extended_configs: :class:`huaweicloudsdkcdm.v1.ExtendedConfigs`
        """
        
        

        self._configs = None
        self._extended_configs = None
        self.discriminator = None

        self.configs = configs
        if extended_configs is not None:
            self.extended_configs = extended_configs

    @property
    def configs(self):
        r"""Gets the configs of this ConfigValues.

        源连接参数、目的连接参数和作业任务参数，它们的配置数据结构相同，其中“inputs”里的参数不一样，详细请参见configs数据结构说明

        :return: The configs of this ConfigValues.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Configs`]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this ConfigValues.

        源连接参数、目的连接参数和作业任务参数，它们的配置数据结构相同，其中“inputs”里的参数不一样，详细请参见configs数据结构说明

        :param configs: The configs of this ConfigValues.
        :type configs: list[:class:`huaweicloudsdkcdm.v1.Configs`]
        """
        self._configs = configs

    @property
    def extended_configs(self):
        r"""Gets the extended_configs of this ConfigValues.

        :return: The extended_configs of this ConfigValues.
        :rtype: :class:`huaweicloudsdkcdm.v1.ExtendedConfigs`
        """
        return self._extended_configs

    @extended_configs.setter
    def extended_configs(self, extended_configs):
        r"""Sets the extended_configs of this ConfigValues.

        :param extended_configs: The extended_configs of this ConfigValues.
        :type extended_configs: :class:`huaweicloudsdkcdm.v1.ExtendedConfigs`
        """
        self._extended_configs = extended_configs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
