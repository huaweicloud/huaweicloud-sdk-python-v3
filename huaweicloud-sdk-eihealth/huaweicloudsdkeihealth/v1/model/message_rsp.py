# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MessageRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_type': 'str',
        'eihealth_project_name': 'str',
        'resource_type': 'str',
        'resource_name': 'str',
        'operator': 'str',
        'status': 'str',
        'operate_time': 'str',
        'message_detail': 'str'
    }

    attribute_map = {
        'message_type': 'message_type',
        'eihealth_project_name': 'eihealth_project_name',
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'operator': 'operator',
        'status': 'status',
        'operate_time': 'operate_time',
        'message_detail': 'message_detail'
    }

    def __init__(self, message_type=None, eihealth_project_name=None, resource_type=None, resource_name=None, operator=None, status=None, operate_time=None, message_detail=None):
        """MessageRsp

        The model defined in huaweicloud sdk

        :param message_type: 消息类型
        :type message_type: str
        :param eihealth_project_name: 项目名称
        :type eihealth_project_name: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param operator: 操作用户
        :type operator: str
        :param status: 状态
        :type status: str
        :param operate_time: 操作时间
        :type operate_time: str
        :param message_detail: 详情
        :type message_detail: str
        """
        
        

        self._message_type = None
        self._eihealth_project_name = None
        self._resource_type = None
        self._resource_name = None
        self._operator = None
        self._status = None
        self._operate_time = None
        self._message_detail = None
        self.discriminator = None

        if message_type is not None:
            self.message_type = message_type
        if eihealth_project_name is not None:
            self.eihealth_project_name = eihealth_project_name
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if operator is not None:
            self.operator = operator
        if status is not None:
            self.status = status
        if operate_time is not None:
            self.operate_time = operate_time
        if message_detail is not None:
            self.message_detail = message_detail

    @property
    def message_type(self):
        """Gets the message_type of this MessageRsp.

        消息类型

        :return: The message_type of this MessageRsp.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this MessageRsp.

        消息类型

        :param message_type: The message_type of this MessageRsp.
        :type message_type: str
        """
        self._message_type = message_type

    @property
    def eihealth_project_name(self):
        """Gets the eihealth_project_name of this MessageRsp.

        项目名称

        :return: The eihealth_project_name of this MessageRsp.
        :rtype: str
        """
        return self._eihealth_project_name

    @eihealth_project_name.setter
    def eihealth_project_name(self, eihealth_project_name):
        """Sets the eihealth_project_name of this MessageRsp.

        项目名称

        :param eihealth_project_name: The eihealth_project_name of this MessageRsp.
        :type eihealth_project_name: str
        """
        self._eihealth_project_name = eihealth_project_name

    @property
    def resource_type(self):
        """Gets the resource_type of this MessageRsp.

        资源类型

        :return: The resource_type of this MessageRsp.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this MessageRsp.

        资源类型

        :param resource_type: The resource_type of this MessageRsp.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        """Gets the resource_name of this MessageRsp.

        资源名称

        :return: The resource_name of this MessageRsp.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this MessageRsp.

        资源名称

        :param resource_name: The resource_name of this MessageRsp.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def operator(self):
        """Gets the operator of this MessageRsp.

        操作用户

        :return: The operator of this MessageRsp.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this MessageRsp.

        操作用户

        :param operator: The operator of this MessageRsp.
        :type operator: str
        """
        self._operator = operator

    @property
    def status(self):
        """Gets the status of this MessageRsp.

        状态

        :return: The status of this MessageRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MessageRsp.

        状态

        :param status: The status of this MessageRsp.
        :type status: str
        """
        self._status = status

    @property
    def operate_time(self):
        """Gets the operate_time of this MessageRsp.

        操作时间

        :return: The operate_time of this MessageRsp.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this MessageRsp.

        操作时间

        :param operate_time: The operate_time of this MessageRsp.
        :type operate_time: str
        """
        self._operate_time = operate_time

    @property
    def message_detail(self):
        """Gets the message_detail of this MessageRsp.

        详情

        :return: The message_detail of this MessageRsp.
        :rtype: str
        """
        return self._message_detail

    @message_detail.setter
    def message_detail(self, message_detail):
        """Sets the message_detail of this MessageRsp.

        详情

        :param message_detail: The message_detail of this MessageRsp.
        :type message_detail: str
        """
        self._message_detail = message_detail

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
        if not isinstance(other, MessageRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
