# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessInstanceResponseResultReviewConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approval_type': 'int',
        'ratio_value': 'str',
        'skip_decisioning': 'bool',
        'approval_roles': 'str',
        'review_roles': 'str'
    }

    attribute_map = {
        'approval_type': 'approval_type',
        'ratio_value': 'ratio_value',
        'skip_decisioning': 'skip_decisioning',
        'approval_roles': 'approval_roles',
        'review_roles': 'review_roles'
    }

    def __init__(self, approval_type=None, ratio_value=None, skip_decisioning=None, approval_roles=None, review_roles=None):
        r"""ProcessInstanceResponseResultReviewConfig

        The model defined in huaweicloud sdk

        :param approval_type: 审批类型
        :type approval_type: int
        :param ratio_value: 审批进度
        :type ratio_value: str
        :param skip_decisioning: 是否跳过决策
        :type skip_decisioning: bool
        :param approval_roles: 决策角色
        :type approval_roles: str
        :param review_roles: 审批角色
        :type review_roles: str
        """
        
        

        self._approval_type = None
        self._ratio_value = None
        self._skip_decisioning = None
        self._approval_roles = None
        self._review_roles = None
        self.discriminator = None

        if approval_type is not None:
            self.approval_type = approval_type
        if ratio_value is not None:
            self.ratio_value = ratio_value
        if skip_decisioning is not None:
            self.skip_decisioning = skip_decisioning
        if approval_roles is not None:
            self.approval_roles = approval_roles
        if review_roles is not None:
            self.review_roles = review_roles

    @property
    def approval_type(self):
        r"""Gets the approval_type of this ProcessInstanceResponseResultReviewConfig.

        审批类型

        :return: The approval_type of this ProcessInstanceResponseResultReviewConfig.
        :rtype: int
        """
        return self._approval_type

    @approval_type.setter
    def approval_type(self, approval_type):
        r"""Sets the approval_type of this ProcessInstanceResponseResultReviewConfig.

        审批类型

        :param approval_type: The approval_type of this ProcessInstanceResponseResultReviewConfig.
        :type approval_type: int
        """
        self._approval_type = approval_type

    @property
    def ratio_value(self):
        r"""Gets the ratio_value of this ProcessInstanceResponseResultReviewConfig.

        审批进度

        :return: The ratio_value of this ProcessInstanceResponseResultReviewConfig.
        :rtype: str
        """
        return self._ratio_value

    @ratio_value.setter
    def ratio_value(self, ratio_value):
        r"""Sets the ratio_value of this ProcessInstanceResponseResultReviewConfig.

        审批进度

        :param ratio_value: The ratio_value of this ProcessInstanceResponseResultReviewConfig.
        :type ratio_value: str
        """
        self._ratio_value = ratio_value

    @property
    def skip_decisioning(self):
        r"""Gets the skip_decisioning of this ProcessInstanceResponseResultReviewConfig.

        是否跳过决策

        :return: The skip_decisioning of this ProcessInstanceResponseResultReviewConfig.
        :rtype: bool
        """
        return self._skip_decisioning

    @skip_decisioning.setter
    def skip_decisioning(self, skip_decisioning):
        r"""Sets the skip_decisioning of this ProcessInstanceResponseResultReviewConfig.

        是否跳过决策

        :param skip_decisioning: The skip_decisioning of this ProcessInstanceResponseResultReviewConfig.
        :type skip_decisioning: bool
        """
        self._skip_decisioning = skip_decisioning

    @property
    def approval_roles(self):
        r"""Gets the approval_roles of this ProcessInstanceResponseResultReviewConfig.

        决策角色

        :return: The approval_roles of this ProcessInstanceResponseResultReviewConfig.
        :rtype: str
        """
        return self._approval_roles

    @approval_roles.setter
    def approval_roles(self, approval_roles):
        r"""Sets the approval_roles of this ProcessInstanceResponseResultReviewConfig.

        决策角色

        :param approval_roles: The approval_roles of this ProcessInstanceResponseResultReviewConfig.
        :type approval_roles: str
        """
        self._approval_roles = approval_roles

    @property
    def review_roles(self):
        r"""Gets the review_roles of this ProcessInstanceResponseResultReviewConfig.

        审批角色

        :return: The review_roles of this ProcessInstanceResponseResultReviewConfig.
        :rtype: str
        """
        return self._review_roles

    @review_roles.setter
    def review_roles(self, review_roles):
        r"""Sets the review_roles of this ProcessInstanceResponseResultReviewConfig.

        审批角色

        :param review_roles: The review_roles of this ProcessInstanceResponseResultReviewConfig.
        :type review_roles: str
        """
        self._review_roles = review_roles

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
        if not isinstance(other, ProcessInstanceResponseResultReviewConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
