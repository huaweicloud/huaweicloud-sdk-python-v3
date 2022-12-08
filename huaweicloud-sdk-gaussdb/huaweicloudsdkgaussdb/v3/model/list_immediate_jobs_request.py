# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImmediateJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'status': 'str',
        'job_name': 'str',
        'job_id': 'str',
        'offset': 'str',
        'limit': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'status': 'status',
        'job_name': 'job_name',
        'job_id': 'job_id',
        'offset': 'offset',
        'limit': 'limit',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, x_language=None, status=None, job_name=None, job_id=None, offset=None, limit=None, start_time=None, end_time=None):
        """ListImmediateJobsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param status: 任务执行状态。 取值： - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。 - 值为“Pending”，表示任务未执行。
        :type status: str
        :param job_name: 任务名称。取值有：  - \&quot;CreateGaussDBforMySQLInstance\&quot;表示创建实例。  - \&quot;RestoreGaussDBforMySQLNewInstance\&quot;表示恢复新实例。  - \&quot;AddGaussDBforMySQLNodes\&quot;表示添加节点。  - \&quot;DeleteGaussDBforMySQLNode\&quot;表示删除节点。  - \&quot;RebootGaussDBforMySQLInstance\&quot;表示重启实例。  - \&quot;ModifyGaussDBforMySQLPort\&quot;表示修改实例端口。  - \&quot;ModifyGaussDBforMySQLSecurityGroup\&quot;表示修改实例安全组。  - \&quot;ResizeGaussDBforMySQLFlavor\&quot;表示实例规格变更。  - \&quot;SwitchoverGaussDBforMySQLMasterNode\&quot;表示只读升主。  - \&quot;GaussDBforMySQLBindEIP\&quot;表示绑定弹性公网IP。  - \&quot;GaussDBforMySQLUnbindEIP\&quot;表示解绑弹性公网IP。  - \&quot;RenameGaussDBforMySQLInstance\&quot;表示修改实例名称。  - \&quot;DeleteGaussDBforMySQLInstance\&quot;表示删除实例集群。  - \&quot;UpgradeGaussDBforMySQLDatabaseVersion\&quot;表示版本升级。  - \&quot;EnlargeGaussDBforMySQLProxy\&quot;表示实例的数据库代理节点扩容。  - \&quot;OpenGaussDBforMySQLProxy\&quot;表示开启实例的数据库代理。  - \&quot;CloseGaussDBforMySQLProxy\&quot;表示关闭实例的数据库代理。  - \&quot;GaussdbforMySQLModifyProxyIp\&quot;表示修改数据库代理ip。  - \&quot;ScaleGaussDBforMySQLProxy\&quot;表示实例的数据库代理节点规格变更。  - \&quot;GaussDBforMySQLModifyInstanceMetricExtend\&quot;表示实例秒级监控。  - \&quot;GaussDBforMySQLModifyInstanceDataVip\&quot;表示修改实例数据Vip。  - \&quot;GaussDBforMySQLSwitchSSL\&quot;表示切换实例SSL开关。  - \&quot;GaussDBforMySQLModifyProxyConsist\&quot;表示修改代理一致性。  - \&quot;GaussDBforMySQLModifyProxyWeight\&quot;表示修改代理权重。
        :type job_name: str
        :param job_id: 任务ID。
        :type job_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为1，必须为数字，不能为负数。
        :type offset: str
        :param limit: 查询记录数。默认为10，取值为10、20、50。
        :type limit: str
        :param start_time: 起始时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type start_time: str
        :param end_time: 结束时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type end_time: str
        """
        
        

        self._x_language = None
        self._status = None
        self._job_name = None
        self._job_id = None
        self._offset = None
        self._limit = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if status is not None:
            self.status = status
        if job_name is not None:
            self.job_name = job_name
        if job_id is not None:
            self.job_id = job_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def x_language(self):
        """Gets the x_language of this ListImmediateJobsRequest.

        语言。

        :return: The x_language of this ListImmediateJobsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListImmediateJobsRequest.

        语言。

        :param x_language: The x_language of this ListImmediateJobsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def status(self):
        """Gets the status of this ListImmediateJobsRequest.

        任务执行状态。 取值： - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。 - 值为“Pending”，表示任务未执行。

        :return: The status of this ListImmediateJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListImmediateJobsRequest.

        任务执行状态。 取值： - 值为“Running”，表示任务正在执行。 - 值为“Completed”，表示任务执行成功。 - 值为“Failed”，表示任务执行失败。 - 值为“Pending”，表示任务未执行。

        :param status: The status of this ListImmediateJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def job_name(self):
        """Gets the job_name of this ListImmediateJobsRequest.

        任务名称。取值有：  - \"CreateGaussDBforMySQLInstance\"表示创建实例。  - \"RestoreGaussDBforMySQLNewInstance\"表示恢复新实例。  - \"AddGaussDBforMySQLNodes\"表示添加节点。  - \"DeleteGaussDBforMySQLNode\"表示删除节点。  - \"RebootGaussDBforMySQLInstance\"表示重启实例。  - \"ModifyGaussDBforMySQLPort\"表示修改实例端口。  - \"ModifyGaussDBforMySQLSecurityGroup\"表示修改实例安全组。  - \"ResizeGaussDBforMySQLFlavor\"表示实例规格变更。  - \"SwitchoverGaussDBforMySQLMasterNode\"表示只读升主。  - \"GaussDBforMySQLBindEIP\"表示绑定弹性公网IP。  - \"GaussDBforMySQLUnbindEIP\"表示解绑弹性公网IP。  - \"RenameGaussDBforMySQLInstance\"表示修改实例名称。  - \"DeleteGaussDBforMySQLInstance\"表示删除实例集群。  - \"UpgradeGaussDBforMySQLDatabaseVersion\"表示版本升级。  - \"EnlargeGaussDBforMySQLProxy\"表示实例的数据库代理节点扩容。  - \"OpenGaussDBforMySQLProxy\"表示开启实例的数据库代理。  - \"CloseGaussDBforMySQLProxy\"表示关闭实例的数据库代理。  - \"GaussdbforMySQLModifyProxyIp\"表示修改数据库代理ip。  - \"ScaleGaussDBforMySQLProxy\"表示实例的数据库代理节点规格变更。  - \"GaussDBforMySQLModifyInstanceMetricExtend\"表示实例秒级监控。  - \"GaussDBforMySQLModifyInstanceDataVip\"表示修改实例数据Vip。  - \"GaussDBforMySQLSwitchSSL\"表示切换实例SSL开关。  - \"GaussDBforMySQLModifyProxyConsist\"表示修改代理一致性。  - \"GaussDBforMySQLModifyProxyWeight\"表示修改代理权重。

        :return: The job_name of this ListImmediateJobsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ListImmediateJobsRequest.

        任务名称。取值有：  - \"CreateGaussDBforMySQLInstance\"表示创建实例。  - \"RestoreGaussDBforMySQLNewInstance\"表示恢复新实例。  - \"AddGaussDBforMySQLNodes\"表示添加节点。  - \"DeleteGaussDBforMySQLNode\"表示删除节点。  - \"RebootGaussDBforMySQLInstance\"表示重启实例。  - \"ModifyGaussDBforMySQLPort\"表示修改实例端口。  - \"ModifyGaussDBforMySQLSecurityGroup\"表示修改实例安全组。  - \"ResizeGaussDBforMySQLFlavor\"表示实例规格变更。  - \"SwitchoverGaussDBforMySQLMasterNode\"表示只读升主。  - \"GaussDBforMySQLBindEIP\"表示绑定弹性公网IP。  - \"GaussDBforMySQLUnbindEIP\"表示解绑弹性公网IP。  - \"RenameGaussDBforMySQLInstance\"表示修改实例名称。  - \"DeleteGaussDBforMySQLInstance\"表示删除实例集群。  - \"UpgradeGaussDBforMySQLDatabaseVersion\"表示版本升级。  - \"EnlargeGaussDBforMySQLProxy\"表示实例的数据库代理节点扩容。  - \"OpenGaussDBforMySQLProxy\"表示开启实例的数据库代理。  - \"CloseGaussDBforMySQLProxy\"表示关闭实例的数据库代理。  - \"GaussdbforMySQLModifyProxyIp\"表示修改数据库代理ip。  - \"ScaleGaussDBforMySQLProxy\"表示实例的数据库代理节点规格变更。  - \"GaussDBforMySQLModifyInstanceMetricExtend\"表示实例秒级监控。  - \"GaussDBforMySQLModifyInstanceDataVip\"表示修改实例数据Vip。  - \"GaussDBforMySQLSwitchSSL\"表示切换实例SSL开关。  - \"GaussDBforMySQLModifyProxyConsist\"表示修改代理一致性。  - \"GaussDBforMySQLModifyProxyWeight\"表示修改代理权重。

        :param job_name: The job_name of this ListImmediateJobsRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_id(self):
        """Gets the job_id of this ListImmediateJobsRequest.

        任务ID。

        :return: The job_id of this ListImmediateJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListImmediateJobsRequest.

        任务ID。

        :param job_id: The job_id of this ListImmediateJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def offset(self):
        """Gets the offset of this ListImmediateJobsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为1，必须为数字，不能为负数。

        :return: The offset of this ListImmediateJobsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListImmediateJobsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为1，必须为数字，不能为负数。

        :param offset: The offset of this ListImmediateJobsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListImmediateJobsRequest.

        查询记录数。默认为10，取值为10、20、50。

        :return: The limit of this ListImmediateJobsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListImmediateJobsRequest.

        查询记录数。默认为10，取值为10、20、50。

        :param limit: The limit of this ListImmediateJobsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def start_time(self):
        """Gets the start_time of this ListImmediateJobsRequest.

        起始时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The start_time of this ListImmediateJobsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListImmediateJobsRequest.

        起始时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param start_time: The start_time of this ListImmediateJobsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListImmediateJobsRequest.

        结束时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The end_time of this ListImmediateJobsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListImmediateJobsRequest.

        结束时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param end_time: The end_time of this ListImmediateJobsRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListImmediateJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
