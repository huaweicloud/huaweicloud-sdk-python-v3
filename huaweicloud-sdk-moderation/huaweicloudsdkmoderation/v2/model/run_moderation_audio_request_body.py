# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunModerationAudioRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'str',
        'url': 'str',
        'config': 'RunModerationAudioRequestBodyConfig',
        'categories': 'list[str]'
    }

    attribute_map = {
        'data': 'data',
        'url': 'url',
        'config': 'config',
        'categories': 'categories'
    }

    def __init__(self, data=None, url=None, config=None, categories=None):
        """RunModerationAudioRequestBody

        The model defined in huaweicloud sdk

        :param data: 与url二选一  语音文件Base64编码字符串。要求base64编码后大小不超过4M。语音时长不超过1分钟。 
        :type data: str
        :param url: 与data二选一  语音的URL路径，目前支持对服务授权访问华为云上OBS的URL，华为云上OBS提供的临时授权访问的URL和匿名公开授权的URL。 OBS服务的访问权限设置请参见配置OBS访问权限。 出于安全的考虑，当前服务不支持从公网上任意URL读取数据。 
        :type url: str
        :param config: 
        :type config: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioRequestBodyConfig`
        :param categories: 审核场景。 当前支持的场景有默认场景和用户自定义场景： ● 默认场景为：   – politics：涉政   – porn：涉黄   – ad：广告   – abuse：辱骂   – contraband：违禁品 ● 用户自定义场景为：自定义词库。 说明 自定义词库的创建和使用请参见配置自定义词库。 
        :type categories: list[str]
        """
        
        

        self._data = None
        self._url = None
        self._config = None
        self._categories = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if url is not None:
            self.url = url
        self.config = config
        if categories is not None:
            self.categories = categories

    @property
    def data(self):
        """Gets the data of this RunModerationAudioRequestBody.

        与url二选一  语音文件Base64编码字符串。要求base64编码后大小不超过4M。语音时长不超过1分钟。 

        :return: The data of this RunModerationAudioRequestBody.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this RunModerationAudioRequestBody.

        与url二选一  语音文件Base64编码字符串。要求base64编码后大小不超过4M。语音时长不超过1分钟。 

        :param data: The data of this RunModerationAudioRequestBody.
        :type data: str
        """
        self._data = data

    @property
    def url(self):
        """Gets the url of this RunModerationAudioRequestBody.

        与data二选一  语音的URL路径，目前支持对服务授权访问华为云上OBS的URL，华为云上OBS提供的临时授权访问的URL和匿名公开授权的URL。 OBS服务的访问权限设置请参见配置OBS访问权限。 出于安全的考虑，当前服务不支持从公网上任意URL读取数据。 

        :return: The url of this RunModerationAudioRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RunModerationAudioRequestBody.

        与data二选一  语音的URL路径，目前支持对服务授权访问华为云上OBS的URL，华为云上OBS提供的临时授权访问的URL和匿名公开授权的URL。 OBS服务的访问权限设置请参见配置OBS访问权限。 出于安全的考虑，当前服务不支持从公网上任意URL读取数据。 

        :param url: The url of this RunModerationAudioRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def config(self):
        """Gets the config of this RunModerationAudioRequestBody.

        :return: The config of this RunModerationAudioRequestBody.
        :rtype: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioRequestBodyConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this RunModerationAudioRequestBody.

        :param config: The config of this RunModerationAudioRequestBody.
        :type config: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioRequestBodyConfig`
        """
        self._config = config

    @property
    def categories(self):
        """Gets the categories of this RunModerationAudioRequestBody.

        审核场景。 当前支持的场景有默认场景和用户自定义场景： ● 默认场景为：   – politics：涉政   – porn：涉黄   – ad：广告   – abuse：辱骂   – contraband：违禁品 ● 用户自定义场景为：自定义词库。 说明 自定义词库的创建和使用请参见配置自定义词库。 

        :return: The categories of this RunModerationAudioRequestBody.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this RunModerationAudioRequestBody.

        审核场景。 当前支持的场景有默认场景和用户自定义场景： ● 默认场景为：   – politics：涉政   – porn：涉黄   – ad：广告   – abuse：辱骂   – contraband：违禁品 ● 用户自定义场景为：自定义词库。 说明 自定义词库的创建和使用请参见配置自定义词库。 

        :param categories: The categories of this RunModerationAudioRequestBody.
        :type categories: list[str]
        """
        self._categories = categories

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
        if not isinstance(other, RunModerationAudioRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
