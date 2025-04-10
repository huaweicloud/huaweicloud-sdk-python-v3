# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CapRef:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cap_id': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'cap_id': 'cap_id',
        'version_id': 'version_id'
    }

    def __init__(self, cap_id=None, version_id=None):
        r"""CapRef

        The model defined in huaweicloud sdk

        :param cap_id: CapId，32~36位的英文、数字、短横组合
        :type cap_id: str
        :param version_id: CapVersionId，32~36位的英文、数字、短横组合
        :type version_id: str
        """
        
        

        self._cap_id = None
        self._version_id = None
        self.discriminator = None

        if cap_id is not None:
            self.cap_id = cap_id
        if version_id is not None:
            self.version_id = version_id

    @property
    def cap_id(self):
        r"""Gets the cap_id of this CapRef.

        CapId，32~36位的英文、数字、短横组合

        :return: The cap_id of this CapRef.
        :rtype: str
        """
        return self._cap_id

    @cap_id.setter
    def cap_id(self, cap_id):
        r"""Sets the cap_id of this CapRef.

        CapId，32~36位的英文、数字、短横组合

        :param cap_id: The cap_id of this CapRef.
        :type cap_id: str
        """
        self._cap_id = cap_id

    @property
    def version_id(self):
        r"""Gets the version_id of this CapRef.

        CapVersionId，32~36位的英文、数字、短横组合

        :return: The version_id of this CapRef.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this CapRef.

        CapVersionId，32~36位的英文、数字、短横组合

        :param version_id: The version_id of this CapRef.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, CapRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
