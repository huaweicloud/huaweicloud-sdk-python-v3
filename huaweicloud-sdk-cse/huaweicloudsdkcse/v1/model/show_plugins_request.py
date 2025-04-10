# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPluginsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway_id': 'str',
        'accept': 'str'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'accept': 'Accept'
    }

    def __init__(self, gateway_id=None, accept=None):
        r"""ShowPluginsRequest

        The model defined in huaweicloud sdk

        :param gateway_id: 网关实例id
        :type gateway_id: str
        :param accept: 该字段内容填为 \&quot;application/json\&quot;
        :type accept: str
        """
        
        

        self._gateway_id = None
        self._accept = None
        self.discriminator = None

        self.gateway_id = gateway_id
        if accept is not None:
            self.accept = accept

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this ShowPluginsRequest.

        网关实例id

        :return: The gateway_id of this ShowPluginsRequest.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this ShowPluginsRequest.

        网关实例id

        :param gateway_id: The gateway_id of this ShowPluginsRequest.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def accept(self):
        r"""Gets the accept of this ShowPluginsRequest.

        该字段内容填为 \"application/json\"

        :return: The accept of this ShowPluginsRequest.
        :rtype: str
        """
        return self._accept

    @accept.setter
    def accept(self, accept):
        r"""Sets the accept of this ShowPluginsRequest.

        该字段内容填为 \"application/json\"

        :param accept: The accept of this ShowPluginsRequest.
        :type accept: str
        """
        self._accept = accept

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
        if not isinstance(other, ShowPluginsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
