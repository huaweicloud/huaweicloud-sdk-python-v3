# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVocabularyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vocabulary_id': 'str'
    }

    attribute_map = {
        'vocabulary_id': 'vocabulary_id'
    }

    def __init__(self, vocabulary_id=None):
        """UpdateVocabularyResponse

        The model defined in huaweicloud sdk

        :param vocabulary_id: 调用成功返回热词表ID，调用失败时无此字段。
        :type vocabulary_id: str
        """
        
        super(UpdateVocabularyResponse, self).__init__()

        self._vocabulary_id = None
        self.discriminator = None

        if vocabulary_id is not None:
            self.vocabulary_id = vocabulary_id

    @property
    def vocabulary_id(self):
        """Gets the vocabulary_id of this UpdateVocabularyResponse.

        调用成功返回热词表ID，调用失败时无此字段。

        :return: The vocabulary_id of this UpdateVocabularyResponse.
        :rtype: str
        """
        return self._vocabulary_id

    @vocabulary_id.setter
    def vocabulary_id(self, vocabulary_id):
        """Sets the vocabulary_id of this UpdateVocabularyResponse.

        调用成功返回热词表ID，调用失败时无此字段。

        :param vocabulary_id: The vocabulary_id of this UpdateVocabularyResponse.
        :type vocabulary_id: str
        """
        self._vocabulary_id = vocabulary_id

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
        if not isinstance(other, UpdateVocabularyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
