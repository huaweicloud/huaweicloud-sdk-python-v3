# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BranchSimpleDto:

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
        'default': 'bool',
        'can_delete': 'bool',
        'can_read': 'bool',
        'can_download': 'bool',
        'can_push': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'default': 'default',
        'can_delete': 'can_delete',
        'can_read': 'can_read',
        'can_download': 'can_download',
        'can_push': 'can_push'
    }

    def __init__(self, name=None, default=None, can_delete=None, can_read=None, can_download=None, can_push=None):
        r"""BranchSimpleDto

        The model defined in huaweicloud sdk

        :param name: 分支名称
        :type name: str
        :param default: 是否为默认分支
        :type default: bool
        :param can_delete: 用户是否为默认分支
        :type can_delete: bool
        :param can_read: 是否为默认分支
        :type can_read: bool
        :param can_download: 是否为默认分支
        :type can_download: bool
        :param can_push: 是否为默认分支
        :type can_push: bool
        """
        
        

        self._name = None
        self._default = None
        self._can_delete = None
        self._can_read = None
        self._can_download = None
        self._can_push = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if default is not None:
            self.default = default
        if can_delete is not None:
            self.can_delete = can_delete
        if can_read is not None:
            self.can_read = can_read
        if can_download is not None:
            self.can_download = can_download
        if can_push is not None:
            self.can_push = can_push

    @property
    def name(self):
        r"""Gets the name of this BranchSimpleDto.

        分支名称

        :return: The name of this BranchSimpleDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BranchSimpleDto.

        分支名称

        :param name: The name of this BranchSimpleDto.
        :type name: str
        """
        self._name = name

    @property
    def default(self):
        r"""Gets the default of this BranchSimpleDto.

        是否为默认分支

        :return: The default of this BranchSimpleDto.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this BranchSimpleDto.

        是否为默认分支

        :param default: The default of this BranchSimpleDto.
        :type default: bool
        """
        self._default = default

    @property
    def can_delete(self):
        r"""Gets the can_delete of this BranchSimpleDto.

        用户是否为默认分支

        :return: The can_delete of this BranchSimpleDto.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this BranchSimpleDto.

        用户是否为默认分支

        :param can_delete: The can_delete of this BranchSimpleDto.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_read(self):
        r"""Gets the can_read of this BranchSimpleDto.

        是否为默认分支

        :return: The can_read of this BranchSimpleDto.
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        r"""Sets the can_read of this BranchSimpleDto.

        是否为默认分支

        :param can_read: The can_read of this BranchSimpleDto.
        :type can_read: bool
        """
        self._can_read = can_read

    @property
    def can_download(self):
        r"""Gets the can_download of this BranchSimpleDto.

        是否为默认分支

        :return: The can_download of this BranchSimpleDto.
        :rtype: bool
        """
        return self._can_download

    @can_download.setter
    def can_download(self, can_download):
        r"""Sets the can_download of this BranchSimpleDto.

        是否为默认分支

        :param can_download: The can_download of this BranchSimpleDto.
        :type can_download: bool
        """
        self._can_download = can_download

    @property
    def can_push(self):
        r"""Gets the can_push of this BranchSimpleDto.

        是否为默认分支

        :return: The can_push of this BranchSimpleDto.
        :rtype: bool
        """
        return self._can_push

    @can_push.setter
    def can_push(self, can_push):
        r"""Sets the can_push of this BranchSimpleDto.

        是否为默认分支

        :param can_push: The can_push of this BranchSimpleDto.
        :type can_push: bool
        """
        self._can_push = can_push

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
        if not isinstance(other, BranchSimpleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
