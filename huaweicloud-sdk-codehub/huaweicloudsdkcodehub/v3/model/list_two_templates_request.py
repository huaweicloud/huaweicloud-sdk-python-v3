# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTwoTemplatesRequest:

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
        'enter_type': 'str',
        'search': 'str',
        'date_order': 'str',
        'used_time_order': 'str',
        'type': 'str',
        'region': 'str',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'platform': 'platform',
        'language': 'language',
        'pipeline': 'pipeline',
        'enter_type': 'enter_type',
        'search': 'search',
        'date_order': 'date_order',
        'used_time_order': 'used_time_order',
        'type': 'type',
        'region': 'region',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, platform=None, language=None, pipeline=None, enter_type=None, search=None, date_order=None, used_time_order=None, type=None, region=None, page_no=None, page_size=None):
        """ListTwoTemplatesRequest

        The model defined in huaweicloud sdk

        :param platform: 模板平台类型
        :type platform: str
        :param language: 语言类型
        :type language: str
        :param pipeline: 是否支持流水线
        :type pipeline: str
        :param enter_type: 模板分类
        :type enter_type: str
        :param search: 模板名称
        :type search: str
        :param date_order: 模板日期排序
        :type date_order: str
        :param used_time_order: 模板引用次数排序
        :type used_time_order: str
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
        self._enter_type = None
        self._search = None
        self._date_order = None
        self._used_time_order = None
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
        if enter_type is not None:
            self.enter_type = enter_type
        if search is not None:
            self.search = search
        if date_order is not None:
            self.date_order = date_order
        if used_time_order is not None:
            self.used_time_order = used_time_order
        if type is not None:
            self.type = type
        if region is not None:
            self.region = region
        self.page_no = page_no
        self.page_size = page_size

    @property
    def platform(self):
        """Gets the platform of this ListTwoTemplatesRequest.

        模板平台类型

        :return: The platform of this ListTwoTemplatesRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ListTwoTemplatesRequest.

        模板平台类型

        :param platform: The platform of this ListTwoTemplatesRequest.
        :type platform: str
        """
        self._platform = platform

    @property
    def language(self):
        """Gets the language of this ListTwoTemplatesRequest.

        语言类型

        :return: The language of this ListTwoTemplatesRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ListTwoTemplatesRequest.

        语言类型

        :param language: The language of this ListTwoTemplatesRequest.
        :type language: str
        """
        self._language = language

    @property
    def pipeline(self):
        """Gets the pipeline of this ListTwoTemplatesRequest.

        是否支持流水线

        :return: The pipeline of this ListTwoTemplatesRequest.
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this ListTwoTemplatesRequest.

        是否支持流水线

        :param pipeline: The pipeline of this ListTwoTemplatesRequest.
        :type pipeline: str
        """
        self._pipeline = pipeline

    @property
    def enter_type(self):
        """Gets the enter_type of this ListTwoTemplatesRequest.

        模板分类

        :return: The enter_type of this ListTwoTemplatesRequest.
        :rtype: str
        """
        return self._enter_type

    @enter_type.setter
    def enter_type(self, enter_type):
        """Sets the enter_type of this ListTwoTemplatesRequest.

        模板分类

        :param enter_type: The enter_type of this ListTwoTemplatesRequest.
        :type enter_type: str
        """
        self._enter_type = enter_type

    @property
    def search(self):
        """Gets the search of this ListTwoTemplatesRequest.

        模板名称

        :return: The search of this ListTwoTemplatesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this ListTwoTemplatesRequest.

        模板名称

        :param search: The search of this ListTwoTemplatesRequest.
        :type search: str
        """
        self._search = search

    @property
    def date_order(self):
        """Gets the date_order of this ListTwoTemplatesRequest.

        模板日期排序

        :return: The date_order of this ListTwoTemplatesRequest.
        :rtype: str
        """
        return self._date_order

    @date_order.setter
    def date_order(self, date_order):
        """Sets the date_order of this ListTwoTemplatesRequest.

        模板日期排序

        :param date_order: The date_order of this ListTwoTemplatesRequest.
        :type date_order: str
        """
        self._date_order = date_order

    @property
    def used_time_order(self):
        """Gets the used_time_order of this ListTwoTemplatesRequest.

        模板引用次数排序

        :return: The used_time_order of this ListTwoTemplatesRequest.
        :rtype: str
        """
        return self._used_time_order

    @used_time_order.setter
    def used_time_order(self, used_time_order):
        """Sets the used_time_order of this ListTwoTemplatesRequest.

        模板引用次数排序

        :param used_time_order: The used_time_order of this ListTwoTemplatesRequest.
        :type used_time_order: str
        """
        self._used_time_order = used_time_order

    @property
    def type(self):
        """Gets the type of this ListTwoTemplatesRequest.

        模板公开类型

        :return: The type of this ListTwoTemplatesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListTwoTemplatesRequest.

        模板公开类型

        :param type: The type of this ListTwoTemplatesRequest.
        :type type: str
        """
        self._type = type

    @property
    def region(self):
        """Gets the region of this ListTwoTemplatesRequest.

        大区名称

        :return: The region of this ListTwoTemplatesRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListTwoTemplatesRequest.

        大区名称

        :param region: The region of this ListTwoTemplatesRequest.
        :type region: str
        """
        self._region = region

    @property
    def page_no(self):
        """Gets the page_no of this ListTwoTemplatesRequest.

        分页页数

        :return: The page_no of this ListTwoTemplatesRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ListTwoTemplatesRequest.

        分页页数

        :param page_no: The page_no of this ListTwoTemplatesRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this ListTwoTemplatesRequest.

        每页数据数

        :return: The page_size of this ListTwoTemplatesRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListTwoTemplatesRequest.

        每页数据数

        :param page_size: The page_size of this ListTwoTemplatesRequest.
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
        if not isinstance(other, ListTwoTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
