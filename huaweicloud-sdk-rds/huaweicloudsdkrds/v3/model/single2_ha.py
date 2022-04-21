# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Single2Ha:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'single_to_ha': 'Single2HaObject'
    }

    attribute_map = {
        'single_to_ha': 'single_to_ha'
    }

    def __init__(self, single_to_ha=None):
        """Single2Ha

        The model defined in huaweicloud sdk

        :param single_to_ha: 
        :type single_to_ha: :class:`huaweicloudsdkrds.v3.Single2HaObject`
        """
        
        

        self._single_to_ha = None
        self.discriminator = None

        self.single_to_ha = single_to_ha

    @property
    def single_to_ha(self):
        """Gets the single_to_ha of this Single2Ha.


        :return: The single_to_ha of this Single2Ha.
        :rtype: :class:`huaweicloudsdkrds.v3.Single2HaObject`
        """
        return self._single_to_ha

    @single_to_ha.setter
    def single_to_ha(self, single_to_ha):
        """Sets the single_to_ha of this Single2Ha.


        :param single_to_ha: The single_to_ha of this Single2Ha.
        :type single_to_ha: :class:`huaweicloudsdkrds.v3.Single2HaObject`
        """
        self._single_to_ha = single_to_ha

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
        if not isinstance(other, Single2Ha):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
