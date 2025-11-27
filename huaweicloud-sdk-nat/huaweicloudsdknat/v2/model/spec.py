# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Spec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'code': 'str',
        'cbc_code': 'str',
        'rule_max': 'int',
        'sess_max': 'int',
        'bps_max': 'int',
        'pps_max': 'int',
        'qps_max': 'int'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'cbc_code': 'cbc_code',
        'rule_max': 'rule_max',
        'sess_max': 'sess_max',
        'bps_max': 'bps_max',
        'pps_max': 'pps_max',
        'qps_max': 'qps_max'
    }

    def __init__(self, name=None, code=None, cbc_code=None, rule_max=None, sess_max=None, bps_max=None, pps_max=None, qps_max=None):
        r"""Spec

        The model defined in huaweicloud sdk

        :param name: 规格名称。
        :type name: str
        :param code: 规格编号。
        :type code: str
        :param cbc_code: 规格cbc编码。
        :type cbc_code: str
        :param rule_max: 最大规则数。
        :type rule_max: int
        :param sess_max: 最大连接数。
        :type sess_max: int
        :param bps_max: 最大bps。
        :type bps_max: int
        :param pps_max: 最大pps。
        :type pps_max: int
        :param qps_max: 最大qps。
        :type qps_max: int
        """
        
        

        self._name = None
        self._code = None
        self._cbc_code = None
        self._rule_max = None
        self._sess_max = None
        self._bps_max = None
        self._pps_max = None
        self._qps_max = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if cbc_code is not None:
            self.cbc_code = cbc_code
        if rule_max is not None:
            self.rule_max = rule_max
        if sess_max is not None:
            self.sess_max = sess_max
        if bps_max is not None:
            self.bps_max = bps_max
        if pps_max is not None:
            self.pps_max = pps_max
        if qps_max is not None:
            self.qps_max = qps_max

    @property
    def name(self):
        r"""Gets the name of this Spec.

        规格名称。

        :return: The name of this Spec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Spec.

        规格名称。

        :param name: The name of this Spec.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        r"""Gets the code of this Spec.

        规格编号。

        :return: The code of this Spec.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this Spec.

        规格编号。

        :param code: The code of this Spec.
        :type code: str
        """
        self._code = code

    @property
    def cbc_code(self):
        r"""Gets the cbc_code of this Spec.

        规格cbc编码。

        :return: The cbc_code of this Spec.
        :rtype: str
        """
        return self._cbc_code

    @cbc_code.setter
    def cbc_code(self, cbc_code):
        r"""Sets the cbc_code of this Spec.

        规格cbc编码。

        :param cbc_code: The cbc_code of this Spec.
        :type cbc_code: str
        """
        self._cbc_code = cbc_code

    @property
    def rule_max(self):
        r"""Gets the rule_max of this Spec.

        最大规则数。

        :return: The rule_max of this Spec.
        :rtype: int
        """
        return self._rule_max

    @rule_max.setter
    def rule_max(self, rule_max):
        r"""Sets the rule_max of this Spec.

        最大规则数。

        :param rule_max: The rule_max of this Spec.
        :type rule_max: int
        """
        self._rule_max = rule_max

    @property
    def sess_max(self):
        r"""Gets the sess_max of this Spec.

        最大连接数。

        :return: The sess_max of this Spec.
        :rtype: int
        """
        return self._sess_max

    @sess_max.setter
    def sess_max(self, sess_max):
        r"""Sets the sess_max of this Spec.

        最大连接数。

        :param sess_max: The sess_max of this Spec.
        :type sess_max: int
        """
        self._sess_max = sess_max

    @property
    def bps_max(self):
        r"""Gets the bps_max of this Spec.

        最大bps。

        :return: The bps_max of this Spec.
        :rtype: int
        """
        return self._bps_max

    @bps_max.setter
    def bps_max(self, bps_max):
        r"""Sets the bps_max of this Spec.

        最大bps。

        :param bps_max: The bps_max of this Spec.
        :type bps_max: int
        """
        self._bps_max = bps_max

    @property
    def pps_max(self):
        r"""Gets the pps_max of this Spec.

        最大pps。

        :return: The pps_max of this Spec.
        :rtype: int
        """
        return self._pps_max

    @pps_max.setter
    def pps_max(self, pps_max):
        r"""Sets the pps_max of this Spec.

        最大pps。

        :param pps_max: The pps_max of this Spec.
        :type pps_max: int
        """
        self._pps_max = pps_max

    @property
    def qps_max(self):
        r"""Gets the qps_max of this Spec.

        最大qps。

        :return: The qps_max of this Spec.
        :rtype: int
        """
        return self._qps_max

    @qps_max.setter
    def qps_max(self, qps_max):
        r"""Sets the qps_max of this Spec.

        最大qps。

        :param qps_max: The qps_max of this Spec.
        :type qps_max: int
        """
        self._qps_max = qps_max

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
        if not isinstance(other, Spec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
