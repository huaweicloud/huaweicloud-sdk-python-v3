# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTestReportsByConditionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'page_size': 'int',
        'page_no': 'str',
        'key_word': 'str',
        'own': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'page_size': 'page_size',
        'page_no': 'page_no',
        'key_word': 'key_word',
        'own': 'own'
    }

    def __init__(self, project_id=None, page_size=None, page_no=None, key_word=None, own=None):
        r"""ListTestReportsByConditionRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param page_size: 每页显示的条目数量,最大支持200条
        :type page_size: int
        :param page_no: 当前页数
        :type page_no: str
        :param key_word: 名称关键词
        :type key_word: str
        :param own: 是否是我的测试报告
        :type own: bool
        """
        
        

        self._project_id = None
        self._page_size = None
        self._page_no = None
        self._key_word = None
        self._own = None
        self.discriminator = None

        self.project_id = project_id
        self.page_size = page_size
        if page_no is not None:
            self.page_no = page_no
        if key_word is not None:
            self.key_word = key_word
        if own is not None:
            self.own = own

    @property
    def project_id(self):
        r"""Gets the project_id of this ListTestReportsByConditionRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this ListTestReportsByConditionRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListTestReportsByConditionRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this ListTestReportsByConditionRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def page_size(self):
        r"""Gets the page_size of this ListTestReportsByConditionRequest.

        每页显示的条目数量,最大支持200条

        :return: The page_size of this ListTestReportsByConditionRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListTestReportsByConditionRequest.

        每页显示的条目数量,最大支持200条

        :param page_size: The page_size of this ListTestReportsByConditionRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_no(self):
        r"""Gets the page_no of this ListTestReportsByConditionRequest.

        当前页数

        :return: The page_no of this ListTestReportsByConditionRequest.
        :rtype: str
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListTestReportsByConditionRequest.

        当前页数

        :param page_no: The page_no of this ListTestReportsByConditionRequest.
        :type page_no: str
        """
        self._page_no = page_no

    @property
    def key_word(self):
        r"""Gets the key_word of this ListTestReportsByConditionRequest.

        名称关键词

        :return: The key_word of this ListTestReportsByConditionRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this ListTestReportsByConditionRequest.

        名称关键词

        :param key_word: The key_word of this ListTestReportsByConditionRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def own(self):
        r"""Gets the own of this ListTestReportsByConditionRequest.

        是否是我的测试报告

        :return: The own of this ListTestReportsByConditionRequest.
        :rtype: bool
        """
        return self._own

    @own.setter
    def own(self, own):
        r"""Sets the own of this ListTestReportsByConditionRequest.

        是否是我的测试报告

        :param own: The own of this ListTestReportsByConditionRequest.
        :type own: bool
        """
        self._own = own

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
        if not isinstance(other, ListTestReportsByConditionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
