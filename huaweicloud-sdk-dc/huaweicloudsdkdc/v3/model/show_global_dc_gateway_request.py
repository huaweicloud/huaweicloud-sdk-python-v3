# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGlobalDcGatewayRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_dc_gateway_id': 'str',
        'fields': 'list[str]',
        'ext_fields': 'list[str]'
    }

    attribute_map = {
        'global_dc_gateway_id': 'global_dc_gateway_id',
        'fields': 'fields',
        'ext_fields': 'ext_fields'
    }

    def __init__(self, global_dc_gateway_id=None, fields=None, ext_fields=None):
        """ShowGlobalDcGatewayRequest

        The model defined in huaweicloud sdk

        :param global_dc_gateway_id: 全球接入网关ID
        :type global_dc_gateway_id: str
        :param fields: 显示字段列表
        :type fields: list[str]
        :param ext_fields: show response ext-fields
        :type ext_fields: list[str]
        """
        
        

        self._global_dc_gateway_id = None
        self._fields = None
        self._ext_fields = None
        self.discriminator = None

        self.global_dc_gateway_id = global_dc_gateway_id
        if fields is not None:
            self.fields = fields
        if ext_fields is not None:
            self.ext_fields = ext_fields

    @property
    def global_dc_gateway_id(self):
        """Gets the global_dc_gateway_id of this ShowGlobalDcGatewayRequest.

        全球接入网关ID

        :return: The global_dc_gateway_id of this ShowGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._global_dc_gateway_id

    @global_dc_gateway_id.setter
    def global_dc_gateway_id(self, global_dc_gateway_id):
        """Sets the global_dc_gateway_id of this ShowGlobalDcGatewayRequest.

        全球接入网关ID

        :param global_dc_gateway_id: The global_dc_gateway_id of this ShowGlobalDcGatewayRequest.
        :type global_dc_gateway_id: str
        """
        self._global_dc_gateway_id = global_dc_gateway_id

    @property
    def fields(self):
        """Gets the fields of this ShowGlobalDcGatewayRequest.

        显示字段列表

        :return: The fields of this ShowGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ShowGlobalDcGatewayRequest.

        显示字段列表

        :param fields: The fields of this ShowGlobalDcGatewayRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def ext_fields(self):
        """Gets the ext_fields of this ShowGlobalDcGatewayRequest.

        show response ext-fields

        :return: The ext_fields of this ShowGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._ext_fields

    @ext_fields.setter
    def ext_fields(self, ext_fields):
        """Sets the ext_fields of this ShowGlobalDcGatewayRequest.

        show response ext-fields

        :param ext_fields: The ext_fields of this ShowGlobalDcGatewayRequest.
        :type ext_fields: list[str]
        """
        self._ext_fields = ext_fields

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
        if not isinstance(other, ShowGlobalDcGatewayRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
