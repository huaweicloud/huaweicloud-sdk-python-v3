# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgentConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'int',
        'address': 'str',
        'version': 'str',
        'agent_id': 'str',
        'alias': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'address': 'address',
        'version': 'version',
        'agent_id': 'agent_id',
        'alias': 'alias'
    }

    def __init__(self, app_id=None, address=None, version=None, agent_id=None, alias=None):
        r"""ShowAgentConfigRequestBody

        The model defined in huaweicloud sdk

        :param app_id: 应用id
        :type app_id: int
        :param address: 探针的内网地址
        :type address: str
        :param version: 探针的版本
        :type version: str
        :param agent_id: 探针id，非必填，不填是注册探针，填了是更新探针配置
        :type agent_id: str
        :param alias: 探针别名
        :type alias: str
        """
        
        

        self._app_id = None
        self._address = None
        self._version = None
        self._agent_id = None
        self._alias = None
        self.discriminator = None

        self.app_id = app_id
        self.address = address
        self.version = version
        if agent_id is not None:
            self.agent_id = agent_id
        if alias is not None:
            self.alias = alias

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowAgentConfigRequestBody.

        应用id

        :return: The app_id of this ShowAgentConfigRequestBody.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowAgentConfigRequestBody.

        应用id

        :param app_id: The app_id of this ShowAgentConfigRequestBody.
        :type app_id: int
        """
        self._app_id = app_id

    @property
    def address(self):
        r"""Gets the address of this ShowAgentConfigRequestBody.

        探针的内网地址

        :return: The address of this ShowAgentConfigRequestBody.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this ShowAgentConfigRequestBody.

        探针的内网地址

        :param address: The address of this ShowAgentConfigRequestBody.
        :type address: str
        """
        self._address = address

    @property
    def version(self):
        r"""Gets the version of this ShowAgentConfigRequestBody.

        探针的版本

        :return: The version of this ShowAgentConfigRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowAgentConfigRequestBody.

        探针的版本

        :param version: The version of this ShowAgentConfigRequestBody.
        :type version: str
        """
        self._version = version

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ShowAgentConfigRequestBody.

        探针id，非必填，不填是注册探针，填了是更新探针配置

        :return: The agent_id of this ShowAgentConfigRequestBody.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ShowAgentConfigRequestBody.

        探针id，非必填，不填是注册探针，填了是更新探针配置

        :param agent_id: The agent_id of this ShowAgentConfigRequestBody.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def alias(self):
        r"""Gets the alias of this ShowAgentConfigRequestBody.

        探针别名

        :return: The alias of this ShowAgentConfigRequestBody.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this ShowAgentConfigRequestBody.

        探针别名

        :param alias: The alias of this ShowAgentConfigRequestBody.
        :type alias: str
        """
        self._alias = alias

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
        if not isinstance(other, ShowAgentConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
