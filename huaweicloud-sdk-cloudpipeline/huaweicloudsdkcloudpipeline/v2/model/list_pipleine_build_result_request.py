# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipleineBuildResultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'project_id': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'project_id': 'project_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, project_id=None, start_date=None, end_date=None, offset=None, limit=None):
        """ListPipleineBuildResultRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言类型 中文:zh-cn 英文:en-us，默认en-us
        :type x_language: str
        :param project_id: 项目id
        :type project_id: str
        :param start_date: 起始日期,起始日期和结束日期间隔不超过一个月，查询包含起始日期
        :type start_date: str
        :param end_date: 结束日期，起始日期和结束日期间隔不超过一个月，查询包含结束日期
        :type end_date: str
        :param offset: 偏移量,表示从此偏移量开始查询,offset大于等于0
        :type offset: int
        :param limit: 每次查询的条目数量
        :type limit: int
        """
        
        

        self._x_language = None
        self._project_id = None
        self._start_date = None
        self._end_date = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.project_id = project_id
        self.start_date = start_date
        self.end_date = end_date
        self.offset = offset
        self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListPipleineBuildResultRequest.

        语言类型 中文:zh-cn 英文:en-us，默认en-us

        :return: The x_language of this ListPipleineBuildResultRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListPipleineBuildResultRequest.

        语言类型 中文:zh-cn 英文:en-us，默认en-us

        :param x_language: The x_language of this ListPipleineBuildResultRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def project_id(self):
        """Gets the project_id of this ListPipleineBuildResultRequest.

        项目id

        :return: The project_id of this ListPipleineBuildResultRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListPipleineBuildResultRequest.

        项目id

        :param project_id: The project_id of this ListPipleineBuildResultRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def start_date(self):
        """Gets the start_date of this ListPipleineBuildResultRequest.

        起始日期,起始日期和结束日期间隔不超过一个月，查询包含起始日期

        :return: The start_date of this ListPipleineBuildResultRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ListPipleineBuildResultRequest.

        起始日期,起始日期和结束日期间隔不超过一个月，查询包含起始日期

        :param start_date: The start_date of this ListPipleineBuildResultRequest.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ListPipleineBuildResultRequest.

        结束日期，起始日期和结束日期间隔不超过一个月，查询包含结束日期

        :return: The end_date of this ListPipleineBuildResultRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ListPipleineBuildResultRequest.

        结束日期，起始日期和结束日期间隔不超过一个月，查询包含结束日期

        :param end_date: The end_date of this ListPipleineBuildResultRequest.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def offset(self):
        """Gets the offset of this ListPipleineBuildResultRequest.

        偏移量,表示从此偏移量开始查询,offset大于等于0

        :return: The offset of this ListPipleineBuildResultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPipleineBuildResultRequest.

        偏移量,表示从此偏移量开始查询,offset大于等于0

        :param offset: The offset of this ListPipleineBuildResultRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPipleineBuildResultRequest.

        每次查询的条目数量

        :return: The limit of this ListPipleineBuildResultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPipleineBuildResultRequest.

        每次查询的条目数量

        :param limit: The limit of this ListPipleineBuildResultRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListPipleineBuildResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
