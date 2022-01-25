# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEngineSupportFeaturesEntity:


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
        'properties': 'ListEngineSupportFeaturesPropertiesEntity'
    }

    attribute_map = {
        'name': 'name',
        'properties': 'properties'
    }

    def __init__(self, name=None, properties=None):
        """ListEngineSupportFeaturesEntity - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._properties = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties

    @property
    def name(self):
        """Gets the name of this ListEngineSupportFeaturesEntity.

        功能名称。

        :return: The name of this ListEngineSupportFeaturesEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEngineSupportFeaturesEntity.

        功能名称。

        :param name: The name of this ListEngineSupportFeaturesEntity.
        :type: str
        """
        self._name = name

    @property
    def properties(self):
        """Gets the properties of this ListEngineSupportFeaturesEntity.


        :return: The properties of this ListEngineSupportFeaturesEntity.
        :rtype: ListEngineSupportFeaturesPropertiesEntity
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ListEngineSupportFeaturesEntity.


        :param properties: The properties of this ListEngineSupportFeaturesEntity.
        :type: ListEngineSupportFeaturesPropertiesEntity
        """
        self._properties = properties

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
        if not isinstance(other, ListEngineSupportFeaturesEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
