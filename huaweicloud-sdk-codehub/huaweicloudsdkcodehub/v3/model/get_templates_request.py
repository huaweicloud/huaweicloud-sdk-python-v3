# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'platform': 'str',
        'language': 'str',
        'pipeline': 'str',
        'entertype': 'str',
        'search': 'str',
        'dateorder': 'str',
        'usedtimeorder': 'str',
        'type': 'str',
        'region': 'str',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'platform': 'platform',
        'language': 'language',
        'pipeline': 'pipeline',
        'entertype': 'entertype',
        'search': 'search',
        'dateorder': 'dateorder',
        'usedtimeorder': 'usedtimeorder',
        'type': 'type',
        'region': 'region',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, platform=None, language=None, pipeline=None, entertype=None, search=None, dateorder=None, usedtimeorder=None, type=None, region=None, page_no=None, page_size=None):
        """GetTemplatesRequest

        The model defined in huaweicloud sdk

        :param platform: 模板平台类型
        :type platform: str
        :param language: 语言类型
        :type language: str
        :param pipeline: 是否支持流水线
        :type pipeline: str
        :param entertype: 模板分类
        :type entertype: str
        :param search: 模板名称
        :type search: str
        :param dateorder: 模板日期排序
        :type dateorder: str
        :param usedtimeorder: 模板引用次数排序
        :type usedtimeorder: str
        :param type: 模板公开类型
        :type type: str
        :param region: 大区名称
        :type region: str
        :param page_no: 分页页数
        :type page_no: int
        :param page_size: 每页数据数
        :type page_size: int
        """
        
        

        self._platform = None
        self._language = None
        self._pipeline = None
        self._entertype = None
        self._search = None
        self._dateorder = None
        self._usedtimeorder = None
        self._type = None
        self._region = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if platform is not None:
            self.platform = platform
        if language is not None:
            self.language = language
        if pipeline is not None:
            self.pipeline = pipeline
        if entertype is not None:
            self.entertype = entertype
        if search is not None:
            self.search = search
        if dateorder is not None:
            self.dateorder = dateorder
        if usedtimeorder is not None:
            self.usedtimeorder = usedtimeorder
        if type is not None:
            self.type = type
        if region is not None:
            self.region = region
        self.page_no = page_no
        self.page_size = page_size

    @property
    def platform(self):
        """Gets the platform of this GetTemplatesRequest.

        模板平台类型

        :return: The platform of this GetTemplatesRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this GetTemplatesRequest.

        模板平台类型

        :param platform: The platform of this GetTemplatesRequest.
        :type platform: str
        """
        self._platform = platform

    @property
    def language(self):
        """Gets the language of this GetTemplatesRequest.

        语言类型

        :return: The language of this GetTemplatesRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this GetTemplatesRequest.

        语言类型

        :param language: The language of this GetTemplatesRequest.
        :type language: str
        """
        self._language = language

    @property
    def pipeline(self):
        """Gets the pipeline of this GetTemplatesRequest.

        是否支持流水线

        :return: The pipeline of this GetTemplatesRequest.
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this GetTemplatesRequest.

        是否支持流水线

        :param pipeline: The pipeline of this GetTemplatesRequest.
        :type pipeline: str
        """
        self._pipeline = pipeline

    @property
    def entertype(self):
        """Gets the entertype of this GetTemplatesRequest.

        模板分类

        :return: The entertype of this GetTemplatesRequest.
        :rtype: str
        """
        return self._entertype

    @entertype.setter
    def entertype(self, entertype):
        """Sets the entertype of this GetTemplatesRequest.

        模板分类

        :param entertype: The entertype of this GetTemplatesRequest.
        :type entertype: str
        """
        self._entertype = entertype

    @property
    def search(self):
        """Gets the search of this GetTemplatesRequest.

        模板名称

        :return: The search of this GetTemplatesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this GetTemplatesRequest.

        模板名称

        :param search: The search of this GetTemplatesRequest.
        :type search: str
        """
        self._search = search

    @property
    def dateorder(self):
        """Gets the dateorder of this GetTemplatesRequest.

        模板日期排序

        :return: The dateorder of this GetTemplatesRequest.
        :rtype: str
        """
        return self._dateorder

    @dateorder.setter
    def dateorder(self, dateorder):
        """Sets the dateorder of this GetTemplatesRequest.

        模板日期排序

        :param dateorder: The dateorder of this GetTemplatesRequest.
        :type dateorder: str
        """
        self._dateorder = dateorder

    @property
    def usedtimeorder(self):
        """Gets the usedtimeorder of this GetTemplatesRequest.

        模板引用次数排序

        :return: The usedtimeorder of this GetTemplatesRequest.
        :rtype: str
        """
        return self._usedtimeorder

    @usedtimeorder.setter
    def usedtimeorder(self, usedtimeorder):
        """Sets the usedtimeorder of this GetTemplatesRequest.

        模板引用次数排序

        :param usedtimeorder: The usedtimeorder of this GetTemplatesRequest.
        :type usedtimeorder: str
        """
        self._usedtimeorder = usedtimeorder

    @property
    def type(self):
        """Gets the type of this GetTemplatesRequest.

        模板公开类型

        :return: The type of this GetTemplatesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetTemplatesRequest.

        模板公开类型

        :param type: The type of this GetTemplatesRequest.
        :type type: str
        """
        self._type = type

    @property
    def region(self):
        """Gets the region of this GetTemplatesRequest.

        大区名称

        :return: The region of this GetTemplatesRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this GetTemplatesRequest.

        大区名称

        :param region: The region of this GetTemplatesRequest.
        :type region: str
        """
        self._region = region

    @property
    def page_no(self):
        """Gets the page_no of this GetTemplatesRequest.

        分页页数

        :return: The page_no of this GetTemplatesRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetTemplatesRequest.

        分页页数

        :param page_no: The page_no of this GetTemplatesRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetTemplatesRequest.

        每页数据数

        :return: The page_size of this GetTemplatesRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetTemplatesRequest.

        每页数据数

        :param page_size: The page_size of this GetTemplatesRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, GetTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
