# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InviteAccountReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target': 'TargetDto',
        'notes': 'str',
        'tags': 'list[TagDto]'
    }

    attribute_map = {
        'target': 'target',
        'notes': 'notes',
        'tags': 'tags'
    }

    def __init__(self, target=None, notes=None, tags=None):
        """InviteAccountReqBody

        The model defined in huaweicloud sdk

        :param target: 
        :type target: :class:`huaweicloudsdkorganizations.v1.TargetDto`
        :param notes: 给收件帐号所有者的邮件中的附加信息。
        :type notes: str
        :param tags: 要绑定到新创建的帐号的标签列表。
        :type tags: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        
        

        self._target = None
        self._notes = None
        self._tags = None
        self.discriminator = None

        self.target = target
        self.notes = notes
        if tags is not None:
            self.tags = tags

    @property
    def target(self):
        """Gets the target of this InviteAccountReqBody.

        :return: The target of this InviteAccountReqBody.
        :rtype: :class:`huaweicloudsdkorganizations.v1.TargetDto`
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this InviteAccountReqBody.

        :param target: The target of this InviteAccountReqBody.
        :type target: :class:`huaweicloudsdkorganizations.v1.TargetDto`
        """
        self._target = target

    @property
    def notes(self):
        """Gets the notes of this InviteAccountReqBody.

        给收件帐号所有者的邮件中的附加信息。

        :return: The notes of this InviteAccountReqBody.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this InviteAccountReqBody.

        给收件帐号所有者的邮件中的附加信息。

        :param notes: The notes of this InviteAccountReqBody.
        :type notes: str
        """
        self._notes = notes

    @property
    def tags(self):
        """Gets the tags of this InviteAccountReqBody.

        要绑定到新创建的帐号的标签列表。

        :return: The tags of this InviteAccountReqBody.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InviteAccountReqBody.

        要绑定到新创建的帐号的标签列表。

        :param tags: The tags of this InviteAccountReqBody.
        :type tags: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        self._tags = tags

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
        if not isinstance(other, InviteAccountReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
