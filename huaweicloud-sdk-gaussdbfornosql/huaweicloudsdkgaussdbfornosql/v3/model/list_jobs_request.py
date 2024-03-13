# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

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
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'id': 'id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, id=None, start_time=None, end_time=None, status=None, name=None, offset=None, limit=None):
        """ListJobsRequest

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param start_time: 查询开始时间，默认当前时间往前30天，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始，Z指时区偏移量
        :type start_time: str
        :param end_time: 查询结束时间，默认当前时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间，时间跨度不超过30天。 其中，T指某个时间的开始，Z指时区偏移量。
        :type end_time: str
        :param status: 任务状态： 取值为“Running”为执行中； 取值为“Completed”为完成； 取值为“Failed” 为失败。
        :type status: str
        :param name: 任务名称。对应取值如下： - \&quot;CreateInstance\&quot;：创建实例 - \&quot;RestoreNewInstance\&quot;：恢复到新实例 - \&quot;EnlargeInstance\&quot;：扩容实例 - \&quot;ReduceInstance\&quot;：缩容实例 - \&quot;RestartInstance\&quot;：重启实例 - \&quot;RestartNode\&quot;：重启节点 - \&quot;EnlargeInstanceVolume\&quot;：扩容实例磁盘 - \&quot;ReduceInstanceVolume\&quot;：缩容实例磁盘 - \&quot;ResizeInstance\&quot;：规格变更实例 - \&quot;UpgradeDbVersion\&quot;：升级数据库版本 - \&quot;BindPublicIP\&quot;：绑定公网IP - \&quot;UnbindPublicIP\&quot;：解绑公网IP - \&quot;DeleteInstance\&quot;：删除实例 - \&quot;EnlargeInstanceColdVolume\&quot;：扩容实例冷存储 - \&quot;AddInstanceColdVolume\&quot;：增加实例冷存储 - \&quot;ModifySecurityGroup\&quot;：修改安全组 - \&quot;ModifyCcmCert\&quot;：修改CCM证书 - \&quot;ModifyPort\&quot;：修改端口 - \&quot;ConstructDisasterRecovery\&quot;：构造容灾关系 - \&quot;DeConstructDisasterRecovery\&quot;：解除容灾关系 - \&quot;SwitchOverDisasterRecovery\&quot;：切换容灾关系 - \&quot;BuildBiActiveInstance\&quot;：构建双活实例 - \&quot;ReleaseBiActiveInstance\&quot;：解除双活实例关系 - \&quot;BackupInstance\&quot;：备份实例
        :type name: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。取值 10 20 50 ，默认为50。
        :type limit: int
        """
        
        

        self._id = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def id(self):
        """Gets the id of this ListJobsRequest.

        任务ID。

        :return: The id of this ListJobsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListJobsRequest.

        任务ID。

        :param id: The id of this ListJobsRequest.
        :type id: str
        """
        self._id = id

    @property
    def start_time(self):
        """Gets the start_time of this ListJobsRequest.

        查询开始时间，默认当前时间往前30天，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始，Z指时区偏移量

        :return: The start_time of this ListJobsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListJobsRequest.

        查询开始时间，默认当前时间往前30天，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始，Z指时区偏移量

        :param start_time: The start_time of this ListJobsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListJobsRequest.

        查询结束时间，默认当前时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间，时间跨度不超过30天。 其中，T指某个时间的开始，Z指时区偏移量。

        :return: The end_time of this ListJobsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListJobsRequest.

        查询结束时间，默认当前时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间，时间跨度不超过30天。 其中，T指某个时间的开始，Z指时区偏移量。

        :param end_time: The end_time of this ListJobsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ListJobsRequest.

        任务状态： 取值为“Running”为执行中； 取值为“Completed”为完成； 取值为“Failed” 为失败。

        :return: The status of this ListJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListJobsRequest.

        任务状态： 取值为“Running”为执行中； 取值为“Completed”为完成； 取值为“Failed” 为失败。

        :param status: The status of this ListJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this ListJobsRequest.

        任务名称。对应取值如下： - \"CreateInstance\"：创建实例 - \"RestoreNewInstance\"：恢复到新实例 - \"EnlargeInstance\"：扩容实例 - \"ReduceInstance\"：缩容实例 - \"RestartInstance\"：重启实例 - \"RestartNode\"：重启节点 - \"EnlargeInstanceVolume\"：扩容实例磁盘 - \"ReduceInstanceVolume\"：缩容实例磁盘 - \"ResizeInstance\"：规格变更实例 - \"UpgradeDbVersion\"：升级数据库版本 - \"BindPublicIP\"：绑定公网IP - \"UnbindPublicIP\"：解绑公网IP - \"DeleteInstance\"：删除实例 - \"EnlargeInstanceColdVolume\"：扩容实例冷存储 - \"AddInstanceColdVolume\"：增加实例冷存储 - \"ModifySecurityGroup\"：修改安全组 - \"ModifyCcmCert\"：修改CCM证书 - \"ModifyPort\"：修改端口 - \"ConstructDisasterRecovery\"：构造容灾关系 - \"DeConstructDisasterRecovery\"：解除容灾关系 - \"SwitchOverDisasterRecovery\"：切换容灾关系 - \"BuildBiActiveInstance\"：构建双活实例 - \"ReleaseBiActiveInstance\"：解除双活实例关系 - \"BackupInstance\"：备份实例

        :return: The name of this ListJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListJobsRequest.

        任务名称。对应取值如下： - \"CreateInstance\"：创建实例 - \"RestoreNewInstance\"：恢复到新实例 - \"EnlargeInstance\"：扩容实例 - \"ReduceInstance\"：缩容实例 - \"RestartInstance\"：重启实例 - \"RestartNode\"：重启节点 - \"EnlargeInstanceVolume\"：扩容实例磁盘 - \"ReduceInstanceVolume\"：缩容实例磁盘 - \"ResizeInstance\"：规格变更实例 - \"UpgradeDbVersion\"：升级数据库版本 - \"BindPublicIP\"：绑定公网IP - \"UnbindPublicIP\"：解绑公网IP - \"DeleteInstance\"：删除实例 - \"EnlargeInstanceColdVolume\"：扩容实例冷存储 - \"AddInstanceColdVolume\"：增加实例冷存储 - \"ModifySecurityGroup\"：修改安全组 - \"ModifyCcmCert\"：修改CCM证书 - \"ModifyPort\"：修改端口 - \"ConstructDisasterRecovery\"：构造容灾关系 - \"DeConstructDisasterRecovery\"：解除容灾关系 - \"SwitchOverDisasterRecovery\"：切换容灾关系 - \"BuildBiActiveInstance\"：构建双活实例 - \"ReleaseBiActiveInstance\"：解除双活实例关系 - \"BackupInstance\"：备份实例

        :param name: The name of this ListJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListJobsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListJobsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListJobsRequest.

        查询记录数。取值 10 20 50 ，默认为50。

        :return: The limit of this ListJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListJobsRequest.

        查询记录数。取值 10 20 50 ，默认为50。

        :param limit: The limit of this ListJobsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
