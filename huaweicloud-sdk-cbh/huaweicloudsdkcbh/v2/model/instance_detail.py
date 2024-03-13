# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetail:

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
        'server_id': 'str',
        'instance_id': 'str',
        'alter_permit': 'bool',
        'enterprise_project_id': 'str',
        'period_num': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'created_time': 'str',
        'upgrade_time': 'int',
        'update': 'str',
        'bastion_version': 'str',
        'az_info': 'InstanceDetailAzInfo',
        'status_info': 'InstanceDetailStatusInfo',
        'resource_info': 'InstanceDetailResourceInfo',
        'network': 'InstanceDetailNetwork',
        'ha_info': 'InstanceDetailHaInfo'
    }

    attribute_map = {
        'name': 'name',
        'server_id': 'server_id',
        'instance_id': 'instance_id',
        'alter_permit': 'alter_permit',
        'enterprise_project_id': 'enterprise_project_id',
        'period_num': 'period_num',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'created_time': 'created_time',
        'upgrade_time': 'upgrade_time',
        'update': 'update',
        'bastion_version': 'bastion_version',
        'az_info': 'az_info',
        'status_info': 'status_info',
        'resource_info': 'resource_info',
        'network': 'network',
        'ha_info': 'ha_info'
    }

    def __init__(self, name=None, server_id=None, instance_id=None, alter_permit=None, enterprise_project_id=None, period_num=None, start_time=None, end_time=None, created_time=None, upgrade_time=None, update=None, bastion_version=None, az_info=None, status_info=None, resource_info=None, network=None, ha_info=None):
        """InstanceDetail

        The model defined in huaweicloud sdk

        :param name: 云堡垒机实例名称。
        :type name: str
        :param server_id: 云堡垒机服务器id。
        :type server_id: str
        :param instance_id: 云堡垒机实例id。
        :type instance_id: str
        :param alter_permit: 云堡垒机实例是否可以扩容。 - true：是 - false：否
        :type alter_permit: bool
        :param enterprise_project_id: 项目ID。
        :type enterprise_project_id: str
        :param period_num: 云堡垒机实例订购周期数。
        :type period_num: str
        :param start_time: 云堡垒机实例开始时间，使用时间戳格式表示。
        :type start_time: str
        :param end_time: 云堡垒机实例结束时间，使用时间戳格式表示。
        :type end_time: str
        :param created_time: 云堡垒机实例创建时间，使用UTC时间表示。
        :type created_time: str
        :param upgrade_time: 云堡垒机实例升级定时时间，使用时间戳格式表示。
        :type upgrade_time: int
        :param update: 云堡垒机实例是否可以升级。 - OLD：当前已是最新版本 - NEW：可以升级小版本 - CROSS_OS：可以跨版本升级 - ROLLBACK：可以回滚
        :type update: str
        :param bastion_version: 云堡垒机实例当前版本。
        :type bastion_version: str
        :param az_info: 
        :type az_info: :class:`huaweicloudsdkcbh.v2.InstanceDetailAzInfo`
        :param status_info: 
        :type status_info: :class:`huaweicloudsdkcbh.v2.InstanceDetailStatusInfo`
        :param resource_info: 
        :type resource_info: :class:`huaweicloudsdkcbh.v2.InstanceDetailResourceInfo`
        :param network: 
        :type network: :class:`huaweicloudsdkcbh.v2.InstanceDetailNetwork`
        :param ha_info: 
        :type ha_info: :class:`huaweicloudsdkcbh.v2.InstanceDetailHaInfo`
        """
        
        

        self._name = None
        self._server_id = None
        self._instance_id = None
        self._alter_permit = None
        self._enterprise_project_id = None
        self._period_num = None
        self._start_time = None
        self._end_time = None
        self._created_time = None
        self._upgrade_time = None
        self._update = None
        self._bastion_version = None
        self._az_info = None
        self._status_info = None
        self._resource_info = None
        self._network = None
        self._ha_info = None
        self.discriminator = None

        self.name = name
        self.server_id = server_id
        self.instance_id = instance_id
        self.alter_permit = alter_permit
        self.enterprise_project_id = enterprise_project_id
        self.period_num = period_num
        self.start_time = start_time
        self.end_time = end_time
        self.created_time = created_time
        if upgrade_time is not None:
            self.upgrade_time = upgrade_time
        self.update = update
        self.bastion_version = bastion_version
        self.az_info = az_info
        self.status_info = status_info
        self.resource_info = resource_info
        self.network = network
        if ha_info is not None:
            self.ha_info = ha_info

    @property
    def name(self):
        """Gets the name of this InstanceDetail.

        云堡垒机实例名称。

        :return: The name of this InstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceDetail.

        云堡垒机实例名称。

        :param name: The name of this InstanceDetail.
        :type name: str
        """
        self._name = name

    @property
    def server_id(self):
        """Gets the server_id of this InstanceDetail.

        云堡垒机服务器id。

        :return: The server_id of this InstanceDetail.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this InstanceDetail.

        云堡垒机服务器id。

        :param server_id: The server_id of this InstanceDetail.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceDetail.

        云堡垒机实例id。

        :return: The instance_id of this InstanceDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceDetail.

        云堡垒机实例id。

        :param instance_id: The instance_id of this InstanceDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def alter_permit(self):
        """Gets the alter_permit of this InstanceDetail.

        云堡垒机实例是否可以扩容。 - true：是 - false：否

        :return: The alter_permit of this InstanceDetail.
        :rtype: bool
        """
        return self._alter_permit

    @alter_permit.setter
    def alter_permit(self, alter_permit):
        """Sets the alter_permit of this InstanceDetail.

        云堡垒机实例是否可以扩容。 - true：是 - false：否

        :param alter_permit: The alter_permit of this InstanceDetail.
        :type alter_permit: bool
        """
        self._alter_permit = alter_permit

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this InstanceDetail.

        项目ID。

        :return: The enterprise_project_id of this InstanceDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this InstanceDetail.

        项目ID。

        :param enterprise_project_id: The enterprise_project_id of this InstanceDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def period_num(self):
        """Gets the period_num of this InstanceDetail.

        云堡垒机实例订购周期数。

        :return: The period_num of this InstanceDetail.
        :rtype: str
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this InstanceDetail.

        云堡垒机实例订购周期数。

        :param period_num: The period_num of this InstanceDetail.
        :type period_num: str
        """
        self._period_num = period_num

    @property
    def start_time(self):
        """Gets the start_time of this InstanceDetail.

        云堡垒机实例开始时间，使用时间戳格式表示。

        :return: The start_time of this InstanceDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InstanceDetail.

        云堡垒机实例开始时间，使用时间戳格式表示。

        :param start_time: The start_time of this InstanceDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this InstanceDetail.

        云堡垒机实例结束时间，使用时间戳格式表示。

        :return: The end_time of this InstanceDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InstanceDetail.

        云堡垒机实例结束时间，使用时间戳格式表示。

        :param end_time: The end_time of this InstanceDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def created_time(self):
        """Gets the created_time of this InstanceDetail.

        云堡垒机实例创建时间，使用UTC时间表示。

        :return: The created_time of this InstanceDetail.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this InstanceDetail.

        云堡垒机实例创建时间，使用UTC时间表示。

        :param created_time: The created_time of this InstanceDetail.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def upgrade_time(self):
        """Gets the upgrade_time of this InstanceDetail.

        云堡垒机实例升级定时时间，使用时间戳格式表示。

        :return: The upgrade_time of this InstanceDetail.
        :rtype: int
        """
        return self._upgrade_time

    @upgrade_time.setter
    def upgrade_time(self, upgrade_time):
        """Sets the upgrade_time of this InstanceDetail.

        云堡垒机实例升级定时时间，使用时间戳格式表示。

        :param upgrade_time: The upgrade_time of this InstanceDetail.
        :type upgrade_time: int
        """
        self._upgrade_time = upgrade_time

    @property
    def update(self):
        """Gets the update of this InstanceDetail.

        云堡垒机实例是否可以升级。 - OLD：当前已是最新版本 - NEW：可以升级小版本 - CROSS_OS：可以跨版本升级 - ROLLBACK：可以回滚

        :return: The update of this InstanceDetail.
        :rtype: str
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this InstanceDetail.

        云堡垒机实例是否可以升级。 - OLD：当前已是最新版本 - NEW：可以升级小版本 - CROSS_OS：可以跨版本升级 - ROLLBACK：可以回滚

        :param update: The update of this InstanceDetail.
        :type update: str
        """
        self._update = update

    @property
    def bastion_version(self):
        """Gets the bastion_version of this InstanceDetail.

        云堡垒机实例当前版本。

        :return: The bastion_version of this InstanceDetail.
        :rtype: str
        """
        return self._bastion_version

    @bastion_version.setter
    def bastion_version(self, bastion_version):
        """Sets the bastion_version of this InstanceDetail.

        云堡垒机实例当前版本。

        :param bastion_version: The bastion_version of this InstanceDetail.
        :type bastion_version: str
        """
        self._bastion_version = bastion_version

    @property
    def az_info(self):
        """Gets the az_info of this InstanceDetail.

        :return: The az_info of this InstanceDetail.
        :rtype: :class:`huaweicloudsdkcbh.v2.InstanceDetailAzInfo`
        """
        return self._az_info

    @az_info.setter
    def az_info(self, az_info):
        """Sets the az_info of this InstanceDetail.

        :param az_info: The az_info of this InstanceDetail.
        :type az_info: :class:`huaweicloudsdkcbh.v2.InstanceDetailAzInfo`
        """
        self._az_info = az_info

    @property
    def status_info(self):
        """Gets the status_info of this InstanceDetail.

        :return: The status_info of this InstanceDetail.
        :rtype: :class:`huaweicloudsdkcbh.v2.InstanceDetailStatusInfo`
        """
        return self._status_info

    @status_info.setter
    def status_info(self, status_info):
        """Sets the status_info of this InstanceDetail.

        :param status_info: The status_info of this InstanceDetail.
        :type status_info: :class:`huaweicloudsdkcbh.v2.InstanceDetailStatusInfo`
        """
        self._status_info = status_info

    @property
    def resource_info(self):
        """Gets the resource_info of this InstanceDetail.

        :return: The resource_info of this InstanceDetail.
        :rtype: :class:`huaweicloudsdkcbh.v2.InstanceDetailResourceInfo`
        """
        return self._resource_info

    @resource_info.setter
    def resource_info(self, resource_info):
        """Sets the resource_info of this InstanceDetail.

        :param resource_info: The resource_info of this InstanceDetail.
        :type resource_info: :class:`huaweicloudsdkcbh.v2.InstanceDetailResourceInfo`
        """
        self._resource_info = resource_info

    @property
    def network(self):
        """Gets the network of this InstanceDetail.

        :return: The network of this InstanceDetail.
        :rtype: :class:`huaweicloudsdkcbh.v2.InstanceDetailNetwork`
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this InstanceDetail.

        :param network: The network of this InstanceDetail.
        :type network: :class:`huaweicloudsdkcbh.v2.InstanceDetailNetwork`
        """
        self._network = network

    @property
    def ha_info(self):
        """Gets the ha_info of this InstanceDetail.

        :return: The ha_info of this InstanceDetail.
        :rtype: :class:`huaweicloudsdkcbh.v2.InstanceDetailHaInfo`
        """
        return self._ha_info

    @ha_info.setter
    def ha_info(self, ha_info):
        """Sets the ha_info of this InstanceDetail.

        :param ha_info: The ha_info of this InstanceDetail.
        :type ha_info: :class:`huaweicloudsdkcbh.v2.InstanceDetailHaInfo`
        """
        self._ha_info = ha_info

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
        if not isinstance(other, InstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
