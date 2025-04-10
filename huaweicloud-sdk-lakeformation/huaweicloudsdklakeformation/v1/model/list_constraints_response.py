# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConstraintsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'constraint_type': 'str',
        'foreign_keys': 'list[ForeignKey]',
        'primary_keys': 'list[PrimaryKey]',
        'not_null_constraints': 'list[NotNullConstraint]',
        'check_constraints': 'list[CheckConstraint]',
        'unique_constraints': 'list[UniqueConstraint]',
        'default_constraints': 'list[DefaultConstraint]'
    }

    attribute_map = {
        'constraint_type': 'constraint_type',
        'foreign_keys': 'foreign_keys',
        'primary_keys': 'primary_keys',
        'not_null_constraints': 'not_null_constraints',
        'check_constraints': 'check_constraints',
        'unique_constraints': 'unique_constraints',
        'default_constraints': 'default_constraints'
    }

    def __init__(self, constraint_type=None, foreign_keys=None, primary_keys=None, not_null_constraints=None, check_constraints=None, unique_constraints=None, default_constraints=None):
        r"""ListConstraintsResponse

        The model defined in huaweicloud sdk

        :param constraint_type: 限制类型
        :type constraint_type: str
        :param foreign_keys: 外键列表
        :type foreign_keys: list[:class:`huaweicloudsdklakeformation.v1.ForeignKey`]
        :param primary_keys: 主键列表
        :type primary_keys: list[:class:`huaweicloudsdklakeformation.v1.PrimaryKey`]
        :param not_null_constraints: 非空限制列表
        :type not_null_constraints: list[:class:`huaweicloudsdklakeformation.v1.NotNullConstraint`]
        :param check_constraints: 检查限制列表
        :type check_constraints: list[:class:`huaweicloudsdklakeformation.v1.CheckConstraint`]
        :param unique_constraints: 唯一值限制列表
        :type unique_constraints: list[:class:`huaweicloudsdklakeformation.v1.UniqueConstraint`]
        :param default_constraints: 默认限制列表
        :type default_constraints: list[:class:`huaweicloudsdklakeformation.v1.DefaultConstraint`]
        """
        
        super(ListConstraintsResponse, self).__init__()

        self._constraint_type = None
        self._foreign_keys = None
        self._primary_keys = None
        self._not_null_constraints = None
        self._check_constraints = None
        self._unique_constraints = None
        self._default_constraints = None
        self.discriminator = None

        if constraint_type is not None:
            self.constraint_type = constraint_type
        if foreign_keys is not None:
            self.foreign_keys = foreign_keys
        if primary_keys is not None:
            self.primary_keys = primary_keys
        if not_null_constraints is not None:
            self.not_null_constraints = not_null_constraints
        if check_constraints is not None:
            self.check_constraints = check_constraints
        if unique_constraints is not None:
            self.unique_constraints = unique_constraints
        if default_constraints is not None:
            self.default_constraints = default_constraints

    @property
    def constraint_type(self):
        r"""Gets the constraint_type of this ListConstraintsResponse.

        限制类型

        :return: The constraint_type of this ListConstraintsResponse.
        :rtype: str
        """
        return self._constraint_type

    @constraint_type.setter
    def constraint_type(self, constraint_type):
        r"""Sets the constraint_type of this ListConstraintsResponse.

        限制类型

        :param constraint_type: The constraint_type of this ListConstraintsResponse.
        :type constraint_type: str
        """
        self._constraint_type = constraint_type

    @property
    def foreign_keys(self):
        r"""Gets the foreign_keys of this ListConstraintsResponse.

        外键列表

        :return: The foreign_keys of this ListConstraintsResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.ForeignKey`]
        """
        return self._foreign_keys

    @foreign_keys.setter
    def foreign_keys(self, foreign_keys):
        r"""Sets the foreign_keys of this ListConstraintsResponse.

        外键列表

        :param foreign_keys: The foreign_keys of this ListConstraintsResponse.
        :type foreign_keys: list[:class:`huaweicloudsdklakeformation.v1.ForeignKey`]
        """
        self._foreign_keys = foreign_keys

    @property
    def primary_keys(self):
        r"""Gets the primary_keys of this ListConstraintsResponse.

        主键列表

        :return: The primary_keys of this ListConstraintsResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PrimaryKey`]
        """
        return self._primary_keys

    @primary_keys.setter
    def primary_keys(self, primary_keys):
        r"""Sets the primary_keys of this ListConstraintsResponse.

        主键列表

        :param primary_keys: The primary_keys of this ListConstraintsResponse.
        :type primary_keys: list[:class:`huaweicloudsdklakeformation.v1.PrimaryKey`]
        """
        self._primary_keys = primary_keys

    @property
    def not_null_constraints(self):
        r"""Gets the not_null_constraints of this ListConstraintsResponse.

        非空限制列表

        :return: The not_null_constraints of this ListConstraintsResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.NotNullConstraint`]
        """
        return self._not_null_constraints

    @not_null_constraints.setter
    def not_null_constraints(self, not_null_constraints):
        r"""Sets the not_null_constraints of this ListConstraintsResponse.

        非空限制列表

        :param not_null_constraints: The not_null_constraints of this ListConstraintsResponse.
        :type not_null_constraints: list[:class:`huaweicloudsdklakeformation.v1.NotNullConstraint`]
        """
        self._not_null_constraints = not_null_constraints

    @property
    def check_constraints(self):
        r"""Gets the check_constraints of this ListConstraintsResponse.

        检查限制列表

        :return: The check_constraints of this ListConstraintsResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.CheckConstraint`]
        """
        return self._check_constraints

    @check_constraints.setter
    def check_constraints(self, check_constraints):
        r"""Sets the check_constraints of this ListConstraintsResponse.

        检查限制列表

        :param check_constraints: The check_constraints of this ListConstraintsResponse.
        :type check_constraints: list[:class:`huaweicloudsdklakeformation.v1.CheckConstraint`]
        """
        self._check_constraints = check_constraints

    @property
    def unique_constraints(self):
        r"""Gets the unique_constraints of this ListConstraintsResponse.

        唯一值限制列表

        :return: The unique_constraints of this ListConstraintsResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.UniqueConstraint`]
        """
        return self._unique_constraints

    @unique_constraints.setter
    def unique_constraints(self, unique_constraints):
        r"""Sets the unique_constraints of this ListConstraintsResponse.

        唯一值限制列表

        :param unique_constraints: The unique_constraints of this ListConstraintsResponse.
        :type unique_constraints: list[:class:`huaweicloudsdklakeformation.v1.UniqueConstraint`]
        """
        self._unique_constraints = unique_constraints

    @property
    def default_constraints(self):
        r"""Gets the default_constraints of this ListConstraintsResponse.

        默认限制列表

        :return: The default_constraints of this ListConstraintsResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.DefaultConstraint`]
        """
        return self._default_constraints

    @default_constraints.setter
    def default_constraints(self, default_constraints):
        r"""Sets the default_constraints of this ListConstraintsResponse.

        默认限制列表

        :param default_constraints: The default_constraints of this ListConstraintsResponse.
        :type default_constraints: list[:class:`huaweicloudsdklakeformation.v1.DefaultConstraint`]
        """
        self._default_constraints = default_constraints

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
        if not isinstance(other, ListConstraintsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
