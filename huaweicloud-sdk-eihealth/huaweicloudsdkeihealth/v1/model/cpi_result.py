# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CpiResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'header': 'str',
        'fasta': 'str',
        'prop_names': 'list[str]',
        'result': 'list[CpiResultItem]',
        'custom_props': 'list[CustomProp]'
    }

    attribute_map = {
        'header': 'header',
        'fasta': 'fasta',
        'prop_names': 'prop_names',
        'result': 'result',
        'custom_props': 'custom_props'
    }

    def __init__(self, header=None, fasta=None, prop_names=None, result=None, custom_props=None):
        """CpiResult

        The model defined in huaweicloud sdk

        :param header: 蛋白质FASTA标题
        :type header: str
        :param fasta: 蛋白质FASTA序列
        :type fasta: str
        :param prop_names: 分子ADMET属性名列表
        :type prop_names: list[str]
        :param result: 返回CPI的模型结果
        :type result: list[:class:`huaweicloudsdkeihealth.v1.CpiResultItem`]
        :param custom_props: 用户已开启的自定义属性集合
        :type custom_props: list[:class:`huaweicloudsdkeihealth.v1.CustomProp`]
        """
        
        

        self._header = None
        self._fasta = None
        self._prop_names = None
        self._result = None
        self._custom_props = None
        self.discriminator = None

        if header is not None:
            self.header = header
        self.fasta = fasta
        if prop_names is not None:
            self.prop_names = prop_names
        self.result = result
        if custom_props is not None:
            self.custom_props = custom_props

    @property
    def header(self):
        """Gets the header of this CpiResult.

        蛋白质FASTA标题

        :return: The header of this CpiResult.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this CpiResult.

        蛋白质FASTA标题

        :param header: The header of this CpiResult.
        :type header: str
        """
        self._header = header

    @property
    def fasta(self):
        """Gets the fasta of this CpiResult.

        蛋白质FASTA序列

        :return: The fasta of this CpiResult.
        :rtype: str
        """
        return self._fasta

    @fasta.setter
    def fasta(self, fasta):
        """Sets the fasta of this CpiResult.

        蛋白质FASTA序列

        :param fasta: The fasta of this CpiResult.
        :type fasta: str
        """
        self._fasta = fasta

    @property
    def prop_names(self):
        """Gets the prop_names of this CpiResult.

        分子ADMET属性名列表

        :return: The prop_names of this CpiResult.
        :rtype: list[str]
        """
        return self._prop_names

    @prop_names.setter
    def prop_names(self, prop_names):
        """Sets the prop_names of this CpiResult.

        分子ADMET属性名列表

        :param prop_names: The prop_names of this CpiResult.
        :type prop_names: list[str]
        """
        self._prop_names = prop_names

    @property
    def result(self):
        """Gets the result of this CpiResult.

        返回CPI的模型结果

        :return: The result of this CpiResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.CpiResultItem`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CpiResult.

        返回CPI的模型结果

        :param result: The result of this CpiResult.
        :type result: list[:class:`huaweicloudsdkeihealth.v1.CpiResultItem`]
        """
        self._result = result

    @property
    def custom_props(self):
        """Gets the custom_props of this CpiResult.

        用户已开启的自定义属性集合

        :return: The custom_props of this CpiResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.CustomProp`]
        """
        return self._custom_props

    @custom_props.setter
    def custom_props(self, custom_props):
        """Sets the custom_props of this CpiResult.

        用户已开启的自定义属性集合

        :param custom_props: The custom_props of this CpiResult.
        :type custom_props: list[:class:`huaweicloudsdkeihealth.v1.CustomProp`]
        """
        self._custom_props = custom_props

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
        if not isinstance(other, CpiResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
