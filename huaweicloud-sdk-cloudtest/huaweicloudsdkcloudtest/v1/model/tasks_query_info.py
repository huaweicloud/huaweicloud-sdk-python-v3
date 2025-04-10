# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TasksQueryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uris': 'list[str]',
        'keyword': 'str',
        'tags': 'list[str]',
        'own': 'bool',
        'service_type': 'int',
        'release_dev_list': 'list[str]',
        'result_codes': 'list[str]',
        'status_codes': 'list[str]',
        'owner_ids': 'list[str]',
        'executor_ids': 'list[str]',
        'creator_ids': 'list[str]',
        'sort_field': 'str',
        'sort_type': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'is_polling_query': 'bool',
        'is_query_associated_case_list': 'bool',
        'plan_start_start_timestamp': 'int',
        'plan_start_end_timestamp': 'int',
        'plan_end_start_timestamp': 'int',
        'plan_end_end_timestamp': 'int',
        'expiration_status_list': 'list[int]'
    }

    attribute_map = {
        'uris': 'uris',
        'keyword': 'keyword',
        'tags': 'tags',
        'own': 'own',
        'service_type': 'service_type',
        'release_dev_list': 'release_dev_list',
        'result_codes': 'result_codes',
        'status_codes': 'status_codes',
        'owner_ids': 'owner_ids',
        'executor_ids': 'executor_ids',
        'creator_ids': 'creator_ids',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'is_polling_query': 'is_polling_query',
        'is_query_associated_case_list': 'is_query_associated_case_list',
        'plan_start_start_timestamp': 'plan_start_start_timestamp',
        'plan_start_end_timestamp': 'plan_start_end_timestamp',
        'plan_end_start_timestamp': 'plan_end_start_timestamp',
        'plan_end_end_timestamp': 'plan_end_end_timestamp',
        'expiration_status_list': 'expiration_status_list'
    }

    def __init__(self, uris=None, keyword=None, tags=None, own=None, service_type=None, release_dev_list=None, result_codes=None, status_codes=None, owner_ids=None, executor_ids=None, creator_ids=None, sort_field=None, sort_type=None, page_no=None, page_size=None, is_polling_query=None, is_query_associated_case_list=None, plan_start_start_timestamp=None, plan_start_end_timestamp=None, plan_end_start_timestamp=None, plan_end_end_timestamp=None, expiration_status_list=None):
        r"""TasksQueryInfo

        The model defined in huaweicloud sdk

        :param uris: 测试任务URI集合
        :type uris: list[str]
        :param keyword: 关键字查询，任务名或编号
        :type keyword: str
        :param tags: 标签集合
        :type tags: list[str]
        :param own: 是否是我的
        :type own: bool
        :param service_type: 服务类型
        :type service_type: int
        :param release_dev_list: 发布版本号集合
        :type release_dev_list: list[str]
        :param result_codes: 结果Code集合
        :type result_codes: list[str]
        :param status_codes: 状态Code集合
        :type status_codes: list[str]
        :param owner_ids: 责任人ID集合
        :type owner_ids: list[str]
        :param executor_ids: 执行者ID集合
        :type executor_ids: list[str]
        :param creator_ids: 创建者ID集合
        :type creator_ids: list[str]
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_type: 排序方式
        :type sort_type: str
        :param page_no: 当前页数
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        :param is_polling_query: 是否轮询查询
        :type is_polling_query: bool
        :param is_query_associated_case_list: 是否获取关联用例列表
        :type is_query_associated_case_list: bool
        :param plan_start_start_timestamp: 计划开始时间过滤起始时间戳
        :type plan_start_start_timestamp: int
        :param plan_start_end_timestamp: 计划开始时间过滤结束时间戳
        :type plan_start_end_timestamp: int
        :param plan_end_start_timestamp: 计划结束时间过滤起始时间戳
        :type plan_end_start_timestamp: int
        :param plan_end_end_timestamp: 计划结束时间过滤结束时间戳
        :type plan_end_end_timestamp: int
        :param expiration_status_list: 测试套超期状态过滤，超期状态值分别为：无状态(null)、未超期(0)、即将超期(1)、已超期(2)、延期完成(3)、按期完成(4)
        :type expiration_status_list: list[int]
        """
        
        

        self._uris = None
        self._keyword = None
        self._tags = None
        self._own = None
        self._service_type = None
        self._release_dev_list = None
        self._result_codes = None
        self._status_codes = None
        self._owner_ids = None
        self._executor_ids = None
        self._creator_ids = None
        self._sort_field = None
        self._sort_type = None
        self._page_no = None
        self._page_size = None
        self._is_polling_query = None
        self._is_query_associated_case_list = None
        self._plan_start_start_timestamp = None
        self._plan_start_end_timestamp = None
        self._plan_end_start_timestamp = None
        self._plan_end_end_timestamp = None
        self._expiration_status_list = None
        self.discriminator = None

        if uris is not None:
            self.uris = uris
        if keyword is not None:
            self.keyword = keyword
        if tags is not None:
            self.tags = tags
        if own is not None:
            self.own = own
        if service_type is not None:
            self.service_type = service_type
        if release_dev_list is not None:
            self.release_dev_list = release_dev_list
        if result_codes is not None:
            self.result_codes = result_codes
        if status_codes is not None:
            self.status_codes = status_codes
        if owner_ids is not None:
            self.owner_ids = owner_ids
        if executor_ids is not None:
            self.executor_ids = executor_ids
        if creator_ids is not None:
            self.creator_ids = creator_ids
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if is_polling_query is not None:
            self.is_polling_query = is_polling_query
        if is_query_associated_case_list is not None:
            self.is_query_associated_case_list = is_query_associated_case_list
        if plan_start_start_timestamp is not None:
            self.plan_start_start_timestamp = plan_start_start_timestamp
        if plan_start_end_timestamp is not None:
            self.plan_start_end_timestamp = plan_start_end_timestamp
        if plan_end_start_timestamp is not None:
            self.plan_end_start_timestamp = plan_end_start_timestamp
        if plan_end_end_timestamp is not None:
            self.plan_end_end_timestamp = plan_end_end_timestamp
        if expiration_status_list is not None:
            self.expiration_status_list = expiration_status_list

    @property
    def uris(self):
        r"""Gets the uris of this TasksQueryInfo.

        测试任务URI集合

        :return: The uris of this TasksQueryInfo.
        :rtype: list[str]
        """
        return self._uris

    @uris.setter
    def uris(self, uris):
        r"""Sets the uris of this TasksQueryInfo.

        测试任务URI集合

        :param uris: The uris of this TasksQueryInfo.
        :type uris: list[str]
        """
        self._uris = uris

    @property
    def keyword(self):
        r"""Gets the keyword of this TasksQueryInfo.

        关键字查询，任务名或编号

        :return: The keyword of this TasksQueryInfo.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this TasksQueryInfo.

        关键字查询，任务名或编号

        :param keyword: The keyword of this TasksQueryInfo.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def tags(self):
        r"""Gets the tags of this TasksQueryInfo.

        标签集合

        :return: The tags of this TasksQueryInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TasksQueryInfo.

        标签集合

        :param tags: The tags of this TasksQueryInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def own(self):
        r"""Gets the own of this TasksQueryInfo.

        是否是我的

        :return: The own of this TasksQueryInfo.
        :rtype: bool
        """
        return self._own

    @own.setter
    def own(self, own):
        r"""Sets the own of this TasksQueryInfo.

        是否是我的

        :param own: The own of this TasksQueryInfo.
        :type own: bool
        """
        self._own = own

    @property
    def service_type(self):
        r"""Gets the service_type of this TasksQueryInfo.

        服务类型

        :return: The service_type of this TasksQueryInfo.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this TasksQueryInfo.

        服务类型

        :param service_type: The service_type of this TasksQueryInfo.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def release_dev_list(self):
        r"""Gets the release_dev_list of this TasksQueryInfo.

        发布版本号集合

        :return: The release_dev_list of this TasksQueryInfo.
        :rtype: list[str]
        """
        return self._release_dev_list

    @release_dev_list.setter
    def release_dev_list(self, release_dev_list):
        r"""Sets the release_dev_list of this TasksQueryInfo.

        发布版本号集合

        :param release_dev_list: The release_dev_list of this TasksQueryInfo.
        :type release_dev_list: list[str]
        """
        self._release_dev_list = release_dev_list

    @property
    def result_codes(self):
        r"""Gets the result_codes of this TasksQueryInfo.

        结果Code集合

        :return: The result_codes of this TasksQueryInfo.
        :rtype: list[str]
        """
        return self._result_codes

    @result_codes.setter
    def result_codes(self, result_codes):
        r"""Sets the result_codes of this TasksQueryInfo.

        结果Code集合

        :param result_codes: The result_codes of this TasksQueryInfo.
        :type result_codes: list[str]
        """
        self._result_codes = result_codes

    @property
    def status_codes(self):
        r"""Gets the status_codes of this TasksQueryInfo.

        状态Code集合

        :return: The status_codes of this TasksQueryInfo.
        :rtype: list[str]
        """
        return self._status_codes

    @status_codes.setter
    def status_codes(self, status_codes):
        r"""Sets the status_codes of this TasksQueryInfo.

        状态Code集合

        :param status_codes: The status_codes of this TasksQueryInfo.
        :type status_codes: list[str]
        """
        self._status_codes = status_codes

    @property
    def owner_ids(self):
        r"""Gets the owner_ids of this TasksQueryInfo.

        责任人ID集合

        :return: The owner_ids of this TasksQueryInfo.
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        r"""Sets the owner_ids of this TasksQueryInfo.

        责任人ID集合

        :param owner_ids: The owner_ids of this TasksQueryInfo.
        :type owner_ids: list[str]
        """
        self._owner_ids = owner_ids

    @property
    def executor_ids(self):
        r"""Gets the executor_ids of this TasksQueryInfo.

        执行者ID集合

        :return: The executor_ids of this TasksQueryInfo.
        :rtype: list[str]
        """
        return self._executor_ids

    @executor_ids.setter
    def executor_ids(self, executor_ids):
        r"""Sets the executor_ids of this TasksQueryInfo.

        执行者ID集合

        :param executor_ids: The executor_ids of this TasksQueryInfo.
        :type executor_ids: list[str]
        """
        self._executor_ids = executor_ids

    @property
    def creator_ids(self):
        r"""Gets the creator_ids of this TasksQueryInfo.

        创建者ID集合

        :return: The creator_ids of this TasksQueryInfo.
        :rtype: list[str]
        """
        return self._creator_ids

    @creator_ids.setter
    def creator_ids(self, creator_ids):
        r"""Sets the creator_ids of this TasksQueryInfo.

        创建者ID集合

        :param creator_ids: The creator_ids of this TasksQueryInfo.
        :type creator_ids: list[str]
        """
        self._creator_ids = creator_ids

    @property
    def sort_field(self):
        r"""Gets the sort_field of this TasksQueryInfo.

        排序字段

        :return: The sort_field of this TasksQueryInfo.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this TasksQueryInfo.

        排序字段

        :param sort_field: The sort_field of this TasksQueryInfo.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this TasksQueryInfo.

        排序方式

        :return: The sort_type of this TasksQueryInfo.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this TasksQueryInfo.

        排序方式

        :param sort_type: The sort_type of this TasksQueryInfo.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def page_no(self):
        r"""Gets the page_no of this TasksQueryInfo.

        当前页数

        :return: The page_no of this TasksQueryInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this TasksQueryInfo.

        当前页数

        :param page_no: The page_no of this TasksQueryInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this TasksQueryInfo.

        每页条数

        :return: The page_size of this TasksQueryInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this TasksQueryInfo.

        每页条数

        :param page_size: The page_size of this TasksQueryInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def is_polling_query(self):
        r"""Gets the is_polling_query of this TasksQueryInfo.

        是否轮询查询

        :return: The is_polling_query of this TasksQueryInfo.
        :rtype: bool
        """
        return self._is_polling_query

    @is_polling_query.setter
    def is_polling_query(self, is_polling_query):
        r"""Sets the is_polling_query of this TasksQueryInfo.

        是否轮询查询

        :param is_polling_query: The is_polling_query of this TasksQueryInfo.
        :type is_polling_query: bool
        """
        self._is_polling_query = is_polling_query

    @property
    def is_query_associated_case_list(self):
        r"""Gets the is_query_associated_case_list of this TasksQueryInfo.

        是否获取关联用例列表

        :return: The is_query_associated_case_list of this TasksQueryInfo.
        :rtype: bool
        """
        return self._is_query_associated_case_list

    @is_query_associated_case_list.setter
    def is_query_associated_case_list(self, is_query_associated_case_list):
        r"""Sets the is_query_associated_case_list of this TasksQueryInfo.

        是否获取关联用例列表

        :param is_query_associated_case_list: The is_query_associated_case_list of this TasksQueryInfo.
        :type is_query_associated_case_list: bool
        """
        self._is_query_associated_case_list = is_query_associated_case_list

    @property
    def plan_start_start_timestamp(self):
        r"""Gets the plan_start_start_timestamp of this TasksQueryInfo.

        计划开始时间过滤起始时间戳

        :return: The plan_start_start_timestamp of this TasksQueryInfo.
        :rtype: int
        """
        return self._plan_start_start_timestamp

    @plan_start_start_timestamp.setter
    def plan_start_start_timestamp(self, plan_start_start_timestamp):
        r"""Sets the plan_start_start_timestamp of this TasksQueryInfo.

        计划开始时间过滤起始时间戳

        :param plan_start_start_timestamp: The plan_start_start_timestamp of this TasksQueryInfo.
        :type plan_start_start_timestamp: int
        """
        self._plan_start_start_timestamp = plan_start_start_timestamp

    @property
    def plan_start_end_timestamp(self):
        r"""Gets the plan_start_end_timestamp of this TasksQueryInfo.

        计划开始时间过滤结束时间戳

        :return: The plan_start_end_timestamp of this TasksQueryInfo.
        :rtype: int
        """
        return self._plan_start_end_timestamp

    @plan_start_end_timestamp.setter
    def plan_start_end_timestamp(self, plan_start_end_timestamp):
        r"""Sets the plan_start_end_timestamp of this TasksQueryInfo.

        计划开始时间过滤结束时间戳

        :param plan_start_end_timestamp: The plan_start_end_timestamp of this TasksQueryInfo.
        :type plan_start_end_timestamp: int
        """
        self._plan_start_end_timestamp = plan_start_end_timestamp

    @property
    def plan_end_start_timestamp(self):
        r"""Gets the plan_end_start_timestamp of this TasksQueryInfo.

        计划结束时间过滤起始时间戳

        :return: The plan_end_start_timestamp of this TasksQueryInfo.
        :rtype: int
        """
        return self._plan_end_start_timestamp

    @plan_end_start_timestamp.setter
    def plan_end_start_timestamp(self, plan_end_start_timestamp):
        r"""Sets the plan_end_start_timestamp of this TasksQueryInfo.

        计划结束时间过滤起始时间戳

        :param plan_end_start_timestamp: The plan_end_start_timestamp of this TasksQueryInfo.
        :type plan_end_start_timestamp: int
        """
        self._plan_end_start_timestamp = plan_end_start_timestamp

    @property
    def plan_end_end_timestamp(self):
        r"""Gets the plan_end_end_timestamp of this TasksQueryInfo.

        计划结束时间过滤结束时间戳

        :return: The plan_end_end_timestamp of this TasksQueryInfo.
        :rtype: int
        """
        return self._plan_end_end_timestamp

    @plan_end_end_timestamp.setter
    def plan_end_end_timestamp(self, plan_end_end_timestamp):
        r"""Sets the plan_end_end_timestamp of this TasksQueryInfo.

        计划结束时间过滤结束时间戳

        :param plan_end_end_timestamp: The plan_end_end_timestamp of this TasksQueryInfo.
        :type plan_end_end_timestamp: int
        """
        self._plan_end_end_timestamp = plan_end_end_timestamp

    @property
    def expiration_status_list(self):
        r"""Gets the expiration_status_list of this TasksQueryInfo.

        测试套超期状态过滤，超期状态值分别为：无状态(null)、未超期(0)、即将超期(1)、已超期(2)、延期完成(3)、按期完成(4)

        :return: The expiration_status_list of this TasksQueryInfo.
        :rtype: list[int]
        """
        return self._expiration_status_list

    @expiration_status_list.setter
    def expiration_status_list(self, expiration_status_list):
        r"""Sets the expiration_status_list of this TasksQueryInfo.

        测试套超期状态过滤，超期状态值分别为：无状态(null)、未超期(0)、即将超期(1)、已超期(2)、延期完成(3)、按期完成(4)

        :param expiration_status_list: The expiration_status_list of this TasksQueryInfo.
        :type expiration_status_list: list[int]
        """
        self._expiration_status_list = expiration_status_list

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
        if not isinstance(other, TasksQueryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
