# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamRuntimeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'staging_uri': 'str',
        'logging': 'StreamLoggingConfig',
        'properties': 'Properties',
        'flink_runtime_config': 'FlinkRuntimeConfig'
    }

    attribute_map = {
        'staging_uri': 'staging_uri',
        'logging': 'logging',
        'properties': 'properties',
        'flink_runtime_config': 'flink_runtime_config'
    }

    def __init__(self, staging_uri=None, logging=None, properties=None, flink_runtime_config=None):
        """StreamRuntimeConfig

        The model defined in huaweicloud sdk

        :param staging_uri: 临时文件存储 URI，作业运行时产生的临时文件存储的 OBS 路径。（当前不支持配置）
        :type staging_uri: str
        :param logging: 
        :type logging: :class:`huaweicloudsdkdli.v1.StreamLoggingConfig`
        :param properties: 
        :type properties: :class:`huaweicloudsdkdli.v1.Properties`
        :param flink_runtime_config: 
        :type flink_runtime_config: :class:`huaweicloudsdkdli.v1.FlinkRuntimeConfig`
        """
        
        

        self._staging_uri = None
        self._logging = None
        self._properties = None
        self._flink_runtime_config = None
        self.discriminator = None

        if staging_uri is not None:
            self.staging_uri = staging_uri
        if logging is not None:
            self.logging = logging
        if properties is not None:
            self.properties = properties
        if flink_runtime_config is not None:
            self.flink_runtime_config = flink_runtime_config

    @property
    def staging_uri(self):
        """Gets the staging_uri of this StreamRuntimeConfig.

        临时文件存储 URI，作业运行时产生的临时文件存储的 OBS 路径。（当前不支持配置）

        :return: The staging_uri of this StreamRuntimeConfig.
        :rtype: str
        """
        return self._staging_uri

    @staging_uri.setter
    def staging_uri(self, staging_uri):
        """Sets the staging_uri of this StreamRuntimeConfig.

        临时文件存储 URI，作业运行时产生的临时文件存储的 OBS 路径。（当前不支持配置）

        :param staging_uri: The staging_uri of this StreamRuntimeConfig.
        :type staging_uri: str
        """
        self._staging_uri = staging_uri

    @property
    def logging(self):
        """Gets the logging of this StreamRuntimeConfig.

        :return: The logging of this StreamRuntimeConfig.
        :rtype: :class:`huaweicloudsdkdli.v1.StreamLoggingConfig`
        """
        return self._logging

    @logging.setter
    def logging(self, logging):
        """Sets the logging of this StreamRuntimeConfig.

        :param logging: The logging of this StreamRuntimeConfig.
        :type logging: :class:`huaweicloudsdkdli.v1.StreamLoggingConfig`
        """
        self._logging = logging

    @property
    def properties(self):
        """Gets the properties of this StreamRuntimeConfig.

        :return: The properties of this StreamRuntimeConfig.
        :rtype: :class:`huaweicloudsdkdli.v1.Properties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this StreamRuntimeConfig.

        :param properties: The properties of this StreamRuntimeConfig.
        :type properties: :class:`huaweicloudsdkdli.v1.Properties`
        """
        self._properties = properties

    @property
    def flink_runtime_config(self):
        """Gets the flink_runtime_config of this StreamRuntimeConfig.

        :return: The flink_runtime_config of this StreamRuntimeConfig.
        :rtype: :class:`huaweicloudsdkdli.v1.FlinkRuntimeConfig`
        """
        return self._flink_runtime_config

    @flink_runtime_config.setter
    def flink_runtime_config(self, flink_runtime_config):
        """Sets the flink_runtime_config of this StreamRuntimeConfig.

        :param flink_runtime_config: The flink_runtime_config of this StreamRuntimeConfig.
        :type flink_runtime_config: :class:`huaweicloudsdkdli.v1.FlinkRuntimeConfig`
        """
        self._flink_runtime_config = flink_runtime_config

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
        if not isinstance(other, StreamRuntimeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
