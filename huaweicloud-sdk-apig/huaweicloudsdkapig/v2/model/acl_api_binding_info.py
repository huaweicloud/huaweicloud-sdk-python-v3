# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AclApiBindingInfo:

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
        'api_id': 'str',
        'env_id': 'str',
        'acl_id': 'str',
        'create_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'api_id': 'api_id',
        'env_id': 'env_id',
        'acl_id': 'acl_id',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, api_id=None, env_id=None, acl_id=None, create_time=None):
        r"""AclApiBindingInfo

        The model defined in huaweicloud sdk

        :param id: 绑定关系编号
        :type id: str
        :param api_id: API编号
        :type api_id: str
        :param env_id: 环境编号
        :type env_id: str
        :param acl_id: ACL策略编号
        :type acl_id: str
        :param create_time: 绑定时间
        :type create_time: datetime
        """
        
        

        self._id = None
        self._api_id = None
        self._env_id = None
        self._acl_id = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if api_id is not None:
            self.api_id = api_id
        if env_id is not None:
            self.env_id = env_id
        if acl_id is not None:
            self.acl_id = acl_id
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this AclApiBindingInfo.

        绑定关系编号

        :return: The id of this AclApiBindingInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AclApiBindingInfo.

        绑定关系编号

        :param id: The id of this AclApiBindingInfo.
        :type id: str
        """
        self._id = id

    @property
    def api_id(self):
        r"""Gets the api_id of this AclApiBindingInfo.

        API编号

        :return: The api_id of this AclApiBindingInfo.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this AclApiBindingInfo.

        API编号

        :param api_id: The api_id of this AclApiBindingInfo.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def env_id(self):
        r"""Gets the env_id of this AclApiBindingInfo.

        环境编号

        :return: The env_id of this AclApiBindingInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this AclApiBindingInfo.

        环境编号

        :param env_id: The env_id of this AclApiBindingInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def acl_id(self):
        r"""Gets the acl_id of this AclApiBindingInfo.

        ACL策略编号

        :return: The acl_id of this AclApiBindingInfo.
        :rtype: str
        """
        return self._acl_id

    @acl_id.setter
    def acl_id(self, acl_id):
        r"""Sets the acl_id of this AclApiBindingInfo.

        ACL策略编号

        :param acl_id: The acl_id of this AclApiBindingInfo.
        :type acl_id: str
        """
        self._acl_id = acl_id

    @property
    def create_time(self):
        r"""Gets the create_time of this AclApiBindingInfo.

        绑定时间

        :return: The create_time of this AclApiBindingInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AclApiBindingInfo.

        绑定时间

        :param create_time: The create_time of this AclApiBindingInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, AclApiBindingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
