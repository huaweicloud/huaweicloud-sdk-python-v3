# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCesInstanceRspBodyInstances:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'medialive_mpc': 'ListCesInstanceRspBodyMedialiveMpc',
        'pipeline': 'ListCesInstanceRspBodyPipeline',
        'audio': 'ListCesInstanceRspBodyAudio'
    }

    attribute_map = {
        'medialive_mpc': 'medialive_mpc',
        'pipeline': 'pipeline',
        'audio': 'audio'
    }

    def __init__(self, medialive_mpc=None, pipeline=None, audio=None):
        r"""ListCesInstanceRspBodyInstances

        The model defined in huaweicloud sdk

        :param medialive_mpc: 
        :type medialive_mpc: :class:`huaweicloudsdklive.v1.ListCesInstanceRspBodyMedialiveMpc`
        :param pipeline: 
        :type pipeline: :class:`huaweicloudsdklive.v1.ListCesInstanceRspBodyPipeline`
        :param audio: 
        :type audio: :class:`huaweicloudsdklive.v1.ListCesInstanceRspBodyAudio`
        """
        
        

        self._medialive_mpc = None
        self._pipeline = None
        self._audio = None
        self.discriminator = None

        self.medialive_mpc = medialive_mpc
        if pipeline is not None:
            self.pipeline = pipeline
        if audio is not None:
            self.audio = audio

    @property
    def medialive_mpc(self):
        r"""Gets the medialive_mpc of this ListCesInstanceRspBodyInstances.

        :return: The medialive_mpc of this ListCesInstanceRspBodyInstances.
        :rtype: :class:`huaweicloudsdklive.v1.ListCesInstanceRspBodyMedialiveMpc`
        """
        return self._medialive_mpc

    @medialive_mpc.setter
    def medialive_mpc(self, medialive_mpc):
        r"""Sets the medialive_mpc of this ListCesInstanceRspBodyInstances.

        :param medialive_mpc: The medialive_mpc of this ListCesInstanceRspBodyInstances.
        :type medialive_mpc: :class:`huaweicloudsdklive.v1.ListCesInstanceRspBodyMedialiveMpc`
        """
        self._medialive_mpc = medialive_mpc

    @property
    def pipeline(self):
        r"""Gets the pipeline of this ListCesInstanceRspBodyInstances.

        :return: The pipeline of this ListCesInstanceRspBodyInstances.
        :rtype: :class:`huaweicloudsdklive.v1.ListCesInstanceRspBodyPipeline`
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        r"""Sets the pipeline of this ListCesInstanceRspBodyInstances.

        :param pipeline: The pipeline of this ListCesInstanceRspBodyInstances.
        :type pipeline: :class:`huaweicloudsdklive.v1.ListCesInstanceRspBodyPipeline`
        """
        self._pipeline = pipeline

    @property
    def audio(self):
        r"""Gets the audio of this ListCesInstanceRspBodyInstances.

        :return: The audio of this ListCesInstanceRspBodyInstances.
        :rtype: :class:`huaweicloudsdklive.v1.ListCesInstanceRspBodyAudio`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        r"""Sets the audio of this ListCesInstanceRspBodyInstances.

        :param audio: The audio of this ListCesInstanceRspBodyInstances.
        :type audio: :class:`huaweicloudsdklive.v1.ListCesInstanceRspBodyAudio`
        """
        self._audio = audio

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
        if not isinstance(other, ListCesInstanceRspBodyInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
