# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIteratorByDefectResponse(SdkResponse):

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
        'version': 'str',
        'owner': 'str',
        'creator': 'str',
        'iterations': 'str',
        'description': 'str',
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
        'is_master': 'int',
        'is_iterator': 'int',
        'plan_start_date': 'datetime',
        'plan_end_date': 'datetime',
        'service_id': 'str',
        'service_name': 'str',
        'pbi_id': 'str',
        'pbi_name': 'str',
        'plan_id': 'str',
        'metric_pbi_ids': 'str',
        'metric_pbi_id_names': 'str',
        'last_syn_date': 'datetime',
        'is_closed': 'str',
        'asyn_git': 'str',
        'schema_no': 'int',
        'finish_date': 'datetime',
        'owner_name': 'str',
        'creator_name': 'str',
        'current_stage': 'str',
        'service_types': 'str',
        'risk_rating': 'int',
        'risk_des': 'str',
        'project_uuid': 'str',
        'domain_id': 'str',
        'pi_id': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'type': 'type',
        'author': 'author',
        'name': 'name',
        'rank': 'rank',
        'version': 'version',
        'owner': 'owner',
        'creator': 'creator',
        'iterations': 'iterations',
        'description': 'description',
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
        'is_master': 'is_master',
        'is_iterator': 'is_iterator',
        'plan_start_date': 'plan_start_date',
        'plan_end_date': 'plan_end_date',
        'service_id': 'service_id',
        'service_name': 'service_name',
        'pbi_id': 'pbi_id',
        'pbi_name': 'pbi_name',
        'plan_id': 'plan_id',
        'metric_pbi_ids': 'metric_pbi_ids',
        'metric_pbi_id_names': 'metric_pbi_id_names',
        'last_syn_date': 'last_syn_date',
        'is_closed': 'is_closed',
        'asyn_git': 'asyn_git',
        'schema_no': 'schema_no',
        'finish_date': 'finish_date',
        'owner_name': 'owner_name',
        'creator_name': 'creator_name',
        'current_stage': 'current_stage',
        'service_types': 'service_types',
        'risk_rating': 'risk_rating',
        'risk_des': 'risk_des',
        'project_uuid': 'project_uuid',
        'domain_id': 'domain_id',
        'pi_id': 'pi_id'
    }

    def __init__(self, uri=None, type=None, author=None, name=None, rank=None, version=None, owner=None, creator=None, iterations=None, description=None, region=None, last_modifier=None, last_modified=None, last_modified_timestamp=None, last_change_time=None, version_uri=None, origin_uri=None, parent_uri=None, parent_path=None, creation_version_uri=None, creation_date=None, creation_date_timestamp=None, author_name=None, comment=None, number=None, is_master=None, is_iterator=None, plan_start_date=None, plan_end_date=None, service_id=None, service_name=None, pbi_id=None, pbi_name=None, plan_id=None, metric_pbi_ids=None, metric_pbi_id_names=None, last_syn_date=None, is_closed=None, asyn_git=None, schema_no=None, finish_date=None, owner_name=None, creator_name=None, current_stage=None, service_types=None, risk_rating=None, risk_des=None, project_uuid=None, domain_id=None, pi_id=None):
        """ShowIteratorByDefectResponse

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
        :param version: 待测版本
        :type version: str
        :param owner: 处理者ID
        :type owner: str
        :param creator: 创建人ID
        :type creator: str
        :param iterations: 关联迭代
        :type iterations: str
        :param description: 描述
        :type description: str
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
        :param is_master: 是否为Master分支
        :type is_master: int
        :param is_iterator: 是否为迭代
        :type is_iterator: int
        :param plan_start_date: 开始时间
        :type plan_start_date: datetime
        :param plan_end_date: 结束时间
        :type plan_end_date: datetime
        :param service_id: 微服务ID
        :type service_id: str
        :param service_name: 微服务名
        :type service_name: str
        :param pbi_id: PBI ID
        :type pbi_id: str
        :param pbi_name: PBI信息
        :type pbi_name: str
        :param plan_id: 计划ID
        :type plan_id: str
        :param metric_pbi_ids: 度量PBI ID
        :type metric_pbi_ids: str
        :param metric_pbi_id_names: 度量PBI名称
        :type metric_pbi_id_names: str
        :param last_syn_date: 最后同步时间
        :type last_syn_date: datetime
        :param is_closed: 版本是否关闭
        :type is_closed: str
        :param asyn_git: 是否同步git库
        :type asyn_git: str
        :param schema_no: schema编号
        :type schema_no: int
        :param finish_date: 迭代实际完成时间
        :type finish_date: datetime
        :param owner_name: 处理者名称
        :type owner_name: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param current_stage: 当前所处阶段
        :type current_stage: str
        :param service_types: 服务类型
        :type service_types: str
        :param risk_rating: 风险等级
        :type risk_rating: int
        :param risk_des: 风险描述
        :type risk_des: str
        :param project_uuid: 项目ID
        :type project_uuid: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param pi_id: pi的id
        :type pi_id: str
        """
        
        super(ShowIteratorByDefectResponse, self).__init__()

        self._uri = None
        self._type = None
        self._author = None
        self._name = None
        self._rank = None
        self._version = None
        self._owner = None
        self._creator = None
        self._iterations = None
        self._description = None
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
        self._is_master = None
        self._is_iterator = None
        self._plan_start_date = None
        self._plan_end_date = None
        self._service_id = None
        self._service_name = None
        self._pbi_id = None
        self._pbi_name = None
        self._plan_id = None
        self._metric_pbi_ids = None
        self._metric_pbi_id_names = None
        self._last_syn_date = None
        self._is_closed = None
        self._asyn_git = None
        self._schema_no = None
        self._finish_date = None
        self._owner_name = None
        self._creator_name = None
        self._current_stage = None
        self._service_types = None
        self._risk_rating = None
        self._risk_des = None
        self._project_uuid = None
        self._domain_id = None
        self._pi_id = None
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
        if version is not None:
            self.version = version
        if owner is not None:
            self.owner = owner
        if creator is not None:
            self.creator = creator
        if iterations is not None:
            self.iterations = iterations
        if description is not None:
            self.description = description
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
        if is_master is not None:
            self.is_master = is_master
        if is_iterator is not None:
            self.is_iterator = is_iterator
        if plan_start_date is not None:
            self.plan_start_date = plan_start_date
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if pbi_id is not None:
            self.pbi_id = pbi_id
        if pbi_name is not None:
            self.pbi_name = pbi_name
        if plan_id is not None:
            self.plan_id = plan_id
        if metric_pbi_ids is not None:
            self.metric_pbi_ids = metric_pbi_ids
        if metric_pbi_id_names is not None:
            self.metric_pbi_id_names = metric_pbi_id_names
        if last_syn_date is not None:
            self.last_syn_date = last_syn_date
        if is_closed is not None:
            self.is_closed = is_closed
        if asyn_git is not None:
            self.asyn_git = asyn_git
        if schema_no is not None:
            self.schema_no = schema_no
        if finish_date is not None:
            self.finish_date = finish_date
        if owner_name is not None:
            self.owner_name = owner_name
        if creator_name is not None:
            self.creator_name = creator_name
        if current_stage is not None:
            self.current_stage = current_stage
        if service_types is not None:
            self.service_types = service_types
        if risk_rating is not None:
            self.risk_rating = risk_rating
        if risk_des is not None:
            self.risk_des = risk_des
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if domain_id is not None:
            self.domain_id = domain_id
        if pi_id is not None:
            self.pi_id = pi_id

    @property
    def uri(self):
        """Gets the uri of this ShowIteratorByDefectResponse.

        资源URI

        :return: The uri of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ShowIteratorByDefectResponse.

        资源URI

        :param uri: The uri of this ShowIteratorByDefectResponse.
        :type uri: str
        """
        self._uri = uri

    @property
    def type(self):
        """Gets the type of this ShowIteratorByDefectResponse.

        资源类型

        :return: The type of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowIteratorByDefectResponse.

        资源类型

        :param type: The type of this ShowIteratorByDefectResponse.
        :type type: str
        """
        self._type = type

    @property
    def author(self):
        """Gets the author of this ShowIteratorByDefectResponse.

        创建人

        :return: The author of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ShowIteratorByDefectResponse.

        创建人

        :param author: The author of this ShowIteratorByDefectResponse.
        :type author: str
        """
        self._author = author

    @property
    def name(self):
        """Gets the name of this ShowIteratorByDefectResponse.

        名称

        :return: The name of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowIteratorByDefectResponse.

        名称

        :param name: The name of this ShowIteratorByDefectResponse.
        :type name: str
        """
        self._name = name

    @property
    def rank(self):
        """Gets the rank of this ShowIteratorByDefectResponse.

        级别

        :return: The rank of this ShowIteratorByDefectResponse.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this ShowIteratorByDefectResponse.

        级别

        :param rank: The rank of this ShowIteratorByDefectResponse.
        :type rank: int
        """
        self._rank = rank

    @property
    def version(self):
        """Gets the version of this ShowIteratorByDefectResponse.

        待测版本

        :return: The version of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowIteratorByDefectResponse.

        待测版本

        :param version: The version of this ShowIteratorByDefectResponse.
        :type version: str
        """
        self._version = version

    @property
    def owner(self):
        """Gets the owner of this ShowIteratorByDefectResponse.

        处理者ID

        :return: The owner of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowIteratorByDefectResponse.

        处理者ID

        :param owner: The owner of this ShowIteratorByDefectResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def creator(self):
        """Gets the creator of this ShowIteratorByDefectResponse.

        创建人ID

        :return: The creator of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowIteratorByDefectResponse.

        创建人ID

        :param creator: The creator of this ShowIteratorByDefectResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def iterations(self):
        """Gets the iterations of this ShowIteratorByDefectResponse.

        关联迭代

        :return: The iterations of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._iterations

    @iterations.setter
    def iterations(self, iterations):
        """Sets the iterations of this ShowIteratorByDefectResponse.

        关联迭代

        :param iterations: The iterations of this ShowIteratorByDefectResponse.
        :type iterations: str
        """
        self._iterations = iterations

    @property
    def description(self):
        """Gets the description of this ShowIteratorByDefectResponse.

        描述

        :return: The description of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowIteratorByDefectResponse.

        描述

        :param description: The description of this ShowIteratorByDefectResponse.
        :type description: str
        """
        self._description = description

    @property
    def region(self):
        """Gets the region of this ShowIteratorByDefectResponse.

        区域

        :return: The region of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowIteratorByDefectResponse.

        区域

        :param region: The region of this ShowIteratorByDefectResponse.
        :type region: str
        """
        self._region = region

    @property
    def last_modifier(self):
        """Gets the last_modifier of this ShowIteratorByDefectResponse.

        最后修改人

        :return: The last_modifier of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._last_modifier

    @last_modifier.setter
    def last_modifier(self, last_modifier):
        """Sets the last_modifier of this ShowIteratorByDefectResponse.

        最后修改人

        :param last_modifier: The last_modifier of this ShowIteratorByDefectResponse.
        :type last_modifier: str
        """
        self._last_modifier = last_modifier

    @property
    def last_modified(self):
        """Gets the last_modified of this ShowIteratorByDefectResponse.

        最后修改时间

        :return: The last_modified of this ShowIteratorByDefectResponse.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ShowIteratorByDefectResponse.

        最后修改时间

        :param last_modified: The last_modified of this ShowIteratorByDefectResponse.
        :type last_modified: datetime
        """
        self._last_modified = last_modified

    @property
    def last_modified_timestamp(self):
        """Gets the last_modified_timestamp of this ShowIteratorByDefectResponse.

        修改时间时间戳

        :return: The last_modified_timestamp of this ShowIteratorByDefectResponse.
        :rtype: int
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(self, last_modified_timestamp):
        """Sets the last_modified_timestamp of this ShowIteratorByDefectResponse.

        修改时间时间戳

        :param last_modified_timestamp: The last_modified_timestamp of this ShowIteratorByDefectResponse.
        :type last_modified_timestamp: int
        """
        self._last_modified_timestamp = last_modified_timestamp

    @property
    def last_change_time(self):
        """Gets the last_change_time of this ShowIteratorByDefectResponse.

        最后变更时间

        :return: The last_change_time of this ShowIteratorByDefectResponse.
        :rtype: datetime
        """
        return self._last_change_time

    @last_change_time.setter
    def last_change_time(self, last_change_time):
        """Sets the last_change_time of this ShowIteratorByDefectResponse.

        最后变更时间

        :param last_change_time: The last_change_time of this ShowIteratorByDefectResponse.
        :type last_change_time: datetime
        """
        self._last_change_time = last_change_time

    @property
    def version_uri(self):
        """Gets the version_uri of this ShowIteratorByDefectResponse.

        版本URI

        :return: The version_uri of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this ShowIteratorByDefectResponse.

        版本URI

        :param version_uri: The version_uri of this ShowIteratorByDefectResponse.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def origin_uri(self):
        """Gets the origin_uri of this ShowIteratorByDefectResponse.

        源资源URI

        :return: The origin_uri of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._origin_uri

    @origin_uri.setter
    def origin_uri(self, origin_uri):
        """Sets the origin_uri of this ShowIteratorByDefectResponse.

        源资源URI

        :param origin_uri: The origin_uri of this ShowIteratorByDefectResponse.
        :type origin_uri: str
        """
        self._origin_uri = origin_uri

    @property
    def parent_uri(self):
        """Gets the parent_uri of this ShowIteratorByDefectResponse.

        父资源URI

        :return: The parent_uri of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        """Sets the parent_uri of this ShowIteratorByDefectResponse.

        父资源URI

        :param parent_uri: The parent_uri of this ShowIteratorByDefectResponse.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def parent_path(self):
        """Gets the parent_path of this ShowIteratorByDefectResponse.

        父资源路径

        :return: The parent_path of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._parent_path

    @parent_path.setter
    def parent_path(self, parent_path):
        """Sets the parent_path of this ShowIteratorByDefectResponse.

        父资源路径

        :param parent_path: The parent_path of this ShowIteratorByDefectResponse.
        :type parent_path: str
        """
        self._parent_path = parent_path

    @property
    def creation_version_uri(self):
        """Gets the creation_version_uri of this ShowIteratorByDefectResponse.

        创建版本URI

        :return: The creation_version_uri of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._creation_version_uri

    @creation_version_uri.setter
    def creation_version_uri(self, creation_version_uri):
        """Sets the creation_version_uri of this ShowIteratorByDefectResponse.

        创建版本URI

        :param creation_version_uri: The creation_version_uri of this ShowIteratorByDefectResponse.
        :type creation_version_uri: str
        """
        self._creation_version_uri = creation_version_uri

    @property
    def creation_date(self):
        """Gets the creation_date of this ShowIteratorByDefectResponse.

        创建时间

        :return: The creation_date of this ShowIteratorByDefectResponse.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ShowIteratorByDefectResponse.

        创建时间

        :param creation_date: The creation_date of this ShowIteratorByDefectResponse.
        :type creation_date: datetime
        """
        self._creation_date = creation_date

    @property
    def creation_date_timestamp(self):
        """Gets the creation_date_timestamp of this ShowIteratorByDefectResponse.

        创建时间时间戳

        :return: The creation_date_timestamp of this ShowIteratorByDefectResponse.
        :rtype: int
        """
        return self._creation_date_timestamp

    @creation_date_timestamp.setter
    def creation_date_timestamp(self, creation_date_timestamp):
        """Sets the creation_date_timestamp of this ShowIteratorByDefectResponse.

        创建时间时间戳

        :param creation_date_timestamp: The creation_date_timestamp of this ShowIteratorByDefectResponse.
        :type creation_date_timestamp: int
        """
        self._creation_date_timestamp = creation_date_timestamp

    @property
    def author_name(self):
        """Gets the author_name of this ShowIteratorByDefectResponse.

        创建人名称

        :return: The author_name of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this ShowIteratorByDefectResponse.

        创建人名称

        :param author_name: The author_name of this ShowIteratorByDefectResponse.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def comment(self):
        """Gets the comment of this ShowIteratorByDefectResponse.

        备注

        :return: The comment of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ShowIteratorByDefectResponse.

        备注

        :param comment: The comment of this ShowIteratorByDefectResponse.
        :type comment: str
        """
        self._comment = comment

    @property
    def number(self):
        """Gets the number of this ShowIteratorByDefectResponse.

        编号

        :return: The number of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ShowIteratorByDefectResponse.

        编号

        :param number: The number of this ShowIteratorByDefectResponse.
        :type number: str
        """
        self._number = number

    @property
    def is_master(self):
        """Gets the is_master of this ShowIteratorByDefectResponse.

        是否为Master分支

        :return: The is_master of this ShowIteratorByDefectResponse.
        :rtype: int
        """
        return self._is_master

    @is_master.setter
    def is_master(self, is_master):
        """Sets the is_master of this ShowIteratorByDefectResponse.

        是否为Master分支

        :param is_master: The is_master of this ShowIteratorByDefectResponse.
        :type is_master: int
        """
        self._is_master = is_master

    @property
    def is_iterator(self):
        """Gets the is_iterator of this ShowIteratorByDefectResponse.

        是否为迭代

        :return: The is_iterator of this ShowIteratorByDefectResponse.
        :rtype: int
        """
        return self._is_iterator

    @is_iterator.setter
    def is_iterator(self, is_iterator):
        """Sets the is_iterator of this ShowIteratorByDefectResponse.

        是否为迭代

        :param is_iterator: The is_iterator of this ShowIteratorByDefectResponse.
        :type is_iterator: int
        """
        self._is_iterator = is_iterator

    @property
    def plan_start_date(self):
        """Gets the plan_start_date of this ShowIteratorByDefectResponse.

        开始时间

        :return: The plan_start_date of this ShowIteratorByDefectResponse.
        :rtype: datetime
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        """Sets the plan_start_date of this ShowIteratorByDefectResponse.

        开始时间

        :param plan_start_date: The plan_start_date of this ShowIteratorByDefectResponse.
        :type plan_start_date: datetime
        """
        self._plan_start_date = plan_start_date

    @property
    def plan_end_date(self):
        """Gets the plan_end_date of this ShowIteratorByDefectResponse.

        结束时间

        :return: The plan_end_date of this ShowIteratorByDefectResponse.
        :rtype: datetime
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        """Sets the plan_end_date of this ShowIteratorByDefectResponse.

        结束时间

        :param plan_end_date: The plan_end_date of this ShowIteratorByDefectResponse.
        :type plan_end_date: datetime
        """
        self._plan_end_date = plan_end_date

    @property
    def service_id(self):
        """Gets the service_id of this ShowIteratorByDefectResponse.

        微服务ID

        :return: The service_id of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ShowIteratorByDefectResponse.

        微服务ID

        :param service_id: The service_id of this ShowIteratorByDefectResponse.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def service_name(self):
        """Gets the service_name of this ShowIteratorByDefectResponse.

        微服务名

        :return: The service_name of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this ShowIteratorByDefectResponse.

        微服务名

        :param service_name: The service_name of this ShowIteratorByDefectResponse.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def pbi_id(self):
        """Gets the pbi_id of this ShowIteratorByDefectResponse.

        PBI ID

        :return: The pbi_id of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._pbi_id

    @pbi_id.setter
    def pbi_id(self, pbi_id):
        """Sets the pbi_id of this ShowIteratorByDefectResponse.

        PBI ID

        :param pbi_id: The pbi_id of this ShowIteratorByDefectResponse.
        :type pbi_id: str
        """
        self._pbi_id = pbi_id

    @property
    def pbi_name(self):
        """Gets the pbi_name of this ShowIteratorByDefectResponse.

        PBI信息

        :return: The pbi_name of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._pbi_name

    @pbi_name.setter
    def pbi_name(self, pbi_name):
        """Sets the pbi_name of this ShowIteratorByDefectResponse.

        PBI信息

        :param pbi_name: The pbi_name of this ShowIteratorByDefectResponse.
        :type pbi_name: str
        """
        self._pbi_name = pbi_name

    @property
    def plan_id(self):
        """Gets the plan_id of this ShowIteratorByDefectResponse.

        计划ID

        :return: The plan_id of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this ShowIteratorByDefectResponse.

        计划ID

        :param plan_id: The plan_id of this ShowIteratorByDefectResponse.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def metric_pbi_ids(self):
        """Gets the metric_pbi_ids of this ShowIteratorByDefectResponse.

        度量PBI ID

        :return: The metric_pbi_ids of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._metric_pbi_ids

    @metric_pbi_ids.setter
    def metric_pbi_ids(self, metric_pbi_ids):
        """Sets the metric_pbi_ids of this ShowIteratorByDefectResponse.

        度量PBI ID

        :param metric_pbi_ids: The metric_pbi_ids of this ShowIteratorByDefectResponse.
        :type metric_pbi_ids: str
        """
        self._metric_pbi_ids = metric_pbi_ids

    @property
    def metric_pbi_id_names(self):
        """Gets the metric_pbi_id_names of this ShowIteratorByDefectResponse.

        度量PBI名称

        :return: The metric_pbi_id_names of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._metric_pbi_id_names

    @metric_pbi_id_names.setter
    def metric_pbi_id_names(self, metric_pbi_id_names):
        """Sets the metric_pbi_id_names of this ShowIteratorByDefectResponse.

        度量PBI名称

        :param metric_pbi_id_names: The metric_pbi_id_names of this ShowIteratorByDefectResponse.
        :type metric_pbi_id_names: str
        """
        self._metric_pbi_id_names = metric_pbi_id_names

    @property
    def last_syn_date(self):
        """Gets the last_syn_date of this ShowIteratorByDefectResponse.

        最后同步时间

        :return: The last_syn_date of this ShowIteratorByDefectResponse.
        :rtype: datetime
        """
        return self._last_syn_date

    @last_syn_date.setter
    def last_syn_date(self, last_syn_date):
        """Sets the last_syn_date of this ShowIteratorByDefectResponse.

        最后同步时间

        :param last_syn_date: The last_syn_date of this ShowIteratorByDefectResponse.
        :type last_syn_date: datetime
        """
        self._last_syn_date = last_syn_date

    @property
    def is_closed(self):
        """Gets the is_closed of this ShowIteratorByDefectResponse.

        版本是否关闭

        :return: The is_closed of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """Sets the is_closed of this ShowIteratorByDefectResponse.

        版本是否关闭

        :param is_closed: The is_closed of this ShowIteratorByDefectResponse.
        :type is_closed: str
        """
        self._is_closed = is_closed

    @property
    def asyn_git(self):
        """Gets the asyn_git of this ShowIteratorByDefectResponse.

        是否同步git库

        :return: The asyn_git of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._asyn_git

    @asyn_git.setter
    def asyn_git(self, asyn_git):
        """Sets the asyn_git of this ShowIteratorByDefectResponse.

        是否同步git库

        :param asyn_git: The asyn_git of this ShowIteratorByDefectResponse.
        :type asyn_git: str
        """
        self._asyn_git = asyn_git

    @property
    def schema_no(self):
        """Gets the schema_no of this ShowIteratorByDefectResponse.

        schema编号

        :return: The schema_no of this ShowIteratorByDefectResponse.
        :rtype: int
        """
        return self._schema_no

    @schema_no.setter
    def schema_no(self, schema_no):
        """Sets the schema_no of this ShowIteratorByDefectResponse.

        schema编号

        :param schema_no: The schema_no of this ShowIteratorByDefectResponse.
        :type schema_no: int
        """
        self._schema_no = schema_no

    @property
    def finish_date(self):
        """Gets the finish_date of this ShowIteratorByDefectResponse.

        迭代实际完成时间

        :return: The finish_date of this ShowIteratorByDefectResponse.
        :rtype: datetime
        """
        return self._finish_date

    @finish_date.setter
    def finish_date(self, finish_date):
        """Sets the finish_date of this ShowIteratorByDefectResponse.

        迭代实际完成时间

        :param finish_date: The finish_date of this ShowIteratorByDefectResponse.
        :type finish_date: datetime
        """
        self._finish_date = finish_date

    @property
    def owner_name(self):
        """Gets the owner_name of this ShowIteratorByDefectResponse.

        处理者名称

        :return: The owner_name of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this ShowIteratorByDefectResponse.

        处理者名称

        :param owner_name: The owner_name of this ShowIteratorByDefectResponse.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def creator_name(self):
        """Gets the creator_name of this ShowIteratorByDefectResponse.

        创建人名称

        :return: The creator_name of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ShowIteratorByDefectResponse.

        创建人名称

        :param creator_name: The creator_name of this ShowIteratorByDefectResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def current_stage(self):
        """Gets the current_stage of this ShowIteratorByDefectResponse.

        当前所处阶段

        :return: The current_stage of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
        """Sets the current_stage of this ShowIteratorByDefectResponse.

        当前所处阶段

        :param current_stage: The current_stage of this ShowIteratorByDefectResponse.
        :type current_stage: str
        """
        self._current_stage = current_stage

    @property
    def service_types(self):
        """Gets the service_types of this ShowIteratorByDefectResponse.

        服务类型

        :return: The service_types of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._service_types

    @service_types.setter
    def service_types(self, service_types):
        """Sets the service_types of this ShowIteratorByDefectResponse.

        服务类型

        :param service_types: The service_types of this ShowIteratorByDefectResponse.
        :type service_types: str
        """
        self._service_types = service_types

    @property
    def risk_rating(self):
        """Gets the risk_rating of this ShowIteratorByDefectResponse.

        风险等级

        :return: The risk_rating of this ShowIteratorByDefectResponse.
        :rtype: int
        """
        return self._risk_rating

    @risk_rating.setter
    def risk_rating(self, risk_rating):
        """Sets the risk_rating of this ShowIteratorByDefectResponse.

        风险等级

        :param risk_rating: The risk_rating of this ShowIteratorByDefectResponse.
        :type risk_rating: int
        """
        self._risk_rating = risk_rating

    @property
    def risk_des(self):
        """Gets the risk_des of this ShowIteratorByDefectResponse.

        风险描述

        :return: The risk_des of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._risk_des

    @risk_des.setter
    def risk_des(self, risk_des):
        """Sets the risk_des of this ShowIteratorByDefectResponse.

        风险描述

        :param risk_des: The risk_des of this ShowIteratorByDefectResponse.
        :type risk_des: str
        """
        self._risk_des = risk_des

    @property
    def project_uuid(self):
        """Gets the project_uuid of this ShowIteratorByDefectResponse.

        项目ID

        :return: The project_uuid of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this ShowIteratorByDefectResponse.

        项目ID

        :param project_uuid: The project_uuid of this ShowIteratorByDefectResponse.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowIteratorByDefectResponse.

        租户ID

        :return: The domain_id of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowIteratorByDefectResponse.

        租户ID

        :param domain_id: The domain_id of this ShowIteratorByDefectResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def pi_id(self):
        """Gets the pi_id of this ShowIteratorByDefectResponse.

        pi的id

        :return: The pi_id of this ShowIteratorByDefectResponse.
        :rtype: str
        """
        return self._pi_id

    @pi_id.setter
    def pi_id(self, pi_id):
        """Sets the pi_id of this ShowIteratorByDefectResponse.

        pi的id

        :param pi_id: The pi_id of this ShowIteratorByDefectResponse.
        :type pi_id: str
        """
        self._pi_id = pi_id

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
        if not isinstance(other, ShowIteratorByDefectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
