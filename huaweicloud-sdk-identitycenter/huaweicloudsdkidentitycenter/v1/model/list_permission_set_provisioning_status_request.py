# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionSetProvisioningStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'instance_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'status': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'instance_id': 'instance_id',
        'limit': 'limit',
        'marker': 'marker',
        'status': 'status'
    }

    def __init__(self, x_security_token=None, instance_id=None, limit=None, marker=None, status=None):
        r"""ListPermissionSetProvisioningStatusRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param instance_id: IAM Identity Center实例的全局唯一标识符（ID）
        :type instance_id: str
        :param limit: 每个请求返回的最大结果数。
        :type limit: int
        :param marker: 分页标记
        :type marker: str
        :param status: 根据传递的属性值过滤操作状态列表
        :type status: str
        """
        
        

        self._x_security_token = None
        self._instance_id = None
        self._limit = None
        self._marker = None
        self._status = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if status is not None:
            self.status = status

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListPermissionSetProvisioningStatusRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListPermissionSetProvisioningStatusRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListPermissionSetProvisioningStatusRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListPermissionSetProvisioningStatusRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListPermissionSetProvisioningStatusRequest.

        IAM Identity Center实例的全局唯一标识符（ID）

        :return: The instance_id of this ListPermissionSetProvisioningStatusRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListPermissionSetProvisioningStatusRequest.

        IAM Identity Center实例的全局唯一标识符（ID）

        :param instance_id: The instance_id of this ListPermissionSetProvisioningStatusRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListPermissionSetProvisioningStatusRequest.

        每个请求返回的最大结果数。

        :return: The limit of this ListPermissionSetProvisioningStatusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPermissionSetProvisioningStatusRequest.

        每个请求返回的最大结果数。

        :param limit: The limit of this ListPermissionSetProvisioningStatusRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListPermissionSetProvisioningStatusRequest.

        分页标记

        :return: The marker of this ListPermissionSetProvisioningStatusRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPermissionSetProvisioningStatusRequest.

        分页标记

        :param marker: The marker of this ListPermissionSetProvisioningStatusRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def status(self):
        r"""Gets the status of this ListPermissionSetProvisioningStatusRequest.

        根据传递的属性值过滤操作状态列表

        :return: The status of this ListPermissionSetProvisioningStatusRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPermissionSetProvisioningStatusRequest.

        根据传递的属性值过滤操作状态列表

        :param status: The status of this ListPermissionSetProvisioningStatusRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListPermissionSetProvisioningStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
