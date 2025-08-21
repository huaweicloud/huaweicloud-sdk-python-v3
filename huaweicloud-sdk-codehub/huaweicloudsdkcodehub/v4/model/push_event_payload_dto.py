# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PushEventPayloadDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commit_count': 'int',
        'action': 'str',
        'ref_type': 'str',
        'commit_from': 'str',
        'commit_to': 'str',
        'ref': 'str',
        'commit_title': 'str'
    }

    attribute_map = {
        'commit_count': 'commit_count',
        'action': 'action',
        'ref_type': 'ref_type',
        'commit_from': 'commit_from',
        'commit_to': 'commit_to',
        'ref': 'ref',
        'commit_title': 'commit_title'
    }

    def __init__(self, commit_count=None, action=None, ref_type=None, commit_from=None, commit_to=None, ref=None, commit_title=None):
        r"""PushEventPayloadDto

        The model defined in huaweicloud sdk

        :param commit_count: **参数解释：** 提交数量。
        :type commit_count: int
        :param action: **参数解释：** 操作类型。
        :type action: str
        :param ref_type: **参数解释：** ref类型。
        :type ref_type: str
        :param commit_from: **参数解释：** 源Commit。
        :type commit_from: str
        :param commit_to: **参数解释：** 目标Commit。
        :type commit_to: str
        :param ref: **参数解释：** 分支。
        :type ref: str
        :param commit_title: **参数解释：** 提交标题。
        :type commit_title: str
        """
        
        

        self._commit_count = None
        self._action = None
        self._ref_type = None
        self._commit_from = None
        self._commit_to = None
        self._ref = None
        self._commit_title = None
        self.discriminator = None

        if commit_count is not None:
            self.commit_count = commit_count
        if action is not None:
            self.action = action
        if ref_type is not None:
            self.ref_type = ref_type
        if commit_from is not None:
            self.commit_from = commit_from
        if commit_to is not None:
            self.commit_to = commit_to
        if ref is not None:
            self.ref = ref
        if commit_title is not None:
            self.commit_title = commit_title

    @property
    def commit_count(self):
        r"""Gets the commit_count of this PushEventPayloadDto.

        **参数解释：** 提交数量。

        :return: The commit_count of this PushEventPayloadDto.
        :rtype: int
        """
        return self._commit_count

    @commit_count.setter
    def commit_count(self, commit_count):
        r"""Sets the commit_count of this PushEventPayloadDto.

        **参数解释：** 提交数量。

        :param commit_count: The commit_count of this PushEventPayloadDto.
        :type commit_count: int
        """
        self._commit_count = commit_count

    @property
    def action(self):
        r"""Gets the action of this PushEventPayloadDto.

        **参数解释：** 操作类型。

        :return: The action of this PushEventPayloadDto.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this PushEventPayloadDto.

        **参数解释：** 操作类型。

        :param action: The action of this PushEventPayloadDto.
        :type action: str
        """
        self._action = action

    @property
    def ref_type(self):
        r"""Gets the ref_type of this PushEventPayloadDto.

        **参数解释：** ref类型。

        :return: The ref_type of this PushEventPayloadDto.
        :rtype: str
        """
        return self._ref_type

    @ref_type.setter
    def ref_type(self, ref_type):
        r"""Sets the ref_type of this PushEventPayloadDto.

        **参数解释：** ref类型。

        :param ref_type: The ref_type of this PushEventPayloadDto.
        :type ref_type: str
        """
        self._ref_type = ref_type

    @property
    def commit_from(self):
        r"""Gets the commit_from of this PushEventPayloadDto.

        **参数解释：** 源Commit。

        :return: The commit_from of this PushEventPayloadDto.
        :rtype: str
        """
        return self._commit_from

    @commit_from.setter
    def commit_from(self, commit_from):
        r"""Sets the commit_from of this PushEventPayloadDto.

        **参数解释：** 源Commit。

        :param commit_from: The commit_from of this PushEventPayloadDto.
        :type commit_from: str
        """
        self._commit_from = commit_from

    @property
    def commit_to(self):
        r"""Gets the commit_to of this PushEventPayloadDto.

        **参数解释：** 目标Commit。

        :return: The commit_to of this PushEventPayloadDto.
        :rtype: str
        """
        return self._commit_to

    @commit_to.setter
    def commit_to(self, commit_to):
        r"""Sets the commit_to of this PushEventPayloadDto.

        **参数解释：** 目标Commit。

        :param commit_to: The commit_to of this PushEventPayloadDto.
        :type commit_to: str
        """
        self._commit_to = commit_to

    @property
    def ref(self):
        r"""Gets the ref of this PushEventPayloadDto.

        **参数解释：** 分支。

        :return: The ref of this PushEventPayloadDto.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this PushEventPayloadDto.

        **参数解释：** 分支。

        :param ref: The ref of this PushEventPayloadDto.
        :type ref: str
        """
        self._ref = ref

    @property
    def commit_title(self):
        r"""Gets the commit_title of this PushEventPayloadDto.

        **参数解释：** 提交标题。

        :return: The commit_title of this PushEventPayloadDto.
        :rtype: str
        """
        return self._commit_title

    @commit_title.setter
    def commit_title(self, commit_title):
        r"""Sets the commit_title of this PushEventPayloadDto.

        **参数解释：** 提交标题。

        :param commit_title: The commit_title of this PushEventPayloadDto.
        :type commit_title: str
        """
        self._commit_title = commit_title

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
        if not isinstance(other, PushEventPayloadDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
