# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLtsCloudLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_name': 'str',
        'config_name': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'source_name': 'source_name',
        'config_name': 'config_name',
        'success': 'success'
    }

    def __init__(self, source_name=None, config_name=None, success=None):
        r"""DeleteLtsCloudLogResponse

        The model defined in huaweicloud sdk

        :param source_name: 日志名称
        :type source_name: str
        :param config_name: 配置名称
        :type config_name: str
        :param success: 是否成功
        :type success: bool
        """
        
        super().__init__()

        self._source_name = None
        self._config_name = None
        self._success = None
        self.discriminator = None

        if source_name is not None:
            self.source_name = source_name
        if config_name is not None:
            self.config_name = config_name
        if success is not None:
            self.success = success

    @property
    def source_name(self):
        r"""Gets the source_name of this DeleteLtsCloudLogResponse.

        日志名称

        :return: The source_name of this DeleteLtsCloudLogResponse.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this DeleteLtsCloudLogResponse.

        日志名称

        :param source_name: The source_name of this DeleteLtsCloudLogResponse.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def config_name(self):
        r"""Gets the config_name of this DeleteLtsCloudLogResponse.

        配置名称

        :return: The config_name of this DeleteLtsCloudLogResponse.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        r"""Sets the config_name of this DeleteLtsCloudLogResponse.

        配置名称

        :param config_name: The config_name of this DeleteLtsCloudLogResponse.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def success(self):
        r"""Gets the success of this DeleteLtsCloudLogResponse.

        是否成功

        :return: The success of this DeleteLtsCloudLogResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this DeleteLtsCloudLogResponse.

        是否成功

        :param success: The success of this DeleteLtsCloudLogResponse.
        :type success: bool
        """
        self._success = success

    def to_dict(self):
        import warnings
        warnings.warn("DeleteLtsCloudLogResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, DeleteLtsCloudLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
