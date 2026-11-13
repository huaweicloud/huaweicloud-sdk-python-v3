# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDPDetailVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add_idp': 'IDPInfo',
        'update_idp': 'IDPInfo',
        'del_idp': 'IDPInfo'
    }

    attribute_map = {
        'add_idp': 'add_idp',
        'update_idp': 'update_idp',
        'del_idp': 'del_idp'
    }

    def __init__(self, add_idp=None, update_idp=None, del_idp=None):
        r"""IDPDetailVo

        The model defined in huaweicloud sdk

        :param add_idp: 
        :type add_idp: :class:`huaweicloudsdkdoczip.v1.IDPInfo`
        :param update_idp: 
        :type update_idp: :class:`huaweicloudsdkdoczip.v1.IDPInfo`
        :param del_idp: 
        :type del_idp: :class:`huaweicloudsdkdoczip.v1.IDPInfo`
        """
        
        

        self._add_idp = None
        self._update_idp = None
        self._del_idp = None
        self.discriminator = None

        if add_idp is not None:
            self.add_idp = add_idp
        if update_idp is not None:
            self.update_idp = update_idp
        if del_idp is not None:
            self.del_idp = del_idp

    @property
    def add_idp(self):
        r"""Gets the add_idp of this IDPDetailVo.

        :return: The add_idp of this IDPDetailVo.
        :rtype: :class:`huaweicloudsdkdoczip.v1.IDPInfo`
        """
        return self._add_idp

    @add_idp.setter
    def add_idp(self, add_idp):
        r"""Sets the add_idp of this IDPDetailVo.

        :param add_idp: The add_idp of this IDPDetailVo.
        :type add_idp: :class:`huaweicloudsdkdoczip.v1.IDPInfo`
        """
        self._add_idp = add_idp

    @property
    def update_idp(self):
        r"""Gets the update_idp of this IDPDetailVo.

        :return: The update_idp of this IDPDetailVo.
        :rtype: :class:`huaweicloudsdkdoczip.v1.IDPInfo`
        """
        return self._update_idp

    @update_idp.setter
    def update_idp(self, update_idp):
        r"""Sets the update_idp of this IDPDetailVo.

        :param update_idp: The update_idp of this IDPDetailVo.
        :type update_idp: :class:`huaweicloudsdkdoczip.v1.IDPInfo`
        """
        self._update_idp = update_idp

    @property
    def del_idp(self):
        r"""Gets the del_idp of this IDPDetailVo.

        :return: The del_idp of this IDPDetailVo.
        :rtype: :class:`huaweicloudsdkdoczip.v1.IDPInfo`
        """
        return self._del_idp

    @del_idp.setter
    def del_idp(self, del_idp):
        r"""Sets the del_idp of this IDPDetailVo.

        :param del_idp: The del_idp of this IDPDetailVo.
        :type del_idp: :class:`huaweicloudsdkdoczip.v1.IDPInfo`
        """
        self._del_idp = del_idp

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
        if not isinstance(other, IDPDetailVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
