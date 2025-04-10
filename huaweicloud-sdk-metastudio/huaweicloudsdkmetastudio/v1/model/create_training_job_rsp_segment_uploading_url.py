# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTrainingJobRspSegmentUploadingUrl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_uploading_url': 'list[str]',
        'txt_uploading_url': 'list[str]'
    }

    attribute_map = {
        'audio_uploading_url': 'audio_uploading_url',
        'txt_uploading_url': 'txt_uploading_url'
    }

    def __init__(self, audio_uploading_url=None, txt_uploading_url=None):
        r"""CreateTrainingJobRspSegmentUploadingUrl

        The model defined in huaweicloud sdk

        :param audio_uploading_url: 音频上传的地址。  通过该obs地址上传时，需设置content-type为audio/wav
        :type audio_uploading_url: list[str]
        :param txt_uploading_url: 文本上传的地址。  通过该obs地址上传时需设置content-type为text/plain
        :type txt_uploading_url: list[str]
        """
        
        

        self._audio_uploading_url = None
        self._txt_uploading_url = None
        self.discriminator = None

        if audio_uploading_url is not None:
            self.audio_uploading_url = audio_uploading_url
        if txt_uploading_url is not None:
            self.txt_uploading_url = txt_uploading_url

    @property
    def audio_uploading_url(self):
        r"""Gets the audio_uploading_url of this CreateTrainingJobRspSegmentUploadingUrl.

        音频上传的地址。  通过该obs地址上传时，需设置content-type为audio/wav

        :return: The audio_uploading_url of this CreateTrainingJobRspSegmentUploadingUrl.
        :rtype: list[str]
        """
        return self._audio_uploading_url

    @audio_uploading_url.setter
    def audio_uploading_url(self, audio_uploading_url):
        r"""Sets the audio_uploading_url of this CreateTrainingJobRspSegmentUploadingUrl.

        音频上传的地址。  通过该obs地址上传时，需设置content-type为audio/wav

        :param audio_uploading_url: The audio_uploading_url of this CreateTrainingJobRspSegmentUploadingUrl.
        :type audio_uploading_url: list[str]
        """
        self._audio_uploading_url = audio_uploading_url

    @property
    def txt_uploading_url(self):
        r"""Gets the txt_uploading_url of this CreateTrainingJobRspSegmentUploadingUrl.

        文本上传的地址。  通过该obs地址上传时需设置content-type为text/plain

        :return: The txt_uploading_url of this CreateTrainingJobRspSegmentUploadingUrl.
        :rtype: list[str]
        """
        return self._txt_uploading_url

    @txt_uploading_url.setter
    def txt_uploading_url(self, txt_uploading_url):
        r"""Sets the txt_uploading_url of this CreateTrainingJobRspSegmentUploadingUrl.

        文本上传的地址。  通过该obs地址上传时需设置content-type为text/plain

        :param txt_uploading_url: The txt_uploading_url of this CreateTrainingJobRspSegmentUploadingUrl.
        :type txt_uploading_url: list[str]
        """
        self._txt_uploading_url = txt_uploading_url

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
        if not isinstance(other, CreateTrainingJobRspSegmentUploadingUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
