# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProbeDrugFile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'DrugFileSource',
        'url': 'str',
        'format': 'str',
        'data': 'str'
    }

    attribute_map = {
        'source': 'source',
        'url': 'url',
        'format': 'format',
        'data': 'data'
    }

    def __init__(self, source=None, url=None, format=None, data=None):
        r"""ProbeDrugFile

        The model defined in huaweicloud sdk

        :param source: 
        :type source: :class:`huaweicloudsdkeihealth.v1.DrugFileSource`
        :param url: 文件URL，当数据源为外部网络数据时为https地址；用户私有数据中心为项目路径、公共数据场景为obs地址
        :type url: str
        :param format: 文件格式，支持PDB、SDF、MOL2，仅数据源为RAW时提供
        :type format: str
        :param data: 文件原始数据，仅数据源为RAW时提供
        :type data: str
        """
        
        

        self._source = None
        self._url = None
        self._format = None
        self._data = None
        self.discriminator = None

        self.source = source
        if url is not None:
            self.url = url
        if format is not None:
            self.format = format
        if data is not None:
            self.data = data

    @property
    def source(self):
        r"""Gets the source of this ProbeDrugFile.

        :return: The source of this ProbeDrugFile.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFileSource`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ProbeDrugFile.

        :param source: The source of this ProbeDrugFile.
        :type source: :class:`huaweicloudsdkeihealth.v1.DrugFileSource`
        """
        self._source = source

    @property
    def url(self):
        r"""Gets the url of this ProbeDrugFile.

        文件URL，当数据源为外部网络数据时为https地址；用户私有数据中心为项目路径、公共数据场景为obs地址

        :return: The url of this ProbeDrugFile.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ProbeDrugFile.

        文件URL，当数据源为外部网络数据时为https地址；用户私有数据中心为项目路径、公共数据场景为obs地址

        :param url: The url of this ProbeDrugFile.
        :type url: str
        """
        self._url = url

    @property
    def format(self):
        r"""Gets the format of this ProbeDrugFile.

        文件格式，支持PDB、SDF、MOL2，仅数据源为RAW时提供

        :return: The format of this ProbeDrugFile.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ProbeDrugFile.

        文件格式，支持PDB、SDF、MOL2，仅数据源为RAW时提供

        :param format: The format of this ProbeDrugFile.
        :type format: str
        """
        self._format = format

    @property
    def data(self):
        r"""Gets the data of this ProbeDrugFile.

        文件原始数据，仅数据源为RAW时提供

        :return: The data of this ProbeDrugFile.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ProbeDrugFile.

        文件原始数据，仅数据源为RAW时提供

        :param data: The data of this ProbeDrugFile.
        :type data: str
        """
        self._data = data

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
        if not isinstance(other, ProbeDrugFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
