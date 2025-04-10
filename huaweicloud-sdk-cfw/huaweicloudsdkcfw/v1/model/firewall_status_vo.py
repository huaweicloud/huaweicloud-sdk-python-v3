# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallStatusVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'available_eip_count': 'int',
        'beyond_max_count': 'bool',
        'eip_protected_self': 'int',
        'eip_total': 'int',
        'eip_un_protected': 'int',
        'object_id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'available_eip_count': 'available_eip_count',
        'beyond_max_count': 'beyond_max_count',
        'eip_protected_self': 'eip_protected_self',
        'eip_total': 'eip_total',
        'eip_un_protected': 'eip_un_protected',
        'object_id': 'object_id',
        'status': 'status'
    }

    def __init__(self, available_eip_count=None, beyond_max_count=None, eip_protected_self=None, eip_total=None, eip_un_protected=None, object_id=None, status=None):
        r"""FirewallStatusVO

        The model defined in huaweicloud sdk

        :param available_eip_count: 可防护eip数量
        :type available_eip_count: int
        :param beyond_max_count: 是否超出eip数量限制
        :type beyond_max_count: bool
        :param eip_protected_self: 已防护eip数量
        :type eip_protected_self: int
        :param eip_total: eip总数
        :type eip_total: int
        :param eip_un_protected: 未防护eip数量
        :type eip_un_protected: int
        :param object_id: 防护对象id
        :type object_id: str
        :param status: 是否开启新增eip自动防护，1；是，0：否
        :type status: int
        """
        
        

        self._available_eip_count = None
        self._beyond_max_count = None
        self._eip_protected_self = None
        self._eip_total = None
        self._eip_un_protected = None
        self._object_id = None
        self._status = None
        self.discriminator = None

        if available_eip_count is not None:
            self.available_eip_count = available_eip_count
        if beyond_max_count is not None:
            self.beyond_max_count = beyond_max_count
        if eip_protected_self is not None:
            self.eip_protected_self = eip_protected_self
        if eip_total is not None:
            self.eip_total = eip_total
        if eip_un_protected is not None:
            self.eip_un_protected = eip_un_protected
        if object_id is not None:
            self.object_id = object_id
        if status is not None:
            self.status = status

    @property
    def available_eip_count(self):
        r"""Gets the available_eip_count of this FirewallStatusVO.

        可防护eip数量

        :return: The available_eip_count of this FirewallStatusVO.
        :rtype: int
        """
        return self._available_eip_count

    @available_eip_count.setter
    def available_eip_count(self, available_eip_count):
        r"""Sets the available_eip_count of this FirewallStatusVO.

        可防护eip数量

        :param available_eip_count: The available_eip_count of this FirewallStatusVO.
        :type available_eip_count: int
        """
        self._available_eip_count = available_eip_count

    @property
    def beyond_max_count(self):
        r"""Gets the beyond_max_count of this FirewallStatusVO.

        是否超出eip数量限制

        :return: The beyond_max_count of this FirewallStatusVO.
        :rtype: bool
        """
        return self._beyond_max_count

    @beyond_max_count.setter
    def beyond_max_count(self, beyond_max_count):
        r"""Sets the beyond_max_count of this FirewallStatusVO.

        是否超出eip数量限制

        :param beyond_max_count: The beyond_max_count of this FirewallStatusVO.
        :type beyond_max_count: bool
        """
        self._beyond_max_count = beyond_max_count

    @property
    def eip_protected_self(self):
        r"""Gets the eip_protected_self of this FirewallStatusVO.

        已防护eip数量

        :return: The eip_protected_self of this FirewallStatusVO.
        :rtype: int
        """
        return self._eip_protected_self

    @eip_protected_self.setter
    def eip_protected_self(self, eip_protected_self):
        r"""Sets the eip_protected_self of this FirewallStatusVO.

        已防护eip数量

        :param eip_protected_self: The eip_protected_self of this FirewallStatusVO.
        :type eip_protected_self: int
        """
        self._eip_protected_self = eip_protected_self

    @property
    def eip_total(self):
        r"""Gets the eip_total of this FirewallStatusVO.

        eip总数

        :return: The eip_total of this FirewallStatusVO.
        :rtype: int
        """
        return self._eip_total

    @eip_total.setter
    def eip_total(self, eip_total):
        r"""Sets the eip_total of this FirewallStatusVO.

        eip总数

        :param eip_total: The eip_total of this FirewallStatusVO.
        :type eip_total: int
        """
        self._eip_total = eip_total

    @property
    def eip_un_protected(self):
        r"""Gets the eip_un_protected of this FirewallStatusVO.

        未防护eip数量

        :return: The eip_un_protected of this FirewallStatusVO.
        :rtype: int
        """
        return self._eip_un_protected

    @eip_un_protected.setter
    def eip_un_protected(self, eip_un_protected):
        r"""Sets the eip_un_protected of this FirewallStatusVO.

        未防护eip数量

        :param eip_un_protected: The eip_un_protected of this FirewallStatusVO.
        :type eip_un_protected: int
        """
        self._eip_un_protected = eip_un_protected

    @property
    def object_id(self):
        r"""Gets the object_id of this FirewallStatusVO.

        防护对象id

        :return: The object_id of this FirewallStatusVO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this FirewallStatusVO.

        防护对象id

        :param object_id: The object_id of this FirewallStatusVO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def status(self):
        r"""Gets the status of this FirewallStatusVO.

        是否开启新增eip自动防护，1；是，0：否

        :return: The status of this FirewallStatusVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FirewallStatusVO.

        是否开启新增eip自动防护，1；是，0：否

        :param status: The status of this FirewallStatusVO.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, FirewallStatusVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
