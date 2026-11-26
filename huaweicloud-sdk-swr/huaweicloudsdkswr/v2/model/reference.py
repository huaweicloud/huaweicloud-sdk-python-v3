# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Reference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_id': 'int',
        'child_id': 'int',
        'child_digest': 'str',
        'platform': 'Platform'
    }

    attribute_map = {
        'parent_id': 'parent_id',
        'child_id': 'child_id',
        'child_digest': 'child_digest',
        'platform': 'platform'
    }

    def __init__(self, parent_id=None, child_id=None, child_digest=None, platform=None):
        r"""Reference

        The model defined in huaweicloud sdk

        :param parent_id: 父制品的ID。
        :type parent_id: int
        :param child_id: 子制品的ID。
        :type child_id: int
        :param child_digest: 子制品的digest。
        :type child_digest: str
        :param platform: 
        :type platform: :class:`huaweicloudsdkswr.v2.Platform`
        """
        
        

        self._parent_id = None
        self._child_id = None
        self._child_digest = None
        self._platform = None
        self.discriminator = None

        if parent_id is not None:
            self.parent_id = parent_id
        if child_id is not None:
            self.child_id = child_id
        if child_digest is not None:
            self.child_digest = child_digest
        if platform is not None:
            self.platform = platform

    @property
    def parent_id(self):
        r"""Gets the parent_id of this Reference.

        父制品的ID。

        :return: The parent_id of this Reference.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this Reference.

        父制品的ID。

        :param parent_id: The parent_id of this Reference.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def child_id(self):
        r"""Gets the child_id of this Reference.

        子制品的ID。

        :return: The child_id of this Reference.
        :rtype: int
        """
        return self._child_id

    @child_id.setter
    def child_id(self, child_id):
        r"""Sets the child_id of this Reference.

        子制品的ID。

        :param child_id: The child_id of this Reference.
        :type child_id: int
        """
        self._child_id = child_id

    @property
    def child_digest(self):
        r"""Gets the child_digest of this Reference.

        子制品的digest。

        :return: The child_digest of this Reference.
        :rtype: str
        """
        return self._child_digest

    @child_digest.setter
    def child_digest(self, child_digest):
        r"""Sets the child_digest of this Reference.

        子制品的digest。

        :param child_digest: The child_digest of this Reference.
        :type child_digest: str
        """
        self._child_digest = child_digest

    @property
    def platform(self):
        r"""Gets the platform of this Reference.

        :return: The platform of this Reference.
        :rtype: :class:`huaweicloudsdkswr.v2.Platform`
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this Reference.

        :param platform: The platform of this Reference.
        :type platform: :class:`huaweicloudsdkswr.v2.Platform`
        """
        self._platform = platform

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Reference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
