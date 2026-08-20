# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessInstanceResponseResultCurrOwner:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'watcher': 'str',
        'user_id': 'str',
        'user_num_id': 'str',
        'user_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'nick_name': 'str',
        'role_id': 'str',
        'role_name': 'str',
        'image_id': 'str',
        'region': 'str',
        'opinion': 'str',
        'description': 'str',
        'owner': 'str',
        'ccb_id': 'str',
        'has_removed': 'str'
    }

    attribute_map = {
        'watcher': 'watcher',
        'user_id': 'user_id',
        'user_num_id': 'user_num_id',
        'user_name': 'user_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'nick_name': 'nick_name',
        'role_id': 'role_id',
        'role_name': 'role_name',
        'image_id': 'image_id',
        'region': 'region',
        'opinion': 'opinion',
        'description': 'description',
        'owner': 'owner',
        'ccb_id': 'ccbId',
        'has_removed': 'has_removed'
    }

    def __init__(self, watcher=None, user_id=None, user_num_id=None, user_name=None, domain_id=None, domain_name=None, nick_name=None, role_id=None, role_name=None, image_id=None, region=None, opinion=None, description=None, owner=None, ccb_id=None, has_removed=None):
        r"""ProcessInstanceResponseResultCurrOwner

        The model defined in huaweicloud sdk

        :param watcher: 观察者
        :type watcher: str
        :param user_id: 用户ID
        :type user_id: str
        :param user_num_id: 用户数字id
        :type user_num_id: str
        :param user_name: 用户名
        :type user_name: str
        :param domain_id: 租户id
        :type domain_id: str
        :param domain_name: 租户名
        :type domain_name: str
        :param nick_name: 昵称
        :type nick_name: str
        :param role_id: 角色id
        :type role_id: str
        :param role_name: 角色名
        :type role_name: str
        :param image_id: 用户头像
        :type image_id: str
        :param region: 区域
        :type region: str
        :param opinion: 意见
        :type opinion: str
        :param description: 描述
        :type description: str
        :param owner: 责任人
        :type owner: str
        :param ccb_id: 评审id
        :type ccb_id: str
        :param has_removed: 是否已移出项目
        :type has_removed: str
        """
        
        

        self._watcher = None
        self._user_id = None
        self._user_num_id = None
        self._user_name = None
        self._domain_id = None
        self._domain_name = None
        self._nick_name = None
        self._role_id = None
        self._role_name = None
        self._image_id = None
        self._region = None
        self._opinion = None
        self._description = None
        self._owner = None
        self._ccb_id = None
        self._has_removed = None
        self.discriminator = None

        if watcher is not None:
            self.watcher = watcher
        if user_id is not None:
            self.user_id = user_id
        if user_num_id is not None:
            self.user_num_id = user_num_id
        if user_name is not None:
            self.user_name = user_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if nick_name is not None:
            self.nick_name = nick_name
        if role_id is not None:
            self.role_id = role_id
        if role_name is not None:
            self.role_name = role_name
        if image_id is not None:
            self.image_id = image_id
        if region is not None:
            self.region = region
        if opinion is not None:
            self.opinion = opinion
        if description is not None:
            self.description = description
        if owner is not None:
            self.owner = owner
        if ccb_id is not None:
            self.ccb_id = ccb_id
        if has_removed is not None:
            self.has_removed = has_removed

    @property
    def watcher(self):
        r"""Gets the watcher of this ProcessInstanceResponseResultCurrOwner.

        观察者

        :return: The watcher of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._watcher

    @watcher.setter
    def watcher(self, watcher):
        r"""Sets the watcher of this ProcessInstanceResponseResultCurrOwner.

        观察者

        :param watcher: The watcher of this ProcessInstanceResponseResultCurrOwner.
        :type watcher: str
        """
        self._watcher = watcher

    @property
    def user_id(self):
        r"""Gets the user_id of this ProcessInstanceResponseResultCurrOwner.

        用户ID

        :return: The user_id of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ProcessInstanceResponseResultCurrOwner.

        用户ID

        :param user_id: The user_id of this ProcessInstanceResponseResultCurrOwner.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_num_id(self):
        r"""Gets the user_num_id of this ProcessInstanceResponseResultCurrOwner.

        用户数字id

        :return: The user_num_id of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._user_num_id

    @user_num_id.setter
    def user_num_id(self, user_num_id):
        r"""Sets the user_num_id of this ProcessInstanceResponseResultCurrOwner.

        用户数字id

        :param user_num_id: The user_num_id of this ProcessInstanceResponseResultCurrOwner.
        :type user_num_id: str
        """
        self._user_num_id = user_num_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ProcessInstanceResponseResultCurrOwner.

        用户名

        :return: The user_name of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ProcessInstanceResponseResultCurrOwner.

        用户名

        :param user_name: The user_name of this ProcessInstanceResponseResultCurrOwner.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ProcessInstanceResponseResultCurrOwner.

        租户id

        :return: The domain_id of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ProcessInstanceResponseResultCurrOwner.

        租户id

        :param domain_id: The domain_id of this ProcessInstanceResponseResultCurrOwner.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ProcessInstanceResponseResultCurrOwner.

        租户名

        :return: The domain_name of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ProcessInstanceResponseResultCurrOwner.

        租户名

        :param domain_name: The domain_name of this ProcessInstanceResponseResultCurrOwner.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this ProcessInstanceResponseResultCurrOwner.

        昵称

        :return: The nick_name of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this ProcessInstanceResponseResultCurrOwner.

        昵称

        :param nick_name: The nick_name of this ProcessInstanceResponseResultCurrOwner.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def role_id(self):
        r"""Gets the role_id of this ProcessInstanceResponseResultCurrOwner.

        角色id

        :return: The role_id of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this ProcessInstanceResponseResultCurrOwner.

        角色id

        :param role_id: The role_id of this ProcessInstanceResponseResultCurrOwner.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_name(self):
        r"""Gets the role_name of this ProcessInstanceResponseResultCurrOwner.

        角色名

        :return: The role_name of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this ProcessInstanceResponseResultCurrOwner.

        角色名

        :param role_name: The role_name of this ProcessInstanceResponseResultCurrOwner.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def image_id(self):
        r"""Gets the image_id of this ProcessInstanceResponseResultCurrOwner.

        用户头像

        :return: The image_id of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ProcessInstanceResponseResultCurrOwner.

        用户头像

        :param image_id: The image_id of this ProcessInstanceResponseResultCurrOwner.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def region(self):
        r"""Gets the region of this ProcessInstanceResponseResultCurrOwner.

        区域

        :return: The region of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ProcessInstanceResponseResultCurrOwner.

        区域

        :param region: The region of this ProcessInstanceResponseResultCurrOwner.
        :type region: str
        """
        self._region = region

    @property
    def opinion(self):
        r"""Gets the opinion of this ProcessInstanceResponseResultCurrOwner.

        意见

        :return: The opinion of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._opinion

    @opinion.setter
    def opinion(self, opinion):
        r"""Sets the opinion of this ProcessInstanceResponseResultCurrOwner.

        意见

        :param opinion: The opinion of this ProcessInstanceResponseResultCurrOwner.
        :type opinion: str
        """
        self._opinion = opinion

    @property
    def description(self):
        r"""Gets the description of this ProcessInstanceResponseResultCurrOwner.

        描述

        :return: The description of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProcessInstanceResponseResultCurrOwner.

        描述

        :param description: The description of this ProcessInstanceResponseResultCurrOwner.
        :type description: str
        """
        self._description = description

    @property
    def owner(self):
        r"""Gets the owner of this ProcessInstanceResponseResultCurrOwner.

        责任人

        :return: The owner of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ProcessInstanceResponseResultCurrOwner.

        责任人

        :param owner: The owner of this ProcessInstanceResponseResultCurrOwner.
        :type owner: str
        """
        self._owner = owner

    @property
    def ccb_id(self):
        r"""Gets the ccb_id of this ProcessInstanceResponseResultCurrOwner.

        评审id

        :return: The ccb_id of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._ccb_id

    @ccb_id.setter
    def ccb_id(self, ccb_id):
        r"""Sets the ccb_id of this ProcessInstanceResponseResultCurrOwner.

        评审id

        :param ccb_id: The ccb_id of this ProcessInstanceResponseResultCurrOwner.
        :type ccb_id: str
        """
        self._ccb_id = ccb_id

    @property
    def has_removed(self):
        r"""Gets the has_removed of this ProcessInstanceResponseResultCurrOwner.

        是否已移出项目

        :return: The has_removed of this ProcessInstanceResponseResultCurrOwner.
        :rtype: str
        """
        return self._has_removed

    @has_removed.setter
    def has_removed(self, has_removed):
        r"""Sets the has_removed of this ProcessInstanceResponseResultCurrOwner.

        是否已移出项目

        :param has_removed: The has_removed of this ProcessInstanceResponseResultCurrOwner.
        :type has_removed: str
        """
        self._has_removed = has_removed

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
        if not isinstance(other, ProcessInstanceResponseResultCurrOwner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
