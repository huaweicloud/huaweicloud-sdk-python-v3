# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchConfigScenarioSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_ids': 'list[int]',
        'generalization_ids': 'list[int]',
        'suit_ids': 'list[int]'
    }

    attribute_map = {
        'group_ids': 'group_ids',
        'generalization_ids': 'generalization_ids',
        'suit_ids': 'suit_ids'
    }

    def __init__(self, group_ids=None, generalization_ids=None, suit_ids=None):
        r"""BatchConfigScenarioSrlz

        The model defined in huaweicloud sdk

        :param group_ids: 场景库id信息
        :type group_ids: list[int]
        :param generalization_ids: 泛化任务id信息
        :type generalization_ids: list[int]
        :param suit_ids: 测试套件id信息
        :type suit_ids: list[int]
        """
        
        

        self._group_ids = None
        self._generalization_ids = None
        self._suit_ids = None
        self.discriminator = None

        if group_ids is not None:
            self.group_ids = group_ids
        if generalization_ids is not None:
            self.generalization_ids = generalization_ids
        if suit_ids is not None:
            self.suit_ids = suit_ids

    @property
    def group_ids(self):
        r"""Gets the group_ids of this BatchConfigScenarioSrlz.

        场景库id信息

        :return: The group_ids of this BatchConfigScenarioSrlz.
        :rtype: list[int]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        r"""Sets the group_ids of this BatchConfigScenarioSrlz.

        场景库id信息

        :param group_ids: The group_ids of this BatchConfigScenarioSrlz.
        :type group_ids: list[int]
        """
        self._group_ids = group_ids

    @property
    def generalization_ids(self):
        r"""Gets the generalization_ids of this BatchConfigScenarioSrlz.

        泛化任务id信息

        :return: The generalization_ids of this BatchConfigScenarioSrlz.
        :rtype: list[int]
        """
        return self._generalization_ids

    @generalization_ids.setter
    def generalization_ids(self, generalization_ids):
        r"""Sets the generalization_ids of this BatchConfigScenarioSrlz.

        泛化任务id信息

        :param generalization_ids: The generalization_ids of this BatchConfigScenarioSrlz.
        :type generalization_ids: list[int]
        """
        self._generalization_ids = generalization_ids

    @property
    def suit_ids(self):
        r"""Gets the suit_ids of this BatchConfigScenarioSrlz.

        测试套件id信息

        :return: The suit_ids of this BatchConfigScenarioSrlz.
        :rtype: list[int]
        """
        return self._suit_ids

    @suit_ids.setter
    def suit_ids(self, suit_ids):
        r"""Sets the suit_ids of this BatchConfigScenarioSrlz.

        测试套件id信息

        :param suit_ids: The suit_ids of this BatchConfigScenarioSrlz.
        :type suit_ids: list[int]
        """
        self._suit_ids = suit_ids

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
        if not isinstance(other, BatchConfigScenarioSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
