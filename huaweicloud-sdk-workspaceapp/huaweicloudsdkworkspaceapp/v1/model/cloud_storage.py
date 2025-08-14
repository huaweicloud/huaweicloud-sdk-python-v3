# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudStorage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'project_config_id': 'str',
        'create_time': 'datetime',
        'user_claim_count': 'int',
        'share_claim_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_config_id': 'project_config_id',
        'create_time': 'create_time',
        'user_claim_count': 'user_claim_count',
        'share_claim_count': 'share_claim_count'
    }

    def __init__(self, id=None, name=None, project_config_id=None, create_time=None, user_claim_count=None, share_claim_count=None):
        r"""CloudStorage

        The model defined in huaweicloud sdk

        :param id: 云存储id。
        :type id: str
        :param name: 云存储名称。
        :type name: str
        :param project_config_id: 云存储id。
        :type project_config_id: str
        :param create_time: 创建时间。
        :type create_time: datetime
        :param user_claim_count: 个人目录声明数量。
        :type user_claim_count: int
        :param share_claim_count: 共享目录声明数量。
        :type share_claim_count: int
        """
        
        

        self._id = None
        self._name = None
        self._project_config_id = None
        self._create_time = None
        self._user_claim_count = None
        self._share_claim_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_config_id is not None:
            self.project_config_id = project_config_id
        if create_time is not None:
            self.create_time = create_time
        if user_claim_count is not None:
            self.user_claim_count = user_claim_count
        if share_claim_count is not None:
            self.share_claim_count = share_claim_count

    @property
    def id(self):
        r"""Gets the id of this CloudStorage.

        云存储id。

        :return: The id of this CloudStorage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CloudStorage.

        云存储id。

        :param id: The id of this CloudStorage.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CloudStorage.

        云存储名称。

        :return: The name of this CloudStorage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CloudStorage.

        云存储名称。

        :param name: The name of this CloudStorage.
        :type name: str
        """
        self._name = name

    @property
    def project_config_id(self):
        r"""Gets the project_config_id of this CloudStorage.

        云存储id。

        :return: The project_config_id of this CloudStorage.
        :rtype: str
        """
        return self._project_config_id

    @project_config_id.setter
    def project_config_id(self, project_config_id):
        r"""Sets the project_config_id of this CloudStorage.

        云存储id。

        :param project_config_id: The project_config_id of this CloudStorage.
        :type project_config_id: str
        """
        self._project_config_id = project_config_id

    @property
    def create_time(self):
        r"""Gets the create_time of this CloudStorage.

        创建时间。

        :return: The create_time of this CloudStorage.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CloudStorage.

        创建时间。

        :param create_time: The create_time of this CloudStorage.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def user_claim_count(self):
        r"""Gets the user_claim_count of this CloudStorage.

        个人目录声明数量。

        :return: The user_claim_count of this CloudStorage.
        :rtype: int
        """
        return self._user_claim_count

    @user_claim_count.setter
    def user_claim_count(self, user_claim_count):
        r"""Sets the user_claim_count of this CloudStorage.

        个人目录声明数量。

        :param user_claim_count: The user_claim_count of this CloudStorage.
        :type user_claim_count: int
        """
        self._user_claim_count = user_claim_count

    @property
    def share_claim_count(self):
        r"""Gets the share_claim_count of this CloudStorage.

        共享目录声明数量。

        :return: The share_claim_count of this CloudStorage.
        :rtype: int
        """
        return self._share_claim_count

    @share_claim_count.setter
    def share_claim_count(self, share_claim_count):
        r"""Sets the share_claim_count of this CloudStorage.

        共享目录声明数量。

        :param share_claim_count: The share_claim_count of this CloudStorage.
        :type share_claim_count: int
        """
        self._share_claim_count = share_claim_count

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
        if not isinstance(other, CloudStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
