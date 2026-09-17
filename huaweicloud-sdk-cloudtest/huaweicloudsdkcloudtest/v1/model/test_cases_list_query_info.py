# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCasesListQueryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_uri': 'str',
        'case_uris': 'list[str]',
        'owner_ids': 'list[str]',
        'status_codes': 'list[str]',
        'rank_ids': 'list[str]',
        'module_ids': 'list[str]',
        'keyword': 'str',
        'name': 'str',
        'number': 'str',
        'sort_field': 'str',
        'sort_type': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'service_type': 'int',
        'stage_type': 'int',
        'feature_uri': 'str'
    }

    attribute_map = {
        'version_uri': 'version_uri',
        'case_uris': 'case_uris',
        'owner_ids': 'owner_ids',
        'status_codes': 'status_codes',
        'rank_ids': 'rank_ids',
        'module_ids': 'module_ids',
        'keyword': 'keyword',
        'name': 'name',
        'number': 'number',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'service_type': 'service_type',
        'stage_type': 'stage_type',
        'feature_uri': 'feature_uri'
    }

    def __init__(self, version_uri=None, case_uris=None, owner_ids=None, status_codes=None, rank_ids=None, module_ids=None, keyword=None, name=None, number=None, sort_field=None, sort_type=None, page_no=None, page_size=None, service_type=None, stage_type=None, feature_uri=None):
        r"""TestCasesListQueryInfo

        The model defined in huaweicloud sdk

        :param version_uri: 版本URI
        :type version_uri: str
        :param case_uris: 用例URI集合
        :type case_uris: list[str]
        :param owner_ids: 处理者ID集合
        :type owner_ids: list[str]
        :param status_codes: 状态Code集合
        :type status_codes: list[str]
        :param rank_ids: 用例等级ID集合
        :type rank_ids: list[str]
        :param module_ids: 模块ID集合
        :type module_ids: list[str]
        :param keyword: 关键字查询，用例名或编号
        :type keyword: str
        :param name: 用例名称
        :type name: str
        :param number: 用例编号
        :type number: str
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_type: 排序方式
        :type sort_type: str
        :param page_no: 当前页数
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        :param service_type: 服务类型
        :type service_type: int
        :param stage_type: 阶段过程（2：测试设计，3：测试执行，4：质量报告）
        :type stage_type: int
        :param feature_uri: 目录URI
        :type feature_uri: str
        """
        
        

        self._version_uri = None
        self._case_uris = None
        self._owner_ids = None
        self._status_codes = None
        self._rank_ids = None
        self._module_ids = None
        self._keyword = None
        self._name = None
        self._number = None
        self._sort_field = None
        self._sort_type = None
        self._page_no = None
        self._page_size = None
        self._service_type = None
        self._stage_type = None
        self._feature_uri = None
        self.discriminator = None

        if version_uri is not None:
            self.version_uri = version_uri
        if case_uris is not None:
            self.case_uris = case_uris
        if owner_ids is not None:
            self.owner_ids = owner_ids
        if status_codes is not None:
            self.status_codes = status_codes
        if rank_ids is not None:
            self.rank_ids = rank_ids
        if module_ids is not None:
            self.module_ids = module_ids
        if keyword is not None:
            self.keyword = keyword
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if service_type is not None:
            self.service_type = service_type
        if stage_type is not None:
            self.stage_type = stage_type
        if feature_uri is not None:
            self.feature_uri = feature_uri

    @property
    def version_uri(self):
        r"""Gets the version_uri of this TestCasesListQueryInfo.

        版本URI

        :return: The version_uri of this TestCasesListQueryInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this TestCasesListQueryInfo.

        版本URI

        :param version_uri: The version_uri of this TestCasesListQueryInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def case_uris(self):
        r"""Gets the case_uris of this TestCasesListQueryInfo.

        用例URI集合

        :return: The case_uris of this TestCasesListQueryInfo.
        :rtype: list[str]
        """
        return self._case_uris

    @case_uris.setter
    def case_uris(self, case_uris):
        r"""Sets the case_uris of this TestCasesListQueryInfo.

        用例URI集合

        :param case_uris: The case_uris of this TestCasesListQueryInfo.
        :type case_uris: list[str]
        """
        self._case_uris = case_uris

    @property
    def owner_ids(self):
        r"""Gets the owner_ids of this TestCasesListQueryInfo.

        处理者ID集合

        :return: The owner_ids of this TestCasesListQueryInfo.
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        r"""Sets the owner_ids of this TestCasesListQueryInfo.

        处理者ID集合

        :param owner_ids: The owner_ids of this TestCasesListQueryInfo.
        :type owner_ids: list[str]
        """
        self._owner_ids = owner_ids

    @property
    def status_codes(self):
        r"""Gets the status_codes of this TestCasesListQueryInfo.

        状态Code集合

        :return: The status_codes of this TestCasesListQueryInfo.
        :rtype: list[str]
        """
        return self._status_codes

    @status_codes.setter
    def status_codes(self, status_codes):
        r"""Sets the status_codes of this TestCasesListQueryInfo.

        状态Code集合

        :param status_codes: The status_codes of this TestCasesListQueryInfo.
        :type status_codes: list[str]
        """
        self._status_codes = status_codes

    @property
    def rank_ids(self):
        r"""Gets the rank_ids of this TestCasesListQueryInfo.

        用例等级ID集合

        :return: The rank_ids of this TestCasesListQueryInfo.
        :rtype: list[str]
        """
        return self._rank_ids

    @rank_ids.setter
    def rank_ids(self, rank_ids):
        r"""Sets the rank_ids of this TestCasesListQueryInfo.

        用例等级ID集合

        :param rank_ids: The rank_ids of this TestCasesListQueryInfo.
        :type rank_ids: list[str]
        """
        self._rank_ids = rank_ids

    @property
    def module_ids(self):
        r"""Gets the module_ids of this TestCasesListQueryInfo.

        模块ID集合

        :return: The module_ids of this TestCasesListQueryInfo.
        :rtype: list[str]
        """
        return self._module_ids

    @module_ids.setter
    def module_ids(self, module_ids):
        r"""Sets the module_ids of this TestCasesListQueryInfo.

        模块ID集合

        :param module_ids: The module_ids of this TestCasesListQueryInfo.
        :type module_ids: list[str]
        """
        self._module_ids = module_ids

    @property
    def keyword(self):
        r"""Gets the keyword of this TestCasesListQueryInfo.

        关键字查询，用例名或编号

        :return: The keyword of this TestCasesListQueryInfo.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this TestCasesListQueryInfo.

        关键字查询，用例名或编号

        :param keyword: The keyword of this TestCasesListQueryInfo.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def name(self):
        r"""Gets the name of this TestCasesListQueryInfo.

        用例名称

        :return: The name of this TestCasesListQueryInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TestCasesListQueryInfo.

        用例名称

        :param name: The name of this TestCasesListQueryInfo.
        :type name: str
        """
        self._name = name

    @property
    def number(self):
        r"""Gets the number of this TestCasesListQueryInfo.

        用例编号

        :return: The number of this TestCasesListQueryInfo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this TestCasesListQueryInfo.

        用例编号

        :param number: The number of this TestCasesListQueryInfo.
        :type number: str
        """
        self._number = number

    @property
    def sort_field(self):
        r"""Gets the sort_field of this TestCasesListQueryInfo.

        排序字段

        :return: The sort_field of this TestCasesListQueryInfo.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this TestCasesListQueryInfo.

        排序字段

        :param sort_field: The sort_field of this TestCasesListQueryInfo.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this TestCasesListQueryInfo.

        排序方式

        :return: The sort_type of this TestCasesListQueryInfo.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this TestCasesListQueryInfo.

        排序方式

        :param sort_type: The sort_type of this TestCasesListQueryInfo.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def page_no(self):
        r"""Gets the page_no of this TestCasesListQueryInfo.

        当前页数

        :return: The page_no of this TestCasesListQueryInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this TestCasesListQueryInfo.

        当前页数

        :param page_no: The page_no of this TestCasesListQueryInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this TestCasesListQueryInfo.

        每页条数

        :return: The page_size of this TestCasesListQueryInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this TestCasesListQueryInfo.

        每页条数

        :param page_size: The page_size of this TestCasesListQueryInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def service_type(self):
        r"""Gets the service_type of this TestCasesListQueryInfo.

        服务类型

        :return: The service_type of this TestCasesListQueryInfo.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this TestCasesListQueryInfo.

        服务类型

        :param service_type: The service_type of this TestCasesListQueryInfo.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def stage_type(self):
        r"""Gets the stage_type of this TestCasesListQueryInfo.

        阶段过程（2：测试设计，3：测试执行，4：质量报告）

        :return: The stage_type of this TestCasesListQueryInfo.
        :rtype: int
        """
        return self._stage_type

    @stage_type.setter
    def stage_type(self, stage_type):
        r"""Sets the stage_type of this TestCasesListQueryInfo.

        阶段过程（2：测试设计，3：测试执行，4：质量报告）

        :param stage_type: The stage_type of this TestCasesListQueryInfo.
        :type stage_type: int
        """
        self._stage_type = stage_type

    @property
    def feature_uri(self):
        r"""Gets the feature_uri of this TestCasesListQueryInfo.

        目录URI

        :return: The feature_uri of this TestCasesListQueryInfo.
        :rtype: str
        """
        return self._feature_uri

    @feature_uri.setter
    def feature_uri(self, feature_uri):
        r"""Sets the feature_uri of this TestCasesListQueryInfo.

        目录URI

        :param feature_uri: The feature_uri of this TestCasesListQueryInfo.
        :type feature_uri: str
        """
        self._feature_uri = feature_uri

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
        if not isinstance(other, TestCasesListQueryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
