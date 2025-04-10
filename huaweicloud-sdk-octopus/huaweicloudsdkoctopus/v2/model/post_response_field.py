# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostResponseField:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'x_amz_algorithm': 'str',
        'x_amz_credential': 'str',
        'x_amz_date': 'str',
        'policy': 'str',
        'x_amz_signature': 'str'
    }

    attribute_map = {
        'key': 'key',
        'x_amz_algorithm': 'x-amz-algorithm',
        'x_amz_credential': 'x-amz-credential',
        'x_amz_date': 'x-amz-date',
        'policy': 'policy',
        'x_amz_signature': 'x-amz-signature'
    }

    def __init__(self, key=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_date=None, policy=None, x_amz_signature=None):
        r"""PostResponseField

        The model defined in huaweicloud sdk

        :param key: 
        :type key: str
        :param x_amz_algorithm: 
        :type x_amz_algorithm: str
        :param x_amz_credential: 
        :type x_amz_credential: str
        :param x_amz_date: 
        :type x_amz_date: str
        :param policy: 
        :type policy: str
        :param x_amz_signature: 
        :type x_amz_signature: str
        """
        
        

        self._key = None
        self._x_amz_algorithm = None
        self._x_amz_credential = None
        self._x_amz_date = None
        self._policy = None
        self._x_amz_signature = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if x_amz_algorithm is not None:
            self.x_amz_algorithm = x_amz_algorithm
        if x_amz_credential is not None:
            self.x_amz_credential = x_amz_credential
        if x_amz_date is not None:
            self.x_amz_date = x_amz_date
        if policy is not None:
            self.policy = policy
        if x_amz_signature is not None:
            self.x_amz_signature = x_amz_signature

    @property
    def key(self):
        r"""Gets the key of this PostResponseField.

        :return: The key of this PostResponseField.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this PostResponseField.

        :param key: The key of this PostResponseField.
        :type key: str
        """
        self._key = key

    @property
    def x_amz_algorithm(self):
        r"""Gets the x_amz_algorithm of this PostResponseField.

        :return: The x_amz_algorithm of this PostResponseField.
        :rtype: str
        """
        return self._x_amz_algorithm

    @x_amz_algorithm.setter
    def x_amz_algorithm(self, x_amz_algorithm):
        r"""Sets the x_amz_algorithm of this PostResponseField.

        :param x_amz_algorithm: The x_amz_algorithm of this PostResponseField.
        :type x_amz_algorithm: str
        """
        self._x_amz_algorithm = x_amz_algorithm

    @property
    def x_amz_credential(self):
        r"""Gets the x_amz_credential of this PostResponseField.

        :return: The x_amz_credential of this PostResponseField.
        :rtype: str
        """
        return self._x_amz_credential

    @x_amz_credential.setter
    def x_amz_credential(self, x_amz_credential):
        r"""Sets the x_amz_credential of this PostResponseField.

        :param x_amz_credential: The x_amz_credential of this PostResponseField.
        :type x_amz_credential: str
        """
        self._x_amz_credential = x_amz_credential

    @property
    def x_amz_date(self):
        r"""Gets the x_amz_date of this PostResponseField.

        :return: The x_amz_date of this PostResponseField.
        :rtype: str
        """
        return self._x_amz_date

    @x_amz_date.setter
    def x_amz_date(self, x_amz_date):
        r"""Sets the x_amz_date of this PostResponseField.

        :param x_amz_date: The x_amz_date of this PostResponseField.
        :type x_amz_date: str
        """
        self._x_amz_date = x_amz_date

    @property
    def policy(self):
        r"""Gets the policy of this PostResponseField.

        :return: The policy of this PostResponseField.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this PostResponseField.

        :param policy: The policy of this PostResponseField.
        :type policy: str
        """
        self._policy = policy

    @property
    def x_amz_signature(self):
        r"""Gets the x_amz_signature of this PostResponseField.

        :return: The x_amz_signature of this PostResponseField.
        :rtype: str
        """
        return self._x_amz_signature

    @x_amz_signature.setter
    def x_amz_signature(self, x_amz_signature):
        r"""Sets the x_amz_signature of this PostResponseField.

        :param x_amz_signature: The x_amz_signature of this PostResponseField.
        :type x_amz_signature: str
        """
        self._x_amz_signature = x_amz_signature

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
        if not isinstance(other, PostResponseField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
