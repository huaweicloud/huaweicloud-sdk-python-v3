# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConclusionItem:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'params': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'params': 'params'
    }

    def __init__(self, id=None, params=None):
        """ConclusionItem - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._params = None
        self.discriminator = None

        self.id = id
        if params is not None:
            self.params = params

    @property
    def id(self):
        """Gets the id of this ConclusionItem.

        结论id

        :return: The id of this ConclusionItem.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConclusionItem.

        结论id

        :param id: The id of this ConclusionItem.
        :type: int
        """
        self._id = id

    @property
    def params(self):
        """Gets the params of this ConclusionItem.

        结论参数

        :return: The params of this ConclusionItem.
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ConclusionItem.

        结论参数

        :param params: The params of this ConclusionItem.
        :type: dict(str, str)
        """
        self._params = params

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConclusionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other