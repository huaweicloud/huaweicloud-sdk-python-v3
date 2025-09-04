# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserChargeTypeResultMainResourceList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'status': 'status',
        'service_type': 'service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, status=None, service_type=None, resource_type=None, resource_spec_code=None):
        r"""ShowUserChargeTypeResultMainResourceList

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: str
        :param service_type: 服务类型
        :type service_type: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_spec_code: 资源包类型
        :type resource_spec_code: str
        """
        
        

        self._status = None
        self._service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if service_type is not None:
            self.service_type = service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code

    @property
    def status(self):
        r"""Gets the status of this ShowUserChargeTypeResultMainResourceList.

        状态

        :return: The status of this ShowUserChargeTypeResultMainResourceList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowUserChargeTypeResultMainResourceList.

        状态

        :param status: The status of this ShowUserChargeTypeResultMainResourceList.
        :type status: str
        """
        self._status = status

    @property
    def service_type(self):
        r"""Gets the service_type of this ShowUserChargeTypeResultMainResourceList.

        服务类型

        :return: The service_type of this ShowUserChargeTypeResultMainResourceList.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ShowUserChargeTypeResultMainResourceList.

        服务类型

        :param service_type: The service_type of this ShowUserChargeTypeResultMainResourceList.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowUserChargeTypeResultMainResourceList.

        资源类型

        :return: The resource_type of this ShowUserChargeTypeResultMainResourceList.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowUserChargeTypeResultMainResourceList.

        资源类型

        :param resource_type: The resource_type of this ShowUserChargeTypeResultMainResourceList.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ShowUserChargeTypeResultMainResourceList.

        资源包类型

        :return: The resource_spec_code of this ShowUserChargeTypeResultMainResourceList.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ShowUserChargeTypeResultMainResourceList.

        资源包类型

        :param resource_spec_code: The resource_spec_code of this ShowUserChargeTypeResultMainResourceList.
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
        if not isinstance(other, ShowUserChargeTypeResultMainResourceList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
