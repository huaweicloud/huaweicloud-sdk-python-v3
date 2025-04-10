# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteIaConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'ia_id': 'str',
        'config_id': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'ia_id': 'ia_id',
        'config_id': 'config_id'
    }

    def __init__(self, node_id=None, ia_id=None, config_id=None):
        r"""DeleteIaConfigRequest

        The model defined in huaweicloud sdk

        :param node_id: 边缘节点ID
        :type node_id: str
        :param ia_id: 边侧第三方应用的模块ID
        :type ia_id: str
        :param config_id: 配置ID
        :type config_id: str
        """
        
        

        self._node_id = None
        self._ia_id = None
        self._config_id = None
        self.discriminator = None

        self.node_id = node_id
        self.ia_id = ia_id
        self.config_id = config_id

    @property
    def node_id(self):
        r"""Gets the node_id of this DeleteIaConfigRequest.

        边缘节点ID

        :return: The node_id of this DeleteIaConfigRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this DeleteIaConfigRequest.

        边缘节点ID

        :param node_id: The node_id of this DeleteIaConfigRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def ia_id(self):
        r"""Gets the ia_id of this DeleteIaConfigRequest.

        边侧第三方应用的模块ID

        :return: The ia_id of this DeleteIaConfigRequest.
        :rtype: str
        """
        return self._ia_id

    @ia_id.setter
    def ia_id(self, ia_id):
        r"""Sets the ia_id of this DeleteIaConfigRequest.

        边侧第三方应用的模块ID

        :param ia_id: The ia_id of this DeleteIaConfigRequest.
        :type ia_id: str
        """
        self._ia_id = ia_id

    @property
    def config_id(self):
        r"""Gets the config_id of this DeleteIaConfigRequest.

        配置ID

        :return: The config_id of this DeleteIaConfigRequest.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        r"""Sets the config_id of this DeleteIaConfigRequest.

        配置ID

        :param config_id: The config_id of this DeleteIaConfigRequest.
        :type config_id: str
        """
        self._config_id = config_id

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
        if not isinstance(other, DeleteIaConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
