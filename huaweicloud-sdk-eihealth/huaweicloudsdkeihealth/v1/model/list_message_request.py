# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMessageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'eihealth_project_name': 'str',
        'limit': 'int',
        'message_type': 'str',
        'offset': 'int',
        'operator': 'str',
        'resource_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'eihealth_project_name': 'eihealth_project_name',
        'limit': 'limit',
        'message_type': 'message_type',
        'offset': 'offset',
        'operator': 'operator',
        'resource_type': 'resource_type',
        'status': 'status'
    }

    def __init__(self, eihealth_project_name=None, limit=None, message_type=None, offset=None, operator=None, resource_type=None, status=None):
        """ListMessageRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_name: 医疗智能体项目名
        :type eihealth_project_name: str
        :param limit: 查询条数
        :type limit: int
        :param message_type: 消息类型
        :type message_type: str
        :param offset: 查询偏移量
        :type offset: int
        :param operator: 操作者名称
        :type operator: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param status: 操作状态
        :type status: str
        """
        
        

        self._eihealth_project_name = None
        self._limit = None
        self._message_type = None
        self._offset = None
        self._operator = None
        self._resource_type = None
        self._status = None
        self.discriminator = None

        if eihealth_project_name is not None:
            self.eihealth_project_name = eihealth_project_name
        if limit is not None:
            self.limit = limit
        if message_type is not None:
            self.message_type = message_type
        if offset is not None:
            self.offset = offset
        if operator is not None:
            self.operator = operator
        if resource_type is not None:
            self.resource_type = resource_type
        if status is not None:
            self.status = status

    @property
    def eihealth_project_name(self):
        """Gets the eihealth_project_name of this ListMessageRequest.

        医疗智能体项目名

        :return: The eihealth_project_name of this ListMessageRequest.
        :rtype: str
        """
        return self._eihealth_project_name

    @eihealth_project_name.setter
    def eihealth_project_name(self, eihealth_project_name):
        """Sets the eihealth_project_name of this ListMessageRequest.

        医疗智能体项目名

        :param eihealth_project_name: The eihealth_project_name of this ListMessageRequest.
        :type eihealth_project_name: str
        """
        self._eihealth_project_name = eihealth_project_name

    @property
    def limit(self):
        """Gets the limit of this ListMessageRequest.

        查询条数

        :return: The limit of this ListMessageRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMessageRequest.

        查询条数

        :param limit: The limit of this ListMessageRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def message_type(self):
        """Gets the message_type of this ListMessageRequest.

        消息类型

        :return: The message_type of this ListMessageRequest.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this ListMessageRequest.

        消息类型

        :param message_type: The message_type of this ListMessageRequest.
        :type message_type: str
        """
        self._message_type = message_type

    @property
    def offset(self):
        """Gets the offset of this ListMessageRequest.

        查询偏移量

        :return: The offset of this ListMessageRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListMessageRequest.

        查询偏移量

        :param offset: The offset of this ListMessageRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def operator(self):
        """Gets the operator of this ListMessageRequest.

        操作者名称

        :return: The operator of this ListMessageRequest.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ListMessageRequest.

        操作者名称

        :param operator: The operator of this ListMessageRequest.
        :type operator: str
        """
        self._operator = operator

    @property
    def resource_type(self):
        """Gets the resource_type of this ListMessageRequest.

        资源类型

        :return: The resource_type of this ListMessageRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListMessageRequest.

        资源类型

        :param resource_type: The resource_type of this ListMessageRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def status(self):
        """Gets the status of this ListMessageRequest.

        操作状态

        :return: The status of this ListMessageRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListMessageRequest.

        操作状态

        :param status: The status of this ListMessageRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListMessageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
