# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMergeChannelsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'multi_audio': 'MpcMultiAudio'
    }

    attribute_map = {
        'multi_audio': 'multi_audio'
    }

    def __init__(self, multi_audio=None):
        """CreateMergeChannelsReq

        The model defined in huaweicloud sdk

        :param multi_audio: 
        :type multi_audio: :class:`huaweicloudsdkmpc.v1.MpcMultiAudio`
        """
        
        

        self._multi_audio = None
        self.discriminator = None

        if multi_audio is not None:
            self.multi_audio = multi_audio

    @property
    def multi_audio(self):
        """Gets the multi_audio of this CreateMergeChannelsReq.


        :return: The multi_audio of this CreateMergeChannelsReq.
        :rtype: :class:`huaweicloudsdkmpc.v1.MpcMultiAudio`
        """
        return self._multi_audio

    @multi_audio.setter
    def multi_audio(self, multi_audio):
        """Sets the multi_audio of this CreateMergeChannelsReq.


        :param multi_audio: The multi_audio of this CreateMergeChannelsReq.
        :type multi_audio: :class:`huaweicloudsdkmpc.v1.MpcMultiAudio`
        """
        self._multi_audio = multi_audio

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
        if not isinstance(other, CreateMergeChannelsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
