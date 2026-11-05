# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchSupabaseApplicationEipBindRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_bind': 'bool',
        'public_ip_address': 'str',
        'public_ip_id': 'str'
    }

    attribute_map = {
        'is_bind': 'is_bind',
        'public_ip_address': 'public_ip_address',
        'public_ip_id': 'public_ip_id'
    }

    def __init__(self, is_bind=None, public_ip_address=None, public_ip_id=None):
        r"""SwitchSupabaseApplicationEipBindRequestBody

        The model defined in huaweicloud sdk

        :param is_bind: true绑定，false解绑。is_bind&#x3D;true时public_ip_id和public_ip_address必填。
        :type is_bind: bool
        :param public_ip_address: 弹性公网IP地址。
        :type public_ip_address: str
        :param public_ip_id: 弹性公网IP ID（UUID）。
        :type public_ip_id: str
        """
        
        

        self._is_bind = None
        self._public_ip_address = None
        self._public_ip_id = None
        self.discriminator = None

        self.is_bind = is_bind
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id

    @property
    def is_bind(self):
        r"""Gets the is_bind of this SwitchSupabaseApplicationEipBindRequestBody.

        true绑定，false解绑。is_bind=true时public_ip_id和public_ip_address必填。

        :return: The is_bind of this SwitchSupabaseApplicationEipBindRequestBody.
        :rtype: bool
        """
        return self._is_bind

    @is_bind.setter
    def is_bind(self, is_bind):
        r"""Sets the is_bind of this SwitchSupabaseApplicationEipBindRequestBody.

        true绑定，false解绑。is_bind=true时public_ip_id和public_ip_address必填。

        :param is_bind: The is_bind of this SwitchSupabaseApplicationEipBindRequestBody.
        :type is_bind: bool
        """
        self._is_bind = is_bind

    @property
    def public_ip_address(self):
        r"""Gets the public_ip_address of this SwitchSupabaseApplicationEipBindRequestBody.

        弹性公网IP地址。

        :return: The public_ip_address of this SwitchSupabaseApplicationEipBindRequestBody.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        r"""Sets the public_ip_address of this SwitchSupabaseApplicationEipBindRequestBody.

        弹性公网IP地址。

        :param public_ip_address: The public_ip_address of this SwitchSupabaseApplicationEipBindRequestBody.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def public_ip_id(self):
        r"""Gets the public_ip_id of this SwitchSupabaseApplicationEipBindRequestBody.

        弹性公网IP ID（UUID）。

        :return: The public_ip_id of this SwitchSupabaseApplicationEipBindRequestBody.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        r"""Sets the public_ip_id of this SwitchSupabaseApplicationEipBindRequestBody.

        弹性公网IP ID（UUID）。

        :param public_ip_id: The public_ip_id of this SwitchSupabaseApplicationEipBindRequestBody.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

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
        if not isinstance(other, SwitchSupabaseApplicationEipBindRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
