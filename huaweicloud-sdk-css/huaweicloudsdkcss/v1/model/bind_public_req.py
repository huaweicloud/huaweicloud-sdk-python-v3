# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindPublicReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip': 'BindPublicReqEip',
        'white_list': 'str',
        'is_auto_pay': 'int'
    }

    attribute_map = {
        'eip': 'eip',
        'white_list': 'white_list',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, eip=None, white_list=None, is_auto_pay=None):
        r"""BindPublicReq

        The model defined in huaweicloud sdk

        :param eip: 
        :type eip: :class:`huaweicloudsdkcss.v1.BindPublicReqEip`
        :param white_list: 公网访问控制白名单。
        :type white_list: str
        :param is_auto_pay: 
        :type is_auto_pay: int
        """
        
        

        self._eip = None
        self._white_list = None
        self._is_auto_pay = None
        self.discriminator = None

        self.eip = eip
        if white_list is not None:
            self.white_list = white_list
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def eip(self):
        r"""Gets the eip of this BindPublicReq.

        :return: The eip of this BindPublicReq.
        :rtype: :class:`huaweicloudsdkcss.v1.BindPublicReqEip`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this BindPublicReq.

        :param eip: The eip of this BindPublicReq.
        :type eip: :class:`huaweicloudsdkcss.v1.BindPublicReqEip`
        """
        self._eip = eip

    @property
    def white_list(self):
        r"""Gets the white_list of this BindPublicReq.

        公网访问控制白名单。

        :return: The white_list of this BindPublicReq.
        :rtype: str
        """
        return self._white_list

    @white_list.setter
    def white_list(self, white_list):
        r"""Sets the white_list of this BindPublicReq.

        公网访问控制白名单。

        :param white_list: The white_list of this BindPublicReq.
        :type white_list: str
        """
        self._white_list = white_list

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this BindPublicReq.

        :return: The is_auto_pay of this BindPublicReq.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this BindPublicReq.

        :param is_auto_pay: The is_auto_pay of this BindPublicReq.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, BindPublicReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
