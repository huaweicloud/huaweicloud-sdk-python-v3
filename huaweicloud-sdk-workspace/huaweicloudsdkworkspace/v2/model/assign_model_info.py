# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssignModelInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'assign_dimension': 'str',
        'priority_strategy': 'str',
        'desktop_assigin_user_num': 'int',
        'user_assigin_desktop_num': 'int',
        'desktop_name_policy_id': 'str'
    }

    attribute_map = {
        'assign_dimension': 'assign_dimension',
        'priority_strategy': 'priority_strategy',
        'desktop_assigin_user_num': 'desktop_assigin_user_num',
        'user_assigin_desktop_num': 'user_assigin_desktop_num',
        'desktop_name_policy_id': 'desktop_name_policy_id'
    }

    def __init__(self, assign_dimension=None, priority_strategy=None, desktop_assigin_user_num=None, user_assigin_desktop_num=None, desktop_name_policy_id=None):
        r"""AssignModelInfo

        The model defined in huaweicloud sdk

        :param assign_dimension: 分配的维度，当前支持  - USER: “用户为维度” - DESKTOP:“桌面为维度”两种。
        :type assign_dimension: str
        :param priority_strategy: 优先分配的策略，策略名为规则为{维度}_{子策略}  - USER_NO_DESKTOP:  用户维度-无桌面 - USER_FIXED_DESKTOP_NUM: 用户维度-桌面个数固定 - DESKTOP_ASSIGN_USER_PRIORITY： 桌面维度-用户优先 - DESKTOP_ASSIGN_FIXED_USER： 桌面维度-固定用户 - DESKTOP_ASSIGN_USERS_OR_GROUPS： 桌面维度-为每台桌面分配所选的所有用户（组） - FIXED_RELATION: 使用参数中的固定分配关系
        :type priority_strategy: str
        :param desktop_assigin_user_num: 每个桌面自动分配的用户数，当子策略为 DESKTOP_ASSIGN_FIXED_USER 必填。
        :type desktop_assigin_user_num: int
        :param user_assigin_desktop_num: 每个用户自动分配桌面数，当子策略为 USER_NO_DESKTOP、USER_FIXED_DESKTOP_NUM必填。
        :type user_assigin_desktop_num: int
        :param desktop_name_policy_id: 策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。
        :type desktop_name_policy_id: str
        """
        
        

        self._assign_dimension = None
        self._priority_strategy = None
        self._desktop_assigin_user_num = None
        self._user_assigin_desktop_num = None
        self._desktop_name_policy_id = None
        self.discriminator = None

        if assign_dimension is not None:
            self.assign_dimension = assign_dimension
        if priority_strategy is not None:
            self.priority_strategy = priority_strategy
        if desktop_assigin_user_num is not None:
            self.desktop_assigin_user_num = desktop_assigin_user_num
        if user_assigin_desktop_num is not None:
            self.user_assigin_desktop_num = user_assigin_desktop_num
        if desktop_name_policy_id is not None:
            self.desktop_name_policy_id = desktop_name_policy_id

    @property
    def assign_dimension(self):
        r"""Gets the assign_dimension of this AssignModelInfo.

        分配的维度，当前支持  - USER: “用户为维度” - DESKTOP:“桌面为维度”两种。

        :return: The assign_dimension of this AssignModelInfo.
        :rtype: str
        """
        return self._assign_dimension

    @assign_dimension.setter
    def assign_dimension(self, assign_dimension):
        r"""Sets the assign_dimension of this AssignModelInfo.

        分配的维度，当前支持  - USER: “用户为维度” - DESKTOP:“桌面为维度”两种。

        :param assign_dimension: The assign_dimension of this AssignModelInfo.
        :type assign_dimension: str
        """
        self._assign_dimension = assign_dimension

    @property
    def priority_strategy(self):
        r"""Gets the priority_strategy of this AssignModelInfo.

        优先分配的策略，策略名为规则为{维度}_{子策略}  - USER_NO_DESKTOP:  用户维度-无桌面 - USER_FIXED_DESKTOP_NUM: 用户维度-桌面个数固定 - DESKTOP_ASSIGN_USER_PRIORITY： 桌面维度-用户优先 - DESKTOP_ASSIGN_FIXED_USER： 桌面维度-固定用户 - DESKTOP_ASSIGN_USERS_OR_GROUPS： 桌面维度-为每台桌面分配所选的所有用户（组） - FIXED_RELATION: 使用参数中的固定分配关系

        :return: The priority_strategy of this AssignModelInfo.
        :rtype: str
        """
        return self._priority_strategy

    @priority_strategy.setter
    def priority_strategy(self, priority_strategy):
        r"""Sets the priority_strategy of this AssignModelInfo.

        优先分配的策略，策略名为规则为{维度}_{子策略}  - USER_NO_DESKTOP:  用户维度-无桌面 - USER_FIXED_DESKTOP_NUM: 用户维度-桌面个数固定 - DESKTOP_ASSIGN_USER_PRIORITY： 桌面维度-用户优先 - DESKTOP_ASSIGN_FIXED_USER： 桌面维度-固定用户 - DESKTOP_ASSIGN_USERS_OR_GROUPS： 桌面维度-为每台桌面分配所选的所有用户（组） - FIXED_RELATION: 使用参数中的固定分配关系

        :param priority_strategy: The priority_strategy of this AssignModelInfo.
        :type priority_strategy: str
        """
        self._priority_strategy = priority_strategy

    @property
    def desktop_assigin_user_num(self):
        r"""Gets the desktop_assigin_user_num of this AssignModelInfo.

        每个桌面自动分配的用户数，当子策略为 DESKTOP_ASSIGN_FIXED_USER 必填。

        :return: The desktop_assigin_user_num of this AssignModelInfo.
        :rtype: int
        """
        return self._desktop_assigin_user_num

    @desktop_assigin_user_num.setter
    def desktop_assigin_user_num(self, desktop_assigin_user_num):
        r"""Sets the desktop_assigin_user_num of this AssignModelInfo.

        每个桌面自动分配的用户数，当子策略为 DESKTOP_ASSIGN_FIXED_USER 必填。

        :param desktop_assigin_user_num: The desktop_assigin_user_num of this AssignModelInfo.
        :type desktop_assigin_user_num: int
        """
        self._desktop_assigin_user_num = desktop_assigin_user_num

    @property
    def user_assigin_desktop_num(self):
        r"""Gets the user_assigin_desktop_num of this AssignModelInfo.

        每个用户自动分配桌面数，当子策略为 USER_NO_DESKTOP、USER_FIXED_DESKTOP_NUM必填。

        :return: The user_assigin_desktop_num of this AssignModelInfo.
        :rtype: int
        """
        return self._user_assigin_desktop_num

    @user_assigin_desktop_num.setter
    def user_assigin_desktop_num(self, user_assigin_desktop_num):
        r"""Sets the user_assigin_desktop_num of this AssignModelInfo.

        每个用户自动分配桌面数，当子策略为 USER_NO_DESKTOP、USER_FIXED_DESKTOP_NUM必填。

        :param user_assigin_desktop_num: The user_assigin_desktop_num of this AssignModelInfo.
        :type user_assigin_desktop_num: int
        """
        self._user_assigin_desktop_num = user_assigin_desktop_num

    @property
    def desktop_name_policy_id(self):
        r"""Gets the desktop_name_policy_id of this AssignModelInfo.

        策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。

        :return: The desktop_name_policy_id of this AssignModelInfo.
        :rtype: str
        """
        return self._desktop_name_policy_id

    @desktop_name_policy_id.setter
    def desktop_name_policy_id(self, desktop_name_policy_id):
        r"""Sets the desktop_name_policy_id of this AssignModelInfo.

        策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。

        :param desktop_name_policy_id: The desktop_name_policy_id of this AssignModelInfo.
        :type desktop_name_policy_id: str
        """
        self._desktop_name_policy_id = desktop_name_policy_id

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
        if not isinstance(other, AssignModelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
