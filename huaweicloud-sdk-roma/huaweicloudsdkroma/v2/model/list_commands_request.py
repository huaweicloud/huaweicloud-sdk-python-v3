# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCommandsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'service_id': 'str',
        'limit': 'int',
        'command_id': 'int',
        'command_name': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'service_id': 'service_id',
        'limit': 'limit',
        'command_id': 'command_id',
        'command_name': 'command_name',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, service_id=None, limit=None, command_id=None, command_name=None, offset=None):
        """ListCommandsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param service_id: 服务ID
        :type service_id: str
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param command_id: 命令ID
        :type command_id: int
        :param command_name: 命令名称
        :type command_name: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        """
        
        

        self._instance_id = None
        self._service_id = None
        self._limit = None
        self._command_id = None
        self._command_name = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        self.service_id = service_id
        if limit is not None:
            self.limit = limit
        if command_id is not None:
            self.command_id = command_id
        if command_name is not None:
            self.command_name = command_name
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListCommandsRequest.

        实例ID

        :return: The instance_id of this ListCommandsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListCommandsRequest.

        实例ID

        :param instance_id: The instance_id of this ListCommandsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def service_id(self):
        """Gets the service_id of this ListCommandsRequest.

        服务ID

        :return: The service_id of this ListCommandsRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ListCommandsRequest.

        服务ID

        :param service_id: The service_id of this ListCommandsRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def limit(self):
        """Gets the limit of this ListCommandsRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListCommandsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCommandsRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListCommandsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def command_id(self):
        """Gets the command_id of this ListCommandsRequest.

        命令ID

        :return: The command_id of this ListCommandsRequest.
        :rtype: int
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this ListCommandsRequest.

        命令ID

        :param command_id: The command_id of this ListCommandsRequest.
        :type command_id: int
        """
        self._command_id = command_id

    @property
    def command_name(self):
        """Gets the command_name of this ListCommandsRequest.

        命令名称

        :return: The command_name of this ListCommandsRequest.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this ListCommandsRequest.

        命令名称

        :param command_name: The command_name of this ListCommandsRequest.
        :type command_name: str
        """
        self._command_name = command_name

    @property
    def offset(self):
        """Gets the offset of this ListCommandsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListCommandsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCommandsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListCommandsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListCommandsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
