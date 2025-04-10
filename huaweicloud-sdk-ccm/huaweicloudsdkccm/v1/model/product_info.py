# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, cloud_service_type=None, resource_type=None, resource_spec_code=None):
        r"""ProductInfo

        The model defined in huaweicloud sdk

        :param cloud_service_type: 云服务类型，固定为&#39;hws.service.type.ccm&#39;
        :type cloud_service_type: str
        :param resource_type: 资源类型，CA为\&quot;hws.resource.type.pca.duration\&quot;
        :type resource_type: str
        :param resource_spec_code: 资源规格编码，CA为\&quot;ca.duration\&quot;
        :type resource_spec_code: str
        """
        
        

        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self.discriminator = None

        self.cloud_service_type = cloud_service_type
        self.resource_type = resource_type
        self.resource_spec_code = resource_spec_code

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ProductInfo.

        云服务类型，固定为'hws.service.type.ccm'

        :return: The cloud_service_type of this ProductInfo.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ProductInfo.

        云服务类型，固定为'hws.service.type.ccm'

        :param cloud_service_type: The cloud_service_type of this ProductInfo.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ProductInfo.

        资源类型，CA为\"hws.resource.type.pca.duration\"

        :return: The resource_type of this ProductInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ProductInfo.

        资源类型，CA为\"hws.resource.type.pca.duration\"

        :param resource_type: The resource_type of this ProductInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ProductInfo.

        资源规格编码，CA为\"ca.duration\"

        :return: The resource_spec_code of this ProductInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ProductInfo.

        资源规格编码，CA为\"ca.duration\"

        :param resource_spec_code: The resource_spec_code of this ProductInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
        if not isinstance(other, ProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
