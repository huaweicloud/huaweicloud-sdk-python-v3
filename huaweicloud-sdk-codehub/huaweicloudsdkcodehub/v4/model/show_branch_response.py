# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBranchResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'commit': 'CommitDto',
        'merged': 'bool',
        'protected': 'bool',
        'developers_can_push': 'bool',
        'developers_can_merge': 'bool',
        'can_push': 'bool',
        'default': 'bool',
        'x_total': 'str'
    }

    attribute_map = {
        'name': 'name',
        'commit': 'commit',
        'merged': 'merged',
        'protected': 'protected',
        'developers_can_push': 'developers_can_push',
        'developers_can_merge': 'developers_can_merge',
        'can_push': 'can_push',
        'default': 'default',
        'x_total': 'X-Total'
    }

    def __init__(self, name=None, commit=None, merged=None, protected=None, developers_can_push=None, developers_can_merge=None, can_push=None, default=None, x_total=None):
        r"""ShowBranchResponse

        The model defined in huaweicloud sdk

        :param name: 分支名
        :type name: str
        :param commit: 
        :type commit: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        :param merged: 用户id
        :type merged: bool
        :param protected: 是否为保护分支
        :type protected: bool
        :param developers_can_push: 开发者是否可以推送
        :type developers_can_push: bool
        :param developers_can_merge: 开发者是否可以合并
        :type developers_can_merge: bool
        :param can_push: 是否可以推送
        :type can_push: bool
        :param default: 是否为默认分支
        :type default: bool
        :param x_total: 
        :type x_total: str
        """
        
        super(ShowBranchResponse, self).__init__()

        self._name = None
        self._commit = None
        self._merged = None
        self._protected = None
        self._developers_can_push = None
        self._developers_can_merge = None
        self._can_push = None
        self._default = None
        self._x_total = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if commit is not None:
            self.commit = commit
        if merged is not None:
            self.merged = merged
        if protected is not None:
            self.protected = protected
        if developers_can_push is not None:
            self.developers_can_push = developers_can_push
        if developers_can_merge is not None:
            self.developers_can_merge = developers_can_merge
        if can_push is not None:
            self.can_push = can_push
        if default is not None:
            self.default = default
        if x_total is not None:
            self.x_total = x_total

    @property
    def name(self):
        r"""Gets the name of this ShowBranchResponse.

        分支名

        :return: The name of this ShowBranchResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowBranchResponse.

        分支名

        :param name: The name of this ShowBranchResponse.
        :type name: str
        """
        self._name = name

    @property
    def commit(self):
        r"""Gets the commit of this ShowBranchResponse.

        :return: The commit of this ShowBranchResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        r"""Sets the commit of this ShowBranchResponse.

        :param commit: The commit of this ShowBranchResponse.
        :type commit: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        """
        self._commit = commit

    @property
    def merged(self):
        r"""Gets the merged of this ShowBranchResponse.

        用户id

        :return: The merged of this ShowBranchResponse.
        :rtype: bool
        """
        return self._merged

    @merged.setter
    def merged(self, merged):
        r"""Sets the merged of this ShowBranchResponse.

        用户id

        :param merged: The merged of this ShowBranchResponse.
        :type merged: bool
        """
        self._merged = merged

    @property
    def protected(self):
        r"""Gets the protected of this ShowBranchResponse.

        是否为保护分支

        :return: The protected of this ShowBranchResponse.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        r"""Sets the protected of this ShowBranchResponse.

        是否为保护分支

        :param protected: The protected of this ShowBranchResponse.
        :type protected: bool
        """
        self._protected = protected

    @property
    def developers_can_push(self):
        r"""Gets the developers_can_push of this ShowBranchResponse.

        开发者是否可以推送

        :return: The developers_can_push of this ShowBranchResponse.
        :rtype: bool
        """
        return self._developers_can_push

    @developers_can_push.setter
    def developers_can_push(self, developers_can_push):
        r"""Sets the developers_can_push of this ShowBranchResponse.

        开发者是否可以推送

        :param developers_can_push: The developers_can_push of this ShowBranchResponse.
        :type developers_can_push: bool
        """
        self._developers_can_push = developers_can_push

    @property
    def developers_can_merge(self):
        r"""Gets the developers_can_merge of this ShowBranchResponse.

        开发者是否可以合并

        :return: The developers_can_merge of this ShowBranchResponse.
        :rtype: bool
        """
        return self._developers_can_merge

    @developers_can_merge.setter
    def developers_can_merge(self, developers_can_merge):
        r"""Sets the developers_can_merge of this ShowBranchResponse.

        开发者是否可以合并

        :param developers_can_merge: The developers_can_merge of this ShowBranchResponse.
        :type developers_can_merge: bool
        """
        self._developers_can_merge = developers_can_merge

    @property
    def can_push(self):
        r"""Gets the can_push of this ShowBranchResponse.

        是否可以推送

        :return: The can_push of this ShowBranchResponse.
        :rtype: bool
        """
        return self._can_push

    @can_push.setter
    def can_push(self, can_push):
        r"""Sets the can_push of this ShowBranchResponse.

        是否可以推送

        :param can_push: The can_push of this ShowBranchResponse.
        :type can_push: bool
        """
        self._can_push = can_push

    @property
    def default(self):
        r"""Gets the default of this ShowBranchResponse.

        是否为默认分支

        :return: The default of this ShowBranchResponse.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this ShowBranchResponse.

        是否为默认分支

        :param default: The default of this ShowBranchResponse.
        :type default: bool
        """
        self._default = default

    @property
    def x_total(self):
        r"""Gets the x_total of this ShowBranchResponse.

        :return: The x_total of this ShowBranchResponse.
        :rtype: str
        """
        return self._x_total

    @x_total.setter
    def x_total(self, x_total):
        r"""Sets the x_total of this ShowBranchResponse.

        :param x_total: The x_total of this ShowBranchResponse.
        :type x_total: str
        """
        self._x_total = x_total

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
        if not isinstance(other, ShowBranchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
