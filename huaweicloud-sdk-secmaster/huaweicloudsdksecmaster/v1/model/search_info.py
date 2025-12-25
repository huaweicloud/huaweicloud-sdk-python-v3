# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_catalogue': 'str',
        'second_catalogue': 'str',
        'catalogue_status': 'bool',
        'catalogue_type': 'str',
        'layout_name': 'str',
        'publisher_name': 'str',
        'analysis_version': 'str'
    }

    attribute_map = {
        'parent_catalogue': 'parent_catalogue',
        'second_catalogue': 'second_catalogue',
        'catalogue_status': 'catalogue_status',
        'catalogue_type': 'catalogue_type',
        'layout_name': 'layout_name',
        'publisher_name': 'publisher_name',
        'analysis_version': 'analysis_version'
    }

    def __init__(self, parent_catalogue=None, second_catalogue=None, catalogue_status=None, catalogue_type=None, layout_name=None, publisher_name=None, analysis_version=None):
        r"""SearchInfo

        The model defined in huaweicloud sdk

        :param parent_catalogue: 一级目录名称
        :type parent_catalogue: str
        :param second_catalogue: 二级目录名称
        :type second_catalogue: str
        :param catalogue_status: 是否内置
        :type catalogue_status: bool
        :param catalogue_type: 是否内置
        :type catalogue_type: str
        :param layout_name: 布局名称
        :type layout_name: str
        :param publisher_name: 发布者
        :type publisher_name: str
        :param analysis_version: 安全分析版本
        :type analysis_version: str
        """
        
        

        self._parent_catalogue = None
        self._second_catalogue = None
        self._catalogue_status = None
        self._catalogue_type = None
        self._layout_name = None
        self._publisher_name = None
        self._analysis_version = None
        self.discriminator = None

        if parent_catalogue is not None:
            self.parent_catalogue = parent_catalogue
        if second_catalogue is not None:
            self.second_catalogue = second_catalogue
        if catalogue_status is not None:
            self.catalogue_status = catalogue_status
        if catalogue_type is not None:
            self.catalogue_type = catalogue_type
        if layout_name is not None:
            self.layout_name = layout_name
        if publisher_name is not None:
            self.publisher_name = publisher_name
        if analysis_version is not None:
            self.analysis_version = analysis_version

    @property
    def parent_catalogue(self):
        r"""Gets the parent_catalogue of this SearchInfo.

        一级目录名称

        :return: The parent_catalogue of this SearchInfo.
        :rtype: str
        """
        return self._parent_catalogue

    @parent_catalogue.setter
    def parent_catalogue(self, parent_catalogue):
        r"""Sets the parent_catalogue of this SearchInfo.

        一级目录名称

        :param parent_catalogue: The parent_catalogue of this SearchInfo.
        :type parent_catalogue: str
        """
        self._parent_catalogue = parent_catalogue

    @property
    def second_catalogue(self):
        r"""Gets the second_catalogue of this SearchInfo.

        二级目录名称

        :return: The second_catalogue of this SearchInfo.
        :rtype: str
        """
        return self._second_catalogue

    @second_catalogue.setter
    def second_catalogue(self, second_catalogue):
        r"""Sets the second_catalogue of this SearchInfo.

        二级目录名称

        :param second_catalogue: The second_catalogue of this SearchInfo.
        :type second_catalogue: str
        """
        self._second_catalogue = second_catalogue

    @property
    def catalogue_status(self):
        r"""Gets the catalogue_status of this SearchInfo.

        是否内置

        :return: The catalogue_status of this SearchInfo.
        :rtype: bool
        """
        return self._catalogue_status

    @catalogue_status.setter
    def catalogue_status(self, catalogue_status):
        r"""Sets the catalogue_status of this SearchInfo.

        是否内置

        :param catalogue_status: The catalogue_status of this SearchInfo.
        :type catalogue_status: bool
        """
        self._catalogue_status = catalogue_status

    @property
    def catalogue_type(self):
        r"""Gets the catalogue_type of this SearchInfo.

        是否内置

        :return: The catalogue_type of this SearchInfo.
        :rtype: str
        """
        return self._catalogue_type

    @catalogue_type.setter
    def catalogue_type(self, catalogue_type):
        r"""Sets the catalogue_type of this SearchInfo.

        是否内置

        :param catalogue_type: The catalogue_type of this SearchInfo.
        :type catalogue_type: str
        """
        self._catalogue_type = catalogue_type

    @property
    def layout_name(self):
        r"""Gets the layout_name of this SearchInfo.

        布局名称

        :return: The layout_name of this SearchInfo.
        :rtype: str
        """
        return self._layout_name

    @layout_name.setter
    def layout_name(self, layout_name):
        r"""Sets the layout_name of this SearchInfo.

        布局名称

        :param layout_name: The layout_name of this SearchInfo.
        :type layout_name: str
        """
        self._layout_name = layout_name

    @property
    def publisher_name(self):
        r"""Gets the publisher_name of this SearchInfo.

        发布者

        :return: The publisher_name of this SearchInfo.
        :rtype: str
        """
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, publisher_name):
        r"""Sets the publisher_name of this SearchInfo.

        发布者

        :param publisher_name: The publisher_name of this SearchInfo.
        :type publisher_name: str
        """
        self._publisher_name = publisher_name

    @property
    def analysis_version(self):
        r"""Gets the analysis_version of this SearchInfo.

        安全分析版本

        :return: The analysis_version of this SearchInfo.
        :rtype: str
        """
        return self._analysis_version

    @analysis_version.setter
    def analysis_version(self, analysis_version):
        r"""Sets the analysis_version of this SearchInfo.

        安全分析版本

        :param analysis_version: The analysis_version of this SearchInfo.
        :type analysis_version: str
        """
        self._analysis_version = analysis_version

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
        if not isinstance(other, SearchInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
