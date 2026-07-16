# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogExportPath:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_url': 'str',
        'host_path': 'str'
    }

    attribute_map = {
        'obs_url': 'obs_url',
        'host_path': 'host_path'
    }

    def __init__(self, obs_url=None, host_path=None):
        r"""LogExportPath

        The model defined in huaweicloud sdk

        :param obs_url: 训练作业日志保存的OBS地址，如：“obs://example/path”。
        :type obs_url: str
        :param host_path: 训练作业日志保存的宿主机的路径，如：“/example/path”。
        :type host_path: str
        """
        
        

        self._obs_url = None
        self._host_path = None
        self.discriminator = None

        if obs_url is not None:
            self.obs_url = obs_url
        if host_path is not None:
            self.host_path = host_path

    @property
    def obs_url(self):
        r"""Gets the obs_url of this LogExportPath.

        训练作业日志保存的OBS地址，如：“obs://example/path”。

        :return: The obs_url of this LogExportPath.
        :rtype: str
        """
        return self._obs_url

    @obs_url.setter
    def obs_url(self, obs_url):
        r"""Sets the obs_url of this LogExportPath.

        训练作业日志保存的OBS地址，如：“obs://example/path”。

        :param obs_url: The obs_url of this LogExportPath.
        :type obs_url: str
        """
        self._obs_url = obs_url

    @property
    def host_path(self):
        r"""Gets the host_path of this LogExportPath.

        训练作业日志保存的宿主机的路径，如：“/example/path”。

        :return: The host_path of this LogExportPath.
        :rtype: str
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        r"""Sets the host_path of this LogExportPath.

        训练作业日志保存的宿主机的路径，如：“/example/path”。

        :param host_path: The host_path of this LogExportPath.
        :type host_path: str
        """
        self._host_path = host_path

    def to_dict(self):
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
        if not isinstance(other, LogExportPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
