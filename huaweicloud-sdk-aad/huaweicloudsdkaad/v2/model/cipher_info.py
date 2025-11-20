# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CipherInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'algo': 'str',
        'desc_cn': 'str',
        'desc_en': 'str'
    }

    attribute_map = {
        'name': 'name',
        'algo': 'algo',
        'desc_cn': 'desc_cn',
        'desc_en': 'desc_en'
    }

    def __init__(self, name=None, algo=None, desc_cn=None, desc_en=None):
        r"""CipherInfo

        The model defined in huaweicloud sdk

        :param name: 套件名称
        :type name: str
        :param algo: 对应的加密算法
        :type algo: str
        :param desc_cn: 中文描述
        :type desc_cn: str
        :param desc_en: 英文描述
        :type desc_en: str
        """
        
        

        self._name = None
        self._algo = None
        self._desc_cn = None
        self._desc_en = None
        self.discriminator = None

        self.name = name
        self.algo = algo
        self.desc_cn = desc_cn
        self.desc_en = desc_en

    @property
    def name(self):
        r"""Gets the name of this CipherInfo.

        套件名称

        :return: The name of this CipherInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CipherInfo.

        套件名称

        :param name: The name of this CipherInfo.
        :type name: str
        """
        self._name = name

    @property
    def algo(self):
        r"""Gets the algo of this CipherInfo.

        对应的加密算法

        :return: The algo of this CipherInfo.
        :rtype: str
        """
        return self._algo

    @algo.setter
    def algo(self, algo):
        r"""Sets the algo of this CipherInfo.

        对应的加密算法

        :param algo: The algo of this CipherInfo.
        :type algo: str
        """
        self._algo = algo

    @property
    def desc_cn(self):
        r"""Gets the desc_cn of this CipherInfo.

        中文描述

        :return: The desc_cn of this CipherInfo.
        :rtype: str
        """
        return self._desc_cn

    @desc_cn.setter
    def desc_cn(self, desc_cn):
        r"""Sets the desc_cn of this CipherInfo.

        中文描述

        :param desc_cn: The desc_cn of this CipherInfo.
        :type desc_cn: str
        """
        self._desc_cn = desc_cn

    @property
    def desc_en(self):
        r"""Gets the desc_en of this CipherInfo.

        英文描述

        :return: The desc_en of this CipherInfo.
        :rtype: str
        """
        return self._desc_en

    @desc_en.setter
    def desc_en(self, desc_en):
        r"""Sets the desc_en of this CipherInfo.

        英文描述

        :param desc_en: The desc_en of this CipherInfo.
        :type desc_en: str
        """
        self._desc_en = desc_en

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CipherInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
