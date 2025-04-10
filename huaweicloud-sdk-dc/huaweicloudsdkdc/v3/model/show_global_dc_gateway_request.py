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
        'limit': 'int',
        'fields': 'list[str]',
        'ext_fields': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'global_dc_gateway_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'fields': 'fields',
        'ext_fields': 'ext_fields',
        'enterprise_project_id': 'enterprise_project_id',
        'global_dc_gateway_id': 'global_dc_gateway_id'
    }

    def __init__(self, limit=None, fields=None, ext_fields=None, enterprise_project_id=None, global_dc_gateway_id=None):
        r"""ShowGlobalDcGatewayRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~2000。
        :type limit: int
        :param fields: 显示字段列表
        :type fields: list[str]
        :param ext_fields: show response ext-fields
        :type ext_fields: list[str]
        :param enterprise_project_id: 根据企业项目ID过滤资源实例
        :type enterprise_project_id: list[str]
        :param global_dc_gateway_id: 全域接入网关ID
        :type global_dc_gateway_id: str
        """
        
        

        self._limit = None
        self._fields = None
        self._ext_fields = None
        self._enterprise_project_id = None
        self._global_dc_gateway_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if fields is not None:
            self.fields = fields
        if ext_fields is not None:
            self.ext_fields = ext_fields
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.global_dc_gateway_id = global_dc_gateway_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowGlobalDcGatewayRequest.

        每页返回的个数。 取值范围：1~2000。

        :return: The limit of this ShowGlobalDcGatewayRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowGlobalDcGatewayRequest.

        每页返回的个数。 取值范围：1~2000。

        :param limit: The limit of this ShowGlobalDcGatewayRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def fields(self):
        r"""Gets the fields of this ShowGlobalDcGatewayRequest.

        显示字段列表

        :return: The fields of this ShowGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ShowGlobalDcGatewayRequest.

        显示字段列表

        :param fields: The fields of this ShowGlobalDcGatewayRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def ext_fields(self):
        r"""Gets the ext_fields of this ShowGlobalDcGatewayRequest.

        show response ext-fields

        :return: The ext_fields of this ShowGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._ext_fields

    @ext_fields.setter
    def ext_fields(self, ext_fields):
        r"""Sets the ext_fields of this ShowGlobalDcGatewayRequest.

        show response ext-fields

        :param ext_fields: The ext_fields of this ShowGlobalDcGatewayRequest.
        :type ext_fields: list[str]
        """
        self._ext_fields = ext_fields

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowGlobalDcGatewayRequest.

        根据企业项目ID过滤资源实例

        :return: The enterprise_project_id of this ShowGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowGlobalDcGatewayRequest.

        根据企业项目ID过滤资源实例

        :param enterprise_project_id: The enterprise_project_id of this ShowGlobalDcGatewayRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def global_dc_gateway_id(self):
        r"""Gets the global_dc_gateway_id of this ShowGlobalDcGatewayRequest.

        全域接入网关ID

        :return: The global_dc_gateway_id of this ShowGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._global_dc_gateway_id

    @global_dc_gateway_id.setter
    def global_dc_gateway_id(self, global_dc_gateway_id):
        r"""Sets the global_dc_gateway_id of this ShowGlobalDcGatewayRequest.

        全域接入网关ID

        :param global_dc_gateway_id: The global_dc_gateway_id of this ShowGlobalDcGatewayRequest.
        :type global_dc_gateway_id: str
        """
        self._global_dc_gateway_id = global_dc_gateway_id

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
