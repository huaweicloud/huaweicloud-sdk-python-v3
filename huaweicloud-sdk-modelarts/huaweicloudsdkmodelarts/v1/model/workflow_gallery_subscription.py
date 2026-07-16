# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowGallerySubscription:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_id': 'str',
        'version_id': 'str',
        'expired_at': 'str'
    }

    attribute_map = {
        'content_id': 'content_id',
        'version_id': 'version_id',
        'expired_at': 'expired_at'
    }

    def __init__(self, content_id=None, version_id=None, expired_at=None):
        r"""WorkflowGallerySubscription

        The model defined in huaweicloud sdk

        :param content_id: 资产ID。
        :type content_id: str
        :param version_id: 版本ID。
        :type version_id: str
        :param expired_at: 超期时间。
        :type expired_at: str
        """
        
        

        self._content_id = None
        self._version_id = None
        self._expired_at = None
        self.discriminator = None

        if content_id is not None:
            self.content_id = content_id
        if version_id is not None:
            self.version_id = version_id
        if expired_at is not None:
            self.expired_at = expired_at

    @property
    def content_id(self):
        r"""Gets the content_id of this WorkflowGallerySubscription.

        资产ID。

        :return: The content_id of this WorkflowGallerySubscription.
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        r"""Sets the content_id of this WorkflowGallerySubscription.

        资产ID。

        :param content_id: The content_id of this WorkflowGallerySubscription.
        :type content_id: str
        """
        self._content_id = content_id

    @property
    def version_id(self):
        r"""Gets the version_id of this WorkflowGallerySubscription.

        版本ID。

        :return: The version_id of this WorkflowGallerySubscription.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this WorkflowGallerySubscription.

        版本ID。

        :param version_id: The version_id of this WorkflowGallerySubscription.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def expired_at(self):
        r"""Gets the expired_at of this WorkflowGallerySubscription.

        超期时间。

        :return: The expired_at of this WorkflowGallerySubscription.
        :rtype: str
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        r"""Sets the expired_at of this WorkflowGallerySubscription.

        超期时间。

        :param expired_at: The expired_at of this WorkflowGallerySubscription.
        :type expired_at: str
        """
        self._expired_at = expired_at

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
        if not isinstance(other, WorkflowGallerySubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
