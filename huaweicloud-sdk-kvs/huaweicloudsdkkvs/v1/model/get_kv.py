# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetKv:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'oper_id': 'int',
        'primary_key': 'dict'
    }

    attribute_map = {
        'oper_id': 'oper_id',
        'primary_key': 'primary_key'
    }

    def __init__(self, oper_id=None, primary_key=None):
        r"""GetKv

        The model defined in huaweicloud sdk

        :param oper_id: 请求内的操作编码，未成功的操作返回该标识。
        :type oper_id: int
        :param primary_key: 用户自定义的主键名及值。
        :type primary_key: dict
        """
        
        

        self._oper_id = None
        self._primary_key = None
        self.discriminator = None

        self.oper_id = oper_id
        self.primary_key = primary_key

    @property
    def oper_id(self):
        r"""Gets the oper_id of this GetKv.

        请求内的操作编码，未成功的操作返回该标识。

        :return: The oper_id of this GetKv.
        :rtype: int
        """
        return self._oper_id

    @oper_id.setter
    def oper_id(self, oper_id):
        r"""Sets the oper_id of this GetKv.

        请求内的操作编码，未成功的操作返回该标识。

        :param oper_id: The oper_id of this GetKv.
        :type oper_id: int
        """
        self._oper_id = oper_id

    @property
    def primary_key(self):
        r"""Gets the primary_key of this GetKv.

        用户自定义的主键名及值。

        :return: The primary_key of this GetKv.
        :rtype: dict
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this GetKv.

        用户自定义的主键名及值。

        :param primary_key: The primary_key of this GetKv.
        :type primary_key: dict
        """
        self._primary_key = primary_key

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
        if not isinstance(other, GetKv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
