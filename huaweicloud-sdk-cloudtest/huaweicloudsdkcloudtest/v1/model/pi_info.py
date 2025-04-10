# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PiInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sprints': 'list[str]',
        'pi_id': 'str'
    }

    attribute_map = {
        'sprints': 'sprints',
        'pi_id': 'pi_id'
    }

    def __init__(self, sprints=None, pi_id=None):
        r"""PiInfo

        The model defined in huaweicloud sdk

        :param sprints: 迭代列表
        :type sprints: list[str]
        :param pi_id: pi的id，层级关系：pi -&gt; 迭代 -&gt; 需求
        :type pi_id: str
        """
        
        

        self._sprints = None
        self._pi_id = None
        self.discriminator = None

        if sprints is not None:
            self.sprints = sprints
        if pi_id is not None:
            self.pi_id = pi_id

    @property
    def sprints(self):
        r"""Gets the sprints of this PiInfo.

        迭代列表

        :return: The sprints of this PiInfo.
        :rtype: list[str]
        """
        return self._sprints

    @sprints.setter
    def sprints(self, sprints):
        r"""Sets the sprints of this PiInfo.

        迭代列表

        :param sprints: The sprints of this PiInfo.
        :type sprints: list[str]
        """
        self._sprints = sprints

    @property
    def pi_id(self):
        r"""Gets the pi_id of this PiInfo.

        pi的id，层级关系：pi -> 迭代 -> 需求

        :return: The pi_id of this PiInfo.
        :rtype: str
        """
        return self._pi_id

    @pi_id.setter
    def pi_id(self, pi_id):
        r"""Sets the pi_id of this PiInfo.

        pi的id，层级关系：pi -> 迭代 -> 需求

        :param pi_id: The pi_id of this PiInfo.
        :type pi_id: str
        """
        self._pi_id = pi_id

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
        if not isinstance(other, PiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
