# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkSpaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bad_record_location_name': 'str',
        'description': 'str',
        'eps_id': 'str',
        'job_log_location_name': 'str',
        'name': 'str',
        'id': 'str',
        'is_default': 'int',
        'owner_name': 'str',
        'project_id': 'str',
        'domain_id': 'str',
        'instance_id': 'str',
        'create_time': 'float',
        'create_user': 'str',
        'member_num': 'int',
        'update_time': 'float',
        'update_user': 'str'
    }

    attribute_map = {
        'bad_record_location_name': 'bad_record_location_name',
        'description': 'description',
        'eps_id': 'eps_id',
        'job_log_location_name': 'job_log_location_name',
        'name': 'name',
        'id': 'id',
        'is_default': 'is_default',
        'owner_name': 'owner_name',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'instance_id': 'instance_id',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'member_num': 'member_num',
        'update_time': 'update_time',
        'update_user': 'update_user'
    }

    def __init__(self, bad_record_location_name=None, description=None, eps_id=None, job_log_location_name=None, name=None, id=None, is_default=None, owner_name=None, project_id=None, domain_id=None, instance_id=None, create_time=None, create_user=None, member_num=None, update_time=None, update_user=None):
        r"""ShowWorkSpaceResponse

        The model defined in huaweicloud sdk

        :param bad_record_location_name: DLI脏数据OBS路径
        :type bad_record_location_name: str
        :param description: 工作空间描述
        :type description: str
        :param eps_id: 企业项目id，如果当前为公有云，且用户开启企业项目，则必选
        :type eps_id: str
        :param job_log_location_name: 作业日志OBS路径
        :type job_log_location_name: str
        :param name: 工作空间名称
        :type name: str
        :param id: 工作空间id
        :type id: str
        :param is_default: 是否为默认空间，0为私有空间，1为默认空间，2为公共空间
        :type is_default: int
        :param owner_name: 创建者名称
        :type owner_name: str
        :param project_id: 项目id
        :type project_id: str
        :param domain_id: 当前租户所属domain id
        :type domain_id: str
        :param instance_id: 当前工作空间所属实例id
        :type instance_id: str
        :param create_time: 创建时间
        :type create_time: float
        :param create_user: 创建用户名称
        :type create_user: str
        :param member_num: 当前工作空间成员数量
        :type member_num: int
        :param update_time: 更新时间
        :type update_time: float
        :param update_user: 更新用户名称
        :type update_user: str
        """
        
        super(ShowWorkSpaceResponse, self).__init__()

        self._bad_record_location_name = None
        self._description = None
        self._eps_id = None
        self._job_log_location_name = None
        self._name = None
        self._id = None
        self._is_default = None
        self._owner_name = None
        self._project_id = None
        self._domain_id = None
        self._instance_id = None
        self._create_time = None
        self._create_user = None
        self._member_num = None
        self._update_time = None
        self._update_user = None
        self.discriminator = None

        if bad_record_location_name is not None:
            self.bad_record_location_name = bad_record_location_name
        if description is not None:
            self.description = description
        if eps_id is not None:
            self.eps_id = eps_id
        if job_log_location_name is not None:
            self.job_log_location_name = job_log_location_name
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if is_default is not None:
            self.is_default = is_default
        if owner_name is not None:
            self.owner_name = owner_name
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if instance_id is not None:
            self.instance_id = instance_id
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if member_num is not None:
            self.member_num = member_num
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user

    @property
    def bad_record_location_name(self):
        r"""Gets the bad_record_location_name of this ShowWorkSpaceResponse.

        DLI脏数据OBS路径

        :return: The bad_record_location_name of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._bad_record_location_name

    @bad_record_location_name.setter
    def bad_record_location_name(self, bad_record_location_name):
        r"""Sets the bad_record_location_name of this ShowWorkSpaceResponse.

        DLI脏数据OBS路径

        :param bad_record_location_name: The bad_record_location_name of this ShowWorkSpaceResponse.
        :type bad_record_location_name: str
        """
        self._bad_record_location_name = bad_record_location_name

    @property
    def description(self):
        r"""Gets the description of this ShowWorkSpaceResponse.

        工作空间描述

        :return: The description of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowWorkSpaceResponse.

        工作空间描述

        :param description: The description of this ShowWorkSpaceResponse.
        :type description: str
        """
        self._description = description

    @property
    def eps_id(self):
        r"""Gets the eps_id of this ShowWorkSpaceResponse.

        企业项目id，如果当前为公有云，且用户开启企业项目，则必选

        :return: The eps_id of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this ShowWorkSpaceResponse.

        企业项目id，如果当前为公有云，且用户开启企业项目，则必选

        :param eps_id: The eps_id of this ShowWorkSpaceResponse.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def job_log_location_name(self):
        r"""Gets the job_log_location_name of this ShowWorkSpaceResponse.

        作业日志OBS路径

        :return: The job_log_location_name of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._job_log_location_name

    @job_log_location_name.setter
    def job_log_location_name(self, job_log_location_name):
        r"""Sets the job_log_location_name of this ShowWorkSpaceResponse.

        作业日志OBS路径

        :param job_log_location_name: The job_log_location_name of this ShowWorkSpaceResponse.
        :type job_log_location_name: str
        """
        self._job_log_location_name = job_log_location_name

    @property
    def name(self):
        r"""Gets the name of this ShowWorkSpaceResponse.

        工作空间名称

        :return: The name of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowWorkSpaceResponse.

        工作空间名称

        :param name: The name of this ShowWorkSpaceResponse.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ShowWorkSpaceResponse.

        工作空间id

        :return: The id of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowWorkSpaceResponse.

        工作空间id

        :param id: The id of this ShowWorkSpaceResponse.
        :type id: str
        """
        self._id = id

    @property
    def is_default(self):
        r"""Gets the is_default of this ShowWorkSpaceResponse.

        是否为默认空间，0为私有空间，1为默认空间，2为公共空间

        :return: The is_default of this ShowWorkSpaceResponse.
        :rtype: int
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this ShowWorkSpaceResponse.

        是否为默认空间，0为私有空间，1为默认空间，2为公共空间

        :param is_default: The is_default of this ShowWorkSpaceResponse.
        :type is_default: int
        """
        self._is_default = is_default

    @property
    def owner_name(self):
        r"""Gets the owner_name of this ShowWorkSpaceResponse.

        创建者名称

        :return: The owner_name of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this ShowWorkSpaceResponse.

        创建者名称

        :param owner_name: The owner_name of this ShowWorkSpaceResponse.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowWorkSpaceResponse.

        项目id

        :return: The project_id of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowWorkSpaceResponse.

        项目id

        :param project_id: The project_id of this ShowWorkSpaceResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowWorkSpaceResponse.

        当前租户所属domain id

        :return: The domain_id of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowWorkSpaceResponse.

        当前租户所属domain id

        :param domain_id: The domain_id of this ShowWorkSpaceResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowWorkSpaceResponse.

        当前工作空间所属实例id

        :return: The instance_id of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowWorkSpaceResponse.

        当前工作空间所属实例id

        :param instance_id: The instance_id of this ShowWorkSpaceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowWorkSpaceResponse.

        创建时间

        :return: The create_time of this ShowWorkSpaceResponse.
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowWorkSpaceResponse.

        创建时间

        :param create_time: The create_time of this ShowWorkSpaceResponse.
        :type create_time: float
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowWorkSpaceResponse.

        创建用户名称

        :return: The create_user of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowWorkSpaceResponse.

        创建用户名称

        :param create_user: The create_user of this ShowWorkSpaceResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def member_num(self):
        r"""Gets the member_num of this ShowWorkSpaceResponse.

        当前工作空间成员数量

        :return: The member_num of this ShowWorkSpaceResponse.
        :rtype: int
        """
        return self._member_num

    @member_num.setter
    def member_num(self, member_num):
        r"""Sets the member_num of this ShowWorkSpaceResponse.

        当前工作空间成员数量

        :param member_num: The member_num of this ShowWorkSpaceResponse.
        :type member_num: int
        """
        self._member_num = member_num

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowWorkSpaceResponse.

        更新时间

        :return: The update_time of this ShowWorkSpaceResponse.
        :rtype: float
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowWorkSpaceResponse.

        更新时间

        :param update_time: The update_time of this ShowWorkSpaceResponse.
        :type update_time: float
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this ShowWorkSpaceResponse.

        更新用户名称

        :return: The update_user of this ShowWorkSpaceResponse.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this ShowWorkSpaceResponse.

        更新用户名称

        :param update_user: The update_user of this ShowWorkSpaceResponse.
        :type update_user: str
        """
        self._update_user = update_user

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
        if not isinstance(other, ShowWorkSpaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
