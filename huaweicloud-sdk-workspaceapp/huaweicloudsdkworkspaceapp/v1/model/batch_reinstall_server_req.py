# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchReinstallServerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_ids': 'list[str]',
        'update_access_agent': 'bool'
    }

    attribute_map = {
        'server_ids': 'server_ids',
        'update_access_agent': 'update_access_agent'
    }

    def __init__(self, server_ids=None, update_access_agent=None):
        r"""BatchReinstallServerReq

        The model defined in huaweicloud sdk

        :param server_ids: 应用服务器id集合。
        :type server_ids: list[str]
        :param update_access_agent: 是否自动升级hda版本。
        :type update_access_agent: bool
        """
        
        

        self._server_ids = None
        self._update_access_agent = None
        self.discriminator = None

        if server_ids is not None:
            self.server_ids = server_ids
        if update_access_agent is not None:
            self.update_access_agent = update_access_agent

    @property
    def server_ids(self):
        r"""Gets the server_ids of this BatchReinstallServerReq.

        应用服务器id集合。

        :return: The server_ids of this BatchReinstallServerReq.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        r"""Sets the server_ids of this BatchReinstallServerReq.

        应用服务器id集合。

        :param server_ids: The server_ids of this BatchReinstallServerReq.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

    @property
    def update_access_agent(self):
        r"""Gets the update_access_agent of this BatchReinstallServerReq.

        是否自动升级hda版本。

        :return: The update_access_agent of this BatchReinstallServerReq.
        :rtype: bool
        """
        return self._update_access_agent

    @update_access_agent.setter
    def update_access_agent(self, update_access_agent):
        r"""Sets the update_access_agent of this BatchReinstallServerReq.

        是否自动升级hda版本。

        :param update_access_agent: The update_access_agent of this BatchReinstallServerReq.
        :type update_access_agent: bool
        """
        self._update_access_agent = update_access_agent

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
        if not isinstance(other, BatchReinstallServerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
