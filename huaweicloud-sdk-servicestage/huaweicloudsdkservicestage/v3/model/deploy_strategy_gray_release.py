# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployStrategyGrayRelease:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'first_batch_weight': 'int',
        'first_batch_replica': 'int',
        'remaining_batch': 'int'
    }

    attribute_map = {
        'type': 'type',
        'first_batch_weight': 'first_batch_weight',
        'first_batch_replica': 'first_batch_replica',
        'remaining_batch': 'remaining_batch'
    }

    def __init__(self, type=None, first_batch_weight=None, first_batch_replica=None, remaining_batch=None):
        """DeployStrategyGrayRelease

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param first_batch_weight: only used for weight type
        :type first_batch_weight: int
        :param first_batch_replica: 
        :type first_batch_replica: int
        :param remaining_batch: 
        :type remaining_batch: int
        """
        
        

        self._type = None
        self._first_batch_weight = None
        self._first_batch_replica = None
        self._remaining_batch = None
        self.discriminator = None

        self.type = type
        self.first_batch_weight = first_batch_weight
        self.first_batch_replica = first_batch_replica
        self.remaining_batch = remaining_batch

    @property
    def type(self):
        """Gets the type of this DeployStrategyGrayRelease.

        :return: The type of this DeployStrategyGrayRelease.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeployStrategyGrayRelease.

        :param type: The type of this DeployStrategyGrayRelease.
        :type type: str
        """
        self._type = type

    @property
    def first_batch_weight(self):
        """Gets the first_batch_weight of this DeployStrategyGrayRelease.

        only used for weight type

        :return: The first_batch_weight of this DeployStrategyGrayRelease.
        :rtype: int
        """
        return self._first_batch_weight

    @first_batch_weight.setter
    def first_batch_weight(self, first_batch_weight):
        """Sets the first_batch_weight of this DeployStrategyGrayRelease.

        only used for weight type

        :param first_batch_weight: The first_batch_weight of this DeployStrategyGrayRelease.
        :type first_batch_weight: int
        """
        self._first_batch_weight = first_batch_weight

    @property
    def first_batch_replica(self):
        """Gets the first_batch_replica of this DeployStrategyGrayRelease.

        :return: The first_batch_replica of this DeployStrategyGrayRelease.
        :rtype: int
        """
        return self._first_batch_replica

    @first_batch_replica.setter
    def first_batch_replica(self, first_batch_replica):
        """Sets the first_batch_replica of this DeployStrategyGrayRelease.

        :param first_batch_replica: The first_batch_replica of this DeployStrategyGrayRelease.
        :type first_batch_replica: int
        """
        self._first_batch_replica = first_batch_replica

    @property
    def remaining_batch(self):
        """Gets the remaining_batch of this DeployStrategyGrayRelease.

        :return: The remaining_batch of this DeployStrategyGrayRelease.
        :rtype: int
        """
        return self._remaining_batch

    @remaining_batch.setter
    def remaining_batch(self, remaining_batch):
        """Sets the remaining_batch of this DeployStrategyGrayRelease.

        :param remaining_batch: The remaining_batch of this DeployStrategyGrayRelease.
        :type remaining_batch: int
        """
        self._remaining_batch = remaining_batch

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
        if not isinstance(other, DeployStrategyGrayRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
