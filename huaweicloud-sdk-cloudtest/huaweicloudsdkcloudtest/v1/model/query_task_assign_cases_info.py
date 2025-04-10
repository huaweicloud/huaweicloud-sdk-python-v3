# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTaskAssignCasesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stage': 'int',
        'owners': 'list[str]',
        'page_no': 'int',
        'page_size': 'int',
        'results': 'list[str]',
        'status': 'list[str]',
        'version_uri': 'str',
        'release_dev': 'str',
        'sort_field': 'str',
        'sort_type': 'str',
        'feature_uri': 'str',
        'task_result_uri': 'str',
        'rank_ids': 'list[int]',
        'key_word': 'str',
        'issue_id': 'str',
        'associated_issue': 'bool',
        'select_all_pages': 'bool',
        'is_available': 'bool',
        'is_script_exist': 'bool'
    }

    attribute_map = {
        'stage': 'stage',
        'owners': 'owners',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'results': 'results',
        'status': 'status',
        'version_uri': 'version_uri',
        'release_dev': 'release_dev',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'feature_uri': 'feature_uri',
        'task_result_uri': 'task_result_uri',
        'rank_ids': 'rank_ids',
        'key_word': 'key_word',
        'issue_id': 'issue_id',
        'associated_issue': 'associated_issue',
        'select_all_pages': 'select_all_pages',
        'is_available': 'is_available',
        'is_script_exist': 'is_script_exist'
    }

    def __init__(self, stage=None, owners=None, page_no=None, page_size=None, results=None, status=None, version_uri=None, release_dev=None, sort_field=None, sort_type=None, feature_uri=None, task_result_uri=None, rank_ids=None, key_word=None, issue_id=None, associated_issue=None, select_all_pages=None, is_available=None, is_script_exist=None):
        r"""QueryTaskAssignCasesInfo

        The model defined in huaweicloud sdk

        :param stage: 测试用例在任务中的阶段
        :type stage: int
        :param owners: 处理人过滤数组
        :type owners: list[str]
        :param page_no: 页码
        :type page_no: int
        :param page_size: 页数量
        :type page_size: int
        :param results: 结果过滤
        :type results: list[str]
        :param status: 状态过滤
        :type status: list[str]
        :param version_uri: 分支/迭代uri
        :type version_uri: str
        :param release_dev: 任务版本过滤条件，影响关联任务的结果查询，查询当前任务版本下的用例最新结果
        :type release_dev: str
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_type: 排序方法
        :type sort_type: str
        :param feature_uri: 特性目录URI
        :type feature_uri: str
        :param task_result_uri: 测试套结果uri
        :type task_result_uri: str
        :param rank_ids: 用例等级ID集合
        :type rank_ids: list[int]
        :param key_word: 关键字
        :type key_word: str
        :param issue_id: 需求id
        :type issue_id: str
        :param associated_issue: 是否关联需求（null：不限，false：未关联，true：已关联）
        :type associated_issue: bool
        :param select_all_pages: 是否全选所有页（null：不全选，false：不全选，true：全选），用于任务批量执行结果功能，只返回用例uri，不返回其他信息
        :type select_all_pages: bool
        :param is_available: 用例是否可用
        :type is_available: bool
        :param is_script_exist: 用例脚本字段是否有值
        :type is_script_exist: bool
        """
        
        

        self._stage = None
        self._owners = None
        self._page_no = None
        self._page_size = None
        self._results = None
        self._status = None
        self._version_uri = None
        self._release_dev = None
        self._sort_field = None
        self._sort_type = None
        self._feature_uri = None
        self._task_result_uri = None
        self._rank_ids = None
        self._key_word = None
        self._issue_id = None
        self._associated_issue = None
        self._select_all_pages = None
        self._is_available = None
        self._is_script_exist = None
        self.discriminator = None

        if stage is not None:
            self.stage = stage
        if owners is not None:
            self.owners = owners
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if results is not None:
            self.results = results
        if status is not None:
            self.status = status
        if version_uri is not None:
            self.version_uri = version_uri
        if release_dev is not None:
            self.release_dev = release_dev
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if feature_uri is not None:
            self.feature_uri = feature_uri
        if task_result_uri is not None:
            self.task_result_uri = task_result_uri
        if rank_ids is not None:
            self.rank_ids = rank_ids
        if key_word is not None:
            self.key_word = key_word
        if issue_id is not None:
            self.issue_id = issue_id
        if associated_issue is not None:
            self.associated_issue = associated_issue
        if select_all_pages is not None:
            self.select_all_pages = select_all_pages
        if is_available is not None:
            self.is_available = is_available
        if is_script_exist is not None:
            self.is_script_exist = is_script_exist

    @property
    def stage(self):
        r"""Gets the stage of this QueryTaskAssignCasesInfo.

        测试用例在任务中的阶段

        :return: The stage of this QueryTaskAssignCasesInfo.
        :rtype: int
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this QueryTaskAssignCasesInfo.

        测试用例在任务中的阶段

        :param stage: The stage of this QueryTaskAssignCasesInfo.
        :type stage: int
        """
        self._stage = stage

    @property
    def owners(self):
        r"""Gets the owners of this QueryTaskAssignCasesInfo.

        处理人过滤数组

        :return: The owners of this QueryTaskAssignCasesInfo.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        r"""Sets the owners of this QueryTaskAssignCasesInfo.

        处理人过滤数组

        :param owners: The owners of this QueryTaskAssignCasesInfo.
        :type owners: list[str]
        """
        self._owners = owners

    @property
    def page_no(self):
        r"""Gets the page_no of this QueryTaskAssignCasesInfo.

        页码

        :return: The page_no of this QueryTaskAssignCasesInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this QueryTaskAssignCasesInfo.

        页码

        :param page_no: The page_no of this QueryTaskAssignCasesInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this QueryTaskAssignCasesInfo.

        页数量

        :return: The page_size of this QueryTaskAssignCasesInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this QueryTaskAssignCasesInfo.

        页数量

        :param page_size: The page_size of this QueryTaskAssignCasesInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def results(self):
        r"""Gets the results of this QueryTaskAssignCasesInfo.

        结果过滤

        :return: The results of this QueryTaskAssignCasesInfo.
        :rtype: list[str]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this QueryTaskAssignCasesInfo.

        结果过滤

        :param results: The results of this QueryTaskAssignCasesInfo.
        :type results: list[str]
        """
        self._results = results

    @property
    def status(self):
        r"""Gets the status of this QueryTaskAssignCasesInfo.

        状态过滤

        :return: The status of this QueryTaskAssignCasesInfo.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryTaskAssignCasesInfo.

        状态过滤

        :param status: The status of this QueryTaskAssignCasesInfo.
        :type status: list[str]
        """
        self._status = status

    @property
    def version_uri(self):
        r"""Gets the version_uri of this QueryTaskAssignCasesInfo.

        分支/迭代uri

        :return: The version_uri of this QueryTaskAssignCasesInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this QueryTaskAssignCasesInfo.

        分支/迭代uri

        :param version_uri: The version_uri of this QueryTaskAssignCasesInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def release_dev(self):
        r"""Gets the release_dev of this QueryTaskAssignCasesInfo.

        任务版本过滤条件，影响关联任务的结果查询，查询当前任务版本下的用例最新结果

        :return: The release_dev of this QueryTaskAssignCasesInfo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this QueryTaskAssignCasesInfo.

        任务版本过滤条件，影响关联任务的结果查询，查询当前任务版本下的用例最新结果

        :param release_dev: The release_dev of this QueryTaskAssignCasesInfo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def sort_field(self):
        r"""Gets the sort_field of this QueryTaskAssignCasesInfo.

        排序字段

        :return: The sort_field of this QueryTaskAssignCasesInfo.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this QueryTaskAssignCasesInfo.

        排序字段

        :param sort_field: The sort_field of this QueryTaskAssignCasesInfo.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this QueryTaskAssignCasesInfo.

        排序方法

        :return: The sort_type of this QueryTaskAssignCasesInfo.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this QueryTaskAssignCasesInfo.

        排序方法

        :param sort_type: The sort_type of this QueryTaskAssignCasesInfo.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def feature_uri(self):
        r"""Gets the feature_uri of this QueryTaskAssignCasesInfo.

        特性目录URI

        :return: The feature_uri of this QueryTaskAssignCasesInfo.
        :rtype: str
        """
        return self._feature_uri

    @feature_uri.setter
    def feature_uri(self, feature_uri):
        r"""Sets the feature_uri of this QueryTaskAssignCasesInfo.

        特性目录URI

        :param feature_uri: The feature_uri of this QueryTaskAssignCasesInfo.
        :type feature_uri: str
        """
        self._feature_uri = feature_uri

    @property
    def task_result_uri(self):
        r"""Gets the task_result_uri of this QueryTaskAssignCasesInfo.

        测试套结果uri

        :return: The task_result_uri of this QueryTaskAssignCasesInfo.
        :rtype: str
        """
        return self._task_result_uri

    @task_result_uri.setter
    def task_result_uri(self, task_result_uri):
        r"""Sets the task_result_uri of this QueryTaskAssignCasesInfo.

        测试套结果uri

        :param task_result_uri: The task_result_uri of this QueryTaskAssignCasesInfo.
        :type task_result_uri: str
        """
        self._task_result_uri = task_result_uri

    @property
    def rank_ids(self):
        r"""Gets the rank_ids of this QueryTaskAssignCasesInfo.

        用例等级ID集合

        :return: The rank_ids of this QueryTaskAssignCasesInfo.
        :rtype: list[int]
        """
        return self._rank_ids

    @rank_ids.setter
    def rank_ids(self, rank_ids):
        r"""Sets the rank_ids of this QueryTaskAssignCasesInfo.

        用例等级ID集合

        :param rank_ids: The rank_ids of this QueryTaskAssignCasesInfo.
        :type rank_ids: list[int]
        """
        self._rank_ids = rank_ids

    @property
    def key_word(self):
        r"""Gets the key_word of this QueryTaskAssignCasesInfo.

        关键字

        :return: The key_word of this QueryTaskAssignCasesInfo.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        r"""Sets the key_word of this QueryTaskAssignCasesInfo.

        关键字

        :param key_word: The key_word of this QueryTaskAssignCasesInfo.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def issue_id(self):
        r"""Gets the issue_id of this QueryTaskAssignCasesInfo.

        需求id

        :return: The issue_id of this QueryTaskAssignCasesInfo.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this QueryTaskAssignCasesInfo.

        需求id

        :param issue_id: The issue_id of this QueryTaskAssignCasesInfo.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def associated_issue(self):
        r"""Gets the associated_issue of this QueryTaskAssignCasesInfo.

        是否关联需求（null：不限，false：未关联，true：已关联）

        :return: The associated_issue of this QueryTaskAssignCasesInfo.
        :rtype: bool
        """
        return self._associated_issue

    @associated_issue.setter
    def associated_issue(self, associated_issue):
        r"""Sets the associated_issue of this QueryTaskAssignCasesInfo.

        是否关联需求（null：不限，false：未关联，true：已关联）

        :param associated_issue: The associated_issue of this QueryTaskAssignCasesInfo.
        :type associated_issue: bool
        """
        self._associated_issue = associated_issue

    @property
    def select_all_pages(self):
        r"""Gets the select_all_pages of this QueryTaskAssignCasesInfo.

        是否全选所有页（null：不全选，false：不全选，true：全选），用于任务批量执行结果功能，只返回用例uri，不返回其他信息

        :return: The select_all_pages of this QueryTaskAssignCasesInfo.
        :rtype: bool
        """
        return self._select_all_pages

    @select_all_pages.setter
    def select_all_pages(self, select_all_pages):
        r"""Sets the select_all_pages of this QueryTaskAssignCasesInfo.

        是否全选所有页（null：不全选，false：不全选，true：全选），用于任务批量执行结果功能，只返回用例uri，不返回其他信息

        :param select_all_pages: The select_all_pages of this QueryTaskAssignCasesInfo.
        :type select_all_pages: bool
        """
        self._select_all_pages = select_all_pages

    @property
    def is_available(self):
        r"""Gets the is_available of this QueryTaskAssignCasesInfo.

        用例是否可用

        :return: The is_available of this QueryTaskAssignCasesInfo.
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        r"""Sets the is_available of this QueryTaskAssignCasesInfo.

        用例是否可用

        :param is_available: The is_available of this QueryTaskAssignCasesInfo.
        :type is_available: bool
        """
        self._is_available = is_available

    @property
    def is_script_exist(self):
        r"""Gets the is_script_exist of this QueryTaskAssignCasesInfo.

        用例脚本字段是否有值

        :return: The is_script_exist of this QueryTaskAssignCasesInfo.
        :rtype: bool
        """
        return self._is_script_exist

    @is_script_exist.setter
    def is_script_exist(self, is_script_exist):
        r"""Sets the is_script_exist of this QueryTaskAssignCasesInfo.

        用例脚本字段是否有值

        :param is_script_exist: The is_script_exist of this QueryTaskAssignCasesInfo.
        :type is_script_exist: bool
        """
        self._is_script_exist = is_script_exist

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
        if not isinstance(other, QueryTaskAssignCasesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
