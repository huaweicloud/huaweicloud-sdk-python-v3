# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchoverTestRecord:

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
        'tenant_id': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'operation': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'operate_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'operation': 'operation',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'operate_status': 'operate_status'
    }

    def __init__(self, id=None, tenant_id=None, resource_id=None, resource_type=None, operation=None, start_time=None, end_time=None, operate_status=None):
        r"""SwitchoverTestRecord

        The model defined in huaweicloud sdk

        :param id: 倒换测试记录的唯一标识
        :type id: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param resource_id: 倒换测试的资源对象ID
        :type resource_id: str
        :param resource_type: 倒换测试的资源对象类型
        :type resource_type: str
        :param operation: shutdown, undo_shutdown表示倒换测试操作类型
        :type operation: str
        :param start_time: 倒换测试操作的开始时间。采用UTC时间格式，格式为：yyyy-MM-ddTHH:mm:ss.SSSZ
        :type start_time: datetime
        :param end_time: 倒换测试操作的结束时间。采用UTC时间格式，格式为：yyyy-MM-ddTHH:mm:ss.SSSZ
        :type end_time: datetime
        :param operate_status: 倒换测试状态记录 STARTING: 初始状态 INPROGRESS: 配置下发中 COMPLETE: 配置下发完成 ERROR: 配置下发失败
        :type operate_status: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._resource_id = None
        self._resource_type = None
        self._operation = None
        self._start_time = None
        self._end_time = None
        self._operate_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if operation is not None:
            self.operation = operation
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if operate_status is not None:
            self.operate_status = operate_status

    @property
    def id(self):
        r"""Gets the id of this SwitchoverTestRecord.

        倒换测试记录的唯一标识

        :return: The id of this SwitchoverTestRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SwitchoverTestRecord.

        倒换测试记录的唯一标识

        :param id: The id of this SwitchoverTestRecord.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this SwitchoverTestRecord.

        租户ID

        :return: The tenant_id of this SwitchoverTestRecord.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this SwitchoverTestRecord.

        租户ID

        :param tenant_id: The tenant_id of this SwitchoverTestRecord.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this SwitchoverTestRecord.

        倒换测试的资源对象ID

        :return: The resource_id of this SwitchoverTestRecord.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this SwitchoverTestRecord.

        倒换测试的资源对象ID

        :param resource_id: The resource_id of this SwitchoverTestRecord.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this SwitchoverTestRecord.

        倒换测试的资源对象类型

        :return: The resource_type of this SwitchoverTestRecord.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this SwitchoverTestRecord.

        倒换测试的资源对象类型

        :param resource_type: The resource_type of this SwitchoverTestRecord.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def operation(self):
        r"""Gets the operation of this SwitchoverTestRecord.

        shutdown, undo_shutdown表示倒换测试操作类型

        :return: The operation of this SwitchoverTestRecord.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this SwitchoverTestRecord.

        shutdown, undo_shutdown表示倒换测试操作类型

        :param operation: The operation of this SwitchoverTestRecord.
        :type operation: str
        """
        self._operation = operation

    @property
    def start_time(self):
        r"""Gets the start_time of this SwitchoverTestRecord.

        倒换测试操作的开始时间。采用UTC时间格式，格式为：yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The start_time of this SwitchoverTestRecord.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SwitchoverTestRecord.

        倒换测试操作的开始时间。采用UTC时间格式，格式为：yyyy-MM-ddTHH:mm:ss.SSSZ

        :param start_time: The start_time of this SwitchoverTestRecord.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SwitchoverTestRecord.

        倒换测试操作的结束时间。采用UTC时间格式，格式为：yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The end_time of this SwitchoverTestRecord.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SwitchoverTestRecord.

        倒换测试操作的结束时间。采用UTC时间格式，格式为：yyyy-MM-ddTHH:mm:ss.SSSZ

        :param end_time: The end_time of this SwitchoverTestRecord.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def operate_status(self):
        r"""Gets the operate_status of this SwitchoverTestRecord.

        倒换测试状态记录 STARTING: 初始状态 INPROGRESS: 配置下发中 COMPLETE: 配置下发完成 ERROR: 配置下发失败

        :return: The operate_status of this SwitchoverTestRecord.
        :rtype: str
        """
        return self._operate_status

    @operate_status.setter
    def operate_status(self, operate_status):
        r"""Sets the operate_status of this SwitchoverTestRecord.

        倒换测试状态记录 STARTING: 初始状态 INPROGRESS: 配置下发中 COMPLETE: 配置下发完成 ERROR: 配置下发失败

        :param operate_status: The operate_status of this SwitchoverTestRecord.
        :type operate_status: str
        """
        self._operate_status = operate_status

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
        if not isinstance(other, SwitchoverTestRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
