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
        r"""DisasterRecovery

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 容灾ID。 **取值范围**： 不涉及。
        :type id: str
        :param status: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type status: str
        :param name: **参数解释**： 名称。 **取值范围**： 不涉及。
        :type name: str
        :param dr_type: **参数解释**： 容灾类型。 **取值范围**： 不涉及。
        :type dr_type: str
        :param primary_cluster_id: **参数解释**： 主集群ID。 **取值范围**： 不涉及。
        :type primary_cluster_id: str
        :param primary_cluster_name: **参数解释**： 主集群名称。 **取值范围**： 不涉及。
        :type primary_cluster_name: str
        :param standby_cluster_id: **参数解释**： 备集群ID。 **取值范围**： 不涉及。
        :type standby_cluster_id: str
        :param standby_cluster_name: **参数解释**： 备集群名称。 **取值范围**： 不涉及。
        :type standby_cluster_name: str
        :param primary_cluster_role: **参数解释**： 主集群角色。 **取值范围**： 不涉及。
        :type primary_cluster_role: str
        :param standby_cluster_role: **参数解释**： 备集群角色。 **取值范围**： 不涉及。
        :type standby_cluster_role: str
        :param primary_cluster_status: **参数解释**： 主集群状态。 **取值范围**： 不涉及。
        :type primary_cluster_status: str
        :param standby_cluster_status: **参数解释**： 备集群状态。 **取值范围**： 不涉及。
        :type standby_cluster_status: str
        :param primary_cluster_region: **参数解释**： 主集群region。 **取值范围**： 不涉及。
        :type primary_cluster_region: str
        :param standby_cluster_region: **参数解释**： 备集群region。 **取值范围**： 不涉及。
        :type standby_cluster_region: str
        :param primary_cluster_project_id: **参数解释**： 主集群项目ID。 **取值范围**： 不涉及。
        :type primary_cluster_project_id: str
        :param standby_cluster_project_id: **参数解释**： 备集群项目ID。 **取值范围**： 不涉及。
        :type standby_cluster_project_id: str
        :param last_disaster_time: **参数解释**： 最近同步时间。 **取值范围**： 不涉及。
        :type last_disaster_time: str
        :param start_time: **参数解释**： 启动时间。 **取值范围**： 不涉及。
        :type start_time: str
        :param create_time: **参数解释**： 创建时间。 **取值范围**： 不涉及。
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
        r"""Gets the id of this DisasterRecovery.

        **参数解释**： 容灾ID。 **取值范围**： 不涉及。

        :return: The id of this DisasterRecovery.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DisasterRecovery.

        **参数解释**： 容灾ID。 **取值范围**： 不涉及。

        :param id: The id of this DisasterRecovery.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this DisasterRecovery.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The status of this DisasterRecovery.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DisasterRecovery.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param status: The status of this DisasterRecovery.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this DisasterRecovery.

        **参数解释**： 名称。 **取值范围**： 不涉及。

        :return: The name of this DisasterRecovery.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DisasterRecovery.

        **参数解释**： 名称。 **取值范围**： 不涉及。

        :param name: The name of this DisasterRecovery.
        :type name: str
        """
        self._name = name

    @property
    def dr_type(self):
        r"""Gets the dr_type of this DisasterRecovery.

        **参数解释**： 容灾类型。 **取值范围**： 不涉及。

        :return: The dr_type of this DisasterRecovery.
        :rtype: str
        """
        return self._dr_type

    @dr_type.setter
    def dr_type(self, dr_type):
        r"""Sets the dr_type of this DisasterRecovery.

        **参数解释**： 容灾类型。 **取值范围**： 不涉及。

        :param dr_type: The dr_type of this DisasterRecovery.
        :type dr_type: str
        """
        self._dr_type = dr_type

    @property
    def primary_cluster_id(self):
        r"""Gets the primary_cluster_id of this DisasterRecovery.

        **参数解释**： 主集群ID。 **取值范围**： 不涉及。

        :return: The primary_cluster_id of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_id

    @primary_cluster_id.setter
    def primary_cluster_id(self, primary_cluster_id):
        r"""Sets the primary_cluster_id of this DisasterRecovery.

        **参数解释**： 主集群ID。 **取值范围**： 不涉及。

        :param primary_cluster_id: The primary_cluster_id of this DisasterRecovery.
        :type primary_cluster_id: str
        """
        self._primary_cluster_id = primary_cluster_id

    @property
    def primary_cluster_name(self):
        r"""Gets the primary_cluster_name of this DisasterRecovery.

        **参数解释**： 主集群名称。 **取值范围**： 不涉及。

        :return: The primary_cluster_name of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_name

    @primary_cluster_name.setter
    def primary_cluster_name(self, primary_cluster_name):
        r"""Sets the primary_cluster_name of this DisasterRecovery.

        **参数解释**： 主集群名称。 **取值范围**： 不涉及。

        :param primary_cluster_name: The primary_cluster_name of this DisasterRecovery.
        :type primary_cluster_name: str
        """
        self._primary_cluster_name = primary_cluster_name

    @property
    def standby_cluster_id(self):
        r"""Gets the standby_cluster_id of this DisasterRecovery.

        **参数解释**： 备集群ID。 **取值范围**： 不涉及。

        :return: The standby_cluster_id of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_id

    @standby_cluster_id.setter
    def standby_cluster_id(self, standby_cluster_id):
        r"""Sets the standby_cluster_id of this DisasterRecovery.

        **参数解释**： 备集群ID。 **取值范围**： 不涉及。

        :param standby_cluster_id: The standby_cluster_id of this DisasterRecovery.
        :type standby_cluster_id: str
        """
        self._standby_cluster_id = standby_cluster_id

    @property
    def standby_cluster_name(self):
        r"""Gets the standby_cluster_name of this DisasterRecovery.

        **参数解释**： 备集群名称。 **取值范围**： 不涉及。

        :return: The standby_cluster_name of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_name

    @standby_cluster_name.setter
    def standby_cluster_name(self, standby_cluster_name):
        r"""Sets the standby_cluster_name of this DisasterRecovery.

        **参数解释**： 备集群名称。 **取值范围**： 不涉及。

        :param standby_cluster_name: The standby_cluster_name of this DisasterRecovery.
        :type standby_cluster_name: str
        """
        self._standby_cluster_name = standby_cluster_name

    @property
    def primary_cluster_role(self):
        r"""Gets the primary_cluster_role of this DisasterRecovery.

        **参数解释**： 主集群角色。 **取值范围**： 不涉及。

        :return: The primary_cluster_role of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_role

    @primary_cluster_role.setter
    def primary_cluster_role(self, primary_cluster_role):
        r"""Sets the primary_cluster_role of this DisasterRecovery.

        **参数解释**： 主集群角色。 **取值范围**： 不涉及。

        :param primary_cluster_role: The primary_cluster_role of this DisasterRecovery.
        :type primary_cluster_role: str
        """
        self._primary_cluster_role = primary_cluster_role

    @property
    def standby_cluster_role(self):
        r"""Gets the standby_cluster_role of this DisasterRecovery.

        **参数解释**： 备集群角色。 **取值范围**： 不涉及。

        :return: The standby_cluster_role of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_role

    @standby_cluster_role.setter
    def standby_cluster_role(self, standby_cluster_role):
        r"""Sets the standby_cluster_role of this DisasterRecovery.

        **参数解释**： 备集群角色。 **取值范围**： 不涉及。

        :param standby_cluster_role: The standby_cluster_role of this DisasterRecovery.
        :type standby_cluster_role: str
        """
        self._standby_cluster_role = standby_cluster_role

    @property
    def primary_cluster_status(self):
        r"""Gets the primary_cluster_status of this DisasterRecovery.

        **参数解释**： 主集群状态。 **取值范围**： 不涉及。

        :return: The primary_cluster_status of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_status

    @primary_cluster_status.setter
    def primary_cluster_status(self, primary_cluster_status):
        r"""Sets the primary_cluster_status of this DisasterRecovery.

        **参数解释**： 主集群状态。 **取值范围**： 不涉及。

        :param primary_cluster_status: The primary_cluster_status of this DisasterRecovery.
        :type primary_cluster_status: str
        """
        self._primary_cluster_status = primary_cluster_status

    @property
    def standby_cluster_status(self):
        r"""Gets the standby_cluster_status of this DisasterRecovery.

        **参数解释**： 备集群状态。 **取值范围**： 不涉及。

        :return: The standby_cluster_status of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_status

    @standby_cluster_status.setter
    def standby_cluster_status(self, standby_cluster_status):
        r"""Sets the standby_cluster_status of this DisasterRecovery.

        **参数解释**： 备集群状态。 **取值范围**： 不涉及。

        :param standby_cluster_status: The standby_cluster_status of this DisasterRecovery.
        :type standby_cluster_status: str
        """
        self._standby_cluster_status = standby_cluster_status

    @property
    def primary_cluster_region(self):
        r"""Gets the primary_cluster_region of this DisasterRecovery.

        **参数解释**： 主集群region。 **取值范围**： 不涉及。

        :return: The primary_cluster_region of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_region

    @primary_cluster_region.setter
    def primary_cluster_region(self, primary_cluster_region):
        r"""Sets the primary_cluster_region of this DisasterRecovery.

        **参数解释**： 主集群region。 **取值范围**： 不涉及。

        :param primary_cluster_region: The primary_cluster_region of this DisasterRecovery.
        :type primary_cluster_region: str
        """
        self._primary_cluster_region = primary_cluster_region

    @property
    def standby_cluster_region(self):
        r"""Gets the standby_cluster_region of this DisasterRecovery.

        **参数解释**： 备集群region。 **取值范围**： 不涉及。

        :return: The standby_cluster_region of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_region

    @standby_cluster_region.setter
    def standby_cluster_region(self, standby_cluster_region):
        r"""Sets the standby_cluster_region of this DisasterRecovery.

        **参数解释**： 备集群region。 **取值范围**： 不涉及。

        :param standby_cluster_region: The standby_cluster_region of this DisasterRecovery.
        :type standby_cluster_region: str
        """
        self._standby_cluster_region = standby_cluster_region

    @property
    def primary_cluster_project_id(self):
        r"""Gets the primary_cluster_project_id of this DisasterRecovery.

        **参数解释**： 主集群项目ID。 **取值范围**： 不涉及。

        :return: The primary_cluster_project_id of this DisasterRecovery.
        :rtype: str
        """
        return self._primary_cluster_project_id

    @primary_cluster_project_id.setter
    def primary_cluster_project_id(self, primary_cluster_project_id):
        r"""Sets the primary_cluster_project_id of this DisasterRecovery.

        **参数解释**： 主集群项目ID。 **取值范围**： 不涉及。

        :param primary_cluster_project_id: The primary_cluster_project_id of this DisasterRecovery.
        :type primary_cluster_project_id: str
        """
        self._primary_cluster_project_id = primary_cluster_project_id

    @property
    def standby_cluster_project_id(self):
        r"""Gets the standby_cluster_project_id of this DisasterRecovery.

        **参数解释**： 备集群项目ID。 **取值范围**： 不涉及。

        :return: The standby_cluster_project_id of this DisasterRecovery.
        :rtype: str
        """
        return self._standby_cluster_project_id

    @standby_cluster_project_id.setter
    def standby_cluster_project_id(self, standby_cluster_project_id):
        r"""Sets the standby_cluster_project_id of this DisasterRecovery.

        **参数解释**： 备集群项目ID。 **取值范围**： 不涉及。

        :param standby_cluster_project_id: The standby_cluster_project_id of this DisasterRecovery.
        :type standby_cluster_project_id: str
        """
        self._standby_cluster_project_id = standby_cluster_project_id

    @property
    def last_disaster_time(self):
        r"""Gets the last_disaster_time of this DisasterRecovery.

        **参数解释**： 最近同步时间。 **取值范围**： 不涉及。

        :return: The last_disaster_time of this DisasterRecovery.
        :rtype: str
        """
        return self._last_disaster_time

    @last_disaster_time.setter
    def last_disaster_time(self, last_disaster_time):
        r"""Sets the last_disaster_time of this DisasterRecovery.

        **参数解释**： 最近同步时间。 **取值范围**： 不涉及。

        :param last_disaster_time: The last_disaster_time of this DisasterRecovery.
        :type last_disaster_time: str
        """
        self._last_disaster_time = last_disaster_time

    @property
    def start_time(self):
        r"""Gets the start_time of this DisasterRecovery.

        **参数解释**： 启动时间。 **取值范围**： 不涉及。

        :return: The start_time of this DisasterRecovery.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DisasterRecovery.

        **参数解释**： 启动时间。 **取值范围**： 不涉及。

        :param start_time: The start_time of this DisasterRecovery.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def create_time(self):
        r"""Gets the create_time of this DisasterRecovery.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :return: The create_time of this DisasterRecovery.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DisasterRecovery.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

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
