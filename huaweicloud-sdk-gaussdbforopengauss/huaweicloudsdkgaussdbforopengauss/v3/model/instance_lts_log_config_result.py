# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceLtsLogConfigResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'object',
        'lts_configs': 'list[LtsLogConfigResult]'
    }

    attribute_map = {
        'instance': 'instance',
        'lts_configs': 'lts_configs'
    }

    def __init__(self, instance=None, lts_configs=None):
        r"""InstanceLtsLogConfigResult

        The model defined in huaweicloud sdk

        :param instance: **参数解释**: 实例基本信息。
        :type instance: object
        :param lts_configs: **参数解释**: LTS相关信息。
        :type lts_configs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.LtsLogConfigResult`]
        """
        
        

        self._instance = None
        self._lts_configs = None
        self.discriminator = None

        if instance is not None:
            self.instance = instance
        if lts_configs is not None:
            self.lts_configs = lts_configs

    @property
    def instance(self):
        r"""Gets the instance of this InstanceLtsLogConfigResult.

        **参数解释**: 实例基本信息。

        :return: The instance of this InstanceLtsLogConfigResult.
        :rtype: object
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this InstanceLtsLogConfigResult.

        **参数解释**: 实例基本信息。

        :param instance: The instance of this InstanceLtsLogConfigResult.
        :type instance: object
        """
        self._instance = instance

    @property
    def lts_configs(self):
        r"""Gets the lts_configs of this InstanceLtsLogConfigResult.

        **参数解释**: LTS相关信息。

        :return: The lts_configs of this InstanceLtsLogConfigResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.LtsLogConfigResult`]
        """
        return self._lts_configs

    @lts_configs.setter
    def lts_configs(self, lts_configs):
        r"""Sets the lts_configs of this InstanceLtsLogConfigResult.

        **参数解释**: LTS相关信息。

        :param lts_configs: The lts_configs of this InstanceLtsLogConfigResult.
        :type lts_configs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.LtsLogConfigResult`]
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
        if not isinstance(other, InstanceLtsLogConfigResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
