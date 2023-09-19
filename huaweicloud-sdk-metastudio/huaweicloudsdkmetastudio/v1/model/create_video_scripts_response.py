# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVideoScriptsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_id': 'str',
        'audio_files': 'ShootScriptAudioFiles',
        'x_request_id': 'str'
    }

    attribute_map = {
        'script_id': 'script_id',
        'audio_files': 'audio_files',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, script_id=None, audio_files=None, x_request_id=None):
        """CreateVideoScriptsResponse

        The model defined in huaweicloud sdk

        :param script_id: 剧本ID
        :type script_id: str
        :param audio_files: 
        :type audio_files: :class:`huaweicloudsdkmetastudio.v1.ShootScriptAudioFiles`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateVideoScriptsResponse, self).__init__()

        self._script_id = None
        self._audio_files = None
        self._x_request_id = None
        self.discriminator = None

        if script_id is not None:
            self.script_id = script_id
        if audio_files is not None:
            self.audio_files = audio_files
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def script_id(self):
        """Gets the script_id of this CreateVideoScriptsResponse.

        剧本ID

        :return: The script_id of this CreateVideoScriptsResponse.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this CreateVideoScriptsResponse.

        剧本ID

        :param script_id: The script_id of this CreateVideoScriptsResponse.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def audio_files(self):
        """Gets the audio_files of this CreateVideoScriptsResponse.

        :return: The audio_files of this CreateVideoScriptsResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShootScriptAudioFiles`
        """
        return self._audio_files

    @audio_files.setter
    def audio_files(self, audio_files):
        """Sets the audio_files of this CreateVideoScriptsResponse.

        :param audio_files: The audio_files of this CreateVideoScriptsResponse.
        :type audio_files: :class:`huaweicloudsdkmetastudio.v1.ShootScriptAudioFiles`
        """
        self._audio_files = audio_files

    @property
    def x_request_id(self):
        """Gets the x_request_id of this CreateVideoScriptsResponse.

        :return: The x_request_id of this CreateVideoScriptsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this CreateVideoScriptsResponse.

        :param x_request_id: The x_request_id of this CreateVideoScriptsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CreateVideoScriptsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
