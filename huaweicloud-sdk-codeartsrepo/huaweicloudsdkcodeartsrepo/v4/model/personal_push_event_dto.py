# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersonalPushEventDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'author': 'PersonalEventAuthorDto',
        'repository': 'RepositorySimpleDto',
        'push_data': 'PushEventPayloadDto',
        'created_at': 'str'
    }

    attribute_map = {
        'author': 'author',
        'repository': 'repository',
        'push_data': 'push_data',
        'created_at': 'created_at'
    }

    def __init__(self, author=None, repository=None, push_data=None, created_at=None):
        r"""PersonalPushEventDto

        The model defined in huaweicloud sdk

        :param author: 
        :type author: :class:`huaweicloudsdkcodeartsrepo.v4.PersonalEventAuthorDto`
        :param repository: 
        :type repository: :class:`huaweicloudsdkcodeartsrepo.v4.RepositorySimpleDto`
        :param push_data: 
        :type push_data: :class:`huaweicloudsdkcodeartsrepo.v4.PushEventPayloadDto`
        :param created_at: **参数解释：** 创建时间。 **约束限制：** 不涉及
        :type created_at: str
        """
        
        

        self._author = None
        self._repository = None
        self._push_data = None
        self._created_at = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if repository is not None:
            self.repository = repository
        if push_data is not None:
            self.push_data = push_data
        if created_at is not None:
            self.created_at = created_at

    @property
    def author(self):
        r"""Gets the author of this PersonalPushEventDto.

        :return: The author of this PersonalPushEventDto.
        :rtype: :class:`huaweicloudsdkcodeartsrepo.v4.PersonalEventAuthorDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this PersonalPushEventDto.

        :param author: The author of this PersonalPushEventDto.
        :type author: :class:`huaweicloudsdkcodeartsrepo.v4.PersonalEventAuthorDto`
        """
        self._author = author

    @property
    def repository(self):
        r"""Gets the repository of this PersonalPushEventDto.

        :return: The repository of this PersonalPushEventDto.
        :rtype: :class:`huaweicloudsdkcodeartsrepo.v4.RepositorySimpleDto`
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this PersonalPushEventDto.

        :param repository: The repository of this PersonalPushEventDto.
        :type repository: :class:`huaweicloudsdkcodeartsrepo.v4.RepositorySimpleDto`
        """
        self._repository = repository

    @property
    def push_data(self):
        r"""Gets the push_data of this PersonalPushEventDto.

        :return: The push_data of this PersonalPushEventDto.
        :rtype: :class:`huaweicloudsdkcodeartsrepo.v4.PushEventPayloadDto`
        """
        return self._push_data

    @push_data.setter
    def push_data(self, push_data):
        r"""Sets the push_data of this PersonalPushEventDto.

        :param push_data: The push_data of this PersonalPushEventDto.
        :type push_data: :class:`huaweicloudsdkcodeartsrepo.v4.PushEventPayloadDto`
        """
        self._push_data = push_data

    @property
    def created_at(self):
        r"""Gets the created_at of this PersonalPushEventDto.

        **参数解释：** 创建时间。 **约束限制：** 不涉及

        :return: The created_at of this PersonalPushEventDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this PersonalPushEventDto.

        **参数解释：** 创建时间。 **约束限制：** 不涉及

        :param created_at: The created_at of this PersonalPushEventDto.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, PersonalPushEventDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
