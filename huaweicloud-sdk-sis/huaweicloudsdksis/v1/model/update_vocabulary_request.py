# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVocabularyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vocabulary_id': 'str',
        'body': 'PutUpdateVocabReq'
    }

    attribute_map = {
        'vocabulary_id': 'vocabulary_id',
        'body': 'body'
    }

    def __init__(self, vocabulary_id=None, body=None):
        """UpdateVocabularyRequest

        The model defined in huaweicloud sdk

        :param vocabulary_id: 被更新的热词表id。
        :type vocabulary_id: str
        :param body: Body of the UpdateVocabularyRequest
        :type body: :class:`huaweicloudsdksis.v1.PutUpdateVocabReq`
        """
        
        

        self._vocabulary_id = None
        self._body = None
        self.discriminator = None

        self.vocabulary_id = vocabulary_id
        if body is not None:
            self.body = body

    @property
    def vocabulary_id(self):
        """Gets the vocabulary_id of this UpdateVocabularyRequest.

        被更新的热词表id。

        :return: The vocabulary_id of this UpdateVocabularyRequest.
        :rtype: str
        """
        return self._vocabulary_id

    @vocabulary_id.setter
    def vocabulary_id(self, vocabulary_id):
        """Sets the vocabulary_id of this UpdateVocabularyRequest.

        被更新的热词表id。

        :param vocabulary_id: The vocabulary_id of this UpdateVocabularyRequest.
        :type vocabulary_id: str
        """
        self._vocabulary_id = vocabulary_id

    @property
    def body(self):
        """Gets the body of this UpdateVocabularyRequest.

        :return: The body of this UpdateVocabularyRequest.
        :rtype: :class:`huaweicloudsdksis.v1.PutUpdateVocabReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateVocabularyRequest.

        :param body: The body of this UpdateVocabularyRequest.
        :type body: :class:`huaweicloudsdksis.v1.PutUpdateVocabReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateVocabularyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
