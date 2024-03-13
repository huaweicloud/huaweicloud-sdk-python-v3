# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'str',
        'guid': 'str'
    }

    attribute_map = {
        'instance': 'instance',
        'guid': 'guid'
    }

    def __init__(self, instance=None, guid=None):
        """ShowNodesRequest

        The model defined in huaweicloud sdk

        :param instance: 实例id
        :type instance: str
        :param guid: 资产guid
        :type guid: str
        """
        
        

        self._instance = None
        self._guid = None
        self.discriminator = None

        self.instance = instance
        self.guid = guid

    @property
    def instance(self):
        """Gets the instance of this ShowNodesRequest.

        实例id

        :return: The instance of this ShowNodesRequest.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ShowNodesRequest.

        实例id

        :param instance: The instance of this ShowNodesRequest.
        :type instance: str
        """
        self._instance = instance

    @property
    def guid(self):
        """Gets the guid of this ShowNodesRequest.

        资产guid

        :return: The guid of this ShowNodesRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this ShowNodesRequest.

        资产guid

        :param guid: The guid of this ShowNodesRequest.
        :type guid: str
        """
        self._guid = guid

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
        if not isinstance(other, ShowNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
