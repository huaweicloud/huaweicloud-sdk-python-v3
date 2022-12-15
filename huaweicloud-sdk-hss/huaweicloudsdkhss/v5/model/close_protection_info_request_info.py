# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloseProtectionInfoRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id_list': 'list[str]',
        'agent_id_list': 'list[str]',
        'close_protection_type': 'str'
    }

    attribute_map = {
        'host_id_list': 'host_id_list',
        'agent_id_list': 'agent_id_list',
        'close_protection_type': 'close_protection_type'
    }

    def __init__(self, host_id_list=None, agent_id_list=None, close_protection_type=None):
        """CloseProtectionInfoRequestInfo

        The model defined in huaweicloud sdk

        :param host_id_list: 需要关闭勒索防护的主机ID列表
        :type host_id_list: list[str]
        :param agent_id_list: 需要关闭勒索防护的agentID列表
        :type agent_id_list: list[str]
        :param close_protection_type: 关闭防护类型，包含如下：   - close_all : 关闭所有防护   - close_anti : 关闭勒索防护   - close_backup : 关闭备份功能
        :type close_protection_type: str
        """
        
        

        self._host_id_list = None
        self._agent_id_list = None
        self._close_protection_type = None
        self.discriminator = None

        if host_id_list is not None:
            self.host_id_list = host_id_list
        if agent_id_list is not None:
            self.agent_id_list = agent_id_list
        if close_protection_type is not None:
            self.close_protection_type = close_protection_type

    @property
    def host_id_list(self):
        """Gets the host_id_list of this CloseProtectionInfoRequestInfo.

        需要关闭勒索防护的主机ID列表

        :return: The host_id_list of this CloseProtectionInfoRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        """Sets the host_id_list of this CloseProtectionInfoRequestInfo.

        需要关闭勒索防护的主机ID列表

        :param host_id_list: The host_id_list of this CloseProtectionInfoRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def agent_id_list(self):
        """Gets the agent_id_list of this CloseProtectionInfoRequestInfo.

        需要关闭勒索防护的agentID列表

        :return: The agent_id_list of this CloseProtectionInfoRequestInfo.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        """Sets the agent_id_list of this CloseProtectionInfoRequestInfo.

        需要关闭勒索防护的agentID列表

        :param agent_id_list: The agent_id_list of this CloseProtectionInfoRequestInfo.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

    @property
    def close_protection_type(self):
        """Gets the close_protection_type of this CloseProtectionInfoRequestInfo.

        关闭防护类型，包含如下：   - close_all : 关闭所有防护   - close_anti : 关闭勒索防护   - close_backup : 关闭备份功能

        :return: The close_protection_type of this CloseProtectionInfoRequestInfo.
        :rtype: str
        """
        return self._close_protection_type

    @close_protection_type.setter
    def close_protection_type(self, close_protection_type):
        """Sets the close_protection_type of this CloseProtectionInfoRequestInfo.

        关闭防护类型，包含如下：   - close_all : 关闭所有防护   - close_anti : 关闭勒索防护   - close_backup : 关闭备份功能

        :param close_protection_type: The close_protection_type of this CloseProtectionInfoRequestInfo.
        :type close_protection_type: str
        """
        self._close_protection_type = close_protection_type

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
        if not isinstance(other, CloseProtectionInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
