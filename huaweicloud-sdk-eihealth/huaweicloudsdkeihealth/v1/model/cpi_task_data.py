# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CpiTaskData:

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
        'smiles_list': 'list[str]',
        'threshold': 'float',
        'num_results': 'int',
        'custom_props': 'list[CustomProp]'
    }

    attribute_map = {
        'header': 'header',
        'fasta': 'fasta',
        'smiles_list': 'smiles_list',
        'threshold': 'threshold',
        'num_results': 'num_results',
        'custom_props': 'custom_props'
    }

    def __init__(self, header=None, fasta=None, smiles_list=None, threshold=None, num_results=None, custom_props=None):
        """CpiTaskData

        The model defined in huaweicloud sdk

        :param header: 蛋白质FASTA标题
        :type header: str
        :param fasta: 蛋白质FASTA序列
        :type fasta: str
        :param smiles_list: 分子SMILES表达式列表
        :type smiles_list: list[str]
        :param threshold: 打分阈值，分值必须大于该阈值才会返回
        :type threshold: float
        :param num_results: 期望最大返回条目数（排序后取Top）
        :type num_results: int
        :param custom_props: 用户已开启的自定义属性集合
        :type custom_props: list[:class:`huaweicloudsdkeihealth.v1.CustomProp`]
        """
        
        

        self._header = None
        self._fasta = None
        self._smiles_list = None
        self._threshold = None
        self._num_results = None
        self._custom_props = None
        self.discriminator = None

        if header is not None:
            self.header = header
        self.fasta = fasta
        self.smiles_list = smiles_list
        if threshold is not None:
            self.threshold = threshold
        if num_results is not None:
            self.num_results = num_results
        if custom_props is not None:
            self.custom_props = custom_props

    @property
    def header(self):
        """Gets the header of this CpiTaskData.

        蛋白质FASTA标题

        :return: The header of this CpiTaskData.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this CpiTaskData.

        蛋白质FASTA标题

        :param header: The header of this CpiTaskData.
        :type header: str
        """
        self._header = header

    @property
    def fasta(self):
        """Gets the fasta of this CpiTaskData.

        蛋白质FASTA序列

        :return: The fasta of this CpiTaskData.
        :rtype: str
        """
        return self._fasta

    @fasta.setter
    def fasta(self, fasta):
        """Sets the fasta of this CpiTaskData.

        蛋白质FASTA序列

        :param fasta: The fasta of this CpiTaskData.
        :type fasta: str
        """
        self._fasta = fasta

    @property
    def smiles_list(self):
        """Gets the smiles_list of this CpiTaskData.

        分子SMILES表达式列表

        :return: The smiles_list of this CpiTaskData.
        :rtype: list[str]
        """
        return self._smiles_list

    @smiles_list.setter
    def smiles_list(self, smiles_list):
        """Sets the smiles_list of this CpiTaskData.

        分子SMILES表达式列表

        :param smiles_list: The smiles_list of this CpiTaskData.
        :type smiles_list: list[str]
        """
        self._smiles_list = smiles_list

    @property
    def threshold(self):
        """Gets the threshold of this CpiTaskData.

        打分阈值，分值必须大于该阈值才会返回

        :return: The threshold of this CpiTaskData.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this CpiTaskData.

        打分阈值，分值必须大于该阈值才会返回

        :param threshold: The threshold of this CpiTaskData.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def num_results(self):
        """Gets the num_results of this CpiTaskData.

        期望最大返回条目数（排序后取Top）

        :return: The num_results of this CpiTaskData.
        :rtype: int
        """
        return self._num_results

    @num_results.setter
    def num_results(self, num_results):
        """Sets the num_results of this CpiTaskData.

        期望最大返回条目数（排序后取Top）

        :param num_results: The num_results of this CpiTaskData.
        :type num_results: int
        """
        self._num_results = num_results

    @property
    def custom_props(self):
        """Gets the custom_props of this CpiTaskData.

        用户已开启的自定义属性集合

        :return: The custom_props of this CpiTaskData.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.CustomProp`]
        """
        return self._custom_props

    @custom_props.setter
    def custom_props(self, custom_props):
        """Sets the custom_props of this CpiTaskData.

        用户已开启的自定义属性集合

        :param custom_props: The custom_props of this CpiTaskData.
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
        if not isinstance(other, CpiTaskData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
