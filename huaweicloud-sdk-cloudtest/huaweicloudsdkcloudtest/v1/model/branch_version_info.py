# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BranchVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'number': 'str',
        'is_master': 'str',
        'pbi_id': 'str',
        'pbi_name': 'str',
        'plan_start_date': 'str',
        'plan_start_timestamp': 'int',
        'plan_end_date': 'str',
        'plan_end_timestamp': 'int',
        'asyn_git': 'str',
        'project_uuid': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'number': 'number',
        'is_master': 'is_master',
        'pbi_id': 'pbi_id',
        'pbi_name': 'pbi_name',
        'plan_start_date': 'plan_start_date',
        'plan_start_timestamp': 'plan_start_timestamp',
        'plan_end_date': 'plan_end_date',
        'plan_end_timestamp': 'plan_end_timestamp',
        'asyn_git': 'asyn_git',
        'project_uuid': 'project_uuid',
        'project_name': 'project_name'
    }

    def __init__(self, name=None, number=None, is_master=None, pbi_id=None, pbi_name=None, plan_start_date=None, plan_start_timestamp=None, plan_end_date=None, plan_end_timestamp=None, asyn_git=None, project_uuid=None, project_name=None):
        """BranchVersionInfo

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param number: 开发分支名称
        :type number: str
        :param is_master: 是否为Master分支
        :type is_master: str
        :param pbi_id: PBI ID
        :type pbi_id: str
        :param pbi_name: PBI信息
        :type pbi_name: str
        :param plan_start_date: 开始时间
        :type plan_start_date: str
        :param plan_start_timestamp: 开始时间戳
        :type plan_start_timestamp: int
        :param plan_end_date: 结束时间
        :type plan_end_date: str
        :param plan_end_timestamp: 结束时间戳
        :type plan_end_timestamp: int
        :param asyn_git: 是否同步git库
        :type asyn_git: str
        :param project_uuid: 项目ID（云龙场景，传入微服务ID）
        :type project_uuid: str
        :param project_name: 项目名称（云龙场景，传入微服务名）
        :type project_name: str
        """
        
        

        self._name = None
        self._number = None
        self._is_master = None
        self._pbi_id = None
        self._pbi_name = None
        self._plan_start_date = None
        self._plan_start_timestamp = None
        self._plan_end_date = None
        self._plan_end_timestamp = None
        self._asyn_git = None
        self._project_uuid = None
        self._project_name = None
        self.discriminator = None

        self.name = name
        if number is not None:
            self.number = number
        if is_master is not None:
            self.is_master = is_master
        if pbi_id is not None:
            self.pbi_id = pbi_id
        if pbi_name is not None:
            self.pbi_name = pbi_name
        if plan_start_date is not None:
            self.plan_start_date = plan_start_date
        if plan_start_timestamp is not None:
            self.plan_start_timestamp = plan_start_timestamp
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if plan_end_timestamp is not None:
            self.plan_end_timestamp = plan_end_timestamp
        if asyn_git is not None:
            self.asyn_git = asyn_git
        self.project_uuid = project_uuid
        if project_name is not None:
            self.project_name = project_name

    @property
    def name(self):
        """Gets the name of this BranchVersionInfo.

        名称

        :return: The name of this BranchVersionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BranchVersionInfo.

        名称

        :param name: The name of this BranchVersionInfo.
        :type name: str
        """
        self._name = name

    @property
    def number(self):
        """Gets the number of this BranchVersionInfo.

        开发分支名称

        :return: The number of this BranchVersionInfo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this BranchVersionInfo.

        开发分支名称

        :param number: The number of this BranchVersionInfo.
        :type number: str
        """
        self._number = number

    @property
    def is_master(self):
        """Gets the is_master of this BranchVersionInfo.

        是否为Master分支

        :return: The is_master of this BranchVersionInfo.
        :rtype: str
        """
        return self._is_master

    @is_master.setter
    def is_master(self, is_master):
        """Sets the is_master of this BranchVersionInfo.

        是否为Master分支

        :param is_master: The is_master of this BranchVersionInfo.
        :type is_master: str
        """
        self._is_master = is_master

    @property
    def pbi_id(self):
        """Gets the pbi_id of this BranchVersionInfo.

        PBI ID

        :return: The pbi_id of this BranchVersionInfo.
        :rtype: str
        """
        return self._pbi_id

    @pbi_id.setter
    def pbi_id(self, pbi_id):
        """Sets the pbi_id of this BranchVersionInfo.

        PBI ID

        :param pbi_id: The pbi_id of this BranchVersionInfo.
        :type pbi_id: str
        """
        self._pbi_id = pbi_id

    @property
    def pbi_name(self):
        """Gets the pbi_name of this BranchVersionInfo.

        PBI信息

        :return: The pbi_name of this BranchVersionInfo.
        :rtype: str
        """
        return self._pbi_name

    @pbi_name.setter
    def pbi_name(self, pbi_name):
        """Sets the pbi_name of this BranchVersionInfo.

        PBI信息

        :param pbi_name: The pbi_name of this BranchVersionInfo.
        :type pbi_name: str
        """
        self._pbi_name = pbi_name

    @property
    def plan_start_date(self):
        """Gets the plan_start_date of this BranchVersionInfo.

        开始时间

        :return: The plan_start_date of this BranchVersionInfo.
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        """Sets the plan_start_date of this BranchVersionInfo.

        开始时间

        :param plan_start_date: The plan_start_date of this BranchVersionInfo.
        :type plan_start_date: str
        """
        self._plan_start_date = plan_start_date

    @property
    def plan_start_timestamp(self):
        """Gets the plan_start_timestamp of this BranchVersionInfo.

        开始时间戳

        :return: The plan_start_timestamp of this BranchVersionInfo.
        :rtype: int
        """
        return self._plan_start_timestamp

    @plan_start_timestamp.setter
    def plan_start_timestamp(self, plan_start_timestamp):
        """Sets the plan_start_timestamp of this BranchVersionInfo.

        开始时间戳

        :param plan_start_timestamp: The plan_start_timestamp of this BranchVersionInfo.
        :type plan_start_timestamp: int
        """
        self._plan_start_timestamp = plan_start_timestamp

    @property
    def plan_end_date(self):
        """Gets the plan_end_date of this BranchVersionInfo.

        结束时间

        :return: The plan_end_date of this BranchVersionInfo.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        """Sets the plan_end_date of this BranchVersionInfo.

        结束时间

        :param plan_end_date: The plan_end_date of this BranchVersionInfo.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def plan_end_timestamp(self):
        """Gets the plan_end_timestamp of this BranchVersionInfo.

        结束时间戳

        :return: The plan_end_timestamp of this BranchVersionInfo.
        :rtype: int
        """
        return self._plan_end_timestamp

    @plan_end_timestamp.setter
    def plan_end_timestamp(self, plan_end_timestamp):
        """Sets the plan_end_timestamp of this BranchVersionInfo.

        结束时间戳

        :param plan_end_timestamp: The plan_end_timestamp of this BranchVersionInfo.
        :type plan_end_timestamp: int
        """
        self._plan_end_timestamp = plan_end_timestamp

    @property
    def asyn_git(self):
        """Gets the asyn_git of this BranchVersionInfo.

        是否同步git库

        :return: The asyn_git of this BranchVersionInfo.
        :rtype: str
        """
        return self._asyn_git

    @asyn_git.setter
    def asyn_git(self, asyn_git):
        """Sets the asyn_git of this BranchVersionInfo.

        是否同步git库

        :param asyn_git: The asyn_git of this BranchVersionInfo.
        :type asyn_git: str
        """
        self._asyn_git = asyn_git

    @property
    def project_uuid(self):
        """Gets the project_uuid of this BranchVersionInfo.

        项目ID（云龙场景，传入微服务ID）

        :return: The project_uuid of this BranchVersionInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this BranchVersionInfo.

        项目ID（云龙场景，传入微服务ID）

        :param project_uuid: The project_uuid of this BranchVersionInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def project_name(self):
        """Gets the project_name of this BranchVersionInfo.

        项目名称（云龙场景，传入微服务名）

        :return: The project_name of this BranchVersionInfo.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this BranchVersionInfo.

        项目名称（云龙场景，传入微服务名）

        :param project_name: The project_name of this BranchVersionInfo.
        :type project_name: str
        """
        self._project_name = project_name

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
        if not isinstance(other, BranchVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
