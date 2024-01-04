# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMrsFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_name': 'str'
    }

    attribute_map = {
        'version_name': 'version_name'
    }

    def __init__(self, version_name=None):
        """ShowMrsFlavorsRequest

        The model defined in huaweicloud sdk

        :param version_name: MRS集群版本，不支持多版本查询 ，例如 MRS%203.1.5.1
        :type version_name: str
        """
        
        

        self._version_name = None
        self.discriminator = None

        self.version_name = version_name

    @property
    def version_name(self):
        """Gets the version_name of this ShowMrsFlavorsRequest.

        MRS集群版本，不支持多版本查询 ，例如 MRS%203.1.5.1

        :return: The version_name of this ShowMrsFlavorsRequest.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this ShowMrsFlavorsRequest.

        MRS集群版本，不支持多版本查询 ，例如 MRS%203.1.5.1

        :param version_name: The version_name of this ShowMrsFlavorsRequest.
        :type version_name: str
        """
        self._version_name = version_name

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
        if not isinstance(other, ShowMrsFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
