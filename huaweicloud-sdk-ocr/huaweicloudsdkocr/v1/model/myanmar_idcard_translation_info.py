# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MyanmarIdcardTranslationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name_translation': 'str',
        'father_name_translation': 'str',
        'nrc_id_translation': 'str',
        'birth_translation': 'str'
    }

    attribute_map = {
        'name_translation': 'name_translation',
        'father_name_translation': 'father_name_translation',
        'nrc_id_translation': 'nrc_id_translation',
        'birth_translation': 'birth_translation'
    }

    def __init__(self, name_translation=None, father_name_translation=None, nrc_id_translation=None, birth_translation=None):
        r"""MyanmarIdcardTranslationInfo

        The model defined in huaweicloud sdk

        :param name_translation: 名字转译。仅当输入参数return_translation为true时，返回该字段。 
        :type name_translation: str
        :param father_name_translation: 父亲名字的转译。仅当输入参数return_translation为true时，返回该字段。 
        :type father_name_translation: str
        :param nrc_id_translation: 身份证号码转译。仅当输入参数return_translation为true时，返回该字段。 
        :type nrc_id_translation: str
        :param birth_translation: 出生日期转译。仅当输入参数return_translation为true时，返回该字段。 
        :type birth_translation: str
        """
        
        

        self._name_translation = None
        self._father_name_translation = None
        self._nrc_id_translation = None
        self._birth_translation = None
        self.discriminator = None

        if name_translation is not None:
            self.name_translation = name_translation
        if father_name_translation is not None:
            self.father_name_translation = father_name_translation
        if nrc_id_translation is not None:
            self.nrc_id_translation = nrc_id_translation
        if birth_translation is not None:
            self.birth_translation = birth_translation

    @property
    def name_translation(self):
        r"""Gets the name_translation of this MyanmarIdcardTranslationInfo.

        名字转译。仅当输入参数return_translation为true时，返回该字段。 

        :return: The name_translation of this MyanmarIdcardTranslationInfo.
        :rtype: str
        """
        return self._name_translation

    @name_translation.setter
    def name_translation(self, name_translation):
        r"""Sets the name_translation of this MyanmarIdcardTranslationInfo.

        名字转译。仅当输入参数return_translation为true时，返回该字段。 

        :param name_translation: The name_translation of this MyanmarIdcardTranslationInfo.
        :type name_translation: str
        """
        self._name_translation = name_translation

    @property
    def father_name_translation(self):
        r"""Gets the father_name_translation of this MyanmarIdcardTranslationInfo.

        父亲名字的转译。仅当输入参数return_translation为true时，返回该字段。 

        :return: The father_name_translation of this MyanmarIdcardTranslationInfo.
        :rtype: str
        """
        return self._father_name_translation

    @father_name_translation.setter
    def father_name_translation(self, father_name_translation):
        r"""Sets the father_name_translation of this MyanmarIdcardTranslationInfo.

        父亲名字的转译。仅当输入参数return_translation为true时，返回该字段。 

        :param father_name_translation: The father_name_translation of this MyanmarIdcardTranslationInfo.
        :type father_name_translation: str
        """
        self._father_name_translation = father_name_translation

    @property
    def nrc_id_translation(self):
        r"""Gets the nrc_id_translation of this MyanmarIdcardTranslationInfo.

        身份证号码转译。仅当输入参数return_translation为true时，返回该字段。 

        :return: The nrc_id_translation of this MyanmarIdcardTranslationInfo.
        :rtype: str
        """
        return self._nrc_id_translation

    @nrc_id_translation.setter
    def nrc_id_translation(self, nrc_id_translation):
        r"""Sets the nrc_id_translation of this MyanmarIdcardTranslationInfo.

        身份证号码转译。仅当输入参数return_translation为true时，返回该字段。 

        :param nrc_id_translation: The nrc_id_translation of this MyanmarIdcardTranslationInfo.
        :type nrc_id_translation: str
        """
        self._nrc_id_translation = nrc_id_translation

    @property
    def birth_translation(self):
        r"""Gets the birth_translation of this MyanmarIdcardTranslationInfo.

        出生日期转译。仅当输入参数return_translation为true时，返回该字段。 

        :return: The birth_translation of this MyanmarIdcardTranslationInfo.
        :rtype: str
        """
        return self._birth_translation

    @birth_translation.setter
    def birth_translation(self, birth_translation):
        r"""Sets the birth_translation of this MyanmarIdcardTranslationInfo.

        出生日期转译。仅当输入参数return_translation为true时，返回该字段。 

        :param birth_translation: The birth_translation of this MyanmarIdcardTranslationInfo.
        :type birth_translation: str
        """
        self._birth_translation = birth_translation

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
        if not isinstance(other, MyanmarIdcardTranslationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
