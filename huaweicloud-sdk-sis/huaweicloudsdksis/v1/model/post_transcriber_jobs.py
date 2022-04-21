# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostTranscriberJobs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'config': 'TranscriberConfig',
        'data_url': 'str'
    }

    attribute_map = {
        'config': 'config',
        'data_url': 'data_url'
    }

    def __init__(self, config=None, data_url=None):
        """PostTranscriberJobs

        The model defined in huaweicloud sdk

        :param config: 
        :type config: :class:`huaweicloudsdksis.v1.TranscriberConfig`
        :param data_url: 存放在OBS的音频文件路径。OBS的region要和请求服务的region保持一致，region不一致则OBS不可用，即使obs是公开访问权限。
        :type data_url: str
        """
        
        

        self._config = None
        self._data_url = None
        self.discriminator = None

        self.config = config
        self.data_url = data_url

    @property
    def config(self):
        """Gets the config of this PostTranscriberJobs.


        :return: The config of this PostTranscriberJobs.
        :rtype: :class:`huaweicloudsdksis.v1.TranscriberConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this PostTranscriberJobs.


        :param config: The config of this PostTranscriberJobs.
        :type config: :class:`huaweicloudsdksis.v1.TranscriberConfig`
        """
        self._config = config

    @property
    def data_url(self):
        """Gets the data_url of this PostTranscriberJobs.

        存放在OBS的音频文件路径。OBS的region要和请求服务的region保持一致，region不一致则OBS不可用，即使obs是公开访问权限。

        :return: The data_url of this PostTranscriberJobs.
        :rtype: str
        """
        return self._data_url

    @data_url.setter
    def data_url(self, data_url):
        """Sets the data_url of this PostTranscriberJobs.

        存放在OBS的音频文件路径。OBS的region要和请求服务的region保持一致，region不一致则OBS不可用，即使obs是公开访问权限。

        :param data_url: The data_url of this PostTranscriberJobs.
        :type data_url: str
        """
        self._data_url = data_url

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
        if not isinstance(other, PostTranscriberJobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
