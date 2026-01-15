# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class I18n:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zh_cn': 'str',
        'en_us': 'str',
        'es_us': 'str',
        'pt_br': 'str'
    }

    attribute_map = {
        'zh_cn': 'zh_cn',
        'en_us': 'en_us',
        'es_us': 'es_us',
        'pt_br': 'pt_br'
    }

    def __init__(self, zh_cn=None, en_us=None, es_us=None, pt_br=None):
        r"""I18n

        The model defined in huaweicloud sdk

        :param zh_cn: 可用分区中文名称。
        :type zh_cn: str
        :param en_us: 可用分区英语名称。
        :type en_us: str
        :param es_us: 可用分区西班牙语名称。
        :type es_us: str
        :param pt_br: 可用分区葡萄牙语名称。
        :type pt_br: str
        """
        
        

        self._zh_cn = None
        self._en_us = None
        self._es_us = None
        self._pt_br = None
        self.discriminator = None

        if zh_cn is not None:
            self.zh_cn = zh_cn
        if en_us is not None:
            self.en_us = en_us
        if es_us is not None:
            self.es_us = es_us
        if pt_br is not None:
            self.pt_br = pt_br

    @property
    def zh_cn(self):
        r"""Gets the zh_cn of this I18n.

        可用分区中文名称。

        :return: The zh_cn of this I18n.
        :rtype: str
        """
        return self._zh_cn

    @zh_cn.setter
    def zh_cn(self, zh_cn):
        r"""Sets the zh_cn of this I18n.

        可用分区中文名称。

        :param zh_cn: The zh_cn of this I18n.
        :type zh_cn: str
        """
        self._zh_cn = zh_cn

    @property
    def en_us(self):
        r"""Gets the en_us of this I18n.

        可用分区英语名称。

        :return: The en_us of this I18n.
        :rtype: str
        """
        return self._en_us

    @en_us.setter
    def en_us(self, en_us):
        r"""Sets the en_us of this I18n.

        可用分区英语名称。

        :param en_us: The en_us of this I18n.
        :type en_us: str
        """
        self._en_us = en_us

    @property
    def es_us(self):
        r"""Gets the es_us of this I18n.

        可用分区西班牙语名称。

        :return: The es_us of this I18n.
        :rtype: str
        """
        return self._es_us

    @es_us.setter
    def es_us(self, es_us):
        r"""Sets the es_us of this I18n.

        可用分区西班牙语名称。

        :param es_us: The es_us of this I18n.
        :type es_us: str
        """
        self._es_us = es_us

    @property
    def pt_br(self):
        r"""Gets the pt_br of this I18n.

        可用分区葡萄牙语名称。

        :return: The pt_br of this I18n.
        :rtype: str
        """
        return self._pt_br

    @pt_br.setter
    def pt_br(self, pt_br):
        r"""Sets the pt_br of this I18n.

        可用分区葡萄牙语名称。

        :param pt_br: The pt_br of this I18n.
        :type pt_br: str
        """
        self._pt_br = pt_br

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
        if not isinstance(other, I18n):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
