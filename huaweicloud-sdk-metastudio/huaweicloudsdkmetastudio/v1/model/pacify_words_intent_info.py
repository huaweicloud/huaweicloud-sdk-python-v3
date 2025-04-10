# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PacifyWordsIntentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'intent': 'str',
        'desc_cn': 'str',
        'desc_en': 'str'
    }

    attribute_map = {
        'intent': 'intent',
        'desc_cn': 'desc_cn',
        'desc_en': 'desc_en'
    }

    def __init__(self, intent=None, desc_cn=None, desc_en=None):
        r"""PacifyWordsIntentInfo

        The model defined in huaweicloud sdk

        :param intent: 意图名称
        :type intent: str
        :param desc_cn: 意图中文描述
        :type desc_cn: str
        :param desc_en: 意图英文描述
        :type desc_en: str
        """
        
        

        self._intent = None
        self._desc_cn = None
        self._desc_en = None
        self.discriminator = None

        if intent is not None:
            self.intent = intent
        if desc_cn is not None:
            self.desc_cn = desc_cn
        if desc_en is not None:
            self.desc_en = desc_en

    @property
    def intent(self):
        r"""Gets the intent of this PacifyWordsIntentInfo.

        意图名称

        :return: The intent of this PacifyWordsIntentInfo.
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        r"""Sets the intent of this PacifyWordsIntentInfo.

        意图名称

        :param intent: The intent of this PacifyWordsIntentInfo.
        :type intent: str
        """
        self._intent = intent

    @property
    def desc_cn(self):
        r"""Gets the desc_cn of this PacifyWordsIntentInfo.

        意图中文描述

        :return: The desc_cn of this PacifyWordsIntentInfo.
        :rtype: str
        """
        return self._desc_cn

    @desc_cn.setter
    def desc_cn(self, desc_cn):
        r"""Sets the desc_cn of this PacifyWordsIntentInfo.

        意图中文描述

        :param desc_cn: The desc_cn of this PacifyWordsIntentInfo.
        :type desc_cn: str
        """
        self._desc_cn = desc_cn

    @property
    def desc_en(self):
        r"""Gets the desc_en of this PacifyWordsIntentInfo.

        意图英文描述

        :return: The desc_en of this PacifyWordsIntentInfo.
        :rtype: str
        """
        return self._desc_en

    @desc_en.setter
    def desc_en(self, desc_en):
        r"""Sets the desc_en of this PacifyWordsIntentInfo.

        意图英文描述

        :param desc_en: The desc_en of this PacifyWordsIntentInfo.
        :type desc_en: str
        """
        self._desc_en = desc_en

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
        if not isinstance(other, PacifyWordsIntentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
