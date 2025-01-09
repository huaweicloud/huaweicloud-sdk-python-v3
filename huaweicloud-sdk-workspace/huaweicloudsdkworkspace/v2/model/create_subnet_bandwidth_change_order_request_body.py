# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubnetBandwidthChangeOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_name': 'str',
        'bandwidth_size': 'str',
        'cloud_service_console_url': 'str',
        'enterprise_project_id': 'str',
        'extend_param': 'OrderExtendParam'
    }

    attribute_map = {
        'bandwidth_name': 'bandwidth_name',
        'bandwidth_size': 'bandwidth_size',
        'cloud_service_console_url': 'cloud_service_console_url',
        'enterprise_project_id': 'enterprise_project_id',
        'extend_param': 'extend_param'
    }

    def __init__(self, bandwidth_name=None, bandwidth_size=None, cloud_service_console_url=None, enterprise_project_id=None, extend_param=None):
        """CreateSubnetBandwidthChangeOrderRequestBody

        The model defined in huaweicloud sdk

        :param bandwidth_name: 云办公带宽名称。
        :type bandwidth_name: str
        :param bandwidth_size: 变更云办公带宽的带宽大小。
        :type bandwidth_size: str
        :param cloud_service_console_url: 支付后跳转url
        :type cloud_service_console_url: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        
        

        self._bandwidth_name = None
        self._bandwidth_size = None
        self._cloud_service_console_url = None
        self._enterprise_project_id = None
        self._extend_param = None
        self.discriminator = None

        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name
        self.bandwidth_size = bandwidth_size
        if cloud_service_console_url is not None:
            self.cloud_service_console_url = cloud_service_console_url
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def bandwidth_name(self):
        """Gets the bandwidth_name of this CreateSubnetBandwidthChangeOrderRequestBody.

        云办公带宽名称。

        :return: The bandwidth_name of this CreateSubnetBandwidthChangeOrderRequestBody.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        """Sets the bandwidth_name of this CreateSubnetBandwidthChangeOrderRequestBody.

        云办公带宽名称。

        :param bandwidth_name: The bandwidth_name of this CreateSubnetBandwidthChangeOrderRequestBody.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this CreateSubnetBandwidthChangeOrderRequestBody.

        变更云办公带宽的带宽大小。

        :return: The bandwidth_size of this CreateSubnetBandwidthChangeOrderRequestBody.
        :rtype: str
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this CreateSubnetBandwidthChangeOrderRequestBody.

        变更云办公带宽的带宽大小。

        :param bandwidth_size: The bandwidth_size of this CreateSubnetBandwidthChangeOrderRequestBody.
        :type bandwidth_size: str
        """
        self._bandwidth_size = bandwidth_size

    @property
    def cloud_service_console_url(self):
        """Gets the cloud_service_console_url of this CreateSubnetBandwidthChangeOrderRequestBody.

        支付后跳转url

        :return: The cloud_service_console_url of this CreateSubnetBandwidthChangeOrderRequestBody.
        :rtype: str
        """
        return self._cloud_service_console_url

    @cloud_service_console_url.setter
    def cloud_service_console_url(self, cloud_service_console_url):
        """Sets the cloud_service_console_url of this CreateSubnetBandwidthChangeOrderRequestBody.

        支付后跳转url

        :param cloud_service_console_url: The cloud_service_console_url of this CreateSubnetBandwidthChangeOrderRequestBody.
        :type cloud_service_console_url: str
        """
        self._cloud_service_console_url = cloud_service_console_url

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateSubnetBandwidthChangeOrderRequestBody.

        企业项目ID

        :return: The enterprise_project_id of this CreateSubnetBandwidthChangeOrderRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateSubnetBandwidthChangeOrderRequestBody.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateSubnetBandwidthChangeOrderRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def extend_param(self):
        """Gets the extend_param of this CreateSubnetBandwidthChangeOrderRequestBody.

        :return: The extend_param of this CreateSubnetBandwidthChangeOrderRequestBody.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this CreateSubnetBandwidthChangeOrderRequestBody.

        :param extend_param: The extend_param of this CreateSubnetBandwidthChangeOrderRequestBody.
        :type extend_param: :class:`huaweicloudsdkworkspace.v2.OrderExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, CreateSubnetBandwidthChangeOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
