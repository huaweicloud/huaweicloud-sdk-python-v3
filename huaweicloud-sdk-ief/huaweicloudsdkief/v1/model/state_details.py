# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StateDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'register_stat': 'str',
        'purchase_stat': 'str',
        'purchase_error': 'str'
    }

    attribute_map = {
        'register_stat': 'register_stat',
        'purchase_stat': 'purchase_stat',
        'purchase_error': 'purchase_error'
    }

    def __init__(self, register_stat=None, purchase_stat=None, purchase_error=None):
        r"""StateDetails

        The model defined in huaweicloud sdk

        :param register_stat: IEC/IES节点注册状态
        :type register_stat: str
        :param purchase_stat: IEC/IES节点状态
        :type purchase_stat: str
        :param purchase_error: IEC/IES节点错误信息
        :type purchase_error: str
        """
        
        

        self._register_stat = None
        self._purchase_stat = None
        self._purchase_error = None
        self.discriminator = None

        if register_stat is not None:
            self.register_stat = register_stat
        if purchase_stat is not None:
            self.purchase_stat = purchase_stat
        if purchase_error is not None:
            self.purchase_error = purchase_error

    @property
    def register_stat(self):
        r"""Gets the register_stat of this StateDetails.

        IEC/IES节点注册状态

        :return: The register_stat of this StateDetails.
        :rtype: str
        """
        return self._register_stat

    @register_stat.setter
    def register_stat(self, register_stat):
        r"""Sets the register_stat of this StateDetails.

        IEC/IES节点注册状态

        :param register_stat: The register_stat of this StateDetails.
        :type register_stat: str
        """
        self._register_stat = register_stat

    @property
    def purchase_stat(self):
        r"""Gets the purchase_stat of this StateDetails.

        IEC/IES节点状态

        :return: The purchase_stat of this StateDetails.
        :rtype: str
        """
        return self._purchase_stat

    @purchase_stat.setter
    def purchase_stat(self, purchase_stat):
        r"""Sets the purchase_stat of this StateDetails.

        IEC/IES节点状态

        :param purchase_stat: The purchase_stat of this StateDetails.
        :type purchase_stat: str
        """
        self._purchase_stat = purchase_stat

    @property
    def purchase_error(self):
        r"""Gets the purchase_error of this StateDetails.

        IEC/IES节点错误信息

        :return: The purchase_error of this StateDetails.
        :rtype: str
        """
        return self._purchase_error

    @purchase_error.setter
    def purchase_error(self, purchase_error):
        r"""Sets the purchase_error of this StateDetails.

        IEC/IES节点错误信息

        :param purchase_error: The purchase_error of this StateDetails.
        :type purchase_error: str
        """
        self._purchase_error = purchase_error

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
        if not isinstance(other, StateDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
