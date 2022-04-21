# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AclBindApiInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'api_id': 'str',
        'api_name': 'str',
        'group_name': 'str',
        'api_type': 'int',
        'api_remark': 'str',
        'env_id': 'str',
        'env_name': 'str',
        'bind_id': 'str',
        'bind_time': 'datetime',
        'publish_id': 'str'
    }

    attribute_map = {
        'api_id': 'api_id',
        'api_name': 'api_name',
        'group_name': 'group_name',
        'api_type': 'api_type',
        'api_remark': 'api_remark',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'bind_id': 'bind_id',
        'bind_time': 'bind_time',
        'publish_id': 'publish_id'
    }

    def __init__(self, api_id=None, api_name=None, group_name=None, api_type=None, api_remark=None, env_id=None, env_name=None, bind_id=None, bind_time=None, publish_id=None):
        """AclBindApiInfo

        The model defined in huaweicloud sdk

        :param api_id: API编号
        :type api_id: str
        :param api_name: API名称
        :type api_name: str
        :param group_name: API分组名称
        :type group_name: str
        :param api_type: API类型
        :type api_type: int
        :param api_remark: API的描述信息
        :type api_remark: str
        :param env_id: 生效的环境编号
        :type env_id: str
        :param env_name: 生效的环境名称
        :type env_name: str
        :param bind_id: 绑定关系编号
        :type bind_id: str
        :param bind_time: 绑定时间
        :type bind_time: datetime
        :param publish_id: API发布记录编号
        :type publish_id: str
        """
        
        

        self._api_id = None
        self._api_name = None
        self._group_name = None
        self._api_type = None
        self._api_remark = None
        self._env_id = None
        self._env_name = None
        self._bind_id = None
        self._bind_time = None
        self._publish_id = None
        self.discriminator = None

        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if group_name is not None:
            self.group_name = group_name
        if api_type is not None:
            self.api_type = api_type
        if api_remark is not None:
            self.api_remark = api_remark
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if bind_id is not None:
            self.bind_id = bind_id
        if bind_time is not None:
            self.bind_time = bind_time
        if publish_id is not None:
            self.publish_id = publish_id

    @property
    def api_id(self):
        """Gets the api_id of this AclBindApiInfo.

        API编号

        :return: The api_id of this AclBindApiInfo.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this AclBindApiInfo.

        API编号

        :param api_id: The api_id of this AclBindApiInfo.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        """Gets the api_name of this AclBindApiInfo.

        API名称

        :return: The api_name of this AclBindApiInfo.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this AclBindApiInfo.

        API名称

        :param api_name: The api_name of this AclBindApiInfo.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def group_name(self):
        """Gets the group_name of this AclBindApiInfo.

        API分组名称

        :return: The group_name of this AclBindApiInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this AclBindApiInfo.

        API分组名称

        :param group_name: The group_name of this AclBindApiInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def api_type(self):
        """Gets the api_type of this AclBindApiInfo.

        API类型

        :return: The api_type of this AclBindApiInfo.
        :rtype: int
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        """Sets the api_type of this AclBindApiInfo.

        API类型

        :param api_type: The api_type of this AclBindApiInfo.
        :type api_type: int
        """
        self._api_type = api_type

    @property
    def api_remark(self):
        """Gets the api_remark of this AclBindApiInfo.

        API的描述信息

        :return: The api_remark of this AclBindApiInfo.
        :rtype: str
        """
        return self._api_remark

    @api_remark.setter
    def api_remark(self, api_remark):
        """Sets the api_remark of this AclBindApiInfo.

        API的描述信息

        :param api_remark: The api_remark of this AclBindApiInfo.
        :type api_remark: str
        """
        self._api_remark = api_remark

    @property
    def env_id(self):
        """Gets the env_id of this AclBindApiInfo.

        生效的环境编号

        :return: The env_id of this AclBindApiInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this AclBindApiInfo.

        生效的环境编号

        :param env_id: The env_id of this AclBindApiInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        """Gets the env_name of this AclBindApiInfo.

        生效的环境名称

        :return: The env_name of this AclBindApiInfo.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this AclBindApiInfo.

        生效的环境名称

        :param env_name: The env_name of this AclBindApiInfo.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def bind_id(self):
        """Gets the bind_id of this AclBindApiInfo.

        绑定关系编号

        :return: The bind_id of this AclBindApiInfo.
        :rtype: str
        """
        return self._bind_id

    @bind_id.setter
    def bind_id(self, bind_id):
        """Sets the bind_id of this AclBindApiInfo.

        绑定关系编号

        :param bind_id: The bind_id of this AclBindApiInfo.
        :type bind_id: str
        """
        self._bind_id = bind_id

    @property
    def bind_time(self):
        """Gets the bind_time of this AclBindApiInfo.

        绑定时间

        :return: The bind_time of this AclBindApiInfo.
        :rtype: datetime
        """
        return self._bind_time

    @bind_time.setter
    def bind_time(self, bind_time):
        """Sets the bind_time of this AclBindApiInfo.

        绑定时间

        :param bind_time: The bind_time of this AclBindApiInfo.
        :type bind_time: datetime
        """
        self._bind_time = bind_time

    @property
    def publish_id(self):
        """Gets the publish_id of this AclBindApiInfo.

        API发布记录编号

        :return: The publish_id of this AclBindApiInfo.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this AclBindApiInfo.

        API发布记录编号

        :param publish_id: The publish_id of this AclBindApiInfo.
        :type publish_id: str
        """
        self._publish_id = publish_id

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
        if not isinstance(other, AclBindApiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
