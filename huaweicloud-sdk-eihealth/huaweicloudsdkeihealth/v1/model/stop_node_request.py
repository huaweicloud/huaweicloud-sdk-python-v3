# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopNodeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'force': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'force': 'force'
    }

    def __init__(self, id=None, force=None):
        """StopNodeRequest

        The model defined in huaweicloud sdk

        :param id: 计算资源id
        :type id: str
        :param force: 是否强制关闭，默认为false
        :type force: bool
        """
        
        

        self._id = None
        self._force = None
        self.discriminator = None

        self.id = id
        if force is not None:
            self.force = force

    @property
    def id(self):
        """Gets the id of this StopNodeRequest.

        计算资源id

        :return: The id of this StopNodeRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StopNodeRequest.

        计算资源id

        :param id: The id of this StopNodeRequest.
        :type id: str
        """
        self._id = id

    @property
    def force(self):
        """Gets the force of this StopNodeRequest.

        是否强制关闭，默认为false

        :return: The force of this StopNodeRequest.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this StopNodeRequest.

        是否强制关闭，默认为false

        :param force: The force of this StopNodeRequest.
        :type force: bool
        """
        self._force = force

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
        if not isinstance(other, StopNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
