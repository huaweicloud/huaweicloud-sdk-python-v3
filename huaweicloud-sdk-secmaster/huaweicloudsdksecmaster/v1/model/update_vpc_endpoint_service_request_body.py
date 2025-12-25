# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpcEndpointServiceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'list': 'list[UpdateVpcepServiceInfo]',
        'subnet_id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'list': 'list',
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, list=None, subnet_id=None, vpc_id=None):
        r"""UpdateVpcEndpointServiceRequestBody

        The model defined in huaweicloud sdk

        :param list: 更新VpcepServiceInfo
        :type list: list[:class:`huaweicloudsdksecmaster.v1.UpdateVpcepServiceInfo`]
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param vpc_id: UUID
        :type vpc_id: str
        """
        
        

        self._list = None
        self._subnet_id = None
        self._vpc_id = None
        self.discriminator = None

        if list is not None:
            self.list = list
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def list(self):
        r"""Gets the list of this UpdateVpcEndpointServiceRequestBody.

        更新VpcepServiceInfo

        :return: The list of this UpdateVpcEndpointServiceRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.UpdateVpcepServiceInfo`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this UpdateVpcEndpointServiceRequestBody.

        更新VpcepServiceInfo

        :param list: The list of this UpdateVpcEndpointServiceRequestBody.
        :type list: list[:class:`huaweicloudsdksecmaster.v1.UpdateVpcepServiceInfo`]
        """
        self._list = list

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this UpdateVpcEndpointServiceRequestBody.

        子网ID

        :return: The subnet_id of this UpdateVpcEndpointServiceRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this UpdateVpcEndpointServiceRequestBody.

        子网ID

        :param subnet_id: The subnet_id of this UpdateVpcEndpointServiceRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this UpdateVpcEndpointServiceRequestBody.

        UUID

        :return: The vpc_id of this UpdateVpcEndpointServiceRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this UpdateVpcEndpointServiceRequestBody.

        UUID

        :param vpc_id: The vpc_id of this UpdateVpcEndpointServiceRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateVpcEndpointServiceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
