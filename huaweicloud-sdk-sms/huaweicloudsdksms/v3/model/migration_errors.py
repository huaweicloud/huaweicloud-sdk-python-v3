# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrationErrors:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_json': 'str',
        'host_name': 'str',
        'name': 'str',
        'source_id': 'str',
        'source_ip': 'str',
        'target_ip': 'str'
    }

    attribute_map = {
        'error_json': 'error_json',
        'host_name': 'host_name',
        'name': 'name',
        'source_id': 'source_id',
        'source_ip': 'source_ip',
        'target_ip': 'target_ip'
    }

    def __init__(self, error_json=None, host_name=None, name=None, source_id=None, source_ip=None, target_ip=None):
        """MigrationErrors

        The model defined in huaweicloud sdk

        :param error_json: 保存错误信息的json字符串
        :type error_json: str
        :param host_name: 主机名称（从用户系统获取，可能为空）
        :type host_name: str
        :param name: 源端在主机迁移服务中的名称
        :type name: str
        :param source_id: 源端服务器ID
        :type source_id: str
        :param source_ip: 源端服务器的ip
        :type source_ip: str
        :param target_ip: 目的端服务器的ip 
        :type target_ip: str
        """
        
        

        self._error_json = None
        self._host_name = None
        self._name = None
        self._source_id = None
        self._source_ip = None
        self._target_ip = None
        self.discriminator = None

        if error_json is not None:
            self.error_json = error_json
        if host_name is not None:
            self.host_name = host_name
        if name is not None:
            self.name = name
        if source_id is not None:
            self.source_id = source_id
        if source_ip is not None:
            self.source_ip = source_ip
        if target_ip is not None:
            self.target_ip = target_ip

    @property
    def error_json(self):
        """Gets the error_json of this MigrationErrors.

        保存错误信息的json字符串

        :return: The error_json of this MigrationErrors.
        :rtype: str
        """
        return self._error_json

    @error_json.setter
    def error_json(self, error_json):
        """Sets the error_json of this MigrationErrors.

        保存错误信息的json字符串

        :param error_json: The error_json of this MigrationErrors.
        :type error_json: str
        """
        self._error_json = error_json

    @property
    def host_name(self):
        """Gets the host_name of this MigrationErrors.

        主机名称（从用户系统获取，可能为空）

        :return: The host_name of this MigrationErrors.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this MigrationErrors.

        主机名称（从用户系统获取，可能为空）

        :param host_name: The host_name of this MigrationErrors.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def name(self):
        """Gets the name of this MigrationErrors.

        源端在主机迁移服务中的名称

        :return: The name of this MigrationErrors.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MigrationErrors.

        源端在主机迁移服务中的名称

        :param name: The name of this MigrationErrors.
        :type name: str
        """
        self._name = name

    @property
    def source_id(self):
        """Gets the source_id of this MigrationErrors.

        源端服务器ID

        :return: The source_id of this MigrationErrors.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this MigrationErrors.

        源端服务器ID

        :param source_id: The source_id of this MigrationErrors.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def source_ip(self):
        """Gets the source_ip of this MigrationErrors.

        源端服务器的ip

        :return: The source_ip of this MigrationErrors.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """Sets the source_ip of this MigrationErrors.

        源端服务器的ip

        :param source_ip: The source_ip of this MigrationErrors.
        :type source_ip: str
        """
        self._source_ip = source_ip

    @property
    def target_ip(self):
        """Gets the target_ip of this MigrationErrors.

        目的端服务器的ip 

        :return: The target_ip of this MigrationErrors.
        :rtype: str
        """
        return self._target_ip

    @target_ip.setter
    def target_ip(self, target_ip):
        """Sets the target_ip of this MigrationErrors.

        目的端服务器的ip 

        :param target_ip: The target_ip of this MigrationErrors.
        :type target_ip: str
        """
        self._target_ip = target_ip

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
        if not isinstance(other, MigrationErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
