# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitStatisticsResultCommitDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'author_name': 'str',
        'date': 'str',
        'nick_name': 'str',
        'tenant_name': 'str',
        'user_name': 'str',
        'is_merge': 'bool'
    }

    attribute_map = {
        'author_name': 'author_name',
        'date': 'date',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name',
        'user_name': 'user_name',
        'is_merge': 'is_merge'
    }

    def __init__(self, author_name=None, date=None, nick_name=None, tenant_name=None, user_name=None, is_merge=None):
        r"""CommitStatisticsResultCommitDto

        The model defined in huaweicloud sdk

        :param author_name: **参数解释：** 作者名称。
        :type author_name: str
        :param date: **参数解释：** 提交日期。
        :type date: str
        :param nick_name: **参数解释：** 昵称。
        :type nick_name: str
        :param tenant_name: **参数解释：** 租户名。
        :type tenant_name: str
        :param user_name: **参数解释：** 用户名。
        :type user_name: str
        :param is_merge: **参数解释：** 是否通过merge合入。 **取值范围：** - true，通过merge合入。 - false，非通过merge合入。
        :type is_merge: bool
        """
        
        

        self._author_name = None
        self._date = None
        self._nick_name = None
        self._tenant_name = None
        self._user_name = None
        self._is_merge = None
        self.discriminator = None

        if author_name is not None:
            self.author_name = author_name
        if date is not None:
            self.date = date
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if user_name is not None:
            self.user_name = user_name
        if is_merge is not None:
            self.is_merge = is_merge

    @property
    def author_name(self):
        r"""Gets the author_name of this CommitStatisticsResultCommitDto.

        **参数解释：** 作者名称。

        :return: The author_name of this CommitStatisticsResultCommitDto.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this CommitStatisticsResultCommitDto.

        **参数解释：** 作者名称。

        :param author_name: The author_name of this CommitStatisticsResultCommitDto.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def date(self):
        r"""Gets the date of this CommitStatisticsResultCommitDto.

        **参数解释：** 提交日期。

        :return: The date of this CommitStatisticsResultCommitDto.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this CommitStatisticsResultCommitDto.

        **参数解释：** 提交日期。

        :param date: The date of this CommitStatisticsResultCommitDto.
        :type date: str
        """
        self._date = date

    @property
    def nick_name(self):
        r"""Gets the nick_name of this CommitStatisticsResultCommitDto.

        **参数解释：** 昵称。

        :return: The nick_name of this CommitStatisticsResultCommitDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this CommitStatisticsResultCommitDto.

        **参数解释：** 昵称。

        :param nick_name: The nick_name of this CommitStatisticsResultCommitDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this CommitStatisticsResultCommitDto.

        **参数解释：** 租户名。

        :return: The tenant_name of this CommitStatisticsResultCommitDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this CommitStatisticsResultCommitDto.

        **参数解释：** 租户名。

        :param tenant_name: The tenant_name of this CommitStatisticsResultCommitDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def user_name(self):
        r"""Gets the user_name of this CommitStatisticsResultCommitDto.

        **参数解释：** 用户名。

        :return: The user_name of this CommitStatisticsResultCommitDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CommitStatisticsResultCommitDto.

        **参数解释：** 用户名。

        :param user_name: The user_name of this CommitStatisticsResultCommitDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def is_merge(self):
        r"""Gets the is_merge of this CommitStatisticsResultCommitDto.

        **参数解释：** 是否通过merge合入。 **取值范围：** - true，通过merge合入。 - false，非通过merge合入。

        :return: The is_merge of this CommitStatisticsResultCommitDto.
        :rtype: bool
        """
        return self._is_merge

    @is_merge.setter
    def is_merge(self, is_merge):
        r"""Sets the is_merge of this CommitStatisticsResultCommitDto.

        **参数解释：** 是否通过merge合入。 **取值范围：** - true，通过merge合入。 - false，非通过merge合入。

        :param is_merge: The is_merge of this CommitStatisticsResultCommitDto.
        :type is_merge: bool
        """
        self._is_merge = is_merge

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
        if not isinstance(other, CommitStatisticsResultCommitDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
