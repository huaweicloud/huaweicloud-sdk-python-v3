# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentOperateLogV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'incident_log_id': 'str',
        'incident_id': 'str',
        'operate_type': 'int',
        'operator_type': 'int',
        'operator_id': 'str',
        'operator_name': 'str',
        'operate_desc': 'str',
        'operate_time': 'str',
        'timestamp_operate_time': 'datetime'
    }

    attribute_map = {
        'incident_log_id': 'incident_log_id',
        'incident_id': 'incident_id',
        'operate_type': 'operate_type',
        'operator_type': 'operator_type',
        'operator_id': 'operator_id',
        'operator_name': 'operator_name',
        'operate_desc': 'operate_desc',
        'operate_time': 'operate_time',
        'timestamp_operate_time': 'timestamp_operate_time'
    }

    def __init__(self, incident_log_id=None, incident_id=None, operate_type=None, operator_type=None, operator_id=None, operator_name=None, operate_desc=None, operate_time=None, timestamp_operate_time=None):
        """IncidentOperateLogV2

        The model defined in huaweicloud sdk

        :param incident_log_id: 工单日志id
        :type incident_log_id: str
        :param incident_id: 工单id
        :type incident_id: str
        :param operate_type: 操作类型
        :type operate_type: int
        :param operator_type: 操作员类型
        :type operator_type: int
        :param operator_id: 操作员id
        :type operator_id: str
        :param operator_name: 操作员名称
        :type operator_name: str
        :param operate_desc: 操作描述
        :type operate_desc: str
        :param operate_time: 操作时间
        :type operate_time: str
        :param timestamp_operate_time: 工单操作时间
        :type timestamp_operate_time: datetime
        """
        
        

        self._incident_log_id = None
        self._incident_id = None
        self._operate_type = None
        self._operator_type = None
        self._operator_id = None
        self._operator_name = None
        self._operate_desc = None
        self._operate_time = None
        self._timestamp_operate_time = None
        self.discriminator = None

        if incident_log_id is not None:
            self.incident_log_id = incident_log_id
        if incident_id is not None:
            self.incident_id = incident_id
        if operate_type is not None:
            self.operate_type = operate_type
        if operator_type is not None:
            self.operator_type = operator_type
        if operator_id is not None:
            self.operator_id = operator_id
        if operator_name is not None:
            self.operator_name = operator_name
        if operate_desc is not None:
            self.operate_desc = operate_desc
        if operate_time is not None:
            self.operate_time = operate_time
        if timestamp_operate_time is not None:
            self.timestamp_operate_time = timestamp_operate_time

    @property
    def incident_log_id(self):
        """Gets the incident_log_id of this IncidentOperateLogV2.

        工单日志id

        :return: The incident_log_id of this IncidentOperateLogV2.
        :rtype: str
        """
        return self._incident_log_id

    @incident_log_id.setter
    def incident_log_id(self, incident_log_id):
        """Sets the incident_log_id of this IncidentOperateLogV2.

        工单日志id

        :param incident_log_id: The incident_log_id of this IncidentOperateLogV2.
        :type incident_log_id: str
        """
        self._incident_log_id = incident_log_id

    @property
    def incident_id(self):
        """Gets the incident_id of this IncidentOperateLogV2.

        工单id

        :return: The incident_id of this IncidentOperateLogV2.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this IncidentOperateLogV2.

        工单id

        :param incident_id: The incident_id of this IncidentOperateLogV2.
        :type incident_id: str
        """
        self._incident_id = incident_id

    @property
    def operate_type(self):
        """Gets the operate_type of this IncidentOperateLogV2.

        操作类型

        :return: The operate_type of this IncidentOperateLogV2.
        :rtype: int
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this IncidentOperateLogV2.

        操作类型

        :param operate_type: The operate_type of this IncidentOperateLogV2.
        :type operate_type: int
        """
        self._operate_type = operate_type

    @property
    def operator_type(self):
        """Gets the operator_type of this IncidentOperateLogV2.

        操作员类型

        :return: The operator_type of this IncidentOperateLogV2.
        :rtype: int
        """
        return self._operator_type

    @operator_type.setter
    def operator_type(self, operator_type):
        """Sets the operator_type of this IncidentOperateLogV2.

        操作员类型

        :param operator_type: The operator_type of this IncidentOperateLogV2.
        :type operator_type: int
        """
        self._operator_type = operator_type

    @property
    def operator_id(self):
        """Gets the operator_id of this IncidentOperateLogV2.

        操作员id

        :return: The operator_id of this IncidentOperateLogV2.
        :rtype: str
        """
        return self._operator_id

    @operator_id.setter
    def operator_id(self, operator_id):
        """Sets the operator_id of this IncidentOperateLogV2.

        操作员id

        :param operator_id: The operator_id of this IncidentOperateLogV2.
        :type operator_id: str
        """
        self._operator_id = operator_id

    @property
    def operator_name(self):
        """Gets the operator_name of this IncidentOperateLogV2.

        操作员名称

        :return: The operator_name of this IncidentOperateLogV2.
        :rtype: str
        """
        return self._operator_name

    @operator_name.setter
    def operator_name(self, operator_name):
        """Sets the operator_name of this IncidentOperateLogV2.

        操作员名称

        :param operator_name: The operator_name of this IncidentOperateLogV2.
        :type operator_name: str
        """
        self._operator_name = operator_name

    @property
    def operate_desc(self):
        """Gets the operate_desc of this IncidentOperateLogV2.

        操作描述

        :return: The operate_desc of this IncidentOperateLogV2.
        :rtype: str
        """
        return self._operate_desc

    @operate_desc.setter
    def operate_desc(self, operate_desc):
        """Sets the operate_desc of this IncidentOperateLogV2.

        操作描述

        :param operate_desc: The operate_desc of this IncidentOperateLogV2.
        :type operate_desc: str
        """
        self._operate_desc = operate_desc

    @property
    def operate_time(self):
        """Gets the operate_time of this IncidentOperateLogV2.

        操作时间

        :return: The operate_time of this IncidentOperateLogV2.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this IncidentOperateLogV2.

        操作时间

        :param operate_time: The operate_time of this IncidentOperateLogV2.
        :type operate_time: str
        """
        self._operate_time = operate_time

    @property
    def timestamp_operate_time(self):
        """Gets the timestamp_operate_time of this IncidentOperateLogV2.

        工单操作时间

        :return: The timestamp_operate_time of this IncidentOperateLogV2.
        :rtype: datetime
        """
        return self._timestamp_operate_time

    @timestamp_operate_time.setter
    def timestamp_operate_time(self, timestamp_operate_time):
        """Sets the timestamp_operate_time of this IncidentOperateLogV2.

        工单操作时间

        :param timestamp_operate_time: The timestamp_operate_time of this IncidentOperateLogV2.
        :type timestamp_operate_time: datetime
        """
        self._timestamp_operate_time = timestamp_operate_time

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
        if not isinstance(other, IncidentOperateLogV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
