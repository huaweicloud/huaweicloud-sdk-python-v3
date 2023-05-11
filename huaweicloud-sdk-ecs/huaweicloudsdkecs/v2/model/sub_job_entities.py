# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubJobEntities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'nic_id': 'str',
        'errorcode_message': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'nic_id': 'nic_id',
        'errorcode_message': 'errorcode_message'
    }

    def __init__(self, server_id=None, nic_id=None, errorcode_message=None):
        """SubJobEntities

        The model defined in huaweicloud sdk

        :param server_id: 云服务器相关操作显示server_id。
        :type server_id: str
        :param nic_id: 网卡相关操作显示nic_id。
        :type nic_id: str
        :param errorcode_message: 子任务执行失败的具体原因。
        :type errorcode_message: str
        """
        
        

        self._server_id = None
        self._nic_id = None
        self._errorcode_message = None
        self.discriminator = None

        if server_id is not None:
            self.server_id = server_id
        if nic_id is not None:
            self.nic_id = nic_id
        if errorcode_message is not None:
            self.errorcode_message = errorcode_message

    @property
    def server_id(self):
        """Gets the server_id of this SubJobEntities.

        云服务器相关操作显示server_id。

        :return: The server_id of this SubJobEntities.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this SubJobEntities.

        云服务器相关操作显示server_id。

        :param server_id: The server_id of this SubJobEntities.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def nic_id(self):
        """Gets the nic_id of this SubJobEntities.

        网卡相关操作显示nic_id。

        :return: The nic_id of this SubJobEntities.
        :rtype: str
        """
        return self._nic_id

    @nic_id.setter
    def nic_id(self, nic_id):
        """Sets the nic_id of this SubJobEntities.

        网卡相关操作显示nic_id。

        :param nic_id: The nic_id of this SubJobEntities.
        :type nic_id: str
        """
        self._nic_id = nic_id

    @property
    def errorcode_message(self):
        """Gets the errorcode_message of this SubJobEntities.

        子任务执行失败的具体原因。

        :return: The errorcode_message of this SubJobEntities.
        :rtype: str
        """
        return self._errorcode_message

    @errorcode_message.setter
    def errorcode_message(self, errorcode_message):
        """Sets the errorcode_message of this SubJobEntities.

        子任务执行失败的具体原因。

        :param errorcode_message: The errorcode_message of this SubJobEntities.
        :type errorcode_message: str
        """
        self._errorcode_message = errorcode_message

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
        if not isinstance(other, SubJobEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
