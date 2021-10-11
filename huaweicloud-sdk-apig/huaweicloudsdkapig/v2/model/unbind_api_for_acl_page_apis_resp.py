# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnbindApiForAclPageApisResp:


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
        'group_id': 'str',
        'group_name': 'str',
        'type': 'int',
        'remark': 'str',
        'run_env_name': 'str',
        'run_env_id': 'str',
        'publish_id': 'str',
        'acl_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'type': 'type',
        'remark': 'remark',
        'run_env_name': 'run_env_name',
        'run_env_id': 'run_env_id',
        'publish_id': 'publish_id',
        'acl_name': 'acl_name'
    }

    def __init__(self, id=None, name=None, group_id=None, group_name=None, type=None, remark=None, run_env_name=None, run_env_id=None, publish_id=None, acl_name=None):
        """UnbindApiForAclPageApisResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._group_id = None
        self._group_name = None
        self._type = None
        self._remark = None
        self._run_env_name = None
        self._run_env_id = None
        self._publish_id = None
        self._acl_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if type is not None:
            self.type = type
        if remark is not None:
            self.remark = remark
        if run_env_name is not None:
            self.run_env_name = run_env_name
        if run_env_id is not None:
            self.run_env_id = run_env_id
        if publish_id is not None:
            self.publish_id = publish_id
        if acl_name is not None:
            self.acl_name = acl_name

    @property
    def id(self):
        """Gets the id of this UnbindApiForAclPageApisResp.

        API的ID

        :return: The id of this UnbindApiForAclPageApisResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnbindApiForAclPageApisResp.

        API的ID

        :param id: The id of this UnbindApiForAclPageApisResp.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UnbindApiForAclPageApisResp.

        API名称

        :return: The name of this UnbindApiForAclPageApisResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UnbindApiForAclPageApisResp.

        API名称

        :param name: The name of this UnbindApiForAclPageApisResp.
        :type: str
        """
        self._name = name

    @property
    def group_id(self):
        """Gets the group_id of this UnbindApiForAclPageApisResp.

        API所属分组的编号

        :return: The group_id of this UnbindApiForAclPageApisResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UnbindApiForAclPageApisResp.

        API所属分组的编号

        :param group_id: The group_id of this UnbindApiForAclPageApisResp.
        :type: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this UnbindApiForAclPageApisResp.

        API所属分组的名称

        :return: The group_name of this UnbindApiForAclPageApisResp.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this UnbindApiForAclPageApisResp.

        API所属分组的名称

        :param group_name: The group_name of this UnbindApiForAclPageApisResp.
        :type: str
        """
        self._group_name = group_name

    @property
    def type(self):
        """Gets the type of this UnbindApiForAclPageApisResp.

        API开放状态

        :return: The type of this UnbindApiForAclPageApisResp.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UnbindApiForAclPageApisResp.

        API开放状态

        :param type: The type of this UnbindApiForAclPageApisResp.
        :type: int
        """
        self._type = type

    @property
    def remark(self):
        """Gets the remark of this UnbindApiForAclPageApisResp.

        API描述

        :return: The remark of this UnbindApiForAclPageApisResp.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this UnbindApiForAclPageApisResp.

        API描述

        :param remark: The remark of this UnbindApiForAclPageApisResp.
        :type: str
        """
        self._remark = remark

    @property
    def run_env_name(self):
        """Gets the run_env_name of this UnbindApiForAclPageApisResp.

        发布的环境名

        :return: The run_env_name of this UnbindApiForAclPageApisResp.
        :rtype: str
        """
        return self._run_env_name

    @run_env_name.setter
    def run_env_name(self, run_env_name):
        """Sets the run_env_name of this UnbindApiForAclPageApisResp.

        发布的环境名

        :param run_env_name: The run_env_name of this UnbindApiForAclPageApisResp.
        :type: str
        """
        self._run_env_name = run_env_name

    @property
    def run_env_id(self):
        """Gets the run_env_id of this UnbindApiForAclPageApisResp.

        发布的环境id

        :return: The run_env_id of this UnbindApiForAclPageApisResp.
        :rtype: str
        """
        return self._run_env_id

    @run_env_id.setter
    def run_env_id(self, run_env_id):
        """Sets the run_env_id of this UnbindApiForAclPageApisResp.

        发布的环境id

        :param run_env_id: The run_env_id of this UnbindApiForAclPageApisResp.
        :type: str
        """
        self._run_env_id = run_env_id

    @property
    def publish_id(self):
        """Gets the publish_id of this UnbindApiForAclPageApisResp.

        API发布记录编号

        :return: The publish_id of this UnbindApiForAclPageApisResp.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this UnbindApiForAclPageApisResp.

        API发布记录编号

        :param publish_id: The publish_id of this UnbindApiForAclPageApisResp.
        :type: str
        """
        self._publish_id = publish_id

    @property
    def acl_name(self):
        """Gets the acl_name of this UnbindApiForAclPageApisResp.

        绑定的其他同类型的ACL策略名称

        :return: The acl_name of this UnbindApiForAclPageApisResp.
        :rtype: str
        """
        return self._acl_name

    @acl_name.setter
    def acl_name(self, acl_name):
        """Sets the acl_name of this UnbindApiForAclPageApisResp.

        绑定的其他同类型的ACL策略名称

        :param acl_name: The acl_name of this UnbindApiForAclPageApisResp.
        :type: str
        """
        self._acl_name = acl_name

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
        if not isinstance(other, UnbindApiForAclPageApisResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
