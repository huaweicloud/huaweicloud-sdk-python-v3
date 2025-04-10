# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueTreeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner': 'str',
        'issue_id': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'key_word': 'str',
        'iteration_id': 'str',
        'severity_id': 'str',
        'status_id': 'str',
        'module_id': 'str',
        'status_ids': 'str',
        'module_ids': 'str',
        'pi_filter': 'list[IssueListPiFilterInfo]',
        'status_names': 'list[str]'
    }

    attribute_map = {
        'owner': 'owner',
        'issue_id': 'issue_id',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'key_word': 'key_word',
        'iteration_id': 'iteration_id',
        'severity_id': 'severity_id',
        'status_id': 'status_id',
        'module_id': 'module_id',
        'status_ids': 'status_ids',
        'module_ids': 'module_ids',
        'pi_filter': 'pi_filter',
        'status_names': 'status_names'
    }

    def __init__(self, owner=None, issue_id=None, page_no=None, page_size=None, key_word=None, iteration_id=None, severity_id=None, status_id=None, module_id=None, status_ids=None, module_ids=None, pi_filter=None, status_names=None):
        r"""IssueTreeInfo

        The model defined in huaweicloud sdk

        :param owner: 过滤条件：处理人
        :type owner: str
        :param issue_id: 需求ID
        :type issue_id: str
        :param page_no: 页码
        :type page_no: int
        :param page_size: 每页展示条数
        :type page_size: int
        :param key_word: 关键字
        :type key_word: str
        :param iteration_id: 过滤条件：迭代ID
        :type iteration_id: str
        :param severity_id: 过滤条件：重要程度ID
        :type severity_id: str
        :param status_id: 过滤条件：状态ID
        :type status_id: str
        :param module_id: 过滤条件：模块ID
        :type module_id: str
        :param status_ids: 过滤条件：状态ID多个条件，每个条件取或，-2代表搜索未设置
        :type status_ids: str
        :param module_ids: 过滤条件：模块ID多个，每个条件取或，-2代表搜索未设置
        :type module_ids: str
        :param pi_filter: 迭代、pi过滤条件
        :type pi_filter: list[:class:`huaweicloudsdkcloudtest.v1.IssueListPiFilterInfo`]
        :param status_names: 状态名称列表
        :type status_names: list[str]
        """
        
        

        self._owner = None
        self._issue_id = None
        self._page_no = None
        self._page_size = None
        self._key_word = None
        self._iteration_id = None
        self._severity_id = None
        self._status_id = None
        self._module_id = None
        self._status_ids = None
        self._module_ids = None
        self._pi_filter = None
        self._status_names = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if issue_id is not None:
            self.issue_id = issue_id
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if key_word is not None:
            self.key_word = key_word
        if iteration_id is not None:
            self.iteration_id = iteration_id
        if severity_id is not None:
            self.severity_id = severity_id
        if status_id is not None:
            self.status_id = status_id
        if module_id is not None:
            self.module_id = module_id
        if status_ids is not None:
            self.status_ids = status_ids
        if module_ids is not None:
            self.module_ids = module_ids
        if pi_filter is not None:
            self.pi_filter = pi_filter
        if status_names is not None:
            self.status_names = status_names

    @property
    def owner(self):
        r"""Gets the owner of this IssueTreeInfo.

        过滤条件：处理人

        :return: The owner of this IssueTreeInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this IssueTreeInfo.

        过滤条件：处理人

        :param owner: The owner of this IssueTreeInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def issue_id(self):
        r"""Gets the issue_id of this IssueTreeInfo.

        需求ID

        :return: The issue_id of this IssueTreeInfo.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this IssueTreeInfo.

        需求ID

        :param issue_id: The issue_id of this IssueTreeInfo.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def page_no(self):
        r"""Gets the page_no of this IssueTreeInfo.

        页码

        :return: The page_no of this IssueTreeInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this IssueTreeInfo.

        页码

        :param page_no: The page_no of this IssueTreeInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this IssueTreeInfo.

        每页展示条数

        :return: The page_size of this IssueTreeInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this IssueTreeInfo.

        每页展示条数

        :param page_size: The page_size of this IssueTreeInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def key_word(self):
        r"""Gets the key_word of this IssueTreeInfo.

        关键字

        :return: The key_word of this IssueTreeInfo.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this IssueTreeInfo.

        关键字

        :param key_word: The key_word of this IssueTreeInfo.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def iteration_id(self):
        r"""Gets the iteration_id of this IssueTreeInfo.

        过滤条件：迭代ID

        :return: The iteration_id of this IssueTreeInfo.
        :rtype: str
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        r"""Sets the iteration_id of this IssueTreeInfo.

        过滤条件：迭代ID

        :param iteration_id: The iteration_id of this IssueTreeInfo.
        :type iteration_id: str
        """
        self._iteration_id = iteration_id

    @property
    def severity_id(self):
        r"""Gets the severity_id of this IssueTreeInfo.

        过滤条件：重要程度ID

        :return: The severity_id of this IssueTreeInfo.
        :rtype: str
        """
        return self._severity_id

    @severity_id.setter
    def severity_id(self, severity_id):
        r"""Sets the severity_id of this IssueTreeInfo.

        过滤条件：重要程度ID

        :param severity_id: The severity_id of this IssueTreeInfo.
        :type severity_id: str
        """
        self._severity_id = severity_id

    @property
    def status_id(self):
        r"""Gets the status_id of this IssueTreeInfo.

        过滤条件：状态ID

        :return: The status_id of this IssueTreeInfo.
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        r"""Sets the status_id of this IssueTreeInfo.

        过滤条件：状态ID

        :param status_id: The status_id of this IssueTreeInfo.
        :type status_id: str
        """
        self._status_id = status_id

    @property
    def module_id(self):
        r"""Gets the module_id of this IssueTreeInfo.

        过滤条件：模块ID

        :return: The module_id of this IssueTreeInfo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this IssueTreeInfo.

        过滤条件：模块ID

        :param module_id: The module_id of this IssueTreeInfo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def status_ids(self):
        r"""Gets the status_ids of this IssueTreeInfo.

        过滤条件：状态ID多个条件，每个条件取或，-2代表搜索未设置

        :return: The status_ids of this IssueTreeInfo.
        :rtype: str
        """
        return self._status_ids

    @status_ids.setter
    def status_ids(self, status_ids):
        r"""Sets the status_ids of this IssueTreeInfo.

        过滤条件：状态ID多个条件，每个条件取或，-2代表搜索未设置

        :param status_ids: The status_ids of this IssueTreeInfo.
        :type status_ids: str
        """
        self._status_ids = status_ids

    @property
    def module_ids(self):
        r"""Gets the module_ids of this IssueTreeInfo.

        过滤条件：模块ID多个，每个条件取或，-2代表搜索未设置

        :return: The module_ids of this IssueTreeInfo.
        :rtype: str
        """
        return self._module_ids

    @module_ids.setter
    def module_ids(self, module_ids):
        r"""Sets the module_ids of this IssueTreeInfo.

        过滤条件：模块ID多个，每个条件取或，-2代表搜索未设置

        :param module_ids: The module_ids of this IssueTreeInfo.
        :type module_ids: str
        """
        self._module_ids = module_ids

    @property
    def pi_filter(self):
        r"""Gets the pi_filter of this IssueTreeInfo.

        迭代、pi过滤条件

        :return: The pi_filter of this IssueTreeInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.IssueListPiFilterInfo`]
        """
        return self._pi_filter

    @pi_filter.setter
    def pi_filter(self, pi_filter):
        r"""Sets the pi_filter of this IssueTreeInfo.

        迭代、pi过滤条件

        :param pi_filter: The pi_filter of this IssueTreeInfo.
        :type pi_filter: list[:class:`huaweicloudsdkcloudtest.v1.IssueListPiFilterInfo`]
        """
        self._pi_filter = pi_filter

    @property
    def status_names(self):
        r"""Gets the status_names of this IssueTreeInfo.

        状态名称列表

        :return: The status_names of this IssueTreeInfo.
        :rtype: list[str]
        """
        return self._status_names

    @status_names.setter
    def status_names(self, status_names):
        r"""Sets the status_names of this IssueTreeInfo.

        状态名称列表

        :param status_names: The status_names of this IssueTreeInfo.
        :type status_names: list[str]
        """
        self._status_names = status_names

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
        if not isinstance(other, IssueTreeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
