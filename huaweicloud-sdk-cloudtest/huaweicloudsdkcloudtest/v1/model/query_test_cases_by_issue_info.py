# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTestCasesByIssueInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_no': 'int',
        'page_size': 'int',
        'sort_field': 'str',
        'sort_type': 'str',
        'version_uri': 'str',
        'relate_type': 'str',
        'key_word': 'str',
        'rank_ids': 'list[str]',
        'result_codes': 'list[str]'
    }

    attribute_map = {
        'page_no': 'page_no',
        'page_size': 'page_size',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'version_uri': 'version_uri',
        'relate_type': 'relate_type',
        'key_word': 'key_word',
        'rank_ids': 'rank_ids',
        'result_codes': 'result_codes'
    }

    def __init__(self, page_no=None, page_size=None, sort_field=None, sort_type=None, version_uri=None, relate_type=None, key_word=None, rank_ids=None, result_codes=None):
        """QueryTestCasesByIssueInfo

        The model defined in huaweicloud sdk

        :param page_no: 页码
        :type page_no: int
        :param page_size: 每页数量
        :type page_size: int
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_type: 排序类型
        :type sort_type: str
        :param version_uri: 版本uri
        :type version_uri: str
        :param relate_type: 关联关系类型
        :type relate_type: str
        :param key_word: 关键字
        :type key_word: str
        :param rank_ids: 用例等级ID集合
        :type rank_ids: list[str]
        :param result_codes: 结果Code集合
        :type result_codes: list[str]
        """
        
        

        self._page_no = None
        self._page_size = None
        self._sort_field = None
        self._sort_type = None
        self._version_uri = None
        self._relate_type = None
        self._key_word = None
        self._rank_ids = None
        self._result_codes = None
        self.discriminator = None

        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if version_uri is not None:
            self.version_uri = version_uri
        if relate_type is not None:
            self.relate_type = relate_type
        if key_word is not None:
            self.key_word = key_word
        if rank_ids is not None:
            self.rank_ids = rank_ids
        if result_codes is not None:
            self.result_codes = result_codes

    @property
    def page_no(self):
        """Gets the page_no of this QueryTestCasesByIssueInfo.

        页码

        :return: The page_no of this QueryTestCasesByIssueInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this QueryTestCasesByIssueInfo.

        页码

        :param page_no: The page_no of this QueryTestCasesByIssueInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this QueryTestCasesByIssueInfo.

        每页数量

        :return: The page_size of this QueryTestCasesByIssueInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this QueryTestCasesByIssueInfo.

        每页数量

        :param page_size: The page_size of this QueryTestCasesByIssueInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def sort_field(self):
        """Gets the sort_field of this QueryTestCasesByIssueInfo.

        排序字段

        :return: The sort_field of this QueryTestCasesByIssueInfo.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this QueryTestCasesByIssueInfo.

        排序字段

        :param sort_field: The sort_field of this QueryTestCasesByIssueInfo.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        """Gets the sort_type of this QueryTestCasesByIssueInfo.

        排序类型

        :return: The sort_type of this QueryTestCasesByIssueInfo.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this QueryTestCasesByIssueInfo.

        排序类型

        :param sort_type: The sort_type of this QueryTestCasesByIssueInfo.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def version_uri(self):
        """Gets the version_uri of this QueryTestCasesByIssueInfo.

        版本uri

        :return: The version_uri of this QueryTestCasesByIssueInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this QueryTestCasesByIssueInfo.

        版本uri

        :param version_uri: The version_uri of this QueryTestCasesByIssueInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def relate_type(self):
        """Gets the relate_type of this QueryTestCasesByIssueInfo.

        关联关系类型

        :return: The relate_type of this QueryTestCasesByIssueInfo.
        :rtype: str
        """
        return self._relate_type

    @relate_type.setter
    def relate_type(self, relate_type):
        """Sets the relate_type of this QueryTestCasesByIssueInfo.

        关联关系类型

        :param relate_type: The relate_type of this QueryTestCasesByIssueInfo.
        :type relate_type: str
        """
        self._relate_type = relate_type

    @property
    def key_word(self):
        """Gets the key_word of this QueryTestCasesByIssueInfo.

        关键字

        :return: The key_word of this QueryTestCasesByIssueInfo.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        """Sets the key_word of this QueryTestCasesByIssueInfo.

        关键字

        :param key_word: The key_word of this QueryTestCasesByIssueInfo.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def rank_ids(self):
        """Gets the rank_ids of this QueryTestCasesByIssueInfo.

        用例等级ID集合

        :return: The rank_ids of this QueryTestCasesByIssueInfo.
        :rtype: list[str]
        """
        return self._rank_ids

    @rank_ids.setter
    def rank_ids(self, rank_ids):
        """Sets the rank_ids of this QueryTestCasesByIssueInfo.

        用例等级ID集合

        :param rank_ids: The rank_ids of this QueryTestCasesByIssueInfo.
        :type rank_ids: list[str]
        """
        self._rank_ids = rank_ids

    @property
    def result_codes(self):
        """Gets the result_codes of this QueryTestCasesByIssueInfo.

        结果Code集合

        :return: The result_codes of this QueryTestCasesByIssueInfo.
        :rtype: list[str]
        """
        return self._result_codes

    @result_codes.setter
    def result_codes(self, result_codes):
        """Sets the result_codes of this QueryTestCasesByIssueInfo.

        结果Code集合

        :param result_codes: The result_codes of this QueryTestCasesByIssueInfo.
        :type result_codes: list[str]
        """
        self._result_codes = result_codes

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
        if not isinstance(other, QueryTestCasesByIssueInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
