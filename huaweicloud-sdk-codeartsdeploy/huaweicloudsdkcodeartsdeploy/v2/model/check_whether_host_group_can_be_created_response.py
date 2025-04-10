# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckWhetherHostGroupCanBeCreatedResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_created': 'bool'
    }

    attribute_map = {
        'can_created': 'can_created'
    }

    def __init__(self, can_created=None):
        r"""CheckWhetherHostGroupCanBeCreatedResponse

        The model defined in huaweicloud sdk

        :param can_created: 是否有创建主机集群权限，true 有权限 false 无权限
        :type can_created: bool
        """
        
        super(CheckWhetherHostGroupCanBeCreatedResponse, self).__init__()

        self._can_created = None
        self.discriminator = None

        if can_created is not None:
            self.can_created = can_created

    @property
    def can_created(self):
        r"""Gets the can_created of this CheckWhetherHostGroupCanBeCreatedResponse.

        是否有创建主机集群权限，true 有权限 false 无权限

        :return: The can_created of this CheckWhetherHostGroupCanBeCreatedResponse.
        :rtype: bool
        """
        return self._can_created

    @can_created.setter
    def can_created(self, can_created):
        r"""Sets the can_created of this CheckWhetherHostGroupCanBeCreatedResponse.

        是否有创建主机集群权限，true 有权限 false 无权限

        :param can_created: The can_created of this CheckWhetherHostGroupCanBeCreatedResponse.
        :type can_created: bool
        """
        self._can_created = can_created

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
        if not isinstance(other, CheckWhetherHostGroupCanBeCreatedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
