# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceStatusResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_url': 'str',
        'status': 'str'
    }

    attribute_map = {
        'server_url': 'server_url',
        'status': 'status'
    }

    def __init__(self, server_url=None, status=None):
        """InstanceStatusResponse

        The model defined in huaweicloud sdk

        :param server_url: 服务链接
        :type server_url: str
        :param status: 实例状态。 - DELETED 已删除 - DELETE_FAILED 删除失败 - DELETING 删除中 - READY 热实例就绪状态 - RUNNING 正在运行 - STARTING 正在启动 - STOPPED 已停止 - STOPPING 停止中 - UPDATE 更新Schdule信息 - WAITING 热实例创建初始态
        :type status: str
        """
        
        

        self._server_url = None
        self._status = None
        self.discriminator = None

        if server_url is not None:
            self.server_url = server_url
        if status is not None:
            self.status = status

    @property
    def server_url(self):
        """Gets the server_url of this InstanceStatusResponse.

        服务链接

        :return: The server_url of this InstanceStatusResponse.
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """Sets the server_url of this InstanceStatusResponse.

        服务链接

        :param server_url: The server_url of this InstanceStatusResponse.
        :type server_url: str
        """
        self._server_url = server_url

    @property
    def status(self):
        """Gets the status of this InstanceStatusResponse.

        实例状态。 - DELETED 已删除 - DELETE_FAILED 删除失败 - DELETING 删除中 - READY 热实例就绪状态 - RUNNING 正在运行 - STARTING 正在启动 - STOPPED 已停止 - STOPPING 停止中 - UPDATE 更新Schdule信息 - WAITING 热实例创建初始态

        :return: The status of this InstanceStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceStatusResponse.

        实例状态。 - DELETED 已删除 - DELETE_FAILED 删除失败 - DELETING 删除中 - READY 热实例就绪状态 - RUNNING 正在运行 - STARTING 正在启动 - STOPPED 已停止 - STOPPING 停止中 - UPDATE 更新Schdule信息 - WAITING 热实例创建初始态

        :param status: The status of this InstanceStatusResponse.
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
        if not isinstance(other, InstanceStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
