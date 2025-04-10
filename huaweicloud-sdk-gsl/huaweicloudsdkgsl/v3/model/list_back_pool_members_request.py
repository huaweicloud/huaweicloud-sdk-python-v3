# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackPoolMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'back_pool_id': 'int',
        'cid': 'str',
        'limit': 'int',
        'offset': 'int',
        'billing_cycle': 'str'
    }

    attribute_map = {
        'back_pool_id': 'back_pool_id',
        'cid': 'cid',
        'limit': 'limit',
        'offset': 'offset',
        'billing_cycle': 'billing_cycle'
    }

    def __init__(self, back_pool_id=None, cid=None, limit=None, offset=None, billing_cycle=None):
        r"""ListBackPoolMembersRequest

        The model defined in huaweicloud sdk

        :param back_pool_id: 流量池标识
        :type back_pool_id: int
        :param cid: 容器ID
        :type cid: str
        :param limit: 每页记录数
        :type limit: int
        :param offset: 页码
        :type offset: int
        :param billing_cycle: 账期，例如：2021-04
        :type billing_cycle: str
        """
        
        

        self._back_pool_id = None
        self._cid = None
        self._limit = None
        self._offset = None
        self._billing_cycle = None
        self.discriminator = None

        self.back_pool_id = back_pool_id
        if cid is not None:
            self.cid = cid
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.billing_cycle = billing_cycle

    @property
    def back_pool_id(self):
        r"""Gets the back_pool_id of this ListBackPoolMembersRequest.

        流量池标识

        :return: The back_pool_id of this ListBackPoolMembersRequest.
        :rtype: int
        """
        return self._back_pool_id

    @back_pool_id.setter
    def back_pool_id(self, back_pool_id):
        r"""Sets the back_pool_id of this ListBackPoolMembersRequest.

        流量池标识

        :param back_pool_id: The back_pool_id of this ListBackPoolMembersRequest.
        :type back_pool_id: int
        """
        self._back_pool_id = back_pool_id

    @property
    def cid(self):
        r"""Gets the cid of this ListBackPoolMembersRequest.

        容器ID

        :return: The cid of this ListBackPoolMembersRequest.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        r"""Sets the cid of this ListBackPoolMembersRequest.

        容器ID

        :param cid: The cid of this ListBackPoolMembersRequest.
        :type cid: str
        """
        self._cid = cid

    @property
    def limit(self):
        r"""Gets the limit of this ListBackPoolMembersRequest.

        每页记录数

        :return: The limit of this ListBackPoolMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBackPoolMembersRequest.

        每页记录数

        :param limit: The limit of this ListBackPoolMembersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListBackPoolMembersRequest.

        页码

        :return: The offset of this ListBackPoolMembersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBackPoolMembersRequest.

        页码

        :param offset: The offset of this ListBackPoolMembersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def billing_cycle(self):
        r"""Gets the billing_cycle of this ListBackPoolMembersRequest.

        账期，例如：2021-04

        :return: The billing_cycle of this ListBackPoolMembersRequest.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        r"""Sets the billing_cycle of this ListBackPoolMembersRequest.

        账期，例如：2021-04

        :param billing_cycle: The billing_cycle of this ListBackPoolMembersRequest.
        :type billing_cycle: str
        """
        self._billing_cycle = billing_cycle

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
        if not isinstance(other, ListBackPoolMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
