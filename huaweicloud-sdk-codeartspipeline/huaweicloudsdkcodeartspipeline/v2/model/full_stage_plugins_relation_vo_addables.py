# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullStagePluginsRelationVOAddables:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'additional_prop1': 'bool',
        'additional_prop2': 'bool',
        'additional_prop3': 'bool'
    }

    attribute_map = {
        'additional_prop1': 'additionalProp1',
        'additional_prop2': 'additionalProp2',
        'additional_prop3': 'additionalProp3'
    }

    def __init__(self, additional_prop1=None, additional_prop2=None, additional_prop3=None):
        """FullStagePluginsRelationVOAddables

        The model defined in huaweicloud sdk

        :param additional_prop1: 额外属性1
        :type additional_prop1: bool
        :param additional_prop2: 额外属性2
        :type additional_prop2: bool
        :param additional_prop3: 额外属性3
        :type additional_prop3: bool
        """
        
        

        self._additional_prop1 = None
        self._additional_prop2 = None
        self._additional_prop3 = None
        self.discriminator = None

        if additional_prop1 is not None:
            self.additional_prop1 = additional_prop1
        if additional_prop2 is not None:
            self.additional_prop2 = additional_prop2
        if additional_prop3 is not None:
            self.additional_prop3 = additional_prop3

    @property
    def additional_prop1(self):
        """Gets the additional_prop1 of this FullStagePluginsRelationVOAddables.

        额外属性1

        :return: The additional_prop1 of this FullStagePluginsRelationVOAddables.
        :rtype: bool
        """
        return self._additional_prop1

    @additional_prop1.setter
    def additional_prop1(self, additional_prop1):
        """Sets the additional_prop1 of this FullStagePluginsRelationVOAddables.

        额外属性1

        :param additional_prop1: The additional_prop1 of this FullStagePluginsRelationVOAddables.
        :type additional_prop1: bool
        """
        self._additional_prop1 = additional_prop1

    @property
    def additional_prop2(self):
        """Gets the additional_prop2 of this FullStagePluginsRelationVOAddables.

        额外属性2

        :return: The additional_prop2 of this FullStagePluginsRelationVOAddables.
        :rtype: bool
        """
        return self._additional_prop2

    @additional_prop2.setter
    def additional_prop2(self, additional_prop2):
        """Sets the additional_prop2 of this FullStagePluginsRelationVOAddables.

        额外属性2

        :param additional_prop2: The additional_prop2 of this FullStagePluginsRelationVOAddables.
        :type additional_prop2: bool
        """
        self._additional_prop2 = additional_prop2

    @property
    def additional_prop3(self):
        """Gets the additional_prop3 of this FullStagePluginsRelationVOAddables.

        额外属性3

        :return: The additional_prop3 of this FullStagePluginsRelationVOAddables.
        :rtype: bool
        """
        return self._additional_prop3

    @additional_prop3.setter
    def additional_prop3(self, additional_prop3):
        """Sets the additional_prop3 of this FullStagePluginsRelationVOAddables.

        额外属性3

        :param additional_prop3: The additional_prop3 of this FullStagePluginsRelationVOAddables.
        :type additional_prop3: bool
        """
        self._additional_prop3 = additional_prop3

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
        if not isinstance(other, FullStagePluginsRelationVOAddables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
