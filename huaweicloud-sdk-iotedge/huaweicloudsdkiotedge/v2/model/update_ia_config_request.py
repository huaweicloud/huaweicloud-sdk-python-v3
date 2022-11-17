# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIaConfigRequest:

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
        'config_id': 'str',
        'body': 'UpdateIaConfigRequestDTO'
    }

    attribute_map = {
        'node_id': 'node_id',
        'ia_id': 'ia_id',
        'config_id': 'config_id',
        'body': 'body'
    }

    def __init__(self, node_id=None, ia_id=None, config_id=None, body=None):
        """UpdateIaConfigRequest

        The model defined in huaweicloud sdk

        :param node_id: 边缘节点ID
        :type node_id: str
        :param ia_id: 边侧第三方应用的模块ID
        :type ia_id: str
        :param config_id: 配置ID
        :type config_id: str
        :param body: Body of the UpdateIaConfigRequest
        :type body: :class:`huaweicloudsdkiotedge.v2.UpdateIaConfigRequestDTO`
        """
        
        

        self._node_id = None
        self._ia_id = None
        self._config_id = None
        self._body = None
        self.discriminator = None

        self.node_id = node_id
        self.ia_id = ia_id
        self.config_id = config_id
        if body is not None:
            self.body = body

    @property
    def node_id(self):
        """Gets the node_id of this UpdateIaConfigRequest.

        边缘节点ID

        :return: The node_id of this UpdateIaConfigRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this UpdateIaConfigRequest.

        边缘节点ID

        :param node_id: The node_id of this UpdateIaConfigRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def ia_id(self):
        """Gets the ia_id of this UpdateIaConfigRequest.

        边侧第三方应用的模块ID

        :return: The ia_id of this UpdateIaConfigRequest.
        :rtype: str
        """
        return self._ia_id

    @ia_id.setter
    def ia_id(self, ia_id):
        """Sets the ia_id of this UpdateIaConfigRequest.

        边侧第三方应用的模块ID

        :param ia_id: The ia_id of this UpdateIaConfigRequest.
        :type ia_id: str
        """
        self._ia_id = ia_id

    @property
    def config_id(self):
        """Gets the config_id of this UpdateIaConfigRequest.

        配置ID

        :return: The config_id of this UpdateIaConfigRequest.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this UpdateIaConfigRequest.

        配置ID

        :param config_id: The config_id of this UpdateIaConfigRequest.
        :type config_id: str
        """
        self._config_id = config_id

    @property
    def body(self):
        """Gets the body of this UpdateIaConfigRequest.

        :return: The body of this UpdateIaConfigRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateIaConfigRequestDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateIaConfigRequest.

        :param body: The body of this UpdateIaConfigRequest.
        :type body: :class:`huaweicloudsdkiotedge.v2.UpdateIaConfigRequestDTO`
        """
        self._body = body

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
        if not isinstance(other, UpdateIaConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
