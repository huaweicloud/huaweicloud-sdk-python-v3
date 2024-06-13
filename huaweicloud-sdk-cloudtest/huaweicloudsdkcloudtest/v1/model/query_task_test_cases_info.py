# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTaskTestCasesInfo:

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
        'start_index': 'int',
        'end_index': 'int',
        'key_word': 'str',
        'test_case_uris': 'list[str]',
        'iterator_uri': 'str'
    }

    attribute_map = {
        'page_no': 'page_no',
        'page_size': 'page_size',
        'start_index': 'start_index',
        'end_index': 'end_index',
        'key_word': 'key_word',
        'test_case_uris': 'test_case_uris',
        'iterator_uri': 'iterator_uri'
    }

    def __init__(self, page_no=None, page_size=None, start_index=None, end_index=None, key_word=None, test_case_uris=None, iterator_uri=None):
        """QueryTaskTestCasesInfo

        The model defined in huaweicloud sdk

        :param page_no: 页码
        :type page_no: int
        :param page_size: 每页数量
        :type page_size: int
        :param start_index: 起始位
        :type start_index: int
        :param end_index: 结束位
        :type end_index: int
        :param key_word: 关键字
        :type key_word: str
        :param test_case_uris: 用例uri列表
        :type test_case_uris: list[str]
        :param iterator_uri: 测试计划uri
        :type iterator_uri: str
        """
        
        

        self._page_no = None
        self._page_size = None
        self._start_index = None
        self._end_index = None
        self._key_word = None
        self._test_case_uris = None
        self._iterator_uri = None
        self.discriminator = None

        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if start_index is not None:
            self.start_index = start_index
        if end_index is not None:
            self.end_index = end_index
        if key_word is not None:
            self.key_word = key_word
        if test_case_uris is not None:
            self.test_case_uris = test_case_uris
        if iterator_uri is not None:
            self.iterator_uri = iterator_uri

    @property
    def page_no(self):
        """Gets the page_no of this QueryTaskTestCasesInfo.

        页码

        :return: The page_no of this QueryTaskTestCasesInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this QueryTaskTestCasesInfo.

        页码

        :param page_no: The page_no of this QueryTaskTestCasesInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this QueryTaskTestCasesInfo.

        每页数量

        :return: The page_size of this QueryTaskTestCasesInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this QueryTaskTestCasesInfo.

        每页数量

        :param page_size: The page_size of this QueryTaskTestCasesInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def start_index(self):
        """Gets the start_index of this QueryTaskTestCasesInfo.

        起始位

        :return: The start_index of this QueryTaskTestCasesInfo.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this QueryTaskTestCasesInfo.

        起始位

        :param start_index: The start_index of this QueryTaskTestCasesInfo.
        :type start_index: int
        """
        self._start_index = start_index

    @property
    def end_index(self):
        """Gets the end_index of this QueryTaskTestCasesInfo.

        结束位

        :return: The end_index of this QueryTaskTestCasesInfo.
        :rtype: int
        """
        return self._end_index

    @end_index.setter
    def end_index(self, end_index):
        """Sets the end_index of this QueryTaskTestCasesInfo.

        结束位

        :param end_index: The end_index of this QueryTaskTestCasesInfo.
        :type end_index: int
        """
        self._end_index = end_index

    @property
    def key_word(self):
        """Gets the key_word of this QueryTaskTestCasesInfo.

        关键字

        :return: The key_word of this QueryTaskTestCasesInfo.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        """Sets the key_word of this QueryTaskTestCasesInfo.

        关键字

        :param key_word: The key_word of this QueryTaskTestCasesInfo.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def test_case_uris(self):
        """Gets the test_case_uris of this QueryTaskTestCasesInfo.

        用例uri列表

        :return: The test_case_uris of this QueryTaskTestCasesInfo.
        :rtype: list[str]
        """
        return self._test_case_uris

    @test_case_uris.setter
    def test_case_uris(self, test_case_uris):
        """Sets the test_case_uris of this QueryTaskTestCasesInfo.

        用例uri列表

        :param test_case_uris: The test_case_uris of this QueryTaskTestCasesInfo.
        :type test_case_uris: list[str]
        """
        self._test_case_uris = test_case_uris

    @property
    def iterator_uri(self):
        """Gets the iterator_uri of this QueryTaskTestCasesInfo.

        测试计划uri

        :return: The iterator_uri of this QueryTaskTestCasesInfo.
        :rtype: str
        """
        return self._iterator_uri

    @iterator_uri.setter
    def iterator_uri(self, iterator_uri):
        """Sets the iterator_uri of this QueryTaskTestCasesInfo.

        测试计划uri

        :param iterator_uri: The iterator_uri of this QueryTaskTestCasesInfo.
        :type iterator_uri: str
        """
        self._iterator_uri = iterator_uri

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
        if not isinstance(other, QueryTaskTestCasesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
