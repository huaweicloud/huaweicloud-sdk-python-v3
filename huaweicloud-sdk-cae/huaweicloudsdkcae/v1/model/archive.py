# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Archive:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'artifact_namespace': 'str'
    }

    attribute_map = {
        'artifact_namespace': 'artifact_namespace'
    }

    def __init__(self, artifact_namespace=None):
        """Archive

        The model defined in huaweicloud sdk

        :param artifact_namespace: 产物纳管SWR组织。
        :type artifact_namespace: str
        """
        
        

        self._artifact_namespace = None
        self.discriminator = None

        if artifact_namespace is not None:
            self.artifact_namespace = artifact_namespace

    @property
    def artifact_namespace(self):
        """Gets the artifact_namespace of this Archive.

        产物纳管SWR组织。

        :return: The artifact_namespace of this Archive.
        :rtype: str
        """
        return self._artifact_namespace

    @artifact_namespace.setter
    def artifact_namespace(self, artifact_namespace):
        """Sets the artifact_namespace of this Archive.

        产物纳管SWR组织。

        :param artifact_namespace: The artifact_namespace of this Archive.
        :type artifact_namespace: str
        """
        self._artifact_namespace = artifact_namespace

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
        if not isinstance(other, Archive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
