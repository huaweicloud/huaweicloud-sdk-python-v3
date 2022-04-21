# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunModerationAudioResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'detail': 'RunModerationAudioResponseBodyResultDetail',
        'suggestion': 'str'
    }

    attribute_map = {
        'detail': 'detail',
        'suggestion': 'suggestion'
    }

    def __init__(self, detail=None, suggestion=None):
        """RunModerationAudioResponseBodyResult

        The model defined in huaweicloud sdk

        :param detail: 
        :type detail: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioResponseBodyResultDetail`
        :param suggestion: 检测结果是否通过。 block：包含敏感信息，不通过。 pass：不包含敏感信息，通过。 review：需要人工复查 
        :type suggestion: str
        """
        
        

        self._detail = None
        self._suggestion = None
        self.discriminator = None

        if detail is not None:
            self.detail = detail
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def detail(self):
        """Gets the detail of this RunModerationAudioResponseBodyResult.


        :return: The detail of this RunModerationAudioResponseBodyResult.
        :rtype: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioResponseBodyResultDetail`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this RunModerationAudioResponseBodyResult.


        :param detail: The detail of this RunModerationAudioResponseBodyResult.
        :type detail: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioResponseBodyResultDetail`
        """
        self._detail = detail

    @property
    def suggestion(self):
        """Gets the suggestion of this RunModerationAudioResponseBodyResult.

        检测结果是否通过。 block：包含敏感信息，不通过。 pass：不包含敏感信息，通过。 review：需要人工复查 

        :return: The suggestion of this RunModerationAudioResponseBodyResult.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this RunModerationAudioResponseBodyResult.

        检测结果是否通过。 block：包含敏感信息，不通过。 pass：不包含敏感信息，通过。 review：需要人工复查 

        :param suggestion: The suggestion of this RunModerationAudioResponseBodyResult.
        :type suggestion: str
        """
        self._suggestion = suggestion

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
        if not isinstance(other, RunModerationAudioResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
