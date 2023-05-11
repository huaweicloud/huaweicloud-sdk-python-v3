# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubscriptionInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'resources': 'list[ResourceResponse]',
        'is_new_user': 'bool',
        'premium': 'Premium'
    }

    attribute_map = {
        'type': 'type',
        'resources': 'resources',
        'is_new_user': 'isNewUser',
        'premium': 'premium'
    }

    def __init__(self, type=None, resources=None, is_new_user=None, premium=None):
        """ShowSubscriptionInfoResponse

        The model defined in huaweicloud sdk

        :param type: 云模式版本   - -2：已冻结   - -1：未订购   - 2：标准版   - 3：专业版   - 4：铂金版   - 7:入门版   - 22：按需版本
        :type type: int
        :param resources: 资源列表
        :type resources: list[:class:`huaweicloudsdkwaf.v1.ResourceResponse`]
        :param is_new_user: 是否为新用户
        :type is_new_user: bool
        :param premium: 
        :type premium: :class:`huaweicloudsdkwaf.v1.Premium`
        """
        
        super(ShowSubscriptionInfoResponse, self).__init__()

        self._type = None
        self._resources = None
        self._is_new_user = None
        self._premium = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if resources is not None:
            self.resources = resources
        if is_new_user is not None:
            self.is_new_user = is_new_user
        if premium is not None:
            self.premium = premium

    @property
    def type(self):
        """Gets the type of this ShowSubscriptionInfoResponse.

        云模式版本   - -2：已冻结   - -1：未订购   - 2：标准版   - 3：专业版   - 4：铂金版   - 7:入门版   - 22：按需版本

        :return: The type of this ShowSubscriptionInfoResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowSubscriptionInfoResponse.

        云模式版本   - -2：已冻结   - -1：未订购   - 2：标准版   - 3：专业版   - 4：铂金版   - 7:入门版   - 22：按需版本

        :param type: The type of this ShowSubscriptionInfoResponse.
        :type type: int
        """
        self._type = type

    @property
    def resources(self):
        """Gets the resources of this ShowSubscriptionInfoResponse.

        资源列表

        :return: The resources of this ShowSubscriptionInfoResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.ResourceResponse`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ShowSubscriptionInfoResponse.

        资源列表

        :param resources: The resources of this ShowSubscriptionInfoResponse.
        :type resources: list[:class:`huaweicloudsdkwaf.v1.ResourceResponse`]
        """
        self._resources = resources

    @property
    def is_new_user(self):
        """Gets the is_new_user of this ShowSubscriptionInfoResponse.

        是否为新用户

        :return: The is_new_user of this ShowSubscriptionInfoResponse.
        :rtype: bool
        """
        return self._is_new_user

    @is_new_user.setter
    def is_new_user(self, is_new_user):
        """Sets the is_new_user of this ShowSubscriptionInfoResponse.

        是否为新用户

        :param is_new_user: The is_new_user of this ShowSubscriptionInfoResponse.
        :type is_new_user: bool
        """
        self._is_new_user = is_new_user

    @property
    def premium(self):
        """Gets the premium of this ShowSubscriptionInfoResponse.

        :return: The premium of this ShowSubscriptionInfoResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.Premium`
        """
        return self._premium

    @premium.setter
    def premium(self, premium):
        """Sets the premium of this ShowSubscriptionInfoResponse.

        :param premium: The premium of this ShowSubscriptionInfoResponse.
        :type premium: :class:`huaweicloudsdkwaf.v1.Premium`
        """
        self._premium = premium

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
        if not isinstance(other, ShowSubscriptionInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
