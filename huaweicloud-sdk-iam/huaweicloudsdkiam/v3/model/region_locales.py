# coding: utf-8

import pprint
import re

import six





class RegionLocales:


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
        'pt_br': 'str',
        'es_us': 'str',
        'es_es': 'str'
    }

    attribute_map = {
        'zh_cn': 'zh-cn',
        'en_us': 'en-us',
        'pt_br': 'pt-br',
        'es_us': 'es-us',
        'es_es': 'es-es'
    }

    def __init__(self, zh_cn=None, en_us=None, pt_br=None, es_us=None, es_es=None):
        """RegionLocales - a model defined in huaweicloud sdk"""
        
        

        self._zh_cn = None
        self._en_us = None
        self._pt_br = None
        self._es_us = None
        self._es_es = None
        self.discriminator = None

        self.zh_cn = zh_cn
        self.en_us = en_us
        if pt_br is not None:
            self.pt_br = pt_br
        if es_us is not None:
            self.es_us = es_us
        if es_es is not None:
            self.es_es = es_es

    @property
    def zh_cn(self):
        """Gets the zh_cn of this RegionLocales.

        区域的中文名称。

        :return: The zh_cn of this RegionLocales.
        :rtype: str
        """
        return self._zh_cn

    @zh_cn.setter
    def zh_cn(self, zh_cn):
        """Sets the zh_cn of this RegionLocales.

        区域的中文名称。

        :param zh_cn: The zh_cn of this RegionLocales.
        :type: str
        """
        self._zh_cn = zh_cn

    @property
    def en_us(self):
        """Gets the en_us of this RegionLocales.

        区域的英文名称。

        :return: The en_us of this RegionLocales.
        :rtype: str
        """
        return self._en_us

    @en_us.setter
    def en_us(self, en_us):
        """Sets the en_us of this RegionLocales.

        区域的英文名称。

        :param en_us: The en_us of this RegionLocales.
        :type: str
        """
        self._en_us = en_us

    @property
    def pt_br(self):
        """Gets the pt_br of this RegionLocales.

        区域的葡萄牙语名称。

        :return: The pt_br of this RegionLocales.
        :rtype: str
        """
        return self._pt_br

    @pt_br.setter
    def pt_br(self, pt_br):
        """Sets the pt_br of this RegionLocales.

        区域的葡萄牙语名称。

        :param pt_br: The pt_br of this RegionLocales.
        :type: str
        """
        self._pt_br = pt_br

    @property
    def es_us(self):
        """Gets the es_us of this RegionLocales.

        区域的美国西班牙语名称。

        :return: The es_us of this RegionLocales.
        :rtype: str
        """
        return self._es_us

    @es_us.setter
    def es_us(self, es_us):
        """Sets the es_us of this RegionLocales.

        区域的美国西班牙语名称。

        :param es_us: The es_us of this RegionLocales.
        :type: str
        """
        self._es_us = es_us

    @property
    def es_es(self):
        """Gets the es_es of this RegionLocales.

        区域的西班牙语名称。

        :return: The es_es of this RegionLocales.
        :rtype: str
        """
        return self._es_es

    @es_es.setter
    def es_es(self, es_es):
        """Sets the es_es of this RegionLocales.

        区域的西班牙语名称。

        :param es_es: The es_es of this RegionLocales.
        :type: str
        """
        self._es_es = es_es

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RegionLocales):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
