# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkRuntimeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'restore_strategy': 'FlinkRestoreStrategy',
        'resource_config': 'FlinkResourceConfig'
    }

    attribute_map = {
        'version': 'version',
        'restore_strategy': 'restore_strategy',
        'resource_config': 'resource_config'
    }

    def __init__(self, version=None, restore_strategy=None, resource_config=None):
        """FlinkRuntimeConfig

        The model defined in huaweicloud sdk

        :param version: Flink 版本。仅支持 Flink 1.15及以上版本。
        :type version: str
        :param restore_strategy: 
        :type restore_strategy: :class:`huaweicloudsdkdli.v1.FlinkRestoreStrategy`
        :param resource_config: 
        :type resource_config: :class:`huaweicloudsdkdli.v1.FlinkResourceConfig`
        """
        
        

        self._version = None
        self._restore_strategy = None
        self._resource_config = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if restore_strategy is not None:
            self.restore_strategy = restore_strategy
        if resource_config is not None:
            self.resource_config = resource_config

    @property
    def version(self):
        """Gets the version of this FlinkRuntimeConfig.

        Flink 版本。仅支持 Flink 1.15及以上版本。

        :return: The version of this FlinkRuntimeConfig.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FlinkRuntimeConfig.

        Flink 版本。仅支持 Flink 1.15及以上版本。

        :param version: The version of this FlinkRuntimeConfig.
        :type version: str
        """
        self._version = version

    @property
    def restore_strategy(self):
        """Gets the restore_strategy of this FlinkRuntimeConfig.

        :return: The restore_strategy of this FlinkRuntimeConfig.
        :rtype: :class:`huaweicloudsdkdli.v1.FlinkRestoreStrategy`
        """
        return self._restore_strategy

    @restore_strategy.setter
    def restore_strategy(self, restore_strategy):
        """Sets the restore_strategy of this FlinkRuntimeConfig.

        :param restore_strategy: The restore_strategy of this FlinkRuntimeConfig.
        :type restore_strategy: :class:`huaweicloudsdkdli.v1.FlinkRestoreStrategy`
        """
        self._restore_strategy = restore_strategy

    @property
    def resource_config(self):
        """Gets the resource_config of this FlinkRuntimeConfig.

        :return: The resource_config of this FlinkRuntimeConfig.
        :rtype: :class:`huaweicloudsdkdli.v1.FlinkResourceConfig`
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        """Sets the resource_config of this FlinkRuntimeConfig.

        :param resource_config: The resource_config of this FlinkRuntimeConfig.
        :type resource_config: :class:`huaweicloudsdkdli.v1.FlinkResourceConfig`
        """
        self._resource_config = resource_config

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
        if not isinstance(other, FlinkRuntimeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
