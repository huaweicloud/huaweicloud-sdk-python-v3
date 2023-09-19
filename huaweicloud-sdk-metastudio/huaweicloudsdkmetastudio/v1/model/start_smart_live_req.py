# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartSmartLiveReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_config': 'VideoConfig',
        'play_policy': 'PlayPolicy',
        'output_urls': 'list[str]'
    }

    attribute_map = {
        'video_config': 'video_config',
        'play_policy': 'play_policy',
        'output_urls': 'output_urls'
    }

    def __init__(self, video_config=None, play_policy=None, output_urls=None):
        """StartSmartLiveReq

        The model defined in huaweicloud sdk

        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param play_policy: 
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        :param output_urls: 视频推流第三方直播平台地址。
        :type output_urls: list[str]
        """
        
        

        self._video_config = None
        self._play_policy = None
        self._output_urls = None
        self.discriminator = None

        if video_config is not None:
            self.video_config = video_config
        if play_policy is not None:
            self.play_policy = play_policy
        if output_urls is not None:
            self.output_urls = output_urls

    @property
    def video_config(self):
        """Gets the video_config of this StartSmartLiveReq.

        :return: The video_config of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this StartSmartLiveReq.

        :param video_config: The video_config of this StartSmartLiveReq.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def play_policy(self):
        """Gets the play_policy of this StartSmartLiveReq.

        :return: The play_policy of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        return self._play_policy

    @play_policy.setter
    def play_policy(self, play_policy):
        """Sets the play_policy of this StartSmartLiveReq.

        :param play_policy: The play_policy of this StartSmartLiveReq.
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        self._play_policy = play_policy

    @property
    def output_urls(self):
        """Gets the output_urls of this StartSmartLiveReq.

        视频推流第三方直播平台地址。

        :return: The output_urls of this StartSmartLiveReq.
        :rtype: list[str]
        """
        return self._output_urls

    @output_urls.setter
    def output_urls(self, output_urls):
        """Sets the output_urls of this StartSmartLiveReq.

        视频推流第三方直播平台地址。

        :param output_urls: The output_urls of this StartSmartLiveReq.
        :type output_urls: list[str]
        """
        self._output_urls = output_urls

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
        if not isinstance(other, StartSmartLiveReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
