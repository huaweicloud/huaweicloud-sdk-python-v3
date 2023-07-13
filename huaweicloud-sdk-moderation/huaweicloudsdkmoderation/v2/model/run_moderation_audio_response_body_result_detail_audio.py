# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunModerationAudioResponseBodyResultDetailAudio:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'porn': 'list[PornModerationResultDetail]'
    }

    attribute_map = {
        'porn': 'porn'
    }

    def __init__(self, porn=None):
        """RunModerationAudioResponseBodyResultDetailAudio

        The model defined in huaweicloud sdk

        :param porn: 涉黄场景审核结果
        :type porn: list[:class:`huaweicloudsdkmoderation.v2.PornModerationResultDetail`]
        """
        
        

        self._porn = None
        self.discriminator = None

        if porn is not None:
            self.porn = porn

    @property
    def porn(self):
        """Gets the porn of this RunModerationAudioResponseBodyResultDetailAudio.

        涉黄场景审核结果

        :return: The porn of this RunModerationAudioResponseBodyResultDetailAudio.
        :rtype: list[:class:`huaweicloudsdkmoderation.v2.PornModerationResultDetail`]
        """
        return self._porn

    @porn.setter
    def porn(self, porn):
        """Sets the porn of this RunModerationAudioResponseBodyResultDetailAudio.

        涉黄场景审核结果

        :param porn: The porn of this RunModerationAudioResponseBodyResultDetailAudio.
        :type porn: list[:class:`huaweicloudsdkmoderation.v2.PornModerationResultDetail`]
        """
        self._porn = porn

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
        if not isinstance(other, RunModerationAudioResponseBodyResultDetailAudio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
