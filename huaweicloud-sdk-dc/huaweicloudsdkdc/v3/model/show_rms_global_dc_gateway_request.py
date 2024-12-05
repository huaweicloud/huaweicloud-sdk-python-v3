# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRmsGlobalDcGatewayRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rp_name': 'str',
        'domain_id': 'str',
        'region_id': 'str',
        'resource_type': 'str',
        'global_dc_gateway_id': 'str',
        'fields': 'list[str]',
        'ext_fields': 'list[str]'
    }

    attribute_map = {
        'rp_name': 'rp_name',
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'resource_type': 'resource_type',
        'global_dc_gateway_id': 'global_dc_gateway_id',
        'fields': 'fields',
        'ext_fields': 'ext_fields'
    }

    def __init__(self, rp_name=None, domain_id=None, region_id=None, resource_type=None, global_dc_gateway_id=None, fields=None, ext_fields=None):
        """ShowRmsGlobalDcGatewayRequest

        The model defined in huaweicloud sdk

        :param rp_name: 通过rp_name过滤记录
        :type rp_name: str
        :param domain_id: domain_id
        :type domain_id: str
        :param region_id: region_id
        :type region_id: str
        :param resource_type: resource_type
        :type resource_type: str
        :param global_dc_gateway_id: 全球接入网关ID
        :type global_dc_gateway_id: str
        :param fields: 显示字段列表
        :type fields: list[str]
        :param ext_fields: show response ext-fields
        :type ext_fields: list[str]
        """
        
        

        self._rp_name = None
        self._domain_id = None
        self._region_id = None
        self._resource_type = None
        self._global_dc_gateway_id = None
        self._fields = None
        self._ext_fields = None
        self.discriminator = None

        self.rp_name = rp_name
        self.domain_id = domain_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.global_dc_gateway_id = global_dc_gateway_id
        if fields is not None:
            self.fields = fields
        if ext_fields is not None:
            self.ext_fields = ext_fields

    @property
    def rp_name(self):
        """Gets the rp_name of this ShowRmsGlobalDcGatewayRequest.

        通过rp_name过滤记录

        :return: The rp_name of this ShowRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._rp_name

    @rp_name.setter
    def rp_name(self, rp_name):
        """Sets the rp_name of this ShowRmsGlobalDcGatewayRequest.

        通过rp_name过滤记录

        :param rp_name: The rp_name of this ShowRmsGlobalDcGatewayRequest.
        :type rp_name: str
        """
        self._rp_name = rp_name

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowRmsGlobalDcGatewayRequest.

        domain_id

        :return: The domain_id of this ShowRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowRmsGlobalDcGatewayRequest.

        domain_id

        :param domain_id: The domain_id of this ShowRmsGlobalDcGatewayRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        """Gets the region_id of this ShowRmsGlobalDcGatewayRequest.

        region_id

        :return: The region_id of this ShowRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowRmsGlobalDcGatewayRequest.

        region_id

        :param region_id: The region_id of this ShowRmsGlobalDcGatewayRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_type(self):
        """Gets the resource_type of this ShowRmsGlobalDcGatewayRequest.

        resource_type

        :return: The resource_type of this ShowRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ShowRmsGlobalDcGatewayRequest.

        resource_type

        :param resource_type: The resource_type of this ShowRmsGlobalDcGatewayRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def global_dc_gateway_id(self):
        """Gets the global_dc_gateway_id of this ShowRmsGlobalDcGatewayRequest.

        全球接入网关ID

        :return: The global_dc_gateway_id of this ShowRmsGlobalDcGatewayRequest.
        :rtype: str
        """
        return self._global_dc_gateway_id

    @global_dc_gateway_id.setter
    def global_dc_gateway_id(self, global_dc_gateway_id):
        """Sets the global_dc_gateway_id of this ShowRmsGlobalDcGatewayRequest.

        全球接入网关ID

        :param global_dc_gateway_id: The global_dc_gateway_id of this ShowRmsGlobalDcGatewayRequest.
        :type global_dc_gateway_id: str
        """
        self._global_dc_gateway_id = global_dc_gateway_id

    @property
    def fields(self):
        """Gets the fields of this ShowRmsGlobalDcGatewayRequest.

        显示字段列表

        :return: The fields of this ShowRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ShowRmsGlobalDcGatewayRequest.

        显示字段列表

        :param fields: The fields of this ShowRmsGlobalDcGatewayRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def ext_fields(self):
        """Gets the ext_fields of this ShowRmsGlobalDcGatewayRequest.

        show response ext-fields

        :return: The ext_fields of this ShowRmsGlobalDcGatewayRequest.
        :rtype: list[str]
        """
        return self._ext_fields

    @ext_fields.setter
    def ext_fields(self, ext_fields):
        """Sets the ext_fields of this ShowRmsGlobalDcGatewayRequest.

        show response ext-fields

        :param ext_fields: The ext_fields of this ShowRmsGlobalDcGatewayRequest.
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
        if not isinstance(other, ShowRmsGlobalDcGatewayRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
