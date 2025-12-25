# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReceptorDrugFileReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'url': 'str',
        'format': 'str',
        'data': 'str',
        'add_hydrogen': 'bool'
    }

    attribute_map = {
        'source': 'source',
        'url': 'url',
        'format': 'format',
        'data': 'data',
        'add_hydrogen': 'add_hydrogen'
    }

    def __init__(self, source=None, url=None, format=None, data=None, add_hydrogen=None):
        r"""ReceptorDrugFileReq

        The model defined in huaweicloud sdk

        :param source: 受体的数据源：外部网络数据（如RCSB在线数据库）、用户私有数据中心、承载租户公共数据（含样例/公共库）
        :type source: str
        :param url: 文件URL，当数据源为外部网络数据时为https地址；用户私有数据中心为项目路径、公共数据场景为obs地址
        :type url: str
        :param format: 文件格式，仅支持PDB，仅数据源为RAW时提供
        :type format: str
        :param data: 文件原始数据，仅数据源为RAW时提供
        :type data: str
        :param add_hydrogen: 增加氢原子
        :type add_hydrogen: bool
        """
        
        

        self._source = None
        self._url = None
        self._format = None
        self._data = None
        self._add_hydrogen = None
        self.discriminator = None

        self.source = source
        if url is not None:
            self.url = url
        if format is not None:
            self.format = format
        if data is not None:
            self.data = data
        if add_hydrogen is not None:
            self.add_hydrogen = add_hydrogen

    @property
    def source(self):
        r"""Gets the source of this ReceptorDrugFileReq.

        受体的数据源：外部网络数据（如RCSB在线数据库）、用户私有数据中心、承载租户公共数据（含样例/公共库）

        :return: The source of this ReceptorDrugFileReq.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ReceptorDrugFileReq.

        受体的数据源：外部网络数据（如RCSB在线数据库）、用户私有数据中心、承载租户公共数据（含样例/公共库）

        :param source: The source of this ReceptorDrugFileReq.
        :type source: str
        """
        self._source = source

    @property
    def url(self):
        r"""Gets the url of this ReceptorDrugFileReq.

        文件URL，当数据源为外部网络数据时为https地址；用户私有数据中心为项目路径、公共数据场景为obs地址

        :return: The url of this ReceptorDrugFileReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ReceptorDrugFileReq.

        文件URL，当数据源为外部网络数据时为https地址；用户私有数据中心为项目路径、公共数据场景为obs地址

        :param url: The url of this ReceptorDrugFileReq.
        :type url: str
        """
        self._url = url

    @property
    def format(self):
        r"""Gets the format of this ReceptorDrugFileReq.

        文件格式，仅支持PDB，仅数据源为RAW时提供

        :return: The format of this ReceptorDrugFileReq.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ReceptorDrugFileReq.

        文件格式，仅支持PDB，仅数据源为RAW时提供

        :param format: The format of this ReceptorDrugFileReq.
        :type format: str
        """
        self._format = format

    @property
    def data(self):
        r"""Gets the data of this ReceptorDrugFileReq.

        文件原始数据，仅数据源为RAW时提供

        :return: The data of this ReceptorDrugFileReq.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ReceptorDrugFileReq.

        文件原始数据，仅数据源为RAW时提供

        :param data: The data of this ReceptorDrugFileReq.
        :type data: str
        """
        self._data = data

    @property
    def add_hydrogen(self):
        r"""Gets the add_hydrogen of this ReceptorDrugFileReq.

        增加氢原子

        :return: The add_hydrogen of this ReceptorDrugFileReq.
        :rtype: bool
        """
        return self._add_hydrogen

    @add_hydrogen.setter
    def add_hydrogen(self, add_hydrogen):
        r"""Sets the add_hydrogen of this ReceptorDrugFileReq.

        增加氢原子

        :param add_hydrogen: The add_hydrogen of this ReceptorDrugFileReq.
        :type add_hydrogen: bool
        """
        self._add_hydrogen = add_hydrogen

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
        if not isinstance(other, ReceptorDrugFileReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
