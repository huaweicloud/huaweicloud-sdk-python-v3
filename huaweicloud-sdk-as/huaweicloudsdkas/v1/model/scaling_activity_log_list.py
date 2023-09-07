# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingActivityLogList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'id': 'str',
        'instance_removed_list': 'str',
        'instance_deleted_list': 'str',
        'instance_added_list': 'str',
        'scaling_value': 'int',
        'description': 'str',
        'instance_value': 'int',
        'desire_value': 'int'
    }

    attribute_map = {
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'id': 'id',
        'instance_removed_list': 'instance_removed_list',
        'instance_deleted_list': 'instance_deleted_list',
        'instance_added_list': 'instance_added_list',
        'scaling_value': 'scaling_value',
        'description': 'description',
        'instance_value': 'instance_value',
        'desire_value': 'desire_value'
    }

    def __init__(self, status=None, start_time=None, end_time=None, id=None, instance_removed_list=None, instance_deleted_list=None, instance_added_list=None, scaling_value=None, description=None, instance_value=None, desire_value=None):
        """ScalingActivityLogList

        The model defined in huaweicloud sdk

        :param status: 伸缩活动状态：SUCCESS：成功。FAIL：失败。DOING：伸缩过程中。
        :type status: str
        :param start_time: 伸缩活动触发时间，遵循UTC时间。
        :type start_time: datetime
        :param end_time: 伸缩活动结束时间，遵循UTC时间。
        :type end_time: datetime
        :param id: 伸缩活动日志ID。
        :type id: str
        :param instance_removed_list: 完成伸缩活动且只被移出弹性伸缩组的云服务器名称列表，云服务器名之间以逗号分隔。
        :type instance_removed_list: str
        :param instance_deleted_list: 完成伸缩活动且被移出弹性伸缩组并删除的云服务器名称列表，云服务器名之间以逗号分隔。
        :type instance_deleted_list: str
        :param instance_added_list: 完成伸缩活动且被加入弹性伸缩组的云服务器名称列表，云服务器名之间以逗号分割。
        :type instance_added_list: str
        :param scaling_value: 伸缩活动中变化（增加或减少）的云服务器数量。
        :type scaling_value: int
        :param description: 伸缩活动的描述信息。
        :type description: str
        :param instance_value: 伸缩组当前instance值。
        :type instance_value: int
        :param desire_value: 伸缩活动最终desire值。
        :type desire_value: int
        """
        
        

        self._status = None
        self._start_time = None
        self._end_time = None
        self._id = None
        self._instance_removed_list = None
        self._instance_deleted_list = None
        self._instance_added_list = None
        self._scaling_value = None
        self._description = None
        self._instance_value = None
        self._desire_value = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if id is not None:
            self.id = id
        if instance_removed_list is not None:
            self.instance_removed_list = instance_removed_list
        if instance_deleted_list is not None:
            self.instance_deleted_list = instance_deleted_list
        if instance_added_list is not None:
            self.instance_added_list = instance_added_list
        if scaling_value is not None:
            self.scaling_value = scaling_value
        if description is not None:
            self.description = description
        if instance_value is not None:
            self.instance_value = instance_value
        if desire_value is not None:
            self.desire_value = desire_value

    @property
    def status(self):
        """Gets the status of this ScalingActivityLogList.

        伸缩活动状态：SUCCESS：成功。FAIL：失败。DOING：伸缩过程中。

        :return: The status of this ScalingActivityLogList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScalingActivityLogList.

        伸缩活动状态：SUCCESS：成功。FAIL：失败。DOING：伸缩过程中。

        :param status: The status of this ScalingActivityLogList.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this ScalingActivityLogList.

        伸缩活动触发时间，遵循UTC时间。

        :return: The start_time of this ScalingActivityLogList.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScalingActivityLogList.

        伸缩活动触发时间，遵循UTC时间。

        :param start_time: The start_time of this ScalingActivityLogList.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ScalingActivityLogList.

        伸缩活动结束时间，遵循UTC时间。

        :return: The end_time of this ScalingActivityLogList.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScalingActivityLogList.

        伸缩活动结束时间，遵循UTC时间。

        :param end_time: The end_time of this ScalingActivityLogList.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def id(self):
        """Gets the id of this ScalingActivityLogList.

        伸缩活动日志ID。

        :return: The id of this ScalingActivityLogList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScalingActivityLogList.

        伸缩活动日志ID。

        :param id: The id of this ScalingActivityLogList.
        :type id: str
        """
        self._id = id

    @property
    def instance_removed_list(self):
        """Gets the instance_removed_list of this ScalingActivityLogList.

        完成伸缩活动且只被移出弹性伸缩组的云服务器名称列表，云服务器名之间以逗号分隔。

        :return: The instance_removed_list of this ScalingActivityLogList.
        :rtype: str
        """
        return self._instance_removed_list

    @instance_removed_list.setter
    def instance_removed_list(self, instance_removed_list):
        """Sets the instance_removed_list of this ScalingActivityLogList.

        完成伸缩活动且只被移出弹性伸缩组的云服务器名称列表，云服务器名之间以逗号分隔。

        :param instance_removed_list: The instance_removed_list of this ScalingActivityLogList.
        :type instance_removed_list: str
        """
        self._instance_removed_list = instance_removed_list

    @property
    def instance_deleted_list(self):
        """Gets the instance_deleted_list of this ScalingActivityLogList.

        完成伸缩活动且被移出弹性伸缩组并删除的云服务器名称列表，云服务器名之间以逗号分隔。

        :return: The instance_deleted_list of this ScalingActivityLogList.
        :rtype: str
        """
        return self._instance_deleted_list

    @instance_deleted_list.setter
    def instance_deleted_list(self, instance_deleted_list):
        """Sets the instance_deleted_list of this ScalingActivityLogList.

        完成伸缩活动且被移出弹性伸缩组并删除的云服务器名称列表，云服务器名之间以逗号分隔。

        :param instance_deleted_list: The instance_deleted_list of this ScalingActivityLogList.
        :type instance_deleted_list: str
        """
        self._instance_deleted_list = instance_deleted_list

    @property
    def instance_added_list(self):
        """Gets the instance_added_list of this ScalingActivityLogList.

        完成伸缩活动且被加入弹性伸缩组的云服务器名称列表，云服务器名之间以逗号分割。

        :return: The instance_added_list of this ScalingActivityLogList.
        :rtype: str
        """
        return self._instance_added_list

    @instance_added_list.setter
    def instance_added_list(self, instance_added_list):
        """Sets the instance_added_list of this ScalingActivityLogList.

        完成伸缩活动且被加入弹性伸缩组的云服务器名称列表，云服务器名之间以逗号分割。

        :param instance_added_list: The instance_added_list of this ScalingActivityLogList.
        :type instance_added_list: str
        """
        self._instance_added_list = instance_added_list

    @property
    def scaling_value(self):
        """Gets the scaling_value of this ScalingActivityLogList.

        伸缩活动中变化（增加或减少）的云服务器数量。

        :return: The scaling_value of this ScalingActivityLogList.
        :rtype: int
        """
        return self._scaling_value

    @scaling_value.setter
    def scaling_value(self, scaling_value):
        """Sets the scaling_value of this ScalingActivityLogList.

        伸缩活动中变化（增加或减少）的云服务器数量。

        :param scaling_value: The scaling_value of this ScalingActivityLogList.
        :type scaling_value: int
        """
        self._scaling_value = scaling_value

    @property
    def description(self):
        """Gets the description of this ScalingActivityLogList.

        伸缩活动的描述信息。

        :return: The description of this ScalingActivityLogList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScalingActivityLogList.

        伸缩活动的描述信息。

        :param description: The description of this ScalingActivityLogList.
        :type description: str
        """
        self._description = description

    @property
    def instance_value(self):
        """Gets the instance_value of this ScalingActivityLogList.

        伸缩组当前instance值。

        :return: The instance_value of this ScalingActivityLogList.
        :rtype: int
        """
        return self._instance_value

    @instance_value.setter
    def instance_value(self, instance_value):
        """Sets the instance_value of this ScalingActivityLogList.

        伸缩组当前instance值。

        :param instance_value: The instance_value of this ScalingActivityLogList.
        :type instance_value: int
        """
        self._instance_value = instance_value

    @property
    def desire_value(self):
        """Gets the desire_value of this ScalingActivityLogList.

        伸缩活动最终desire值。

        :return: The desire_value of this ScalingActivityLogList.
        :rtype: int
        """
        return self._desire_value

    @desire_value.setter
    def desire_value(self, desire_value):
        """Sets the desire_value of this ScalingActivityLogList.

        伸缩活动最终desire值。

        :param desire_value: The desire_value of this ScalingActivityLogList.
        :type desire_value: int
        """
        self._desire_value = desire_value

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
        if not isinstance(other, ScalingActivityLogList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
