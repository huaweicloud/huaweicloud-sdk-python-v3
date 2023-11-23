# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceLogConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'LogInstanceInfo',
        'lts_configs': 'list[InstanceLogConfigDetail]'
    }

    attribute_map = {
        'instance': 'instance',
        'lts_configs': 'lts_configs'
    }

    def __init__(self, instance=None, lts_configs=None):
        """InstanceLogConfig

        The model defined in huaweicloud sdk

        :param instance: 
        :type instance: :class:`huaweicloudsdkgaussdbfornosql.v3.LogInstanceInfo`
        :param lts_configs: LTS日志配置明细。从未设置LTS日志流，不返回该字段。
        :type lts_configs: list[:class:`huaweicloudsdkgaussdbfornosql.v3.InstanceLogConfigDetail`]
        """
        
        

        self._instance = None
        self._lts_configs = None
        self.discriminator = None

        self.instance = instance
        self.lts_configs = lts_configs

    @property
    def instance(self):
        """Gets the instance of this InstanceLogConfig.

        :return: The instance of this InstanceLogConfig.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.LogInstanceInfo`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this InstanceLogConfig.

        :param instance: The instance of this InstanceLogConfig.
        :type instance: :class:`huaweicloudsdkgaussdbfornosql.v3.LogInstanceInfo`
        """
        self._instance = instance

    @property
    def lts_configs(self):
        """Gets the lts_configs of this InstanceLogConfig.

        LTS日志配置明细。从未设置LTS日志流，不返回该字段。

        :return: The lts_configs of this InstanceLogConfig.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.InstanceLogConfigDetail`]
        """
        return self._lts_configs

    @lts_configs.setter
    def lts_configs(self, lts_configs):
        """Sets the lts_configs of this InstanceLogConfig.

        LTS日志配置明细。从未设置LTS日志流，不返回该字段。

        :param lts_configs: The lts_configs of this InstanceLogConfig.
        :type lts_configs: list[:class:`huaweicloudsdkgaussdbfornosql.v3.InstanceLogConfigDetail`]
        """
        self._lts_configs = lts_configs

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
        if not isinstance(other, InstanceLogConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
