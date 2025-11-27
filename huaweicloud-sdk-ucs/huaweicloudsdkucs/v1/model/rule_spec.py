# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iam_user_i_ds': 'list[str]',
        'type': 'str',
        'contents': 'list[Content]',
        'description': 'str'
    }

    attribute_map = {
        'iam_user_i_ds': 'iamUserIDs',
        'type': 'type',
        'contents': 'contents',
        'description': 'description'
    }

    def __init__(self, iam_user_i_ds=None, type=None, contents=None, description=None):
        r"""RuleSpec

        The model defined in huaweicloud sdk

        :param iam_user_i_ds: 权限策略关联的IAM用户信息
        :type iam_user_i_ds: list[str]
        :param type: 权限策略类型，只允许四种类型：readonly/develop/admin/custom
        :type type: str
        :param contents: 权限策略内容
        :type contents: list[:class:`huaweicloudsdkucs.v1.Content`]
        :param description: 权限策略描述信息
        :type description: str
        """
        
        

        self._iam_user_i_ds = None
        self._type = None
        self._contents = None
        self._description = None
        self.discriminator = None

        if iam_user_i_ds is not None:
            self.iam_user_i_ds = iam_user_i_ds
        if type is not None:
            self.type = type
        if contents is not None:
            self.contents = contents
        if description is not None:
            self.description = description

    @property
    def iam_user_i_ds(self):
        r"""Gets the iam_user_i_ds of this RuleSpec.

        权限策略关联的IAM用户信息

        :return: The iam_user_i_ds of this RuleSpec.
        :rtype: list[str]
        """
        return self._iam_user_i_ds

    @iam_user_i_ds.setter
    def iam_user_i_ds(self, iam_user_i_ds):
        r"""Sets the iam_user_i_ds of this RuleSpec.

        权限策略关联的IAM用户信息

        :param iam_user_i_ds: The iam_user_i_ds of this RuleSpec.
        :type iam_user_i_ds: list[str]
        """
        self._iam_user_i_ds = iam_user_i_ds

    @property
    def type(self):
        r"""Gets the type of this RuleSpec.

        权限策略类型，只允许四种类型：readonly/develop/admin/custom

        :return: The type of this RuleSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuleSpec.

        权限策略类型，只允许四种类型：readonly/develop/admin/custom

        :param type: The type of this RuleSpec.
        :type type: str
        """
        self._type = type

    @property
    def contents(self):
        r"""Gets the contents of this RuleSpec.

        权限策略内容

        :return: The contents of this RuleSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.Content`]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this RuleSpec.

        权限策略内容

        :param contents: The contents of this RuleSpec.
        :type contents: list[:class:`huaweicloudsdkucs.v1.Content`]
        """
        self._contents = contents

    @property
    def description(self):
        r"""Gets the description of this RuleSpec.

        权限策略描述信息

        :return: The description of this RuleSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RuleSpec.

        权限策略描述信息

        :param description: The description of this RuleSpec.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RuleSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
