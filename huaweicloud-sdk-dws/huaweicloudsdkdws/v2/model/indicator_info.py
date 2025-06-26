# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndicatorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'indicator_name': 'str',
        'plugin_name': 'str',
        'default_collect_rate': 'str',
        'support_datastore_version': 'str'
    }

    attribute_map = {
        'indicator_name': 'indicator_name',
        'plugin_name': 'plugin_name',
        'default_collect_rate': 'default_collect_rate',
        'support_datastore_version': 'support_datastore_version'
    }

    def __init__(self, indicator_name=None, plugin_name=None, default_collect_rate=None, support_datastore_version=None):
        r"""IndicatorInfo

        The model defined in huaweicloud sdk

        :param indicator_name: **参数解释**： 监控指标名称。 **取值范围**： 不涉及。
        :type indicator_name: str
        :param plugin_name: **参数解释**： 采集模块名称。 **取值范围**： 不涉及。
        :type plugin_name: str
        :param default_collect_rate: **参数解释**： 默认采集频率。 **取值范围**： 不涉及。
        :type default_collect_rate: str
        :param support_datastore_version: **参数解释**： 支持的集群版本。 **取值范围**： 不涉及。
        :type support_datastore_version: str
        """
        
        

        self._indicator_name = None
        self._plugin_name = None
        self._default_collect_rate = None
        self._support_datastore_version = None
        self.discriminator = None

        if indicator_name is not None:
            self.indicator_name = indicator_name
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if default_collect_rate is not None:
            self.default_collect_rate = default_collect_rate
        if support_datastore_version is not None:
            self.support_datastore_version = support_datastore_version

    @property
    def indicator_name(self):
        r"""Gets the indicator_name of this IndicatorInfo.

        **参数解释**： 监控指标名称。 **取值范围**： 不涉及。

        :return: The indicator_name of this IndicatorInfo.
        :rtype: str
        """
        return self._indicator_name

    @indicator_name.setter
    def indicator_name(self, indicator_name):
        r"""Sets the indicator_name of this IndicatorInfo.

        **参数解释**： 监控指标名称。 **取值范围**： 不涉及。

        :param indicator_name: The indicator_name of this IndicatorInfo.
        :type indicator_name: str
        """
        self._indicator_name = indicator_name

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this IndicatorInfo.

        **参数解释**： 采集模块名称。 **取值范围**： 不涉及。

        :return: The plugin_name of this IndicatorInfo.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this IndicatorInfo.

        **参数解释**： 采集模块名称。 **取值范围**： 不涉及。

        :param plugin_name: The plugin_name of this IndicatorInfo.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def default_collect_rate(self):
        r"""Gets the default_collect_rate of this IndicatorInfo.

        **参数解释**： 默认采集频率。 **取值范围**： 不涉及。

        :return: The default_collect_rate of this IndicatorInfo.
        :rtype: str
        """
        return self._default_collect_rate

    @default_collect_rate.setter
    def default_collect_rate(self, default_collect_rate):
        r"""Sets the default_collect_rate of this IndicatorInfo.

        **参数解释**： 默认采集频率。 **取值范围**： 不涉及。

        :param default_collect_rate: The default_collect_rate of this IndicatorInfo.
        :type default_collect_rate: str
        """
        self._default_collect_rate = default_collect_rate

    @property
    def support_datastore_version(self):
        r"""Gets the support_datastore_version of this IndicatorInfo.

        **参数解释**： 支持的集群版本。 **取值范围**： 不涉及。

        :return: The support_datastore_version of this IndicatorInfo.
        :rtype: str
        """
        return self._support_datastore_version

    @support_datastore_version.setter
    def support_datastore_version(self, support_datastore_version):
        r"""Sets the support_datastore_version of this IndicatorInfo.

        **参数解释**： 支持的集群版本。 **取值范围**： 不涉及。

        :param support_datastore_version: The support_datastore_version of this IndicatorInfo.
        :type support_datastore_version: str
        """
        self._support_datastore_version = support_datastore_version

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
        if not isinstance(other, IndicatorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
