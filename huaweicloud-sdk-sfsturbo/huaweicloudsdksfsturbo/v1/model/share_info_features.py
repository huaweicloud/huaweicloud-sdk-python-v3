# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareInfoFeatures:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup': 'ShareInfoFeature'
    }

    attribute_map = {
        'backup': 'backup'
    }

    def __init__(self, backup=None):
        r"""ShareInfoFeatures

        The model defined in huaweicloud sdk

        :param backup: 
        :type backup: :class:`huaweicloudsdksfsturbo.v1.ShareInfoFeature`
        """
        
        

        self._backup = None
        self.discriminator = None

        if backup is not None:
            self.backup = backup

    @property
    def backup(self):
        r"""Gets the backup of this ShareInfoFeatures.

        :return: The backup of this ShareInfoFeatures.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShareInfoFeature`
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        r"""Sets the backup of this ShareInfoFeatures.

        :param backup: The backup of this ShareInfoFeatures.
        :type backup: :class:`huaweicloudsdksfsturbo.v1.ShareInfoFeature`
        """
        self._backup = backup

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
        if not isinstance(other, ShareInfoFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
