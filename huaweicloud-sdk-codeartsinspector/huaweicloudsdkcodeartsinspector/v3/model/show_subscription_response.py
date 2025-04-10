# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubscriptionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'force_purchase': 'bool',
        'amount': 'int',
        'expire_time': 'str',
        'limit': 'int',
        'resources': 'list[ShowSubscriptionResources]',
        'used': 'int',
        'type': 'int',
        'is_new_user': 'bool',
        'version': 'str'
    }

    attribute_map = {
        'force_purchase': 'forcePurchase',
        'amount': 'amount',
        'expire_time': 'expireTime',
        'limit': 'limit',
        'resources': 'resources',
        'used': 'used',
        'type': 'type',
        'is_new_user': 'isNewUser',
        'version': 'version'
    }

    def __init__(self, force_purchase=None, amount=None, expire_time=None, limit=None, resources=None, used=None, type=None, is_new_user=None, version=None):
        r"""ShowSubscriptionResponse

        The model defined in huaweicloud sdk

        :param force_purchase: forcePurchase
        :type force_purchase: bool
        :param amount: amount
        :type amount: int
        :param expire_time: expire_time
        :type expire_time: str
        :param limit: limit
        :type limit: int
        :param resources: resources
        :type resources: list[:class:`huaweicloudsdkcodeartsinspector.v3.ShowSubscriptionResources`]
        :param used: used
        :type used: int
        :param type: type
        :type type: int
        :param is_new_user: isNewUser
        :type is_new_user: bool
        :param version: version
        :type version: str
        """
        
        super(ShowSubscriptionResponse, self).__init__()

        self._force_purchase = None
        self._amount = None
        self._expire_time = None
        self._limit = None
        self._resources = None
        self._used = None
        self._type = None
        self._is_new_user = None
        self._version = None
        self.discriminator = None

        if force_purchase is not None:
            self.force_purchase = force_purchase
        if amount is not None:
            self.amount = amount
        if expire_time is not None:
            self.expire_time = expire_time
        if limit is not None:
            self.limit = limit
        if resources is not None:
            self.resources = resources
        if used is not None:
            self.used = used
        if type is not None:
            self.type = type
        if is_new_user is not None:
            self.is_new_user = is_new_user
        if version is not None:
            self.version = version

    @property
    def force_purchase(self):
        r"""Gets the force_purchase of this ShowSubscriptionResponse.

        forcePurchase

        :return: The force_purchase of this ShowSubscriptionResponse.
        :rtype: bool
        """
        return self._force_purchase

    @force_purchase.setter
    def force_purchase(self, force_purchase):
        r"""Sets the force_purchase of this ShowSubscriptionResponse.

        forcePurchase

        :param force_purchase: The force_purchase of this ShowSubscriptionResponse.
        :type force_purchase: bool
        """
        self._force_purchase = force_purchase

    @property
    def amount(self):
        r"""Gets the amount of this ShowSubscriptionResponse.

        amount

        :return: The amount of this ShowSubscriptionResponse.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this ShowSubscriptionResponse.

        amount

        :param amount: The amount of this ShowSubscriptionResponse.
        :type amount: int
        """
        self._amount = amount

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ShowSubscriptionResponse.

        expire_time

        :return: The expire_time of this ShowSubscriptionResponse.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ShowSubscriptionResponse.

        expire_time

        :param expire_time: The expire_time of this ShowSubscriptionResponse.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def limit(self):
        r"""Gets the limit of this ShowSubscriptionResponse.

        limit

        :return: The limit of this ShowSubscriptionResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowSubscriptionResponse.

        limit

        :param limit: The limit of this ShowSubscriptionResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def resources(self):
        r"""Gets the resources of this ShowSubscriptionResponse.

        resources

        :return: The resources of this ShowSubscriptionResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsinspector.v3.ShowSubscriptionResources`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ShowSubscriptionResponse.

        resources

        :param resources: The resources of this ShowSubscriptionResponse.
        :type resources: list[:class:`huaweicloudsdkcodeartsinspector.v3.ShowSubscriptionResources`]
        """
        self._resources = resources

    @property
    def used(self):
        r"""Gets the used of this ShowSubscriptionResponse.

        used

        :return: The used of this ShowSubscriptionResponse.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this ShowSubscriptionResponse.

        used

        :param used: The used of this ShowSubscriptionResponse.
        :type used: int
        """
        self._used = used

    @property
    def type(self):
        r"""Gets the type of this ShowSubscriptionResponse.

        type

        :return: The type of this ShowSubscriptionResponse.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowSubscriptionResponse.

        type

        :param type: The type of this ShowSubscriptionResponse.
        :type type: int
        """
        self._type = type

    @property
    def is_new_user(self):
        r"""Gets the is_new_user of this ShowSubscriptionResponse.

        isNewUser

        :return: The is_new_user of this ShowSubscriptionResponse.
        :rtype: bool
        """
        return self._is_new_user

    @is_new_user.setter
    def is_new_user(self, is_new_user):
        r"""Sets the is_new_user of this ShowSubscriptionResponse.

        isNewUser

        :param is_new_user: The is_new_user of this ShowSubscriptionResponse.
        :type is_new_user: bool
        """
        self._is_new_user = is_new_user

    @property
    def version(self):
        r"""Gets the version of this ShowSubscriptionResponse.

        version

        :return: The version of this ShowSubscriptionResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowSubscriptionResponse.

        version

        :param version: The version of this ShowSubscriptionResponse.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ShowSubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
