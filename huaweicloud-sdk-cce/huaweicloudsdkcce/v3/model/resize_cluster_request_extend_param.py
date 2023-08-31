# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeClusterRequestExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dec_master_flavor': 'str',
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'dec_master_flavor': 'decMasterFlavor',
        'is_auto_pay': 'isAutoPay'
    }

    def __init__(self, dec_master_flavor=None, is_auto_pay=None):
        """ResizeClusterRequestExtendParam

        The model defined in huaweicloud sdk

        :param dec_master_flavor: 专属云CCE集群可指定控制节点的规格
        :type dec_master_flavor: str
        :param is_auto_pay: 是否自动扣款 - “true”：自动扣款 - “false”：不自动扣款 &gt; 包周期集群时生效，不填写此参数时默认不会自动扣款。 
        :type is_auto_pay: str
        """
        
        

        self._dec_master_flavor = None
        self._is_auto_pay = None
        self.discriminator = None

        if dec_master_flavor is not None:
            self.dec_master_flavor = dec_master_flavor
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def dec_master_flavor(self):
        """Gets the dec_master_flavor of this ResizeClusterRequestExtendParam.

        专属云CCE集群可指定控制节点的规格

        :return: The dec_master_flavor of this ResizeClusterRequestExtendParam.
        :rtype: str
        """
        return self._dec_master_flavor

    @dec_master_flavor.setter
    def dec_master_flavor(self, dec_master_flavor):
        """Sets the dec_master_flavor of this ResizeClusterRequestExtendParam.

        专属云CCE集群可指定控制节点的规格

        :param dec_master_flavor: The dec_master_flavor of this ResizeClusterRequestExtendParam.
        :type dec_master_flavor: str
        """
        self._dec_master_flavor = dec_master_flavor

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ResizeClusterRequestExtendParam.

        是否自动扣款 - “true”：自动扣款 - “false”：不自动扣款 > 包周期集群时生效，不填写此参数时默认不会自动扣款。 

        :return: The is_auto_pay of this ResizeClusterRequestExtendParam.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ResizeClusterRequestExtendParam.

        是否自动扣款 - “true”：自动扣款 - “false”：不自动扣款 > 包周期集群时生效，不填写此参数时默认不会自动扣款。 

        :param is_auto_pay: The is_auto_pay of this ResizeClusterRequestExtendParam.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, ResizeClusterRequestExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
