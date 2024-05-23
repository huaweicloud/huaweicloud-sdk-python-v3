# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSisHotWords:

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
        'sis_project_id': 'str',
        'region': 'int',
        'language': 'LanguageEnum'
    }

    attribute_map = {
        'vocabulary_id': 'vocabulary_id',
        'sis_project_id': 'sis_project_id',
        'region': 'region',
        'language': 'language'
    }

    def __init__(self, vocabulary_id=None, sis_project_id=None, region=None, language=None):
        """UpdateSisHotWords

        The model defined in huaweicloud sdk

        :param vocabulary_id: 热词ID。
        :type vocabulary_id: str
        :param sis_project_id: SIS服务所在区域projectId
        :type sis_project_id: str
        :param region: 对接SIS服务的区域。 &gt; 0：北京四；3：上海一；
        :type region: int
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        
        

        self._vocabulary_id = None
        self._sis_project_id = None
        self._region = None
        self._language = None
        self.discriminator = None

        if vocabulary_id is not None:
            self.vocabulary_id = vocabulary_id
        if sis_project_id is not None:
            self.sis_project_id = sis_project_id
        if region is not None:
            self.region = region
        if language is not None:
            self.language = language

    @property
    def vocabulary_id(self):
        """Gets the vocabulary_id of this UpdateSisHotWords.

        热词ID。

        :return: The vocabulary_id of this UpdateSisHotWords.
        :rtype: str
        """
        return self._vocabulary_id

    @vocabulary_id.setter
    def vocabulary_id(self, vocabulary_id):
        """Sets the vocabulary_id of this UpdateSisHotWords.

        热词ID。

        :param vocabulary_id: The vocabulary_id of this UpdateSisHotWords.
        :type vocabulary_id: str
        """
        self._vocabulary_id = vocabulary_id

    @property
    def sis_project_id(self):
        """Gets the sis_project_id of this UpdateSisHotWords.

        SIS服务所在区域projectId

        :return: The sis_project_id of this UpdateSisHotWords.
        :rtype: str
        """
        return self._sis_project_id

    @sis_project_id.setter
    def sis_project_id(self, sis_project_id):
        """Sets the sis_project_id of this UpdateSisHotWords.

        SIS服务所在区域projectId

        :param sis_project_id: The sis_project_id of this UpdateSisHotWords.
        :type sis_project_id: str
        """
        self._sis_project_id = sis_project_id

    @property
    def region(self):
        """Gets the region of this UpdateSisHotWords.

        对接SIS服务的区域。 > 0：北京四；3：上海一；

        :return: The region of this UpdateSisHotWords.
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this UpdateSisHotWords.

        对接SIS服务的区域。 > 0：北京四；3：上海一；

        :param region: The region of this UpdateSisHotWords.
        :type region: int
        """
        self._region = region

    @property
    def language(self):
        """Gets the language of this UpdateSisHotWords.

        :return: The language of this UpdateSisHotWords.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UpdateSisHotWords.

        :param language: The language of this UpdateSisHotWords.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

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
        if not isinstance(other, UpdateSisHotWords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
