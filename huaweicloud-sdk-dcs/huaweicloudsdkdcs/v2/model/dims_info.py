# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DimsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dim_k': 'str',
        'dim_v': 'str'
    }

    attribute_map = {
        'dim_k': 'dim_k',
        'dim_v': 'dim_v'
    }

    def __init__(self, dim_k=None, dim_v=None):
        r"""DimsInfo

        The model defined in huaweicloud sdk

        :param dim_k: **参数解释**： CES监控维度路由。 **取值范围**： 不涉及。 
        :type dim_k: str
        :param dim_v: **参数解释**： CES监控维度ID。 **取值范围**： 不涉及。 
        :type dim_v: str
        """
        
        

        self._dim_k = None
        self._dim_v = None
        self.discriminator = None

        if dim_k is not None:
            self.dim_k = dim_k
        if dim_v is not None:
            self.dim_v = dim_v

    @property
    def dim_k(self):
        r"""Gets the dim_k of this DimsInfo.

        **参数解释**： CES监控维度路由。 **取值范围**： 不涉及。 

        :return: The dim_k of this DimsInfo.
        :rtype: str
        """
        return self._dim_k

    @dim_k.setter
    def dim_k(self, dim_k):
        r"""Sets the dim_k of this DimsInfo.

        **参数解释**： CES监控维度路由。 **取值范围**： 不涉及。 

        :param dim_k: The dim_k of this DimsInfo.
        :type dim_k: str
        """
        self._dim_k = dim_k

    @property
    def dim_v(self):
        r"""Gets the dim_v of this DimsInfo.

        **参数解释**： CES监控维度ID。 **取值范围**： 不涉及。 

        :return: The dim_v of this DimsInfo.
        :rtype: str
        """
        return self._dim_v

    @dim_v.setter
    def dim_v(self, dim_v):
        r"""Sets the dim_v of this DimsInfo.

        **参数解释**： CES监控维度ID。 **取值范围**： 不涉及。 

        :param dim_v: The dim_v of this DimsInfo.
        :type dim_v: str
        """
        self._dim_v = dim_v

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
        if not isinstance(other, DimsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
