# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PocketFragment:

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
        'name': 'str',
        'data': 'str',
        'edited': 'EditedLigand',
        'label_sites': 'LabelSite'
    }

    attribute_map = {
        'source': 'source',
        'url': 'url',
        'format': 'format',
        'name': 'name',
        'data': 'data',
        'edited': 'edited',
        'label_sites': 'label_sites'
    }

    def __init__(self, source=None, url=None, format=None, name=None, data=None, edited=None, label_sites=None):
        r"""PocketFragment

        The model defined in huaweicloud sdk

        :param source: 
        :type source: :class:`huaweicloudsdkeihealth.v1.DrugFileSource`
        :param url: 文件URL，当数据源为外部网络数据时为https地址；用户私有数据中心为项目路径、公共数据场景为obs地址
        :type url: str
        :param format: 文件格式，支持PDB、SDF、MOL2、SMI，仅数据源为RAW时提供
        :type format: str
        :param name: 原始配体名称，仅RAW类型时用于配体名称标识
        :type name: str
        :param data: 文件原始数据，仅数据源为RAW时提供
        :type data: str
        :param edited: 
        :type edited: :class:`huaweicloudsdkeihealth.v1.EditedLigand`
        :param label_sites: 
        :type label_sites: :class:`huaweicloudsdkeihealth.v1.LabelSite`
        """
        
        

        self._source = None
        self._url = None
        self._format = None
        self._name = None
        self._data = None
        self._edited = None
        self._label_sites = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if url is not None:
            self.url = url
        if format is not None:
            self.format = format
        if name is not None:
            self.name = name
        if data is not None:
            self.data = data
        if edited is not None:
            self.edited = edited
        if label_sites is not None:
            self.label_sites = label_sites

    @property
    def source(self):
        r"""Gets the source of this PocketFragment.

        :return: The source of this PocketFragment.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFileSource`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this PocketFragment.

        :param source: The source of this PocketFragment.
        :type source: :class:`huaweicloudsdkeihealth.v1.DrugFileSource`
        """
        self._source = source

    @property
    def url(self):
        r"""Gets the url of this PocketFragment.

        文件URL，当数据源为外部网络数据时为https地址；用户私有数据中心为项目路径、公共数据场景为obs地址

        :return: The url of this PocketFragment.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this PocketFragment.

        文件URL，当数据源为外部网络数据时为https地址；用户私有数据中心为项目路径、公共数据场景为obs地址

        :param url: The url of this PocketFragment.
        :type url: str
        """
        self._url = url

    @property
    def format(self):
        r"""Gets the format of this PocketFragment.

        文件格式，支持PDB、SDF、MOL2、SMI，仅数据源为RAW时提供

        :return: The format of this PocketFragment.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this PocketFragment.

        文件格式，支持PDB、SDF、MOL2、SMI，仅数据源为RAW时提供

        :param format: The format of this PocketFragment.
        :type format: str
        """
        self._format = format

    @property
    def name(self):
        r"""Gets the name of this PocketFragment.

        原始配体名称，仅RAW类型时用于配体名称标识

        :return: The name of this PocketFragment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PocketFragment.

        原始配体名称，仅RAW类型时用于配体名称标识

        :param name: The name of this PocketFragment.
        :type name: str
        """
        self._name = name

    @property
    def data(self):
        r"""Gets the data of this PocketFragment.

        文件原始数据，仅数据源为RAW时提供

        :return: The data of this PocketFragment.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this PocketFragment.

        文件原始数据，仅数据源为RAW时提供

        :param data: The data of this PocketFragment.
        :type data: str
        """
        self._data = data

    @property
    def edited(self):
        r"""Gets the edited of this PocketFragment.

        :return: The edited of this PocketFragment.
        :rtype: :class:`huaweicloudsdkeihealth.v1.EditedLigand`
        """
        return self._edited

    @edited.setter
    def edited(self, edited):
        r"""Sets the edited of this PocketFragment.

        :param edited: The edited of this PocketFragment.
        :type edited: :class:`huaweicloudsdkeihealth.v1.EditedLigand`
        """
        self._edited = edited

    @property
    def label_sites(self):
        r"""Gets the label_sites of this PocketFragment.

        :return: The label_sites of this PocketFragment.
        :rtype: :class:`huaweicloudsdkeihealth.v1.LabelSite`
        """
        return self._label_sites

    @label_sites.setter
    def label_sites(self, label_sites):
        r"""Sets the label_sites of this PocketFragment.

        :param label_sites: The label_sites of this PocketFragment.
        :type label_sites: :class:`huaweicloudsdkeihealth.v1.LabelSite`
        """
        self._label_sites = label_sites

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
        if not isinstance(other, PocketFragment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
