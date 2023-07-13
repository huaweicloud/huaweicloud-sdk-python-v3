# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiOutline:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_type': 'str',
        'run_env_name': 'str',
        'group_name': 'str',
        'publish_id': 'str',
        'group_id': 'str',
        'name': 'str',
        'remark': 'str',
        'run_env_id': 'str',
        'id': 'str',
        'req_uri': 'str'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'run_env_name': 'run_env_name',
        'group_name': 'group_name',
        'publish_id': 'publish_id',
        'group_id': 'group_id',
        'name': 'name',
        'remark': 'remark',
        'run_env_id': 'run_env_id',
        'id': 'id',
        'req_uri': 'req_uri'
    }

    def __init__(self, auth_type=None, run_env_name=None, group_name=None, publish_id=None, group_id=None, name=None, remark=None, run_env_id=None, id=None, req_uri=None):
        """ApiOutline

        The model defined in huaweicloud sdk

        :param auth_type: API的认证方式
        :type auth_type: str
        :param run_env_name: 发布的环境名
        :type run_env_name: str
        :param group_name: API所属分组的名称
        :type group_name: str
        :param publish_id: 发布记录的编号
        :type publish_id: str
        :param group_id: API所属分组的编号
        :type group_id: str
        :param name: API名称
        :type name: str
        :param remark: API描述
        :type remark: str
        :param run_env_id: 发布的环境id
        :type run_env_id: str
        :param id: API编号
        :type id: str
        :param req_uri: API的请求地址
        :type req_uri: str
        """
        
        

        self._auth_type = None
        self._run_env_name = None
        self._group_name = None
        self._publish_id = None
        self._group_id = None
        self._name = None
        self._remark = None
        self._run_env_id = None
        self._id = None
        self._req_uri = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if run_env_name is not None:
            self.run_env_name = run_env_name
        if group_name is not None:
            self.group_name = group_name
        if publish_id is not None:
            self.publish_id = publish_id
        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark
        if run_env_id is not None:
            self.run_env_id = run_env_id
        if id is not None:
            self.id = id
        if req_uri is not None:
            self.req_uri = req_uri

    @property
    def auth_type(self):
        """Gets the auth_type of this ApiOutline.

        API的认证方式

        :return: The auth_type of this ApiOutline.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ApiOutline.

        API的认证方式

        :param auth_type: The auth_type of this ApiOutline.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def run_env_name(self):
        """Gets the run_env_name of this ApiOutline.

        发布的环境名

        :return: The run_env_name of this ApiOutline.
        :rtype: str
        """
        return self._run_env_name

    @run_env_name.setter
    def run_env_name(self, run_env_name):
        """Sets the run_env_name of this ApiOutline.

        发布的环境名

        :param run_env_name: The run_env_name of this ApiOutline.
        :type run_env_name: str
        """
        self._run_env_name = run_env_name

    @property
    def group_name(self):
        """Gets the group_name of this ApiOutline.

        API所属分组的名称

        :return: The group_name of this ApiOutline.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ApiOutline.

        API所属分组的名称

        :param group_name: The group_name of this ApiOutline.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def publish_id(self):
        """Gets the publish_id of this ApiOutline.

        发布记录的编号

        :return: The publish_id of this ApiOutline.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this ApiOutline.

        发布记录的编号

        :param publish_id: The publish_id of this ApiOutline.
        :type publish_id: str
        """
        self._publish_id = publish_id

    @property
    def group_id(self):
        """Gets the group_id of this ApiOutline.

        API所属分组的编号

        :return: The group_id of this ApiOutline.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ApiOutline.

        API所属分组的编号

        :param group_id: The group_id of this ApiOutline.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this ApiOutline.

        API名称

        :return: The name of this ApiOutline.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiOutline.

        API名称

        :param name: The name of this ApiOutline.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this ApiOutline.

        API描述

        :return: The remark of this ApiOutline.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ApiOutline.

        API描述

        :param remark: The remark of this ApiOutline.
        :type remark: str
        """
        self._remark = remark

    @property
    def run_env_id(self):
        """Gets the run_env_id of this ApiOutline.

        发布的环境id

        :return: The run_env_id of this ApiOutline.
        :rtype: str
        """
        return self._run_env_id

    @run_env_id.setter
    def run_env_id(self, run_env_id):
        """Sets the run_env_id of this ApiOutline.

        发布的环境id

        :param run_env_id: The run_env_id of this ApiOutline.
        :type run_env_id: str
        """
        self._run_env_id = run_env_id

    @property
    def id(self):
        """Gets the id of this ApiOutline.

        API编号

        :return: The id of this ApiOutline.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiOutline.

        API编号

        :param id: The id of this ApiOutline.
        :type id: str
        """
        self._id = id

    @property
    def req_uri(self):
        """Gets the req_uri of this ApiOutline.

        API的请求地址

        :return: The req_uri of this ApiOutline.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this ApiOutline.

        API的请求地址

        :param req_uri: The req_uri of this ApiOutline.
        :type req_uri: str
        """
        self._req_uri = req_uri

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
        if not isinstance(other, ApiOutline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
