# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteComputingResourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'computing_resource_id': 'str'
    }

    attribute_map = {
        'computing_resource_id': 'computing_resource_id'
    }

    def __init__(self, computing_resource_id=None):
        """DeleteComputingResourceRequest

        The model defined in huaweicloud sdk

        :param computing_resource_id: 计算资源ID。
        :type computing_resource_id: str
        """
        
        

        self._computing_resource_id = None
        self.discriminator = None

        self.computing_resource_id = computing_resource_id

    @property
    def computing_resource_id(self):
        """Gets the computing_resource_id of this DeleteComputingResourceRequest.

        计算资源ID。

        :return: The computing_resource_id of this DeleteComputingResourceRequest.
        :rtype: str
        """
        return self._computing_resource_id

    @computing_resource_id.setter
    def computing_resource_id(self, computing_resource_id):
        """Sets the computing_resource_id of this DeleteComputingResourceRequest.

        计算资源ID。

        :param computing_resource_id: The computing_resource_id of this DeleteComputingResourceRequest.
        :type computing_resource_id: str
        """
        self._computing_resource_id = computing_resource_id

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
        if not isinstance(other, DeleteComputingResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
