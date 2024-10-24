# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountAssignmentCreationStatusRequest:

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
        'status': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'instance_id': 'instance_id',
        'status': 'status',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, x_security_token=None, instance_id=None, status=None, limit=None, marker=None):
        """ListAccountAssignmentCreationStatusRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param instance_id: IAM身份中心实例的全局唯一标识符（ID）。
        :type instance_id: str
        :param status: 根据传递的属性值过滤操作状态列表
        :type status: str
        :param limit: 每个请求返回的最大结果数
        :type limit: int
        :param marker: 分页标记
        :type marker: str
        """
        
        

        self._x_security_token = None
        self._instance_id = None
        self._status = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.instance_id = instance_id
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def x_security_token(self):
        """Gets the x_security_token of this ListAccountAssignmentCreationStatusRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListAccountAssignmentCreationStatusRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        """Sets the x_security_token of this ListAccountAssignmentCreationStatusRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListAccountAssignmentCreationStatusRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def instance_id(self):
        """Gets the instance_id of this ListAccountAssignmentCreationStatusRequest.

        IAM身份中心实例的全局唯一标识符（ID）。

        :return: The instance_id of this ListAccountAssignmentCreationStatusRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListAccountAssignmentCreationStatusRequest.

        IAM身份中心实例的全局唯一标识符（ID）。

        :param instance_id: The instance_id of this ListAccountAssignmentCreationStatusRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        """Gets the status of this ListAccountAssignmentCreationStatusRequest.

        根据传递的属性值过滤操作状态列表

        :return: The status of this ListAccountAssignmentCreationStatusRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAccountAssignmentCreationStatusRequest.

        根据传递的属性值过滤操作状态列表

        :param status: The status of this ListAccountAssignmentCreationStatusRequest.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this ListAccountAssignmentCreationStatusRequest.

        每个请求返回的最大结果数

        :return: The limit of this ListAccountAssignmentCreationStatusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAccountAssignmentCreationStatusRequest.

        每个请求返回的最大结果数

        :param limit: The limit of this ListAccountAssignmentCreationStatusRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListAccountAssignmentCreationStatusRequest.

        分页标记

        :return: The marker of this ListAccountAssignmentCreationStatusRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAccountAssignmentCreationStatusRequest.

        分页标记

        :param marker: The marker of this ListAccountAssignmentCreationStatusRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListAccountAssignmentCreationStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
