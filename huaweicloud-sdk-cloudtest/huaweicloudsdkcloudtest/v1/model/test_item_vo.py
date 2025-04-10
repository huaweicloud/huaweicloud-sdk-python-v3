# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestItemVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'type': 'str',
        'author': 'str',
        'name': 'str',
        'rank': 'int',
        'owner': 'str',
        'frequence': 'str',
        'region': 'str',
        'last_modifier': 'str',
        'last_modified': 'datetime',
        'last_modified_timestamp': 'int',
        'last_change_time': 'datetime',
        'version_uri': 'str',
        'origin_uri': 'str',
        'parent_uri': 'str',
        'parent_path': 'str',
        'creation_version_uri': 'str',
        'creation_date': 'datetime',
        'creation_date_timestamp': 'int',
        'author_name': 'str',
        'comment': 'str',
        'number': 'str',
        'is_feature': 'str',
        'relate_htsm': 'str',
        'aw_unique_id': 'str',
        'test_mind_id': 'str',
        'test_mind_url': 'str',
        'project_uuid': 'str',
        'case_total': 'int',
        'execd_total': 'int',
        'is_direct_relation': 'bool',
        'has_child': 'bool'
    }

    attribute_map = {
        'uri': 'uri',
        'type': 'type',
        'author': 'author',
        'name': 'name',
        'rank': 'rank',
        'owner': 'owner',
        'frequence': 'frequence',
        'region': 'region',
        'last_modifier': 'last_modifier',
        'last_modified': 'last_modified',
        'last_modified_timestamp': 'last_modified_timestamp',
        'last_change_time': 'last_change_time',
        'version_uri': 'version_uri',
        'origin_uri': 'origin_uri',
        'parent_uri': 'parent_uri',
        'parent_path': 'parent_path',
        'creation_version_uri': 'creation_version_uri',
        'creation_date': 'creation_date',
        'creation_date_timestamp': 'creation_date_timestamp',
        'author_name': 'author_name',
        'comment': 'comment',
        'number': 'number',
        'is_feature': 'is_feature',
        'relate_htsm': 'relate_htsm',
        'aw_unique_id': 'aw_unique_id',
        'test_mind_id': 'test_mind_id',
        'test_mind_url': 'test_mind_url',
        'project_uuid': 'project_uuid',
        'case_total': 'case_total',
        'execd_total': 'execd_total',
        'is_direct_relation': 'is_direct_relation',
        'has_child': 'has_child'
    }

    def __init__(self, uri=None, type=None, author=None, name=None, rank=None, owner=None, frequence=None, region=None, last_modifier=None, last_modified=None, last_modified_timestamp=None, last_change_time=None, version_uri=None, origin_uri=None, parent_uri=None, parent_path=None, creation_version_uri=None, creation_date=None, creation_date_timestamp=None, author_name=None, comment=None, number=None, is_feature=None, relate_htsm=None, aw_unique_id=None, test_mind_id=None, test_mind_url=None, project_uuid=None, case_total=None, execd_total=None, is_direct_relation=None, has_child=None):
        r"""TestItemVo

        The model defined in huaweicloud sdk

        :param uri: 资源URI
        :type uri: str
        :param type: 资源类型
        :type type: str
        :param author: 创建人
        :type author: str
        :param name: 名称
        :type name: str
        :param rank: 级别
        :type rank: int
        :param owner: 责任人
        :type owner: str
        :param frequence: frequence值
        :type frequence: str
        :param region: 区域
        :type region: str
        :param last_modifier: 最后修改人
        :type last_modifier: str
        :param last_modified: 最后修改时间
        :type last_modified: datetime
        :param last_modified_timestamp: 修改时间时间戳
        :type last_modified_timestamp: int
        :param last_change_time: 最后变更时间
        :type last_change_time: datetime
        :param version_uri: 版本URI
        :type version_uri: str
        :param origin_uri: 源资源URI
        :type origin_uri: str
        :param parent_uri: 父资源URI
        :type parent_uri: str
        :param parent_path: 父资源路径
        :type parent_path: str
        :param creation_version_uri: 创建版本URI
        :type creation_version_uri: str
        :param creation_date: 创建时间
        :type creation_date: datetime
        :param creation_date_timestamp: 创建时间时间戳
        :type creation_date_timestamp: int
        :param author_name: 创建人名称
        :type author_name: str
        :param comment: 备注
        :type comment: str
        :param number: 编号
        :type number: str
        :param is_feature: 是否特性
        :type is_feature: str
        :param relate_htsm: 是否关联特性
        :type relate_htsm: str
        :param aw_unique_id: aw id
        :type aw_unique_id: str
        :param test_mind_id: 脑图id
        :type test_mind_id: str
        :param test_mind_url: 脑图url
        :type test_mind_url: str
        :param project_uuid: 项目id
        :type project_uuid: str
        :param case_total: 用例总数
        :type case_total: int
        :param execd_total: 执行总数
        :type execd_total: int
        :param is_direct_relation: is_direct_relation
        :type is_direct_relation: bool
        :param has_child: 是否有子特性
        :type has_child: bool
        """
        
        

        self._uri = None
        self._type = None
        self._author = None
        self._name = None
        self._rank = None
        self._owner = None
        self._frequence = None
        self._region = None
        self._last_modifier = None
        self._last_modified = None
        self._last_modified_timestamp = None
        self._last_change_time = None
        self._version_uri = None
        self._origin_uri = None
        self._parent_uri = None
        self._parent_path = None
        self._creation_version_uri = None
        self._creation_date = None
        self._creation_date_timestamp = None
        self._author_name = None
        self._comment = None
        self._number = None
        self._is_feature = None
        self._relate_htsm = None
        self._aw_unique_id = None
        self._test_mind_id = None
        self._test_mind_url = None
        self._project_uuid = None
        self._case_total = None
        self._execd_total = None
        self._is_direct_relation = None
        self._has_child = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if type is not None:
            self.type = type
        if author is not None:
            self.author = author
        if name is not None:
            self.name = name
        if rank is not None:
            self.rank = rank
        if owner is not None:
            self.owner = owner
        if frequence is not None:
            self.frequence = frequence
        if region is not None:
            self.region = region
        if last_modifier is not None:
            self.last_modifier = last_modifier
        if last_modified is not None:
            self.last_modified = last_modified
        if last_modified_timestamp is not None:
            self.last_modified_timestamp = last_modified_timestamp
        if last_change_time is not None:
            self.last_change_time = last_change_time
        if version_uri is not None:
            self.version_uri = version_uri
        if origin_uri is not None:
            self.origin_uri = origin_uri
        if parent_uri is not None:
            self.parent_uri = parent_uri
        if parent_path is not None:
            self.parent_path = parent_path
        if creation_version_uri is not None:
            self.creation_version_uri = creation_version_uri
        if creation_date is not None:
            self.creation_date = creation_date
        if creation_date_timestamp is not None:
            self.creation_date_timestamp = creation_date_timestamp
        if author_name is not None:
            self.author_name = author_name
        if comment is not None:
            self.comment = comment
        if number is not None:
            self.number = number
        if is_feature is not None:
            self.is_feature = is_feature
        if relate_htsm is not None:
            self.relate_htsm = relate_htsm
        if aw_unique_id is not None:
            self.aw_unique_id = aw_unique_id
        if test_mind_id is not None:
            self.test_mind_id = test_mind_id
        if test_mind_url is not None:
            self.test_mind_url = test_mind_url
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if case_total is not None:
            self.case_total = case_total
        if execd_total is not None:
            self.execd_total = execd_total
        if is_direct_relation is not None:
            self.is_direct_relation = is_direct_relation
        if has_child is not None:
            self.has_child = has_child

    @property
    def uri(self):
        r"""Gets the uri of this TestItemVo.

        资源URI

        :return: The uri of this TestItemVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TestItemVo.

        资源URI

        :param uri: The uri of this TestItemVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def type(self):
        r"""Gets the type of this TestItemVo.

        资源类型

        :return: The type of this TestItemVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TestItemVo.

        资源类型

        :param type: The type of this TestItemVo.
        :type type: str
        """
        self._type = type

    @property
    def author(self):
        r"""Gets the author of this TestItemVo.

        创建人

        :return: The author of this TestItemVo.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this TestItemVo.

        创建人

        :param author: The author of this TestItemVo.
        :type author: str
        """
        self._author = author

    @property
    def name(self):
        r"""Gets the name of this TestItemVo.

        名称

        :return: The name of this TestItemVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TestItemVo.

        名称

        :param name: The name of this TestItemVo.
        :type name: str
        """
        self._name = name

    @property
    def rank(self):
        r"""Gets the rank of this TestItemVo.

        级别

        :return: The rank of this TestItemVo.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        r"""Sets the rank of this TestItemVo.

        级别

        :param rank: The rank of this TestItemVo.
        :type rank: int
        """
        self._rank = rank

    @property
    def owner(self):
        r"""Gets the owner of this TestItemVo.

        责任人

        :return: The owner of this TestItemVo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TestItemVo.

        责任人

        :param owner: The owner of this TestItemVo.
        :type owner: str
        """
        self._owner = owner

    @property
    def frequence(self):
        r"""Gets the frequence of this TestItemVo.

        frequence值

        :return: The frequence of this TestItemVo.
        :rtype: str
        """
        return self._frequence

    @frequence.setter
    def frequence(self, frequence):
        r"""Sets the frequence of this TestItemVo.

        frequence值

        :param frequence: The frequence of this TestItemVo.
        :type frequence: str
        """
        self._frequence = frequence

    @property
    def region(self):
        r"""Gets the region of this TestItemVo.

        区域

        :return: The region of this TestItemVo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this TestItemVo.

        区域

        :param region: The region of this TestItemVo.
        :type region: str
        """
        self._region = region

    @property
    def last_modifier(self):
        r"""Gets the last_modifier of this TestItemVo.

        最后修改人

        :return: The last_modifier of this TestItemVo.
        :rtype: str
        """
        return self._last_modifier

    @last_modifier.setter
    def last_modifier(self, last_modifier):
        r"""Sets the last_modifier of this TestItemVo.

        最后修改人

        :param last_modifier: The last_modifier of this TestItemVo.
        :type last_modifier: str
        """
        self._last_modifier = last_modifier

    @property
    def last_modified(self):
        r"""Gets the last_modified of this TestItemVo.

        最后修改时间

        :return: The last_modified of this TestItemVo.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        r"""Sets the last_modified of this TestItemVo.

        最后修改时间

        :param last_modified: The last_modified of this TestItemVo.
        :type last_modified: datetime
        """
        self._last_modified = last_modified

    @property
    def last_modified_timestamp(self):
        r"""Gets the last_modified_timestamp of this TestItemVo.

        修改时间时间戳

        :return: The last_modified_timestamp of this TestItemVo.
        :rtype: int
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(self, last_modified_timestamp):
        r"""Sets the last_modified_timestamp of this TestItemVo.

        修改时间时间戳

        :param last_modified_timestamp: The last_modified_timestamp of this TestItemVo.
        :type last_modified_timestamp: int
        """
        self._last_modified_timestamp = last_modified_timestamp

    @property
    def last_change_time(self):
        r"""Gets the last_change_time of this TestItemVo.

        最后变更时间

        :return: The last_change_time of this TestItemVo.
        :rtype: datetime
        """
        return self._last_change_time

    @last_change_time.setter
    def last_change_time(self, last_change_time):
        r"""Sets the last_change_time of this TestItemVo.

        最后变更时间

        :param last_change_time: The last_change_time of this TestItemVo.
        :type last_change_time: datetime
        """
        self._last_change_time = last_change_time

    @property
    def version_uri(self):
        r"""Gets the version_uri of this TestItemVo.

        版本URI

        :return: The version_uri of this TestItemVo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this TestItemVo.

        版本URI

        :param version_uri: The version_uri of this TestItemVo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def origin_uri(self):
        r"""Gets the origin_uri of this TestItemVo.

        源资源URI

        :return: The origin_uri of this TestItemVo.
        :rtype: str
        """
        return self._origin_uri

    @origin_uri.setter
    def origin_uri(self, origin_uri):
        r"""Sets the origin_uri of this TestItemVo.

        源资源URI

        :param origin_uri: The origin_uri of this TestItemVo.
        :type origin_uri: str
        """
        self._origin_uri = origin_uri

    @property
    def parent_uri(self):
        r"""Gets the parent_uri of this TestItemVo.

        父资源URI

        :return: The parent_uri of this TestItemVo.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        r"""Sets the parent_uri of this TestItemVo.

        父资源URI

        :param parent_uri: The parent_uri of this TestItemVo.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def parent_path(self):
        r"""Gets the parent_path of this TestItemVo.

        父资源路径

        :return: The parent_path of this TestItemVo.
        :rtype: str
        """
        return self._parent_path

    @parent_path.setter
    def parent_path(self, parent_path):
        r"""Sets the parent_path of this TestItemVo.

        父资源路径

        :param parent_path: The parent_path of this TestItemVo.
        :type parent_path: str
        """
        self._parent_path = parent_path

    @property
    def creation_version_uri(self):
        r"""Gets the creation_version_uri of this TestItemVo.

        创建版本URI

        :return: The creation_version_uri of this TestItemVo.
        :rtype: str
        """
        return self._creation_version_uri

    @creation_version_uri.setter
    def creation_version_uri(self, creation_version_uri):
        r"""Sets the creation_version_uri of this TestItemVo.

        创建版本URI

        :param creation_version_uri: The creation_version_uri of this TestItemVo.
        :type creation_version_uri: str
        """
        self._creation_version_uri = creation_version_uri

    @property
    def creation_date(self):
        r"""Gets the creation_date of this TestItemVo.

        创建时间

        :return: The creation_date of this TestItemVo.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        r"""Sets the creation_date of this TestItemVo.

        创建时间

        :param creation_date: The creation_date of this TestItemVo.
        :type creation_date: datetime
        """
        self._creation_date = creation_date

    @property
    def creation_date_timestamp(self):
        r"""Gets the creation_date_timestamp of this TestItemVo.

        创建时间时间戳

        :return: The creation_date_timestamp of this TestItemVo.
        :rtype: int
        """
        return self._creation_date_timestamp

    @creation_date_timestamp.setter
    def creation_date_timestamp(self, creation_date_timestamp):
        r"""Sets the creation_date_timestamp of this TestItemVo.

        创建时间时间戳

        :param creation_date_timestamp: The creation_date_timestamp of this TestItemVo.
        :type creation_date_timestamp: int
        """
        self._creation_date_timestamp = creation_date_timestamp

    @property
    def author_name(self):
        r"""Gets the author_name of this TestItemVo.

        创建人名称

        :return: The author_name of this TestItemVo.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this TestItemVo.

        创建人名称

        :param author_name: The author_name of this TestItemVo.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def comment(self):
        r"""Gets the comment of this TestItemVo.

        备注

        :return: The comment of this TestItemVo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this TestItemVo.

        备注

        :param comment: The comment of this TestItemVo.
        :type comment: str
        """
        self._comment = comment

    @property
    def number(self):
        r"""Gets the number of this TestItemVo.

        编号

        :return: The number of this TestItemVo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this TestItemVo.

        编号

        :param number: The number of this TestItemVo.
        :type number: str
        """
        self._number = number

    @property
    def is_feature(self):
        r"""Gets the is_feature of this TestItemVo.

        是否特性

        :return: The is_feature of this TestItemVo.
        :rtype: str
        """
        return self._is_feature

    @is_feature.setter
    def is_feature(self, is_feature):
        r"""Sets the is_feature of this TestItemVo.

        是否特性

        :param is_feature: The is_feature of this TestItemVo.
        :type is_feature: str
        """
        self._is_feature = is_feature

    @property
    def relate_htsm(self):
        r"""Gets the relate_htsm of this TestItemVo.

        是否关联特性

        :return: The relate_htsm of this TestItemVo.
        :rtype: str
        """
        return self._relate_htsm

    @relate_htsm.setter
    def relate_htsm(self, relate_htsm):
        r"""Sets the relate_htsm of this TestItemVo.

        是否关联特性

        :param relate_htsm: The relate_htsm of this TestItemVo.
        :type relate_htsm: str
        """
        self._relate_htsm = relate_htsm

    @property
    def aw_unique_id(self):
        r"""Gets the aw_unique_id of this TestItemVo.

        aw id

        :return: The aw_unique_id of this TestItemVo.
        :rtype: str
        """
        return self._aw_unique_id

    @aw_unique_id.setter
    def aw_unique_id(self, aw_unique_id):
        r"""Sets the aw_unique_id of this TestItemVo.

        aw id

        :param aw_unique_id: The aw_unique_id of this TestItemVo.
        :type aw_unique_id: str
        """
        self._aw_unique_id = aw_unique_id

    @property
    def test_mind_id(self):
        r"""Gets the test_mind_id of this TestItemVo.

        脑图id

        :return: The test_mind_id of this TestItemVo.
        :rtype: str
        """
        return self._test_mind_id

    @test_mind_id.setter
    def test_mind_id(self, test_mind_id):
        r"""Sets the test_mind_id of this TestItemVo.

        脑图id

        :param test_mind_id: The test_mind_id of this TestItemVo.
        :type test_mind_id: str
        """
        self._test_mind_id = test_mind_id

    @property
    def test_mind_url(self):
        r"""Gets the test_mind_url of this TestItemVo.

        脑图url

        :return: The test_mind_url of this TestItemVo.
        :rtype: str
        """
        return self._test_mind_url

    @test_mind_url.setter
    def test_mind_url(self, test_mind_url):
        r"""Sets the test_mind_url of this TestItemVo.

        脑图url

        :param test_mind_url: The test_mind_url of this TestItemVo.
        :type test_mind_url: str
        """
        self._test_mind_url = test_mind_url

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this TestItemVo.

        项目id

        :return: The project_uuid of this TestItemVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this TestItemVo.

        项目id

        :param project_uuid: The project_uuid of this TestItemVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def case_total(self):
        r"""Gets the case_total of this TestItemVo.

        用例总数

        :return: The case_total of this TestItemVo.
        :rtype: int
        """
        return self._case_total

    @case_total.setter
    def case_total(self, case_total):
        r"""Sets the case_total of this TestItemVo.

        用例总数

        :param case_total: The case_total of this TestItemVo.
        :type case_total: int
        """
        self._case_total = case_total

    @property
    def execd_total(self):
        r"""Gets the execd_total of this TestItemVo.

        执行总数

        :return: The execd_total of this TestItemVo.
        :rtype: int
        """
        return self._execd_total

    @execd_total.setter
    def execd_total(self, execd_total):
        r"""Sets the execd_total of this TestItemVo.

        执行总数

        :param execd_total: The execd_total of this TestItemVo.
        :type execd_total: int
        """
        self._execd_total = execd_total

    @property
    def is_direct_relation(self):
        r"""Gets the is_direct_relation of this TestItemVo.

        is_direct_relation

        :return: The is_direct_relation of this TestItemVo.
        :rtype: bool
        """
        return self._is_direct_relation

    @is_direct_relation.setter
    def is_direct_relation(self, is_direct_relation):
        r"""Sets the is_direct_relation of this TestItemVo.

        is_direct_relation

        :param is_direct_relation: The is_direct_relation of this TestItemVo.
        :type is_direct_relation: bool
        """
        self._is_direct_relation = is_direct_relation

    @property
    def has_child(self):
        r"""Gets the has_child of this TestItemVo.

        是否有子特性

        :return: The has_child of this TestItemVo.
        :rtype: bool
        """
        return self._has_child

    @has_child.setter
    def has_child(self, has_child):
        r"""Sets the has_child of this TestItemVo.

        是否有子特性

        :param has_child: The has_child of this TestItemVo.
        :type has_child: bool
        """
        self._has_child = has_child

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
        if not isinstance(other, TestItemVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
