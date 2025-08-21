# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestReviewerExternalDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'username': 'str',
        'name': 'str',
        'nick_name': 'str',
        'state': 'bool',
        'score': 'int',
        'tenant_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'name': 'name',
        'nick_name': 'nick_name',
        'state': 'state',
        'score': 'score',
        'tenant_name': 'tenant_name'
    }

    def __init__(self, id=None, username=None, name=None, nick_name=None, state=None, score=None, tenant_name=None):
        r"""MergeRequestReviewerExternalDto

        The model defined in huaweicloud sdk

        :param id: 评审人id
        :type id: int
        :param username: 评审人名称
        :type username: str
        :param name: 评审人名称
        :type name: str
        :param nick_name: 评审人昵称
        :type nick_name: str
        :param state: 评审人状态
        :type state: bool
        :param score: 打分
        :type score: int
        :param tenant_name: 租户名称
        :type tenant_name: str
        """
        
        

        self._id = None
        self._username = None
        self._name = None
        self._nick_name = None
        self._state = None
        self._score = None
        self._tenant_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if name is not None:
            self.name = name
        if nick_name is not None:
            self.nick_name = nick_name
        if state is not None:
            self.state = state
        if score is not None:
            self.score = score
        if tenant_name is not None:
            self.tenant_name = tenant_name

    @property
    def id(self):
        r"""Gets the id of this MergeRequestReviewerExternalDto.

        评审人id

        :return: The id of this MergeRequestReviewerExternalDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MergeRequestReviewerExternalDto.

        评审人id

        :param id: The id of this MergeRequestReviewerExternalDto.
        :type id: int
        """
        self._id = id

    @property
    def username(self):
        r"""Gets the username of this MergeRequestReviewerExternalDto.

        评审人名称

        :return: The username of this MergeRequestReviewerExternalDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this MergeRequestReviewerExternalDto.

        评审人名称

        :param username: The username of this MergeRequestReviewerExternalDto.
        :type username: str
        """
        self._username = username

    @property
    def name(self):
        r"""Gets the name of this MergeRequestReviewerExternalDto.

        评审人名称

        :return: The name of this MergeRequestReviewerExternalDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MergeRequestReviewerExternalDto.

        评审人名称

        :param name: The name of this MergeRequestReviewerExternalDto.
        :type name: str
        """
        self._name = name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this MergeRequestReviewerExternalDto.

        评审人昵称

        :return: The nick_name of this MergeRequestReviewerExternalDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this MergeRequestReviewerExternalDto.

        评审人昵称

        :param nick_name: The nick_name of this MergeRequestReviewerExternalDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def state(self):
        r"""Gets the state of this MergeRequestReviewerExternalDto.

        评审人状态

        :return: The state of this MergeRequestReviewerExternalDto.
        :rtype: bool
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this MergeRequestReviewerExternalDto.

        评审人状态

        :param state: The state of this MergeRequestReviewerExternalDto.
        :type state: bool
        """
        self._state = state

    @property
    def score(self):
        r"""Gets the score of this MergeRequestReviewerExternalDto.

        打分

        :return: The score of this MergeRequestReviewerExternalDto.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this MergeRequestReviewerExternalDto.

        打分

        :param score: The score of this MergeRequestReviewerExternalDto.
        :type score: int
        """
        self._score = score

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this MergeRequestReviewerExternalDto.

        租户名称

        :return: The tenant_name of this MergeRequestReviewerExternalDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this MergeRequestReviewerExternalDto.

        租户名称

        :param tenant_name: The tenant_name of this MergeRequestReviewerExternalDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

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
        if not isinstance(other, MergeRequestReviewerExternalDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
