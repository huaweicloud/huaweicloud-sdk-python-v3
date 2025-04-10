# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChInstanceLtsConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lts_configs': 'list[ChLtsConfigs]',
        'instance': 'ChInstanceLtsConfigsInstance'
    }

    attribute_map = {
        'lts_configs': 'lts_configs',
        'instance': 'instance'
    }

    def __init__(self, lts_configs=None, instance=None):
        r"""ChInstanceLtsConfigs

        The model defined in huaweicloud sdk

        :param lts_configs: 实例LTS配置信息。
        :type lts_configs: list[:class:`huaweicloudsdkgaussdb.v3.ChLtsConfigs`]
        :param instance: 
        :type instance: :class:`huaweicloudsdkgaussdb.v3.ChInstanceLtsConfigsInstance`
        """
        
        

        self._lts_configs = None
        self._instance = None
        self.discriminator = None

        if lts_configs is not None:
            self.lts_configs = lts_configs
        if instance is not None:
            self.instance = instance

    @property
    def lts_configs(self):
        r"""Gets the lts_configs of this ChInstanceLtsConfigs.

        实例LTS配置信息。

        :return: The lts_configs of this ChInstanceLtsConfigs.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ChLtsConfigs`]
        """
        return self._lts_configs

    @lts_configs.setter
    def lts_configs(self, lts_configs):
        r"""Sets the lts_configs of this ChInstanceLtsConfigs.

        实例LTS配置信息。

        :param lts_configs: The lts_configs of this ChInstanceLtsConfigs.
        :type lts_configs: list[:class:`huaweicloudsdkgaussdb.v3.ChLtsConfigs`]
        """
        self._lts_configs = lts_configs

    @property
    def instance(self):
        r"""Gets the instance of this ChInstanceLtsConfigs.

        :return: The instance of this ChInstanceLtsConfigs.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChInstanceLtsConfigsInstance`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this ChInstanceLtsConfigs.

        :param instance: The instance of this ChInstanceLtsConfigs.
        :type instance: :class:`huaweicloudsdkgaussdb.v3.ChInstanceLtsConfigsInstance`
        """
        self._instance = instance

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
        if not isinstance(other, ChInstanceLtsConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
