# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisasterRecovery:

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
        'status': 'str',
        'name': 'str',
        'dr_type': 'str',
        'primary_cluster_id': 'str',
        'primary_cluster_name': 'str',
        'standby_cluster_id': 'str',
        'standby_cluster_name': 'str',
        'primary_cluster_role': 'str',
        'standby_cluster_role': 'str',
        'primary_cluster_status': 'str',
        'standby_cluster_status': 'str',
        'primary_cluster_region': 'str',
        'standby_cluster_region': 'str',
        'primary_cluster_project_id': 'str',
        'standby_cluster_project_id': 'str',
        'last_disaster_time': 'str',
        'start_time': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'dr_type': 'dr_type',
        'primary_cluster_id': 'primary_cluster_id',
        'primary_cluster_name': 'primary_cluster_name',
        'standby_cluster_id': 'standby_cluster_id',
        'standby_cluster_name': 'standby_cluster_name',
        'primary_cluster_role': 'primary_cluster_role',
        'standby_cluster_role': 'standby_cluster_role',
        'primary_cluster_status': 'primary_cluster_status',
        'standby_cluster_status': 'standby_cluster_status',
        'primary_cluster_region': 'primary_cluster_region',
        'standby_cluster_region': 'standby_cluster_region',
        'primary_cluster_project_id': 'primary_cluster_project_id',
        'standby_cluster_project_id': 'standby_cluster_project_id',
        'last_disaster_time': 'last_disaster_time',
        'start_time': 'start_time',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, status=None, name=None, dr_type=None, primary_cluster_id=None, primary_cluster_name=None, standby_cluster_id=None, standby_cluster_name=None, primary_cluster_role=None, standby_cluster_role=None, primary_cluster_status=None, standby_cluster_status=None, primary_cluster_region=None, standby_cluster_region=None, primary_cluster_project_id=None, standby_cluster_project_id=None, last_disaster_time=None, start_time=None, create_time=None):
        """DisasterRecovery

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param status: 状态
        :type status: str
        :param name: 名称
        :type name: str
        :param dr_type: 容灾类型
        :type dr_type: str
        :param primary_cluster_id: 主集群ID
        :type primary_cluster_id: str
        :param primary_cluster_name: 主集群名称
        :type primary_cluster_name: str
        :param standby_cluster_id: 备集群ID
        :type standby_cluster_id: str
        :param standby_cluster_name: 备集群名称
        :type standby_cluster_name: str
        :param primary_cluster_role: 主集群角色
        :type primary_cluster_role: str
        :param standby_cluster_role: 备集群角色
        :type standby_cluster_role: str
        :param primary_cluster_status: 主集群状态
        :type primary_cluster_status: str
        :param standby_cluster_status: 备集群状态
        :type standby_cluster_status: str
        :param primary_cluster_region: 主集群region
        :type primary_cluster_region: str
        :param standby_cluster_region: 备集群region
        :type standby_cluster_region: str
        :param primary_cluster_project_id: 主集群project_id
        :type primary_cluster_project_id: str
        :param standby_cluster_project_id: 备集群project_id
        :type standby_cluster_project_id: str
        :param last_disaster_time: 最近同步时间
        :type last_disaster_time: str
        :param start_time: 启动时间
        :type start_time: str
        :param create_time: 创建时间
        :type create_time: str
        """
        
        

        self._id = None
        self._status = None
        self._name = None
        self._dr_type = None
        self._primary_cluster_id = None
        self._primary_cluster_name = None
        self._standby_cluster_id = None
        self._standby_cluster_name = None
        self._primary_cluster_role = None
        self._standby_cluster_role = None
        self._primary_cluster_status = None
        self._standby_cluster_status = None
        self._primary_cluster_region = None
        self._standby_cluster_region = None
        self._primary_cluster_project_id = None
        self._standby_cluster_project_id = None
        self._last_disaster_time = None
        self._start_time = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if dr_type is not None:
            self.dr_type = dr_type
        if primary_cluster_id is not None:
            self.primary_cluster_id = primary_cluster_id
        if primary_cluster_name is not None:
            self.primary_cluster_name = primary_cluster_name
        if standby_cluster_id is not None:
            self.standby_cluster_id = standby_cluster_id
        if standby_cluster_name is not None:
            self.standby_cluster_name = standby_cluster_name
        if primary_cluster_role is not None:
            self.primary_cluster_role = primary_cluster_role
        if standby_cluster_role is not None:
            self.standby_cluster_role = standby_cluster_role
        if primary_cluster_status is not None:
            self.primary_cluster_status = primary_cluster_status
        if standby_cluster_status is not None:
            self.standby_cluster_status = standby_cluster_status
        if primary_cluster_region is not None:
            self.primary_cluster_region = primary_cluster_region
        if standby_cluster_region is not None:
            self.standby_cluster_region = standby_cluster_region
        if primary_cluster_project_id is not None:
            self.primary_cluster_project_id = primary_cluster_project_id
        if standby_cluster_project_id is not None:
            self.standby_cluster_project_id = standby_cluster_project_id
        if last_disaster_time is not None:
            self.last_disaster_time = last_disaster_time
        if start_time is not None:
            self.start_time = start_time
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        """Gets the id of this DisasterRecovery.

        ID

        :return: The id of this DisasterRecovery.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DisasterRecovery.

        ID

        :param id: The id of this DisasterRecovery.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this DisasterRecovery.

        状态

        :return: The status of this DisasterRecovery.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DisasterRecovery.

        状态

        :param status: The status of this DisasterRecovery.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this DisasterRecovery.

        名称

        :return: The name of this DisasterRecovery.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DisasterRecovery.

        名称

        :param name: The name of this DisasterRecovery.
        :type name: str
        """
        self._name = name

    @property
    def dr_type(self):
        """Gets the dr_type of this DisasterRecovery.

        容灾类型

        :return: The dr_type of this DisasterRecovery.
        :rtype: str
        """
        return self._dr_type

    @dr_type.setter
    def dr_type(self, dr_type):
        """Sets the dr_type of this DisasterRecovery.

        容灾类型

        :param dr_type: The dr_type of this DisasterRecovery.
        :type dr_type: str
        """
        self._dr_type = dr_type

    @property
    def primary_cluster_id(self):
        """Gets the primary_cluster_id of this DisasterRecovery.

        主集群ID

        :return: The primary_cluster_id of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_id

    @primary_cluster_id.setter
    def primary_cluster_id(self, primary_cluster_id):
        """Sets the primary_cluster_id of this DisasterRecovery.

        主集群ID

        :param primary_cluster_id: The primary_cluster_id of this DisasterRecovery.
        :type primary_cluster_id: str
        """
        self._primary_cluster_id = primary_cluster_id

    @property
    def primary_cluster_name(self):
        """Gets the primary_cluster_name of this DisasterRecovery.

        主集群名称

        :return: The primary_cluster_name of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_name

    @primary_cluster_name.setter
    def primary_cluster_name(self, primary_cluster_name):
        """Sets the primary_cluster_name of this DisasterRecovery.

        主集群名称

        :param primary_cluster_name: The primary_cluster_name of this DisasterRecovery.
        :type primary_cluster_name: str
        """
        self._primary_cluster_name = primary_cluster_name

    @property
    def standby_cluster_id(self):
        """Gets the standby_cluster_id of this DisasterRecovery.

        备集群ID

        :return: The standby_cluster_id of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_id

    @standby_cluster_id.setter
    def standby_cluster_id(self, standby_cluster_id):
        """Sets the standby_cluster_id of this DisasterRecovery.

        备集群ID

        :param standby_cluster_id: The standby_cluster_id of this DisasterRecovery.
        :type standby_cluster_id: str
        """
        self._standby_cluster_id = standby_cluster_id

    @property
    def standby_cluster_name(self):
        """Gets the standby_cluster_name of this DisasterRecovery.

        备集群名称

        :return: The standby_cluster_name of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_name

    @standby_cluster_name.setter
    def standby_cluster_name(self, standby_cluster_name):
        """Sets the standby_cluster_name of this DisasterRecovery.

        备集群名称

        :param standby_cluster_name: The standby_cluster_name of this DisasterRecovery.
        :type standby_cluster_name: str
        """
        self._standby_cluster_name = standby_cluster_name

    @property
    def primary_cluster_role(self):
        """Gets the primary_cluster_role of this DisasterRecovery.

        主集群角色

        :return: The primary_cluster_role of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_role

    @primary_cluster_role.setter
    def primary_cluster_role(self, primary_cluster_role):
        """Sets the primary_cluster_role of this DisasterRecovery.

        主集群角色

        :param primary_cluster_role: The primary_cluster_role of this DisasterRecovery.
        :type primary_cluster_role: str
        """
        self._primary_cluster_role = primary_cluster_role

    @property
    def standby_cluster_role(self):
        """Gets the standby_cluster_role of this DisasterRecovery.

        备集群角色

        :return: The standby_cluster_role of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_role

    @standby_cluster_role.setter
    def standby_cluster_role(self, standby_cluster_role):
        """Sets the standby_cluster_role of this DisasterRecovery.

        备集群角色

        :param standby_cluster_role: The standby_cluster_role of this DisasterRecovery.
        :type standby_cluster_role: str
        """
        self._standby_cluster_role = standby_cluster_role

    @property
    def primary_cluster_status(self):
        """Gets the primary_cluster_status of this DisasterRecovery.

        主集群状态

        :return: The primary_cluster_status of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_status

    @primary_cluster_status.setter
    def primary_cluster_status(self, primary_cluster_status):
        """Sets the primary_cluster_status of this DisasterRecovery.

        主集群状态

        :param primary_cluster_status: The primary_cluster_status of this DisasterRecovery.
        :type primary_cluster_status: str
        """
        self._primary_cluster_status = primary_cluster_status

    @property
    def standby_cluster_status(self):
        """Gets the standby_cluster_status of this DisasterRecovery.

        备集群状态

        :return: The standby_cluster_status of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_status

    @standby_cluster_status.setter
    def standby_cluster_status(self, standby_cluster_status):
        """Sets the standby_cluster_status of this DisasterRecovery.

        备集群状态

        :param standby_cluster_status: The standby_cluster_status of this DisasterRecovery.
        :type standby_cluster_status: str
        """
        self._standby_cluster_status = standby_cluster_status

    @property
    def primary_cluster_region(self):
        """Gets the primary_cluster_region of this DisasterRecovery.

        主集群region

        :return: The primary_cluster_region of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_region

    @primary_cluster_region.setter
    def primary_cluster_region(self, primary_cluster_region):
        """Sets the primary_cluster_region of this DisasterRecovery.

        主集群region

        :param primary_cluster_region: The primary_cluster_region of this DisasterRecovery.
        :type primary_cluster_region: str
        """
        self._primary_cluster_region = primary_cluster_region

    @property
    def standby_cluster_region(self):
        """Gets the standby_cluster_region of this DisasterRecovery.

        备集群region

        :return: The standby_cluster_region of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_region

    @standby_cluster_region.setter
    def standby_cluster_region(self, standby_cluster_region):
        """Sets the standby_cluster_region of this DisasterRecovery.

        备集群region

        :param standby_cluster_region: The standby_cluster_region of this DisasterRecovery.
        :type standby_cluster_region: str
        """
        self._standby_cluster_region = standby_cluster_region

    @property
    def primary_cluster_project_id(self):
        """Gets the primary_cluster_project_id of this DisasterRecovery.

        主集群project_id

        :return: The primary_cluster_project_id of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_project_id

    @primary_cluster_project_id.setter
    def primary_cluster_project_id(self, primary_cluster_project_id):
        """Sets the primary_cluster_project_id of this DisasterRecovery.

        主集群project_id

        :param primary_cluster_project_id: The primary_cluster_project_id of this DisasterRecovery.
        :type primary_cluster_project_id: str
        """
        self._primary_cluster_project_id = primary_cluster_project_id

    @property
    def standby_cluster_project_id(self):
        """Gets the standby_cluster_project_id of this DisasterRecovery.

        备集群project_id

        :return: The standby_cluster_project_id of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_project_id

    @standby_cluster_project_id.setter
    def standby_cluster_project_id(self, standby_cluster_project_id):
        """Sets the standby_cluster_project_id of this DisasterRecovery.

        备集群project_id

        :param standby_cluster_project_id: The standby_cluster_project_id of this DisasterRecovery.
        :type standby_cluster_project_id: str
        """
        self._standby_cluster_project_id = standby_cluster_project_id

    @property
    def last_disaster_time(self):
        """Gets the last_disaster_time of this DisasterRecovery.

        最近同步时间

        :return: The last_disaster_time of this DisasterRecovery.
        :rtype: str
        """
        return self._last_disaster_time

    @last_disaster_time.setter
    def last_disaster_time(self, last_disaster_time):
        """Sets the last_disaster_time of this DisasterRecovery.

        最近同步时间

        :param last_disaster_time: The last_disaster_time of this DisasterRecovery.
        :type last_disaster_time: str
        """
        self._last_disaster_time = last_disaster_time

    @property
    def start_time(self):
        """Gets the start_time of this DisasterRecovery.

        启动时间

        :return: The start_time of this DisasterRecovery.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DisasterRecovery.

        启动时间

        :param start_time: The start_time of this DisasterRecovery.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def create_time(self):
        """Gets the create_time of this DisasterRecovery.

        创建时间

        :return: The create_time of this DisasterRecovery.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DisasterRecovery.

        创建时间

        :param create_time: The create_time of this DisasterRecovery.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, DisasterRecovery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
