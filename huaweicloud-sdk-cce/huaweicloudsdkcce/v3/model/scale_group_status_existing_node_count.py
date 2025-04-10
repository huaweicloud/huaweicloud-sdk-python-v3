# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleGroupStatusExistingNodeCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'post_paid': 'int',
        'pre_paid': 'int',
        'total': 'int'
    }

    attribute_map = {
        'post_paid': 'postPaid',
        'pre_paid': 'prePaid',
        'total': 'total'
    }

    def __init__(self, post_paid=None, pre_paid=None, total=None):
        r"""ScaleGroupStatusExistingNodeCount

        The model defined in huaweicloud sdk

        :param post_paid: 按需计费节点个数
        :type post_paid: int
        :param pre_paid: 包年包月节点个数
        :type pre_paid: int
        :param total: 按需计费和包年包月节点总数
        :type total: int
        """
        
        

        self._post_paid = None
        self._pre_paid = None
        self._total = None
        self.discriminator = None

        if post_paid is not None:
            self.post_paid = post_paid
        if pre_paid is not None:
            self.pre_paid = pre_paid
        if total is not None:
            self.total = total

    @property
    def post_paid(self):
        r"""Gets the post_paid of this ScaleGroupStatusExistingNodeCount.

        按需计费节点个数

        :return: The post_paid of this ScaleGroupStatusExistingNodeCount.
        :rtype: int
        """
        return self._post_paid

    @post_paid.setter
    def post_paid(self, post_paid):
        r"""Sets the post_paid of this ScaleGroupStatusExistingNodeCount.

        按需计费节点个数

        :param post_paid: The post_paid of this ScaleGroupStatusExistingNodeCount.
        :type post_paid: int
        """
        self._post_paid = post_paid

    @property
    def pre_paid(self):
        r"""Gets the pre_paid of this ScaleGroupStatusExistingNodeCount.

        包年包月节点个数

        :return: The pre_paid of this ScaleGroupStatusExistingNodeCount.
        :rtype: int
        """
        return self._pre_paid

    @pre_paid.setter
    def pre_paid(self, pre_paid):
        r"""Sets the pre_paid of this ScaleGroupStatusExistingNodeCount.

        包年包月节点个数

        :param pre_paid: The pre_paid of this ScaleGroupStatusExistingNodeCount.
        :type pre_paid: int
        """
        self._pre_paid = pre_paid

    @property
    def total(self):
        r"""Gets the total of this ScaleGroupStatusExistingNodeCount.

        按需计费和包年包月节点总数

        :return: The total of this ScaleGroupStatusExistingNodeCount.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ScaleGroupStatusExistingNodeCount.

        按需计费和包年包月节点总数

        :param total: The total of this ScaleGroupStatusExistingNodeCount.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ScaleGroupStatusExistingNodeCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
