# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimPoolMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sim_pool_id': 'int',
        'cid': 'str',
        'limit': 'int',
        'offset': 'int',
        'billing_cycle': 'str'
    }

    attribute_map = {
        'sim_pool_id': 'sim_pool_id',
        'cid': 'cid',
        'limit': 'limit',
        'offset': 'offset',
        'billing_cycle': 'billing_cycle'
    }

    def __init__(self, sim_pool_id=None, cid=None, limit=None, offset=None, billing_cycle=None):
        """ListSimPoolMembersRequest

        The model defined in huaweicloud sdk

        :param sim_pool_id: 流量池标识
        :type sim_pool_id: int
        :param cid: 容器ID
        :type cid: str
        :param limit: 每页记录数
        :type limit: int
        :param offset: 页码
        :type offset: int
        :param billing_cycle: 账期，例如：2021-04
        :type billing_cycle: str
        """
        
        

        self._sim_pool_id = None
        self._cid = None
        self._limit = None
        self._offset = None
        self._billing_cycle = None
        self.discriminator = None

        self.sim_pool_id = sim_pool_id
        if cid is not None:
            self.cid = cid
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.billing_cycle = billing_cycle

    @property
    def sim_pool_id(self):
        """Gets the sim_pool_id of this ListSimPoolMembersRequest.

        流量池标识

        :return: The sim_pool_id of this ListSimPoolMembersRequest.
        :rtype: int
        """
        return self._sim_pool_id

    @sim_pool_id.setter
    def sim_pool_id(self, sim_pool_id):
        """Sets the sim_pool_id of this ListSimPoolMembersRequest.

        流量池标识

        :param sim_pool_id: The sim_pool_id of this ListSimPoolMembersRequest.
        :type sim_pool_id: int
        """
        self._sim_pool_id = sim_pool_id

    @property
    def cid(self):
        """Gets the cid of this ListSimPoolMembersRequest.

        容器ID

        :return: The cid of this ListSimPoolMembersRequest.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this ListSimPoolMembersRequest.

        容器ID

        :param cid: The cid of this ListSimPoolMembersRequest.
        :type cid: str
        """
        self._cid = cid

    @property
    def limit(self):
        """Gets the limit of this ListSimPoolMembersRequest.

        每页记录数

        :return: The limit of this ListSimPoolMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSimPoolMembersRequest.

        每页记录数

        :param limit: The limit of this ListSimPoolMembersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSimPoolMembersRequest.

        页码

        :return: The offset of this ListSimPoolMembersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSimPoolMembersRequest.

        页码

        :param offset: The offset of this ListSimPoolMembersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def billing_cycle(self):
        """Gets the billing_cycle of this ListSimPoolMembersRequest.

        账期，例如：2021-04

        :return: The billing_cycle of this ListSimPoolMembersRequest.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this ListSimPoolMembersRequest.

        账期，例如：2021-04

        :param billing_cycle: The billing_cycle of this ListSimPoolMembersRequest.
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
        if not isinstance(other, ListSimPoolMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
