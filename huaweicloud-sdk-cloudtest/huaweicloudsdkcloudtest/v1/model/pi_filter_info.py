# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PiFilterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pi_sprints': 'list[PiInfo]',
        'all_pi': 'bool'
    }

    attribute_map = {
        'pi_sprints': 'pi_sprints',
        'all_pi': 'all_pi'
    }

    def __init__(self, pi_sprints=None, all_pi=None):
        """PiFilterInfo

        The model defined in huaweicloud sdk

        :param pi_sprints: pi迭代筛选条件
        :type pi_sprints: list[:class:`huaweicloudsdkcloudtest.v1.PiInfo`]
        :param all_pi: pi下拉框全选标识，全选时为true
        :type all_pi: bool
        """
        
        

        self._pi_sprints = None
        self._all_pi = None
        self.discriminator = None

        if pi_sprints is not None:
            self.pi_sprints = pi_sprints
        if all_pi is not None:
            self.all_pi = all_pi

    @property
    def pi_sprints(self):
        """Gets the pi_sprints of this PiFilterInfo.

        pi迭代筛选条件

        :return: The pi_sprints of this PiFilterInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.PiInfo`]
        """
        return self._pi_sprints

    @pi_sprints.setter
    def pi_sprints(self, pi_sprints):
        """Sets the pi_sprints of this PiFilterInfo.

        pi迭代筛选条件

        :param pi_sprints: The pi_sprints of this PiFilterInfo.
        :type pi_sprints: list[:class:`huaweicloudsdkcloudtest.v1.PiInfo`]
        """
        self._pi_sprints = pi_sprints

    @property
    def all_pi(self):
        """Gets the all_pi of this PiFilterInfo.

        pi下拉框全选标识，全选时为true

        :return: The all_pi of this PiFilterInfo.
        :rtype: bool
        """
        return self._all_pi

    @all_pi.setter
    def all_pi(self, all_pi):
        """Sets the all_pi of this PiFilterInfo.

        pi下拉框全选标识，全选时为true

        :param all_pi: The all_pi of this PiFilterInfo.
        :type all_pi: bool
        """
        self._all_pi = all_pi

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
        if not isinstance(other, PiFilterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
