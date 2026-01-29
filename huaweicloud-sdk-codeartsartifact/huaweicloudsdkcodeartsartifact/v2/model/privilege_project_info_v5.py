# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivilegeProjectInfoV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'project_id': 'str',
        'created_time': 'str',
        'repository_num': 'int',
        'total': 'int',
        'repository_id': 'str',
        'region': 'str',
        'domain_id': 'str',
        'ids': 'list[str]',
        'total_records': 'int',
        'associated': 'bool',
        'project_info': 'list[PrivilegeProjectInfoV5]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'project_id': 'project_id',
        'created_time': 'created_time',
        'repository_num': 'repository_num',
        'total': 'total',
        'repository_id': 'repository_id',
        'region': 'region',
        'domain_id': 'domain_id',
        'ids': 'ids',
        'total_records': 'total_records',
        'associated': 'associated',
        'project_info': 'project_info'
    }

    def __init__(self, id=None, name=None, status=None, project_id=None, created_time=None, repository_num=None, total=None, repository_id=None, region=None, domain_id=None, ids=None, total_records=None, associated=None, project_info=None):
        r"""PrivilegeProjectInfoV5

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  项目的序号。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 项目的名称。 **取值范围**： 不涉及。
        :type name: str
        :param status: **参数解释**： 项目的状态（该参数无返回值，请忽略）。 **取值范围**： 该参数无返回值，请忽略。
        :type status: str
        :param project_id: **参数解释**： 项目ID。 **取值范围**： 不涉及。
        :type project_id: str
        :param created_time: **参数解释**： 项目的创建时间。 **取值范围**： 格式为yyyy-MM-dd HH:mm:ss。
        :type created_time: str
        :param repository_num: **参数解释**： 仓库数量。 **取值范围**： 不涉及。
        :type repository_num: int
        :param total: **参数解释**： 项目总数（该参数无返回值，请忽略）。 **取值范围**： 该参数无返回值，请忽略。
        :type total: int
        :param repository_id: **参数解释**： 仓库ID。 **取值范围**： 不涉及。
        :type repository_id: str
        :param region: **参数解释**： 项目所属的区域。 **取值范围**： 不涉及。
        :type region: str
        :param domain_id: **参数解释**： 租户ID。 **取值范围**： 不涉及。
        :type domain_id: str
        :param ids: **参数解释**： 项目的序号列表（该参数无返回值，请忽略）。 **取值范围**： 该参数无返回值，请忽略。
        :type ids: list[str]
        :param total_records: **参数解释**： 项目总数。 **取值范围**： 不涉及。
        :type total_records: int
        :param associated: **参数解释**： 请求参数中的仓库ID是否关联到本项目。 **取值范围**： - true：关联到本项目。 - false：未关联到本项目。
        :type associated: bool
        :param project_info: **参数解释**： 项目的信息。 **取值范围**： 不涉及。
        :type project_info: list[:class:`huaweicloudsdkcodeartsartifact.v2.PrivilegeProjectInfoV5`]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._project_id = None
        self._created_time = None
        self._repository_num = None
        self._total = None
        self._repository_id = None
        self._region = None
        self._domain_id = None
        self._ids = None
        self._total_records = None
        self._associated = None
        self._project_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if project_id is not None:
            self.project_id = project_id
        if created_time is not None:
            self.created_time = created_time
        if repository_num is not None:
            self.repository_num = repository_num
        if total is not None:
            self.total = total
        if repository_id is not None:
            self.repository_id = repository_id
        if region is not None:
            self.region = region
        if domain_id is not None:
            self.domain_id = domain_id
        if ids is not None:
            self.ids = ids
        if total_records is not None:
            self.total_records = total_records
        if associated is not None:
            self.associated = associated
        if project_info is not None:
            self.project_info = project_info

    @property
    def id(self):
        r"""Gets the id of this PrivilegeProjectInfoV5.

        **参数解释**：  项目的序号。 **取值范围**： 不涉及。

        :return: The id of this PrivilegeProjectInfoV5.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PrivilegeProjectInfoV5.

        **参数解释**：  项目的序号。 **取值范围**： 不涉及。

        :param id: The id of this PrivilegeProjectInfoV5.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PrivilegeProjectInfoV5.

        **参数解释**： 项目的名称。 **取值范围**： 不涉及。

        :return: The name of this PrivilegeProjectInfoV5.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PrivilegeProjectInfoV5.

        **参数解释**： 项目的名称。 **取值范围**： 不涉及。

        :param name: The name of this PrivilegeProjectInfoV5.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this PrivilegeProjectInfoV5.

        **参数解释**： 项目的状态（该参数无返回值，请忽略）。 **取值范围**： 该参数无返回值，请忽略。

        :return: The status of this PrivilegeProjectInfoV5.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PrivilegeProjectInfoV5.

        **参数解释**： 项目的状态（该参数无返回值，请忽略）。 **取值范围**： 该参数无返回值，请忽略。

        :param status: The status of this PrivilegeProjectInfoV5.
        :type status: str
        """
        self._status = status

    @property
    def project_id(self):
        r"""Gets the project_id of this PrivilegeProjectInfoV5.

        **参数解释**： 项目ID。 **取值范围**： 不涉及。

        :return: The project_id of this PrivilegeProjectInfoV5.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PrivilegeProjectInfoV5.

        **参数解释**： 项目ID。 **取值范围**： 不涉及。

        :param project_id: The project_id of this PrivilegeProjectInfoV5.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_time(self):
        r"""Gets the created_time of this PrivilegeProjectInfoV5.

        **参数解释**： 项目的创建时间。 **取值范围**： 格式为yyyy-MM-dd HH:mm:ss。

        :return: The created_time of this PrivilegeProjectInfoV5.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this PrivilegeProjectInfoV5.

        **参数解释**： 项目的创建时间。 **取值范围**： 格式为yyyy-MM-dd HH:mm:ss。

        :param created_time: The created_time of this PrivilegeProjectInfoV5.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def repository_num(self):
        r"""Gets the repository_num of this PrivilegeProjectInfoV5.

        **参数解释**： 仓库数量。 **取值范围**： 不涉及。

        :return: The repository_num of this PrivilegeProjectInfoV5.
        :rtype: int
        """
        return self._repository_num

    @repository_num.setter
    def repository_num(self, repository_num):
        r"""Sets the repository_num of this PrivilegeProjectInfoV5.

        **参数解释**： 仓库数量。 **取值范围**： 不涉及。

        :param repository_num: The repository_num of this PrivilegeProjectInfoV5.
        :type repository_num: int
        """
        self._repository_num = repository_num

    @property
    def total(self):
        r"""Gets the total of this PrivilegeProjectInfoV5.

        **参数解释**： 项目总数（该参数无返回值，请忽略）。 **取值范围**： 该参数无返回值，请忽略。

        :return: The total of this PrivilegeProjectInfoV5.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this PrivilegeProjectInfoV5.

        **参数解释**： 项目总数（该参数无返回值，请忽略）。 **取值范围**： 该参数无返回值，请忽略。

        :param total: The total of this PrivilegeProjectInfoV5.
        :type total: int
        """
        self._total = total

    @property
    def repository_id(self):
        r"""Gets the repository_id of this PrivilegeProjectInfoV5.

        **参数解释**： 仓库ID。 **取值范围**： 不涉及。

        :return: The repository_id of this PrivilegeProjectInfoV5.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this PrivilegeProjectInfoV5.

        **参数解释**： 仓库ID。 **取值范围**： 不涉及。

        :param repository_id: The repository_id of this PrivilegeProjectInfoV5.
        :type repository_id: str
        """
        self._repository_id = repository_id

    @property
    def region(self):
        r"""Gets the region of this PrivilegeProjectInfoV5.

        **参数解释**： 项目所属的区域。 **取值范围**： 不涉及。

        :return: The region of this PrivilegeProjectInfoV5.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this PrivilegeProjectInfoV5.

        **参数解释**： 项目所属的区域。 **取值范围**： 不涉及。

        :param region: The region of this PrivilegeProjectInfoV5.
        :type region: str
        """
        self._region = region

    @property
    def domain_id(self):
        r"""Gets the domain_id of this PrivilegeProjectInfoV5.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :return: The domain_id of this PrivilegeProjectInfoV5.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this PrivilegeProjectInfoV5.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :param domain_id: The domain_id of this PrivilegeProjectInfoV5.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def ids(self):
        r"""Gets the ids of this PrivilegeProjectInfoV5.

        **参数解释**： 项目的序号列表（该参数无返回值，请忽略）。 **取值范围**： 该参数无返回值，请忽略。

        :return: The ids of this PrivilegeProjectInfoV5.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this PrivilegeProjectInfoV5.

        **参数解释**： 项目的序号列表（该参数无返回值，请忽略）。 **取值范围**： 该参数无返回值，请忽略。

        :param ids: The ids of this PrivilegeProjectInfoV5.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def total_records(self):
        r"""Gets the total_records of this PrivilegeProjectInfoV5.

        **参数解释**： 项目总数。 **取值范围**： 不涉及。

        :return: The total_records of this PrivilegeProjectInfoV5.
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        r"""Sets the total_records of this PrivilegeProjectInfoV5.

        **参数解释**： 项目总数。 **取值范围**： 不涉及。

        :param total_records: The total_records of this PrivilegeProjectInfoV5.
        :type total_records: int
        """
        self._total_records = total_records

    @property
    def associated(self):
        r"""Gets the associated of this PrivilegeProjectInfoV5.

        **参数解释**： 请求参数中的仓库ID是否关联到本项目。 **取值范围**： - true：关联到本项目。 - false：未关联到本项目。

        :return: The associated of this PrivilegeProjectInfoV5.
        :rtype: bool
        """
        return self._associated

    @associated.setter
    def associated(self, associated):
        r"""Sets the associated of this PrivilegeProjectInfoV5.

        **参数解释**： 请求参数中的仓库ID是否关联到本项目。 **取值范围**： - true：关联到本项目。 - false：未关联到本项目。

        :param associated: The associated of this PrivilegeProjectInfoV5.
        :type associated: bool
        """
        self._associated = associated

    @property
    def project_info(self):
        r"""Gets the project_info of this PrivilegeProjectInfoV5.

        **参数解释**： 项目的信息。 **取值范围**： 不涉及。

        :return: The project_info of this PrivilegeProjectInfoV5.
        :rtype: list[:class:`huaweicloudsdkcodeartsartifact.v2.PrivilegeProjectInfoV5`]
        """
        return self._project_info

    @project_info.setter
    def project_info(self, project_info):
        r"""Sets the project_info of this PrivilegeProjectInfoV5.

        **参数解释**： 项目的信息。 **取值范围**： 不涉及。

        :param project_info: The project_info of this PrivilegeProjectInfoV5.
        :type project_info: list[:class:`huaweicloudsdkcodeartsartifact.v2.PrivilegeProjectInfoV5`]
        """
        self._project_info = project_info

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
        if not isinstance(other, PrivilegeProjectInfoV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
